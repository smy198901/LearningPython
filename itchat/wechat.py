import itchat

itchat.login() #生成一个登陆二维码，扫描二维码登陆微信

friends = itchat.get_friends(update=True)[0:]

print(friends)