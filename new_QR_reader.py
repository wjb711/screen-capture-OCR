from PIL import Image,ImageDraw,ImageFont,ImageGrab

import cv2

import pyperclip

import numpy
from pyzbar.pyzbar import decode
import tkinter
import easygui

 

 

def screen_capture():

    img=ImageGrab.grab()

    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

   

    cv2.namedWindow("ROI selector", cv2.WND_PROP_FULLSCREEN)

    cv2.setWindowProperty("ROI selector", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

   

    r = cv2.selectROI(opencvImage)

    imCrop = opencvImage[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    #cv2.imwrite('tmp.png',imCrop)

    cv2.destroyAllWindows()
    x=decode(imCrop)
    #x=decode(Image.open('tmp.png'))
    y=x[0].data
    print(x,type(x),x[0],type(x[0]),dir(x[0]),x[0].data)
    t=y.decode('utf-8')
    print(t)
    easygui.msgbox(t)
    pyperclip.copy(t)
    #easygui.msgbox(y.decode())
    #return imCrop
def window():
    window=tkinter.Tk()
    window.wm_attributes('-topmost',1)
    #window.title('转文本')
    position_x=window.winfo_screenwidth()-150
    window.geometry('%dx%d+%d+%d' % (100,30,(window.winfo_screenwidth()-100), (window.winfo_screenheight() - 100) ))
    window.resizable(width=False, height=False)

    button0=tkinter.Button(window, text="条码/二维码", command=screen_capture).pack()
    window.mainloop()

print('start')
window()



