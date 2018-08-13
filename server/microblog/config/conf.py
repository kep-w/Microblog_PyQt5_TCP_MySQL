# conf.py

'''配置文件获取模块'''

import configparser
 

class ConfigReader(object):
	def __init__(self,path):
		self.CReader = configparser.ConfigParser()
		self.CReader.readfp(open(path), 'rb')

	def getSection(self):
		return self.CReader.sections()

	def getdic(self,section):
		s={}
		for k,v in self.CReader.items(section):
			s[k]=v
		return s

def getserverdic():
	cf = ConfigReader("./config.ini")
	serverdic = cf.getdic("server")	
	return serverdic

def getdbdic():
	cf = ConfigReader("./config.ini")
	dbdic = cf.getdic("mysql")
	return dbdic

def main():
	dic = getdbdic()
	
	print(dic.get('port'))

if __name__ == '__main__':
	main()





