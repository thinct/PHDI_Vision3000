#!usr/bin/python
# -*- coding: utf-8 -*-


# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ImageCtrlWnd import *
#!<AnyLib: GlobalModule-Begin>
from globalSettingExample import *
#!<AnyLib: GlobalModule-End>


class ReadImageByFileExample:
    index = 1

    @staticmethod
    def OnCreate_Event():
        GlobalSettingExample.imageFilePath = r'D:\viewfile.jpg'
        Image.read(GlobalSettingExample.imgHandle, GlobalSettingExample.imageFilePath)
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)
        
    @staticmethod
    def OnRunning_Event():
        print 'ReadImageByFileExample.OnRunning_Event'
        GlobalSettingExample.imageFilePath = r'D:\%d.bmp'%ReadImageByFileExample.index
        ReadImageByFileExample.index = ReadImageByFileExample.index%2+1
        Image.read(GlobalSettingExample.imgHandle, GlobalSettingExample.imageFilePath)
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

    @staticmethod
    def OnDestory_Event():
        Image.release(ReadImageByFileExample.imgHandle)
        ImageCtrlWnd.destory(ReadImageByFileExample.windowHandle)


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    ReadImageByFileExample.OnCreate_Event()
    GlobalSettingExample.OnRunning_Event()
    ReadImageByFileExample.OnRunning_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
#!<AnyLib: Example-End>
