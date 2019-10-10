import pymysql
import matplotlib.pyplot as plt
from config import DB_info,user_info
import numpy as np

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
        sql = "SELECT CHAR_LENGTH(text),(useful+funny+cool) as user_read FROM review"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.db.close()

if __name__ == '__main__':
    # connect to the database Yelp and fetch the Query result
    db = DB()
    result = db.Query()

    # store the result into a list
    avg_length = [value[0] for value in result]
    user_rate = [value[1] for value in result]

    # calculate the average rating trend
    rate_list = np.zeros(6)
    count_list = np.zeros(6)

    for i in range(len(result)):
        for j in range(6):
            if (avg_length[i] > 1000*j) and (avg_length[i] < 1000*(j+1)):
                count_list[j] += 1
                rate_list[j] += user_rate[i]

    avg_rate = rate_list/count_list
    # print(avg_rate)

    # plot the graph
    X = [0,1000,2000,3000,4000,5000]
    y = avg_rate

    plt.bar(range(len(X)), y, color='cy', tick_label=X)
    plt.ylim(0,10)
    plt.xlabel('Review length')
    plt.ylabel('Average user rating')
    plt.title('Correlation between review length and users perceiving')
    plt.savefig('Review_length_influence')
    plt.show()

    # close the connection
    db.close()







