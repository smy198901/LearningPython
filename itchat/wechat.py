import itchat
from itchat.content import *
import xlrd
import pymysql
import os


#自动添加好友，并打招呼
@itchat.msg_register(FRIENDS)
def auto_add_friend(msg):
	itchat.add_friend(**msg['Text'])
	itchat.send_msg('[自动回复]\n你好，我是您专属O2O运营教练。欢迎您与我交流一切关于合伙人拓展销售、互联网运营的相关问题。欢迎多多交流，彼此相互学习，共同成长！\n我们为您打造了有情怀的朋友圈，如果您不知道朋友圈发什么的时候，欢迎来搬运。\n如果您在销售过程里碰到什么疑难问题，欢迎随时与我沟通。',toUserName=msg['RecommendInfo']['UserName'])

#根据关键字自动回复
@itchat.msg_register([TEXT,PICTURE,NOTE,RECORDING,ATTACHMENT,VIDEO])
def auto_reply(msg):
	db = pymysql.connect("localhost","root","root","zhwhb")
	cursor = db.cursor()
	if msg['Type'] == 'Text':
		message = msg['Text']#获取文本信息
		reply_msg = '[自动回复]'
		if message[0:3] == "问题-":
			#当符合问题关键字时，做以下操作
			str_message = message[3:]
			cursor.execute("SELECT *FROM cost limit 2")
			data = cursor.fetchall()#获取所有结果
			for row in data:
				reply_msg = reply_msg + "\n" + str(row[0]) + ":" + str(row[1])
		itchat.send_msg(reply_msg,toUserName=msg['FromUserName'])

		db.close()
	else:
		itchat.send_msg("[自动回复]\n无法识别",toUserName=msg['FromUserName'])
		itchat.send_msg("[自动回复]\n123",toUserName=msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()
