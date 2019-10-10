import socketserver
import pymysql
import pickle
import sys
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

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn=self.request
        conn.sendall(bytes('Successfully connected to Server.',encoding='utf-8'))
        # print(address,conn)
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding='utf-8')
            if ret_str=='0':
                # sys.exit()
                # conn.close()
                print(self.client_address,'Has disconnected.')
                break
            elif ret_str=='1':
                # print(self.client_address,ret_str)
                # conn.sendall(bytes('Result for'+ret_str,encoding='utf-8'))
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
                    tot_star.append(sum_star / count)

                # close the connection
                db.close()
                X = act_date
                y = tot_star
                listxy=([X,y])
                listserial=pickle.dumps(X)
                print(listserial)
                conn.sendall(bytes(xjson,encoding='utf-8'))
                conn.recv(1024)
                # conn.sendall(bytes(xjson,encoding='utf-8'))
                # conn.recv(1024)
                # conn.sendall(bytes(yjsonlen,encoding='utf-8'))
                # conn.sendall(bytes(yjson,encoding='utf-8'))


if __name__=='__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyServer)
    server.serve_forever()