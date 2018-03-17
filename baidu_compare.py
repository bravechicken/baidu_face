# encoding:utf-8
import urllib, urllib2, sys,os
import ssl
import base64
import urllib
import urllib2
import json
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EL8U4aKIOXGHceWO4doLQs50&client_secret=y55tW4FAohCnLlGVhdm2eWVF9sGI6xMW'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
at = response.read()
#print at
dict = json.loads(at)
access_token = dict["access_token"]
# encoding:utf-8
import base64
import urllib
import urllib2

'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"

f = open('test1.png', 'rb')
# 参数images：图像base64编码
img1 = base64.b64encode(f.read())
# 二进制方式打开图文件
f = open('test2.png', 'rb')
# 参数images：图像base64编码
img2 = base64.b64encode(f.read())

params = {"images":img1 + ',' + img2}
params = urllib.urlencode(params)

#access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content
result = json.loads(content)
score = result["result"][0]["score"]
if score>=90:
	os.system("say 从我的卧室想到的宁静夜晚我正坐在我的卧室柔和的灯光下看着书，抬头向左右望去，我一抬眼就看到了我那张淡绿色的床,上面平整的铺着一张绘画着小熊卡通图案的床单，床头放着一个黄色的长方形枕头，床头边放的床头柜上放着我刚做好的几个乐高玩具，而在床头柜的前面就放着我的书柜，那只一个上面透明，而底下肉色的柜子，里面放着各种各样的书，在灯光的映照下反射出了耀眼的光芒，那些光芒五颜六色，亮的是那么的鲜嫩，那么的惹人喜爱，但我的目光开始回到了我的桌子上，我看着桌子愣起了神。渐渐的家里的宁静消失，而取而代之的则是混乱嘈杂的噪音，我向四周望去，我那张熟悉的床，我的书柜，桌子全部都消失不见了，我坐在了一个温暖整齐，干净的小屋里。窗外射进来了几束金灿灿的阳光，那几束阳光在不断的挪移着，变换着姿态，而屋里的黑暗就像清晨的雾气被阳光所蒸融，而渐渐消散。像其他的地方看去，这是一个不规则的长方形屋子，里面的家具不是特别的多，从我所做的椅子向周围望去，在右边墙面上有两对成双的画作，一幅幅都很抽象，而且风格极像是梵高的画风，我向下看是一张黄色的双人床,平整干爽的床单，上放着两个柔软舒适的黄色枕头，下面铺着一条干净的红色毯子，整个床给人一种温馨舒适的感觉。床边放着两把椅子一都是黄色的。而在房间的一个角落里还放着一个木质的桌子。从窗外射入的那几束阳光渐渐的变为了一束，而木制的桌子，也变成了我自己的桌子，窗外也变的十分宁静。我再次环顾了一下四周，这里是做自己的房间。")
else:
	os.system("say 不是同一个人")



