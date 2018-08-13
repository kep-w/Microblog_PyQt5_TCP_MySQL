# main.py
'''
项目主流程控制模块
'''
import sys, os
import traceback
import signal
from threading import *
from socket import *

from microblog.microblog.conf import conf
from microblog.microblog.deal import msgdeal


def getserverconfig():
	cf = conf.ConfigReader('../config.ini')
	serverconfig = cf.getdic("server")
	return serverconfig


#初始化数据库
def init_database():
	database = mysqlconfig.get("database")
	if not isExsits(database):
		init_tables()


def getsocket(host, port):
	addr = (host, port)
	s = socket()
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind(addr)
	s.listen(10)
	return s


def handler(c):
	dealhandler = msgdeal.MsgDeal(c)
	dealhandler.deal_unpack()
	dealhandler.deal()


def server_start(host, port):
	print("服务器端开始启动")

	try:
		#初始化数据库
		#检查数据库是否存在
		#不存在则执行建库建表语句,存在则无需动作
		# initdatabase()
		s = getsocket(host, port)
		print("服务器端启动成功")
	except Exception as e:
		traceback.print_exc()
		print("服务器端启动失败")
		return

	while True:
		try:
			c, addr = s.accept()
			print("conn from :", addr)
		except KeyboardInterrupt:
			print("服务端退出")
			raise
		except Exception as e:
			traceback.print_exc()
			continue
		t = Thread(target = handler, args = (c,))
		t.setDaemon(True)
		t.start()
	s.close()

#服务器主流程控制函数
def main():
	if len(sys.argv) < 2:
		print("cmd is error , pls use:")
		print("'python3 server.py start' or 'python3 server.py stop'")
		return
	sys.path.append('.')

	#获取服务器配置
	serverconfig = getserverconfig()
	
	host = serverconfig.get("host")
	port = int(serverconfig.get("port"))
	if sys.argv[1] == 'start':
		server_start(host, port)
	else:
		print("cmd is error , pls use folowing:")
		print("'python3 server.py start' or 'python3 server.py stop'")
		return


if __name__ == '__main__':
	main()

	






