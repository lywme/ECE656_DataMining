import pymysql
import matplotlib.pyplot as plt
import numpy as np
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import operator
from config import DB_info,user_info

class DB:
    def __init__(self):
        db_info = DB_info()
        self.db = pymysql.connect(host=db_info.host,
                                  port=db_info.port,
                                  user=db_info.user,
                                  password=db_info.password,
                                  db=db_info.db)
        self.cursor = self.db.cursor()

    def Query(self):
        """ fetch result after query"""
        # sql = "select * from review limit 1"
        sql = 'SELECT B.business_id,U.user_id as user_id,B.stars as other_rate_this_business,U.average_stars as this_rate_all_business,R.stars as this_rate_this_business FROM business as B INNER JOIN review as R using (business_id) INNER JOIN `user` as U using (user_id) order by B.business_id limit 500'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.db.close()

##################################################
# class data: set data attribute
##################################################
class data():
    def __init__(self, classifier):
        self.examples = []
        self.attributes = []
        self.classifier = classifier
        self.class_index = None


##################################################
# class Node: save the tree node class
##################################################
class treeNode():
    def __init__(self, is_leaf, classification, attr_split_index, attr_split_value, parent, upper_child, lower_child,
                 height):
        self.is_leaf = True
        self.height = None
        self.classification = None
        self.attr_split = None
        self.attr_split_index = None
        self.attr_split_value = None
        self.upper_child = None
        self.lower_child = None
        self.parent = parent


##################################################
# function decision_tree: design tree recursively
##################################################
def decision_tree(dataset, parent_node, classifier):
    node = treeNode(True, None, None, None, parent_node, None, None, 0)
    if (parent_node == None):
        node.height = 0
    else:
        node.height = node.parent.height + 1

    ones = num_count(dataset.examples, dataset.attributes)
    for key, value in ones.items():
        if (len(dataset.examples) == value):  # all "yes" data under the leave are in one class, like overcast case
            node.classification = key
            node.is_leaf = True
            return node
    if (sum(ones.values()) == 0):
        node.classification = 0  # all "no"
        node.is_leaf = True
        return node
    else:
        node.is_leaf = False
    attr_to_split = None
    max_gain = 0
    split_val = None
    dataset_entropy = entropy_calculation(dataset)
    for attr_index in range(len(dataset.examples[0])):
        if (dataset.attributes[attr_index] != classifier):  # eliminate the duplicate attribute
            local_max_gain = 0
            local_split_val = None
            attr_value_list = [example[attr_index] for example in
                               dataset.examples]  # these are the values we can split on, now we must find the best one
            attr_value_list = list(set(attr_value_list))  # remove duplicates from list of all attribute values

            for val in attr_value_list:
                # get the max gain
                local_gain = gainInfoRatio(dataset, dataset_entropy, val,
                                           attr_index)  # calculate the gain if we split on this value

                if (local_gain > local_max_gain):
                    local_max_gain = local_gain
                    local_split_val = val

            if (local_max_gain > max_gain):  # until the max gain is chosen
                max_gain = local_max_gain
                split_val = local_split_val
                attr_to_split = attr_index

    if (max_gain <= 0.01 or node.height > 20):
        node.is_leaf = True
        count_dict = num_count(dataset.examples,dataset.attributes)
        optimal_attr = max(count_dict.items(), key=operator.itemgetter(1))[0]
        node.classification = optimal_attr
        return node

    node.attr_split_index = attr_to_split
    node.attr_split = dataset.attributes[attr_to_split]
    node.attr_split_value = split_val

    upper_dataset = data(classifier)
    lower_dataset = data(classifier)
    upper_dataset.attributes = dataset.attributes
    lower_dataset.attributes = dataset.attributes
    # divide the data.example into two classes: upper and lower class
    for example in dataset.examples:
        if (attr_to_split is not None and example[attr_to_split] >= split_val):
            upper_dataset.examples.append(example)
        elif (attr_to_split is not None):
            lower_dataset.examples.append(example)
    # recursively calculate
    node.upper_child = decision_tree(upper_dataset, node, classifier)
    node.lower_child = decision_tree(lower_dataset, node, classifier)

    return node

##################################################
# fun entropy_calculation: Calculate the entropy of the dataset.example
##################################################
def entropy_calculation(dataset):
    count = num_count(dataset.examples, dataset.attributes)  # the dict record the number of each class
    total_examples = len(dataset.examples)

    entropy = 0
    for value in count.values():
        p = int(value) / total_examples
        if (p != 0):
            entropy -= p * np.log2(p)

    return entropy


