# msgdecoder.py

'''消息报文解析类'''
import xml.sax  
import xml.sax.handler  

class MsgDecoder(xml.sax.handler.ContentHandler):  
	def __init__(self):  
		self.buffer = ""
		self.mapping = {}

	def startElement(self, name, attributes):  
		self.buffer = ""

	def characters(self, data):  
		self.buffer += data

	def endElement(self, name):  
		self.mapping[name] = self.buffer

	def getDict(self):
		return self.mapping

def decode_msg_to_dict(msg):
	msgd = MsgDecoder()  
	xml.sax.parseString(msg, msgd)  
	ret = msgd.getDict() 
	return ret




def main():
	data = """00363<?xml version="1.0" encoding="UTF-8"?><microblog><header><interfaceVersion></interfaceVersion><transTimeSource></transTimeSource><transTimeDestination></transTimeDestination><transType>1001</transType><source></source><destination></destination></header><body><LoginReq><username>zhangsan</username><passwd>123456</passwd><mac></mac></LoginReq></body></microblog>"""
	ret = decode_msg_to_dict(data[5:]) 
	print(ret)

if __name__ == "__main__":
    main()




