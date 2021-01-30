import os
import datetime
import time
#闰年判定
def ifrn(yearnow):
	if(int(yearnow)%400==0):#闰年
		r=1
	elif(int(yearnow)%100==0):#平年
		r=0
	elif(int(yearnow)%4==0):#闰年
		r=1
	else:#平年
		r=0
	return int(r)

#获取当前日期
_date_now=datetime.datetime.now()
hourbefore=_date_now.strftime('%H')
#修改日期为可用日期
_date = datetime.datetime.strptime("2019/05/25","%Y/%m/%d")
os.system('date {}'.format(_date))

#启动MindManager.exe
cmd='start MindManager.exe'
if(os.system(cmd)==1):
	msg='echo msgbox "请将此程序放置在MindManager.exe同一目录下，以管理员权限运行",64,"大哥你运行程序之前不看readme的吗？？？？？">alert.vbs && start alert.vbs && ping -n 2 127.1>nul && del alert.vbs'
	os.system(msg)

#获取延迟秒数，默认10秒
try:
	with open('delay.txt',"r") as f:
		delay=float(f.read())
except:
	delay=10


#延迟
time.sleep(delay)

#改回正常日期
hourafter=datetime.datetime.now().strftime('%H')
_today=str(_date_now)[:10]
yearnow=_today[:4]
monthnow=_today[6:7]
daynow=_today[8:10]
if(int(hourbefore) == 23 and int(hourafter) == 0):
	if(int(monthnow)==12 and int(daynow)==31):#跨年了
		_today=str(int(yearnow)+1)+'-01-01'
	elif(monthnow in '01,03,05,07,08,10' and int(daynow)==31):#跨大月
		_today=yearnow+str(int(monthnow)+1)+'-01'
	elif(monthnow in '04,06,09,11' and int(daynow)==30):#跨小月
		_today=yearnow+'-'+str(int(monthnow)+1)+'-01'
	elif(ifrn(int(yearnow))==1 and int(daynow)==29):#跨闰年二月
		_today=yearnow+'-03-01'
	elif(ifrn(int(yearnow))==0 and int(daynow)==28):#跨平年二月
		_today=yearnow+'-03-01'
	else:#跨日不跨月
		_today=yearnow + '-'  + monthnow + '-' + str(int(daynow)+1)
else:
	_today=str(_date_now)[:10]
_date = datetime.datetime.strptime(_today,"%Y-%m-%d")
os.system('date {}'.format(_date))

