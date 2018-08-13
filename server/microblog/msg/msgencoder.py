# msg.py
import time
import xmltodict

class XmlMsgHeader(object):
    def __init__(self,transtype):
        self.interfaceVersion = '00.00.00'
        self.transTimeSource = time.strftime("%Y%m%d%H%M%S")
        self.transTimeDestination = time.strftime("%Y%m%d%H%M%S")
        self.source = 'C'
        self.destination = 'S'
        self.transType = transtype

    def get_dict(self):
        header_dict = {}
        header_dict['header'] = self.__dict__
        return header_dict
        

class XmlMsgBody(object):
    def __init__(self, body_dict):
        body = {}
        body['body'] = body_dict
        self._body = body
    def getbody(self):
        return self._body


class MsgEncoder(object):
    def __init__(self, header, body):
        self._header = header
        self._body = body
    def getheader(self):
        return self._header
    def getbody(self):
        return self._body

    def generate_xml(self):
        xml_dict = {}
        xml_dict['microblog'] = dict(self.getheader().get_dict(),**self.getbody().getbody())
        return xmltodict.unparse(xml_dict)

        
        
        


# header = XmlMsgHeader('1002')
# bodydict = {'LoginReq':{'username':'zhangsan', 'passwd':'123456'}}
# body = XmlMsgBody(bodydict)


# xml = MsgEncoder(header,body)
# print(xml.generate_xml())