##################################################
# fun gainInfoRatio: calculate the GainRatio
##################################################
def gainInfoRatio(dataset, entropy, val, attr_index):
    classifier = dataset.attributes[attr_index]
    attr_entropy = 0
    total_examples = len(dataset.examples)
    upper_gain = data(classifier)
    lower_gain = data(classifier)
    upper_gain.attributes = dataset.attributes
    lower_gain.attributes = dataset.attributes
    for example in dataset.examples:
        if (example[attr_index] >= val):
            upper_gain.examples.append(example)
        elif (example[attr_index] < val):
            lower_gain.examples.append(example)

    if (len(upper_gain.examples) == 0 or len(
            lower_gain.examples) == 0):  # Splitting didn't actually split (we tried to split on the max or min of the attribute's range)
        return -1

    attr_entropy += entropy_calculation(upper_gain) * len(upper_gain.examples) / total_examples  # kind of simplified
    attr_entropy += entropy_calculation(lower_gain) * len(lower_gain.examples) / total_examples

    gain = entropy - attr_entropy

    ## for C4.5
    # if gain == 0:
    #     return 0.00001  # used because of the special case when gain is 0
    # splitE = 0
    # upper = len(upper_gain.examples) / total_examples
    # lower = len(lower_gain.examples) / total_examples
    #
    # splitE -= upper * np.log2(upper)
    # splitE -= lower * np.log2(lower)
    #
    # gain_ratio = gain / splitE

    return gain


##################################################
# fun num_count: count the number of each class in the dataset
##################################################
def num_count(instances, attributes):
    # create the dict
    label_list = [instance[-1] for instance in instances]
    label_list = list(set(label_list))
    count_dict = {}
    for label in label_list:
        count_dict[str(int(label))] = 0
    # count_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
    # print(count_dict)

    # find index of classifier
    class_index = len(attributes) - 1
    for i in instances:
        num = str((int(i[class_index])))

        if num in count_dict:
            count_dict[num] += 1
    return count_dict

##################################################
# fun test_tree: get the testing accuracy
##################################################
def test_tree(node, dataset):
    total = len(dataset.examples)
    correct = 0
    for example in dataset.examples:
        # calculate example accuracy
        correct += validate_example(node, example)
    return correct / total


##################################################
# fun test_example: find the leaf
##################################################
def validate_example(node, example):
    if (node.is_leaf == True):
        projected = node.classification
        actual = int(example[-1])
        # print(projected,actual)
        if (int(projected) - actual) > 1 or (int(projected) - actual) < -1:
            return 0 # wrong prediction
        else:
            return 1
    value = example[node.attr_split_index]
    if (value >= node.attr_split_value):
        return validate_example(node.upper_child, example)
    else:
        return validate_example(node.lower_child, example)


##################################################
# main funct
##################################################

def main():
    db = DB()
    print('Begin processing...')
    result = db.Query()
    # print(result)

    dataset = data("")
    train_data = data("")
    validate_data = data("")

    dataset.examples = [[value[2], value[3],value[4]] for value in result]

    # get the list attributes
    dataset.attributes = ['other_rate_this_business','this_rate_all_business','this_rate_this_business']
    # dataset.attributes = dataset.examples.pop(0)
    train_data.attributes = dataset.attributes
    validate_data.attributes = dataset.attributes

    classifier = dataset.attributes[-1]

    train_data.classifier = classifier
    validate_data.classifier = classifier

    # find index of classifier
    train_data.class_index = range(len(dataset.attributes))[-1]
    validate_data.class_index = range(len(dataset.attributes))[-1]

    # ten times ten fold
    ur = user_info()
    TestSize = ur.test_size
    train_data.examples, validate_data.examples = train_test_split(dataset.examples, test_size=TestSize)

    # generate the decision tree
    root = decision_tree(train_data, None, classifier)
    # test the accuracy of the decision tree
    # max_acc = test_tree(root, validate_data)
    # print(max_acc)

    # print(acc_prune)
    # use the test data to calculate the accuracy
    test_acc = test_tree(root, validate_data)

    # print(acc_list)
    print("Mean accuracy: " + str(100 * test_acc) + "%")
    db.close()


if __name__ == "__main__":
    main()
