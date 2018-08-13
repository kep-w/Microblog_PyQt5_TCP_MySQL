# tcp_client.py


# from socket import *
# sys.path.append('/home/tarena/aid1803')
# from microblog.microblog.conf import conf
# from microblog.microblog.msg import msgdecoder
# from microblog.microblog.msg import msgencoder
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM, 0)
# def getserverconfig():
# 	cf = conf.ConfigReader('../config.ini')
# 	serverconfig = cf.getdic("server")
# 	return serverconfig
# host = serverconfig.get("host")
# port = int(serverconfig.get("port"))

# #发起连接
# sockfd.connect((host, port))

def main():
	if len(sys.argv) < 2:
		print("cmd is error , pls use:")
		print("python3 client.py start")
		return
	try:
		if sys.argv[1] == 'start':
			print("客户端开始启动")
			#调用微博首页的模块
			###
			print("客户端启动成功")
	except Exception as e:
		print("客户端启动失败")
		traceback.print_exc()
		return	


if __name__ == '__main__':
	main()



