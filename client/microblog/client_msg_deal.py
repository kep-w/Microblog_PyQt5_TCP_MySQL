#!/usr/bin/env python3
#coding = utf-8
'''
name：郭磊
功能：客户端功能的逻辑处理模块

'''

import sys
from socket import *
from config.conf import *
from msg.msgdecoder import *
from msg.msgencoder import *
from db.messagestable import *
from db.userinfotable import *
from db.admin import *

serverconfig = getserverdic()
host = serverconfig.get("host")
port = int(serverconfig.get("port"))
buffersize = int(serverconfig.get('buffersize'))

class ClientMsgDeal(object):

	def get_conn(self):
		
		sockfd = socket(AF_INET, SOCK_STREAM, 0)
		sockfd.connect((host, port))
		self.sockfd = sockfd

	def close_conn(self):
		self.sockfd.close()

	#发送前端的请求报文,到服务端,并接收服务端的返回
	def send_msg(self, msg):
		self.get_conn()
		print("开始发送消息:", msg)
		#先接收5位的长度
		self.sockfd.send(msg.encode())
		data_size = int(self.sockfd.recv(5).decode())
		#收到的总长度
		recv_size = 0
		total_data = b""
		print("传入报文长度为:", data_size)
		while recv_size < data_size:
			print("继续等待报文接收:")
			print("已接受报文长度为:",len(total_data))
			data = self.sockfd.recv(buffersize)
			print("*****cdscsc*********", len(data))
			# #如果第一次接收的数据小于缓存区的大小,直接退出
			# if len(data) < buffersize:
			# 	# 1.数据长度小于buffersize,直接接受
			# 	if(data_size < buffersize):
			# 		total_data = data
			# 		break
				
				# 2.服务端数据分两次发送,判断第一次接受的数据大小和buffer对比
				# 3.
			total_data += data
			recv_size += len(data)	
			while data_size - len(total_data) < buffersize:
				#如果数据大小刚好是缓存区大小的倍数,此时可以直接退出
				if data_size - len(total_data) == 0:
					break
				left_data = self.sockfd.recv(data_size - len(total_data))
				total_data += left_data
			if data_size - len(total_data) == 0:
					break
		# print("接收到的响应报文为:", total_data.decode())
		msgdict = decode_msg_to_dict(total_data.decode())
		self.msgdict = msgdict
		self.close_conn()

	def do_login(self,username,passwd):
		''' 
			功能:
				用户登录操作,交易类型1001
			参数:
				username:用户名
				passwd:密码
			返回值:
				statuscode:登录结果
				userid:用户登录成功时,返回用户userid
				statuscode的可能值为:
					0000 登录成功
			        0001 用户已登录
			        0002 账号错误
			        0003 密码错误
			        0004 系统错误
		'''
		#组织登录请求的字典类型结构
		#组织报问体字典
		bodydict = {'LoginReq':
							{'username':username, 
								'passwd':passwd 
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1001')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码
		return self.msgdict.get("statuscode"),self.msgdict.get('userid')

	def do_register(self,username,passwd,phonenum,mail):
		'''
			功能:
				用户注册,交易类型1002
			参数:
				username:用户名
				passwd:密码
				phonenum:手机号
				mail:邮箱
			返回值:
				statuscode:注册结果
				userid:用户登录成功时,返回用户userid
				statuscode的可能值为:
					0000 注册成功
			        0001 该账号已注册
			        0002 系统错误
		'''

		#组织登录请求的字典类型结构
		#组织报问体字典
		bodydict = {'RegisterReq':
							{'username':username, 
								'passwd':passwd,
								'phonenumber':phonenum,
								'mail':mail
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1002')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码
		return self.msgdict.get("statuscode"),self.msgdict.get('userid')

	#查询微博列表,默认按照时间排序
	def do_find(self, search = None):
		'''
			功能:
				微博查询,交易类型1003
			参数:
				search:要查询的内容,默认为空,按照时间查询所有微博
				
			返回值:
				statuscode:查询结果
				resplist:微博动态列表
					列表中存放的是微博动态Messages对象
					Messages对象中有个属性commentlist中存放的是Comments对象
					使用时,请遍历获取

				statuscode的可能值为:
					0000 查询成功
			        0001 暂时无动态
			        0002 系统错误
		'''

		#如果搜索内容为空.默认按照时间查询
		#组织微博查询请求的字典类型结构
		#组织报问体字典
		bodydict = {'SearchReq':
							{
									'search':'' if not search else search
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1003')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		statuscode = self.msgdict.get("statuscode")
		#定义要返回前端的列表
		resplist = []
		#返回码0000,说明返回成功了
		if '0000' == statuscode:	
			
			#得到微博列表字符串
			blogslist = self.msgdict.get('blogslist')
			#按照####&&&&拆分,为一条条的微博
			resplist = self.decoding_msglist(blogslist)

		return statuscode,resplist

	@staticmethod
	def decoding_msglist(blogslist):
		'''
			功能:
				解析服务端返回的bloglist字符串为msglist列表
			参数:
				blogslist
					和前端约定好的固定格式的字符串
			返回:
				resplist
					消息列表,列表中存放的是微博动态Messages对象
					Messages对象中有个属性commentlist中存放的是Comments对象
					使用时,请遍历获取
		'''
		resplist = []
		blist = blogslist.split('####&&&&')
		for blog in blist:
			msg = Messages()
			if not blog:
				continue
			#对每条字符串按照+-*#拆分,得到微博信息的每个属性
			msgl = blog.split('+-*#')
			msg.setmessagesid(msgl[0])
			msg.setuserid(msgl[1])
			msg.setmessagesinfo(msgl[2])
			msg.setmessagesagreenum(msgl[3])
			msg.setmessagestranspondnum(msgl[4])
			msg.setmessagestime(msgl[5])
			msg.username = msgl[6]
			#最后一个信息为评论列表
			commentlist = []
			if msgl[7]:
				#评论列表按照****&&&&拆分出一条条
				comlist = msgl[7].split('****&&&&')
				for comevery in comlist:
					if not comevery:
						continue
					comminfo = comevery.split('!+-*')
					comm = Comments()
					comm.setcommentid(comminfo[0])
					comm.setcommentinfo(comminfo[1])
					comm.setmessagesid(comminfo[2])
					comm.setuserid(comminfo[3])
					comm.setcommentstime(comminfo[4])
					comm.setusername(comminfo[5])
					commentlist.append(comm)
			msg.setcommentlist(commentlist)
			resplist.append(msg)
		return resplist


	def do_publish(self,userid,msg,time = None):
		'''
			功能:
				微博发布,交易类型1004
			参数:
				userid:用户自己的userid,登录成功时由服务端返回
				msg:用户要发布的微博
				
			返回值:
				statuscode:发布结果
				statuscode的可能值为:
					0000 发布成功
			        0001 系统错误
		'''
		bodydict = {'PublishReq':
							{
									'userid':userid,
									'msginfo':msg
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1004')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_agree(self,msgid,userid):
		'''
			功能:
				微博点赞,交易类型1005
			参数:
				msgid:要点赞的消息id	
				userid:用户的userid
			返回值:
				statuscode:点赞结果
				statuscode的可能值为:
					0000 点赞成功
			        0001 系统错误
		'''
		bodydict = {'AgreeReq':
							{
								'msgid':msgid,
								'userid':userid
							}
					}

		#组织报文头结构
		header = XmlMsgHeader('1005')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_forward(self,msgid,userid):

		'''
			功能:
				微博转发,交易类型1006
			参数:
				msgid:要转发的消息id	
				userid:用户的userid
			返回值:
				statuscode:转发结果
				statuscode的可能值为:
					0000 转发成功
			        0001 系统错误
			注意:
				转发成功后客户端还需要调用微博发布接口
		'''

		bodydict = {'ForwardReq':
							{
								'msgid':msgid,
								'userid':userid
							}
					}

		#组织报文头结构
		header = XmlMsgHeader('1006')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_comment(self,userid,msgid,comminfo):
		'''
			功能:
				微博评论,交易类型1007
			参数:
				userid:用户的userid
				msgid:要评论的消息id	
				comminfo:评论内容
			返回值:
				statuscode:评论结果
				statuscode的可能值为:
					0000 评论成功
			        0001 系统错误
		'''
		bodydict = {'CommentReq':
							{
								'userid':userid,
								'msgid':msgid,
								'comminfo':comminfo
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1007')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_modify_pass(self,userid,username,oldpass,newpass):
		'''
			功能:
				修改密码,交易类型1008
			参数:
				userid:用户的userid
				username:用户名	
				oldpass:旧密码
				newpass:新密码
			返回值:
				statuscode:修改结果
				statuscode的可能值为:
					0000 修改成功
			        0001 用户名密码不匹配
			        0002 系统错误
		'''
		bodydict = {'ModifyPassReq':
							{
								'userid':userid,
								'username':username,
								'oldpass':oldpass,
								'newpass':newpass
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1008')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_modify_userinfo(self,userid,nickename,gender,birthday,introduce):
		'''
			功能:
				修改用户信息,交易类型1009
			参数:
				userid:用户的userid
				nickename:昵称
				gender:性别
				birthday:生日
				introduce:个人简介
			返回值:
				statuscode:修改结果
				statuscode的可能值为:
					0000 修改成功
			        0001 系统错误
		'''
		bodydict = {'ModifyUserinfoReq':
							{
								'userid':userid,
								'nickename':nickename,
								'gender':gender,
								'birthday':birthday,
								'introduce':introduce
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1009')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_relate(self,userid,relateid):
		'''
			功能:
				关注用户,交易类型1010
			参数:
				userid:用户的userid
				relateid:要关注的用户userid
			返回值:
				statuscode:关注结果
				statuscode的可能值为:
					0000 关注成功
			        0001 系统错误
		'''
		bodydict = {'FollowReq':
							{
									'userid':userid,
									'relateid':relateid		
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1010')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		return self.msgdict.get("statuscode")

	def do_relate_msg(self,userid):
		'''
			功能:
				查询关注用户的动态,交易类型1011
			参数:
				userid:被关注用户的userid
				
			返回值:
				statuscode:查询结果
				resplist:
					动态列表,列表中存放的是微博动态Messages对象
					Messages对象中有个属性commentlist中存放的是Comments对象
					使用时,请遍历获取
				statuscode的可能值为:
					0000 查询成功
		            0001 好友无动态
		            0002 系统错误
		'''
		bodydict = {'FollowMsgReq':
								{
									'userid':userid				
								}
					}
		#组织报文头结构
		header = XmlMsgHeader('1011')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		statuscode = self.msgdict.get("statuscode")
		#定义要返回前端的列表
		resplist = []
		#返回码0000,说明返回成功了
		if '0000' == statuscode:				
			#得到微博列表字符串
			blogslist = self.msgdict.get('blogslist')
			#按照####&&&&拆分,为一条条的微博
			resplist = self.decoding_msglist(blogslist)
			
		return statuscode,resplist

	def do_show_userinfo(self,userid):
		'''
			功能:
				查询用户详细信息,交易类型1012
			参数:
				userid:用户的userid
				
			返回值:
				statuscode:查询结果
				userinfo:用户信息
				statuscode的可能值为:
					0000 查询成功
		        　　 	0001 无此用户信息
		        　　 	0002 系统错误"
		'''
		bodydict = {'ShowUserinfoReq':
							{
									'userid':userid
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1012')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		statuscode = self.msgdict.get("statuscode")
		userinfo = UserInfo()
		if '0000' == statuscode:
			userinfo.setuserinfoid(self.msgdict.get("userinfoid"))
			userinfo.setnickename(self.msgdict.get("nickname"))
			userinfo.setgender(self.msgdict.get("gender"))
			userinfo.setbirthday(self.msgdict.get("birthday"))
			userinfo.setemail(self.msgdict.get("email"))
			userinfo.setphonenumber(self.msgdict.get("phonenumber"))
			userinfo.setintroduce(self.msgdict.get("introduce"))
			userinfo.setpublishnum(self.msgdict.get("publishnum"))
			userinfo.setlaudnum(self.msgdict.get("laudnum"))
			userinfo.setregisttime(self.msgdict.get("registertime"))
			userinfo.setuserid(userid)

		return statuscode, userinfo

	def do_show_bloginfo(self,userid,infotype):
		'''
			功能:
				查询用户查询已发微博的动态,包括微博的点赞,评论,转发信息,交易类型1013
			参数:
				userid:用户自己的userid
				infotype:消息类型
						 0 : 点赞
						 1 : 转发
						 2 : 评论
				
			返回值:
				statuscode:查询结果
				blogmsglist:信息列表
							管理员消息列表,列表中存放的是管理员消息Admin对象
							Admin对象中有个属性Messages中存放的是Messages对象,
							Message对象有个属性是评论列表,使用时,请遍历获取
				statuscode的可能值为:
					0000 查询成功
			        0001 无消息
			        0002 系统错误
		'''
		bodydict = {'ShowBloginfoReq':
							{
									'userid':userid,
									'infotype':infotype
							}
					}
		#组织报文头结构
		header = XmlMsgHeader('1013')
		#创建报文结构对象
		body = XmlMsgBody(bodydict)
		#生成xml报文
		xml = MsgEncoder(header,body)
		#生成要发送的报文
		msg = "%05d" % len(xml.generate_xml().encode()) + xml.generate_xml()
		#发送报文,并返回字典
		self.send_msg(msg)
		#从字典中获得状态码和状态描述
		statuscode = self.msgdict.get("statuscode")
		
		blogmsglist = []

		if '0000' == statuscode:
			blogmsglist = self.decoding_adminlist(self.msgdict.get('blogmsglist'))
		return statuscode, blogmsglist

	@staticmethod
	def decoding_adminlist(adminlist):
		'''
			功能:
				解析服务端返回的adminlist字符串为adminlist列表
			参数:
				adminlist
					和前端约定好的固定格式的字符串
			返回:
				adminlist
					管理元消息列表,列表中存放的是管理员消息Admin对象
					Admin对象中有个属性Messages中存放的是Messages对象
					使用时,请遍历获取
		'''
		resplist = []
		alist = adminlist.split('####&&&&')
		for adminstr in alist:
			admin = Admin()
			if not adminstr:
				continue
			#对每条字符串按照**--+拆分,得到管理员信息的每个属性
			#adminlist += adminid + '**--+' + messagesid	+ '**--+' + username + '**--+' + admintype	+ '**--+' + userid + '**--+' + acceptuserid	+ '**--+' + adminstime + '**--+' + commentinfo + '**--+' + msglist + '####&&&&'

			adminl = adminstr.split('**--+')

			admin.setadminid(adminl[0])
			admin.setmessagesid(adminl[1])
			admin.setusername(adminl[2])
			admin.setadmintype(adminl[3])
			admin.setuserid(adminl[4])
			admin.setacceptuserid(adminl[5])
			admin.setadminstime(adminl[6])
			admin.setcommentinfo(adminl[7])

			#对字符串按照+-*#拆分,得到message对象的每个属性
			#msglist = msgid + '+-*#'+userid + '+-*#'+msginfo + '+-*#'+agreenum + '+-*#'+transnum + '+-*#'+time + '+-*#'+ username + '+-*#'+comments
			msgl = adminl[8].split('+-*#')
			msg = Messages()
			msg.setmessagesid(msgl[0])
			msg.setuserid(msgl[1])
			msg.setmessagesinfo(msgl[2])
			msg.setmessagesagreenum(msgl[3])
			msg.setmessagestranspondnum(msgl[4])
			msg.setmessagestime(msgl[5])
			msg.setusername(msgl[6])
			commentlist = []
			#评论列表按照****&&&&拆分出一条条
			#comments += comid+"!+-*"+cominfo+"!+-*"+msgid+"!+-*"+userid+"!+-*"+ctime+"!+-*"+username+"****&&&&"
			comlist = msgl[7].split('****&&&&')
			for comevery in comlist:
				if not comevery:
					continue
				#按照!+-*拆分出评论对象的每个字段
				comminfo = comevery.split('!+-*')
				comm = Comments()
				comm.setcommentid(comminfo[0])
				comm.setcommentinfo(comminfo[1])
				comm.setmessagesid(comminfo[2])
				comm.setuserid(comminfo[3])
				comm.setcommentstime(comminfo[4])
				comm.setusername(comminfo[5])
				commentlist.append(comm)
			msg.setcommentlist(commentlist)
			admin.setmessagesobject(msg)
			resplist.append(admin)
		return resplist




def main():
	type = sys.argv[1]
	cmd = ClientMsgDeal()
	if type == '1':
		resp = cmd.do_login('zhangsan', '123456')
	elif type == '2':
		resp = cmd.do_register('zhangsan', '123456', '123456', '126@163.com')
	elif type == '3':
		status,resp = cmd.do_find()
		for msg in resp:
			l = msg.getcommentlist()
			for c in l:
				print(c.__dict__)
	elif type == '4':
		resp = cmd.do_publish(1, '你好')
	elif type == '5':
		resp = cmd.do_agree(1,1)
	elif type == '6':
		resp = cmd.do_forward(1,1)
	elif type == '7':
		resp = cmd.do_comment(1,1,'真不错')
	elif type == '8':
		resp = cmd.do_modify_pass(1,'zhangsan', '123456','654321')
	elif type == '9':
		resp = cmd.do_modify_userinfo(1,'xiaosan','M','19870311','大家好我系渣渣辉')
	elif type == '10':
		resp = cmd.do_relate(1,1)
	elif type == '11':
		status,resp = cmd.do_relate_msg(2)
		for msg in resp:
			l = msg.getcommentlist()
			for c in l:
				print(c.__dict__)
	elif type == '12':
		resp,userinfo = cmd.do_show_userinfo(1)
		print(userinfo.__dict__)
	elif type == '13':
		resp,adminlist = cmd.do_show_bloginfo(1,'1')
		if resp == '0000':
			for ad in adminlist:
				msg = ad.getmessagesobject()
				print(msg.__dict__)
				commlist = msg.getcommentlist()
				for com in commlist:
					print(com.__dict__)
	print(resp)




if __name__ == '__main__':
	main()



	
	

		










