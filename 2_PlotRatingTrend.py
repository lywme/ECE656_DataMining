import pymysql
import matplotlib.pyplot as plt
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
        ur = user_info()
        business_id = ur.business_id
        sql = "select date, avg(stars) as avg_stars from review where business_id = '%s' group by date order by date" % business_id
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
    avg_star = [value[1] for value in result]
    act_date = [value[0] for value in result]


    # calculate the rating trend
    count = 0
    sum_star = 0
    tot_star = []
    for star in avg_star:
        sum_star += star
        count += 1
        tot_star.append(sum_star/count)

    X = act_date
    y = tot_star
    plt.plot(X,y)
    plt.ylim(0,5)
    plt.xlabel('Date from first view to last view')
    plt.ylabel('Average rating')
    plt.title('Rating trend of the business')
    plt.savefig('Rating_trend_graph')
    plt.show()

    # close the connection
    db.close()







