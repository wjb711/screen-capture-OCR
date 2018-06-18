# screen-capture-OCR
#screen-capture-OCR
#本程序目的是截取屏幕，上传至数据库， ocr识别文字后发回客户端
#依赖库的安装pip install opencv-python Pillow baidu-aip easygui
#大致方法是，1，tkinter创建窗口，上面有一个按钮button, 按钮位于屏幕右下角
#按下按钮后， 截屏，并满屏显示，再后来使用opencv截取矩形框，也就是需要识别文字的地方
#最后，把图片上传到服务器上，获取到在线ocr文字后，同过easygui返回。
主程序是 Opencv_Screen_OCR_selectROI.py
