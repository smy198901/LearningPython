#采用itchat实现微信自动回复功能

自动回复功能：
1、根据关键字查找数据库中的相关问题，返回问题序号和问题。
2、根据问题序号，返回问题和问题解答。

关键字定义：
1、“问题-”

用到的库：
1、itchat：
微信的python接口
2、PyMySQL：
python3版本中用于连接MySQL服务器的一个库
# 打开数据库连接
db = pymysql.connect("localhost","root","root","zhwhb")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
# 关闭数据库连接
db.close()


