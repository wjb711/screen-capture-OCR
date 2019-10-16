from PIL import Image, ImageDraw, ImageFont, ImageGrab  # pip install Pillow 一个运行速度非常快的数学库，主要用于数组计算
import cv2  # 下载方式：pip install opencv-python 用于图片的处理
import pyperclip  # pip install pyperclip 用于剪切板的复制粘贴
import numpy  # pip install numpy
import pyzbar.pyzbar as zbar  # pip install pyzbar
from pylibdmtx.pylibdmtx import decode # pip install pylibdmtx
import tkinter  # 窗口视图GUI
import easygui  # pip install easygui 简单图形界面


# 获取屏幕截图
def getScreenImage():
    # 抓取当前屏幕的快照并拷贝到PIL图像内存中
    all_Screen_Image = ImageGrab.grab()
    # 图像转换成RGB格式
    opencv_Image = cv2.cvtColor(numpy.array(all_Screen_Image), cv2.COLOR_RGB2BGR)
    # 构建视频流窗口
    cv2.namedWindow("ROI selector", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("ROI selector", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # 对视频流中的某一帧进行ROI的选择
    image_ROI = cv2.selectROI(opencv_Image)
    # 获取最终截取的图片(数组）
    image_End = opencv_Image[int(image_ROI[1]):int(image_ROI[1] + image_ROI[3]),
                int(image_ROI[0]):int(image_ROI[0] + image_ROI[2])]
    # 释放窗口，简单暴力释放掉所有的窗口
    cv2.destroyAllWindows()
    return image_End


# 获取二维码图像的扫描结果
def getScanResult():
    QR_Image = getScreenImage()
    QRCode = zbar.decode(QR_Image)
    DataMatrix = decode(QR_Image)
    # print(dir(QRCode), QRCode._len_, QRCode.sizeof(), QRCode.index)
    print(QRCode, type(QRCode), QR_Image.data, type(QR_Image))
    # 判断数组是否为空，为空则表示未扫描到QRCode二维码
    if QRCode:
        QR_DATA = (QRCode[0].data).decode('utf-8')
    elif DataMatrix:
        QR_DATA = (DataMatrix[0].data).decode('utf-8')
    else:
        QR_DATA = "未识别！！！"
    # 弹框提示结果
    easygui.msgbox(QR_DATA)
    # 将结果自动拷贝到剪切板
    pyperclip.copy(QR_DATA)


# 窗口显示
def win():
    # 生成主窗口
    Window = tkinter.Tk()
    # 窗口桌面置顶
    Window.wm_attributes('-topmost', 1)
    # 窗口的高：position_h, 窗口的宽：position_w
    # 窗口的右下角坐标（position_x，position_y)
    position_x = Window.winfo_screenwidth() - 150
    position_y = Window.winfo_screenheight() - 100
    position_h = 30
    position_w = 100
    # 设置窗口大小及位置
    Window.geometry('%dx%d+%d+%d' % (position_w, position_h, position_x, position_y))
    # 设置窗口大小不可变
    Window.resizable(width=False, height=False)
    # Button 按钮 , button(窗口， 内容， 执行的函数名) pack():表示在窗口显示
    tkinter.Button(Window, text="条码/二维码", command=getScanResult).pack()
    # 消息循环
    Window.mainloop()

def win1():

    window=tkinter.Tk()

    window.wm_attributes('-topmost',1)

    #window.title('转文本')

    position_x=window.winfo_screenwidth()-150

    window.geometry('%dx%d+%d+%d' % (100,30,(window.winfo_screenwidth()-100), (window.winfo_screenheight() - 100) ))

    window.resizable(width=False, height=False)



    button0=tkinter.Button(window, text="条码/二维码", command=getScanResult).pack()

    window.mainloop()


# main
if __name__ == "__main__":
    print('start')
    win()




