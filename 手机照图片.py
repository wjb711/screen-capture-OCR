import time
import subprocess
import pyautogui
import cv2

#每次操作的间隔时间取决于手机配置，配置越高时间越短
sleep_time = 1
def open():
    time.sleep(3)
    process = subprocess.Popen('adb shell am start -n cn.xuexi.android/com.alibaba.android.rimet.biz.XuexiSchemeTransferActivity',shell=True)
    time.sleep(5)
    #show()
def close():
    process = subprocess.Popen('adb shell am force-stop -n cn.xuexi.android/com.alibaba.android.rimet.biz.XuexiSchemeTransferActivity',shell=True)
    time.sleep(5)
    #show()
    
def swipe():
    
    process = subprocess.Popen('adb shell input swipe 200 1750 200 1300',shell=True)
    time.sleep(5)
    #show()
def click():
    process = subprocess.Popen('adb shell input tap 200 1300',shell=True)
    time.sleep(8)
    #show()
def click1():
    process = subprocess.Popen('adb shell input tap 172 440',shell=True)
    time.sleep(sleep_time)
    #show()
def dianzan():
    process = subprocess.Popen('adb shell input tap 302 1755',shell=True)
    time.sleep(sleep_time)
    #show()
def back():
    process = subprocess.Popen('adb shell input keyevent 4',shell=True)
    time.sleep(sleep_time)
def last():
    process = subprocess.Popen('adb shell input keyevent 123',shell=True)
    time.sleep(sleep_time)
def screencap():

    process = subprocess.Popen(r"adb shell screencap -p | sed 's/\r$//' > screen.png",shell=True)
    time.sleep(sleep_time)
def find_pic(x):
    screencap()
    x,y,w,h=pyautogui.locate(x,'screen.png',confidence=0.9)
    x0=x+int(w/2)
    y0=y+int(h/2)
    print(x0,y0)
    process = subprocess.Popen('adb shell input tap {} {}'.format(x0,y0),shell=True)

    time.sleep(sleep_time)

def show():
    screencap()
    try:
        time.sleep(0.5)
        img = cv2.imread('screen.png')
        img0=cv2.resize(img,(320,500),0,0)
        cv2.imshow('demo',img0)
        cv2.waitKey(1)
    except:
        pass
    

if __name__=='__main__':
    print('start')
    
    #open()

    
    i=0
    while i<1000:
        swipe()
        click()
        swipe()
        swipe()
        swipe()
        swipe()
        swipe()
        #click1()
        #last()
        #dianzan()
        back()
        i=i+1
        print(i)
    back()
    back()
    back()
    back()    
    close()
    print('End')
