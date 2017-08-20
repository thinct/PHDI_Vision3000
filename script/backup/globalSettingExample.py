#!usr/bin/python
# -*- coding: utf-8 -*-


# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ImageCtrlWnd import *


class GlobalSettingExample:
    
    imgHandle,windowHandle = c_long(0), c_long(0)
    parentWindowHandle, x, y, width, height = 0, 0, 0, 768, 680
    imageFilePath = r'D:\Image\WD\FL130130-R-01 WD-5mm.bmp'
    resultDisplay = ''

    @staticmethod
    def OnCreate_Event():
        GlobalSettingExample.imgHandle = Image.init()
        Image.read(GlobalSettingExample.imgHandle, GlobalSettingExample.imageFilePath)
        print GlobalSettingExample.imageFilePath
        GlobalSettingExample.windowHandle = ImageCtrlWnd.create(GlobalSettingExample.parentWindowHandle,
                                                                  GlobalSettingExample.x,
                                                                  GlobalSettingExample.y,
                                                                  GlobalSettingExample.width,
                                                                  GlobalSettingExample.height)
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

    @staticmethod
    def OnRunning_Event():
        GlobalSettingExample.resultDisplay = ''
    
    @staticmethod
    def OnDestory_Event():
        Image.release(GlobalSettingExample.imgHandle)
        ImageCtrlWnd.destory(GlobalSettingExample.windowHandle)

    @staticmethod
    def OnResize_Event():
        ImageCtrlWnd.resize(GlobalSettingExample.windowHandle, GlobalSettingExample.width, GlobalSettingExample.height)
        


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    GlobalSettingExample.OnRunning_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
#!<AnyLib: Example-End>

