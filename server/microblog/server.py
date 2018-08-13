#!/usr/bin/env python3
#coding = utf-8
'''
name：郭磊
功能：服务端的启动控制模块
'''
import sys
import traceback
from socketserver import *
from config.conf import *
from server_deal.server_msg_deal import *
from db.database_main import *


def handler(c):
    dealhandler = ServerMsgDeal(c)
    dealhandler.deal_unpack()
    dealhandler.deal()


# 创建服务器类
class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        try:
            addr = self.request.getpeername()
            print("conn from :", addr)
            handler(self.request)
        except KeyboardInterrupt:
            print("服务端退出")
            sys.exit(0)
        except Exception as e:
            traceback.print_exc()


# 服务器主流程控制函数
def main():
    if len(sys.argv) < 2:
        print("cmd is error , pls use:")
        print("python3 server.py start")
        return

    # 获取服务器配置
    serverconfig = getserverdic()
    host = serverconfig.get("host")
    port = int(serverconfig.get("port"))
    # 初始化数据库
    # WeiBo().init_database()
    MyDatabase().update_database()

    server = Server((host, port), Handler)
    try:
        if sys.argv[1] == 'start':
            print("服务器端开始启动")
            server.serve_forever()
            # print("服务端启动成功")
        else:
            print("cmd is error , pls use folowing:")
            print("python3 server.py start")
            return
    except Exception as e:
        print("服务端启动失败")
        traceback.print_exc()
        return


if __name__ == '__main__':
    main()
