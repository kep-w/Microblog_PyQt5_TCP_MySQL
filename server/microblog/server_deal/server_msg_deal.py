#!/usr/bin/env python3
#coding = utf-8
'''
name：郭磊
功能：多线程服务端的逻辑处理模块
'''
import sys
from config.conf import *
from msg.msgdecoder import *
from msg.msgencoder import *
from db.database_main import *
from db.userstable import *

buffersize = int(getserverdic().get('buffersize'))

class ServerMsgDeal(object):
	def __init__(self, conn):
		self.conn = conn

	def deal_unpack(self):
		'''
			接收xml报文并进行解析
			解析之后的报文字典绑定在对象的msgdict属性上
		'''
		#接收客户端的请求类型
		#获接收请求的总长度,5个字节为长度位
		data_size = int(self.conn.recv(5).decode())
		#收到的总长度
		recv_size = 0
		total_data = b""
		print("传入报文长度为:", data_size)
		while recv_size < data_size:
			print("继续等待报文接收:")
			print("已接受报文长度为:",len(total_data))
			data = self.conn.recv(buffersize)
			#如果第一次接收的数据小于缓存区的大小,直接退出
			if len(data) < buffersize:
				if(data_size < buffersize):
					total_data = data
					break
			total_data += data
			recv_size += len(data)	
			if data_size - len(total_data) < buffersize:
				#如果数据大小刚好是缓存区大小的倍数,此时可以直接退出
				if data_size - len(total_data) == 0:
					break

				left_data = self.conn.recv(data_size - len(total_data))
				total_data += left_data
				if data_size - len(total_data) < buffersize:
					break			
		print("接收到的请求报文为:", total_data.decode())		
		# 解析xml报文
		msgdict = decode_msg_to_dict(total_data.decode())
		self.msgdict = msgdict


	def deal(self):
		'''
		交易分发处理
		根据msgdict信息字典中的交易类型transType,将交易分发到不同的方法中
		'''
		#获取交易类型
		transtype = self.msgdict.get("transType","没有此交易类型")
		self.transtype = transtype
		if '1001' == transtype:
			self.do_login()
		elif '1002' == transtype:
			self.do_register()
		elif '1003' == transtype:
			self.do_find()
		elif '1004' == transtype:
			self.do_publish()
		elif '1005' == transtype:
			self.do_agree()
		elif '1006' == transtype:
			self.do_forward()
		elif '1007' == transtype:
			self.do_comment()
		elif '1008' == transtype:
			self.do_modify_pass()
		elif '1009' == transtype:
			self.do_modify_userinfo()
		elif '1010' == transtype:
			self.do_relate()
		elif '1011' == transtype:
			self.do_relate_msg()
		elif '1012' == transtype:
			self.do_show_userinfo()
		elif '1013' == transtype:
			self.do_show_bloginfo()
		else:
			pass

	def do_login(self):
		print(self.conn.getpeername(), "客户发起登录请求")
		username = self.msgdict.get('username')
		passwd = self.msgdict.get('passwd')
		#调用数据库查询登录,看是否登录成功,返回状态码和描述
		user = Users()
		user.setusername(username)
		user.setuserpasswd(passwd)
		statuscode = MyDatabase().weibo_login(user)
		userid = ''
		if statuscode == '0000':
			userid = user.getuserid()
		header = XmlMsgHeader('1001')
		bodydict = {'LoginResp':{'statuscode':statuscode, 'userid':userid}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_register(self):
		print(self.conn.getpeername(), "客户发起注册请求")
		username = self.msgdict.get('username')
		passwd = self.msgdict.get('passwd')
		misidn = self.msgdict.get('phonenumber')
		mail = self.msgdict.get('mail')
		#调用数据库接口,查询是否能够注册
		user = Users()
		user.setusername(username)
		user.setuserpasswd(passwd)
		user.setemail(mail)
		user.setphonenumber(misidn)
		statuscode = MyDatabase().weibo_register(user)
		userid = ''
		if statuscode == '0000':
			userid = user.getuserid()
		header = XmlMsgHeader('1002')
		bodydict = {'RegisterResp':{'statuscode':statuscode, 'userid':userid}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_find(self):
		print(self.conn.getpeername(), "客户发起查询相关请求")
		search = self.msgdict.get('search')
		print("search:",search)
		#如果查询内容为空,则按时间查询微博
		mdb = MyDatabase()
		#调用数据库接口
		if search == '' or search == None or search.strip() == '':
			statuscode,msglist = mdb.time_order()
		else:
			statuscode,msglist = mdb.vague_query(search)
		print(statuscode,msglist)
		blogslist = ''
		if statuscode == '0000':
			#拆分信息msglist
			blogslist = self.encoding_msglist(msglist)
		bodydict = {'SearchResp':
							{
								'statuscode':statuscode, 
							 	'blogslist':blogslist
							}
					}		
		header = XmlMsgHeader('1003')
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(bytes(resp,'utf-8')) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	@staticmethod
	def encoding_msglist(msglist):
		blogslist = ''
		for msg in msglist:
			msgid = str(msg.getmessagesid())
			userid = str(msg.getuserid())
			msginfo = msg.getmessagesinfo()
			agreenum = str(msg.getmessagesagreenum())
			transnum = str(msg.getmessagestranspondnum())
			time = str(msg.getmessagestime())
			username = msg.getusername()

			commentlist = msg.getcommentlist()
			comments = ''
			for c in commentlist:
				comid = str(c.getcommentid())
				cominfo = c.getcommentinfo()
				msgid = str(c.getmessagesid())
				userid = str(c.getuserid())
				ctime = str(c.getcommentstime())
				username1 = c.getusername()
				comments += comid+"!+-*"+cominfo+"!+-*"+msgid+"!+-*"+userid+"!+-*"+ctime+"!+-*"+username1+"****&&&&"

			blogslist += msgid + '+-*#'+userid + '+-*#'+msginfo + '+-*#'+agreenum + '+-*#'+transnum + '+-*#'+time + '+-*#'+ username + '+-*#'+comments + '####&&&&'
		return blogslist

	def do_publish(self):
		print(self.conn.getpeername(), "客户发起微博发布请求")
		userid = self.msgdict.get('userid')
		msginfo = self.msgdict.get('msginfo')
		msg = Messages()
		msg.setuserid(userid)
		msg.setmessagesinfo(msginfo)
		#调用数据库接口写入
		statuscode = MyDatabase().publish_dynamic(msg)
		header = XmlMsgHeader('1004')
		bodydict = {'PublishResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_agree(self):
		print(self.conn.getpeername(), "客户发起微博点赞请求")
		msgid = self.msgdict.get('msgid')
		userid = self.msgdict.get('userid')

		msg = Messages()
		msg.setmessagesid(msgid)
		msg.setuserid(userid)
		statuscode = MyDatabase().agree_with(msg)
		statusdescription = statuscode
		header = XmlMsgHeader('1005')
		bodydict = {'AgreeResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_forward(self):
		print(self.conn.getpeername(), "客户发起微博转发请求")
		msgid = self.msgdict.get('msgid')
		userid = self.msgdict.get('userid')
		msg = Messages()
		msg.setmessagesid(msgid)
		msg.setuserid(userid)

		statuscode = MyDatabase().forward(msg)
		statusdescription = statuscode
		header = XmlMsgHeader('1006')
		bodydict = {'ForwardResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_comment(self):
		print(self.conn.getpeername(), "客户发起评论请求")
		msgid = self.msgdict.get('msgid')
		userid = self.msgdict.get('userid')
		comminfo = self.msgdict.get('comminfo')
		comm = Comments()
		comm.setcommentinfo(comminfo)
		comm.setmessagesid(msgid)
		comm.setuserid(userid)
		statuscode = MyDatabase().write_comment(comm)
		header = XmlMsgHeader('1007')
		bodydict = {'CommentResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_modify_pass(self):
		print(self.conn.getpeername(), "客户发起密码修改请求")
		userid = self.msgdict.get('userid')
		username = self.msgdict.get('username')
		oldpass = self.msgdict.get('oldpass')
		newpass = self.msgdict.get('newpass')
		user = Users()
		user.setuserid(userid)
		user.setusername(username)
		user.setuserpasswd(oldpass)
		statuscode = MyDatabase().modify_passwd(user,newpass)
		statusdescription = statuscode
		header = XmlMsgHeader('1008')
		bodydict = {'ModifyPassResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_modify_userinfo(self):
		print(self.conn.getpeername(), "客户发起详细信息修改请求")
		userid = self.msgdict.get('userid')
		nickename = self.msgdict.get('nickename')
		gender = self.msgdict.get('gender')
		birthday = self.msgdict.get('birthday')
		introduce = self.msgdict.get('introduce')	
		userinfo = UserInfo()
		userinfo.setuserid(userid)
		userinfo.setnickename(nickename)
		userinfo.setgender(gender)
		userinfo.setbirthday(birthday)
		userinfo.setintroduce(introduce)
		statuscode = MyDatabase().update_userinfo(userinfo)
		statusdescription = statuscode
		header = XmlMsgHeader('1009')
		bodydict = {'ModifyPassResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_relate(self):
		print(self.conn.getpeername(), "客户关注请求")
		userid = self.msgdict.get('userid')
		relateid = self.msgdict.get('relateid')
		relation = Relation()
		relation.setuserid(userid)
		relation.setuserfollow(relateid)
		statuscode = MyDatabase().follow_user(relation)
		header = XmlMsgHeader('1010')
		bodydict = {'ModifyPassResp':{'statuscode':statuscode}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_relate_msg(self):
		print(self.conn.getpeername(), "客户发起查询关注的人的动态的请求")
		userid = self.msgdict.get('userid')
		user = Users()
		user.setuserid(userid)
		statuscode,messagelist = MyDatabase().follow_time_oder(user)
		blogslist = ''
		if '0000' == statuscode:
			blogslist = self.encoding_msglist(messagelist)
		header = XmlMsgHeader('1011')
		bodydict = {'FollowMsgResp':{'statuscode':statuscode,'blogslist':blogslist}}
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	def do_show_userinfo(self):
		print(self.conn.getpeername(), "客户信息查询请求")
		userid = self.msgdict.get('userid')
		userinfo = UserInfo()
		userinfo.setuserid(userid)
		statuscode = MyDatabase().main_select_userinfo(userinfo)
		if '0000' == statuscode:
			userinfoid = userinfo.getuserinfoid()
			nickname = userinfo.getnickename()
			gender = userinfo.getgender()
			birthday = userinfo.getbirthday()
			introduce = userinfo.getintroduce()
			email = userinfo.getemail()
			phonenumber = userinfo.getphonenumber()
			publishnum = userinfo.getpublishnum()
			laudnum = userinfo.getlaudnum()
			registertime = userinfo.getregisttime()

			bodydict = {'ShowUserinfoResp':
								{
									'statuscode':statuscode,
									'userinfoid':userinfoid,
									'nickname':'' if not nickname else nickname,
									'gender':'' if not gender else gender,
									'birthday':'' if not birthday else birthday,
									'introduce':'' if not introduce else introduce,
									'email':'' if not email else email,
									'phonenumber':'' if not phonenumber else phonenumber,
									'publishnum':0 if not publishnum else publishnum,
									'laudnum':0 if not laudnum else laudnum,
									'registertime':'' if not registertime else registertime
								}
						}
		else:
			bodydict = {'ShowUserinfoResp':{'statuscode':statuscode}}
		header = XmlMsgHeader('1012')
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())
	
	def do_show_bloginfo(self):
		print(self.conn.getpeername(), "客户发起动态信息查询请求")
		userid = self.msgdict.get('userid')
		infotype = self.msgdict.get('infotype')
		admin = Admin()
		admin.setacceptuserid(userid)
		admin.setadmintype(infotype)
		statuscode,adminlist = MyDatabase().main_select_admin_info(admin)
		print(statuscode)
		blogmsglist = ''
		if '0000' == statuscode:

			blogmsglist = self.encoding_adminlist(adminlist)

		bodydict = {'ShowBloginfoResp':
							{
								'statuscode':statuscode,
								'blogmsglist':blogmsglist									
							}
					}
		
		header = XmlMsgHeader('1013')
		body = XmlMsgBody(bodydict)
		xml = MsgEncoder(header,body)
		resp = xml.generate_xml()
		resp = '%05d' % len(resp.encode()) + resp
		print("要发送的报文为:", resp)
		self.conn.send(resp.encode())

	@staticmethod
	def encoding_adminlist(adminlist):
		respadminlist = ''
		for admin in adminlist:
			adminid = str(admin.getadminid())
			messagesid = str(admin.getmessagesid())
			username0 = str(admin.getusername())
			admintype = str(admin.getadmintype())
			userid = str(admin.getuserid())
			acceptuserid = str(admin.getacceptuserid())
			adminstime = str(admin.getadminstime())
			commentinfo = admin.getcommentinfo()

			msg = admin.getmessagesobject()
			msgid = str(msg.getmessagesid())
			userid = str(msg.getuserid())
			msginfo = msg.getmessagesinfo()
			agreenum = str(msg.getmessagesagreenum())
			transnum = str(msg.getmessagestranspondnum())
			time = str(msg.getmessagestime())
			username = msg.getusername()
			commentlist = msg.getcommentlist()
			comments = ''
			for c in commentlist:
				comid = str(c.getcommentid())
				cominfo = c.getcommentinfo()
				msgid = str(c.getmessagesid())
				userid = str(c.getuserid())
				ctime = str(c.getcommentstime())
				username1 = c.getusername()
				comments += comid+"!+-*"+cominfo+"!+-*"+msgid+"!+-*"+userid+"!+-*"+ctime+"!+-*"+username1+"****&&&&"
			msglist = msgid + '+-*#'+userid + '+-*#'+msginfo + '+-*#'+agreenum + '+-*#'+transnum + '+-*#'+time + '+-*#'+ username + '+-*#'+comments
		
			respadminlist += adminid + '**--+' + messagesid	+ '**--+' + username0 + '**--+' + admintype	+ '**--+' + userid + '**--+' + acceptuserid	+ '**--+' + adminstime + '**--+' + commentinfo + '**--+' + msglist + '####&&&&'

		return respadminlist
