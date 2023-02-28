import socket
import datetime
from config import dport

def servstatus():
    tsstat = 'Не определено'
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = dport
    conn.settimeout(5)
    try:
        host = '109.87.25.174'
        conn.connect((host, port))
        tsstat = 'Сервер доступен по основному каналу '
#        print(tsstat+str(datetime.datetime.now()))
        conn.close()
    except:
        tsstat = 'ISP1 is down'
#        print('ISP1 is down')

    if tsstat == 'ISP1 is down':
        try:
            host = '77.122.30.236'
            conn.connect((host, port))
            tsstat = 'Сервер доступен по резервному каналу '
#            print(tsstat+str(datetime.datetime.now()))
        except:
#            print("ISP2 is down")
            tsstat = 'Сервер временно недоступен '
#            print(tsstat + str(datetime.datetime.now()))
    return tsstat
print(servstatus()+str(datetime.datetime.now()))