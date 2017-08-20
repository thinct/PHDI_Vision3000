#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from Package.LogView import *

UtilDLL = cdll.LoadLibrary(r"Util.dll")

class GlobalSettingExample:
    windowHandle = c_long(0)
    parentDispViewHandle, logViewHandle = 0, 0

    @staticmethod
    def OnCreate_Event():
        LogView.attach(GlobalSettingExample.logViewHandle)
        LogView.normal(b"*** OnCreate_Event ***")
        UtilDLL.Vision3000_Halcon_CreateWindow(GlobalSettingExample.parentDispViewHandle, byref(GlobalSettingExample.windowHandle))

    @staticmethod
    def OnRunning_Event():
        LogView.normal(b"*** OnRunning_Event ***")
    
    @staticmethod
    def OnDestory_Event():
        LogView.normal(b"*** OnDestory_Event ***")
        UtilDLL.Vision3000_Halcon_DestoryWindow(GlobalSettingExample.windowHandle)

    @staticmethod
    def OnResize_Event(): 
        LogView.normal(b"*** OnResize_Event ***")     
        UtilDLL.Vision3000_Halcon_ResizeWindow(GlobalSettingExample.windowHandle, byref(GlobalSettingExample.windowHandle))  
        if "AnyLib_Global" in dir():
            ThresholdDLL.SetParameter("winHandle", GlobalSettingExample.windowHandle)


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    GlobalSettingExample.OnCreate_Event()
#!<AnyLib: Example-End>

