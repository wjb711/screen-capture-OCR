import time
import subprocess
import pyautogui
import cv2
def screencap():

    process = subprocess.Popen(r"adb shell screencap -p | sed 's/\r$//' > screen.png",shell=True)
    time.sleep(1)
def show():
    #cv2.destroyAllWindows()
    screencap()
    #time.sleep(0.5)
    img = cv2.imread('screen.png')
    img0=cv2.resize(img,(320,600),0,0)
    cv2.imshow('hello',img0)
    cv2.waitKey(1)
i=0
while True:
    try:
        show()
    except:
        pass
    i=i+1
    print(i)
