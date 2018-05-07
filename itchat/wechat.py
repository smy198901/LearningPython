import itchat
from itchat.content import *
import xlrd
	
#自动添加好友，并打招呼
@itchat.msg_register(FRIENDS)
def auto_add_friend(msg):
	itchat.add_friend(**msg['Text'])
	itchat.send_msg('[自动回复]\n你好，我是您专属O2O运营教练。欢迎您与我交流一切关于合伙人拓展销售、互联网运营的相关问题。欢迎多多交流，彼此相互学习，共同成长！\n我们为您打造了有情怀的朋友圈，如果您不知道朋友圈发什么的时候，欢迎来搬运。\n如果您在销售过程里碰到什么疑难问题，欢迎随时与我沟通。',toUserName=msg['RecommendInfo']['UserName'])

#根据关键字自动回复
@itchat.msg_register([TEXT,PICTURE,NOTE,RECORDING,ATTACHMENT,VIDEO])
def auto_reply(msg):
	if msg['Type'] == 'Text':
		workbook = xlrd.open_workbook('C:\\Users\\lenovo\\Desktop\\商户清单.xls')
		sheet = workbook.sheets()[0]
		flag = False
		reply_msg = '[自动回复]\n没有找到该商户'
		for i in range(sheet.nrows):
			str = sheet.row_values(i)
			if msg['Text'] in str[0]:
				flag = True
				reply_msg = '[自动回复]\n商户名称：'+str[0]+'\n结算类型：'+str[1]
				itchat.send_msg(reply_msg,toUserName='filehelper')

		if flag == False:
			itchat.send_msg(reply_msg,toUserName='filehelper')
	# else:
	# 	itchat.send_msg("请使用文本信息",msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()
