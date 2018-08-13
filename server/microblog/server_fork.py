# main.py
'''
项目主流程控制模块
'''
import sys, os
import traceback
import signal
from socket import *
sys.path.append('/Users/guolei/Desktop')

from microblog.microblog.conf import conf
from microblog.microblog.msg import msgdecoder
from microblog.microblog.deal import msgdeal


cf = conf.ConfigReader('../config.ini')
serverconfig = cf.getdic("server")
mysqlconfig = cf.getdic("mysql")

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

def server_start(host, port, buffersize):
	print("服务器端开始启动")

	try:
		#初始化数据库
		#检查数据库是否存在
		#不存在则执行建库建表语句,存在则无需动作
		# initdatabase()
		s = getsocket(host, port)
		signal.signal(signal.SIGCHLD, signal.SIG_IGN)
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
			s.close()
			sys.exit(0)
		except Exception:
			continue

		pid = os.fork()
		if pid < 0:
			print("创建子进程失败")
			c.close()
			continue
		elif pid == 0:
			s.close()

			#创建业务处理对象
			deal = msgdeal.MsgDeal(c)
			#创建客户端通信对象
			while True:
			#接收客户端的请求类型
				#获接收请求的总长度,5个字节为长度位
				data_size = int(c.recv(5).decode())
				#收到的总长度
				recv_size = 0
				total_data = ""
				while recv_size < data_size:
					data = c.recv(buffersize).decode()
					if 0 < data_size - len(data) < buffersize:
						left_data = c.recv(data_size - len(data)).decode()
						total_data += left_data
					total_data += data
					recv_size += len(data)
				
				# print("收到报文体为 :", total_data)
				#解析xml报文
				msgdict = msgdecoder.decode_msg_to_dict(total_data)
				print("交易报文的字典为:", msgdict)
				#获取报文的交易类型
				# transtype = msgdict.get("transType","没有此交易类型")
				
				deal.deal(msgdict)

				# if msgtype == '1001':
				# 	print("我要登录")
				# 	pass
				# elif msgtype == '1002':
				# 	print("我要注册")
				# 	pass
				# elif msgtype == '1003':
				# 	pass
				# elif data[0] == '1004':
				# 	pass
				

		else:
			c.close()
			continue


# def server_stop(pid):
# 	os.kill(pid, signal.SIGKILL)

#服务器主流程控制函数
def main():
	if len(sys.argv) < 2:
		print("cmd is error , pls use:")
		print("'python3 server.py start' or 'python3 server.py stop'")
		return

	#获取服务器配置
	
	host = serverconfig.get("host")
	port = int(serverconfig.get("port"))
	buffersize = int(serverconfig.get("buffersize"))
	pid = os.getpid()

	if sys.argv[1] == 'start':
		server_start(host, port, buffersize)
	# elif sys.argv[1] == 'stop':

	# 	server_stop(pid)
	else:
		print("cmd is error , pls use:")
		print("'python3 server.py start' or 'python3 server.py stop'")
		return











if __name__ == '__main__':
	main()

	






