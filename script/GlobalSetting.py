#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from Package.LogView import *
UtilDLL = cdll.LoadLibrary(r"Util.dll")
MultiWindowDLL = cdll.LoadLibrary(r"D:\MultiWindowDemo\x64\Debug\MultiWindow.dll")

class GlobalSetting:
    windowHandle1, windowHandle2, multiWindowHandle = c_longlong(0), c_longlong(0), c_longlong(0)
    parentDispViewHandle, logViewHandle = 0, 0

    @staticmethod
    def OnCreate_Event():
        LogView.attach(GlobalSetting.logViewHandle)
        LogView.normal(b"*** GlobalSetting::OnCreate_Event ***")
        MultiWindowDLL.Init(byref(GlobalSetting.multiWindowHandle))
        MultiWindowDLL.SetWindowTotalCount(GlobalSetting.multiWindowHandle, c_longlong(GlobalSetting.parentDispViewHandle), 2)
        childHandle1 = c_longlong(0)
        MultiWindowDLL.GetChildWindow(GlobalSetting.multiWindowHandle, 1, byref(childHandle1))
        UtilDLL.Vision3000_Halcon_CreateWindow(childHandle1, byref(GlobalSetting.windowHandle1))
        childHandle2 = c_longlong(0)
        MultiWindowDLL.GetChildWindow(GlobalSetting.multiWindowHandle, 2, byref(childHandle2))
        UtilDLL.Vision3000_Halcon_CreateWindow(childHandle2, byref(GlobalSetting.windowHandle2))

    @staticmethod
    def OnRunning_Event():
        LogView.normal(c_char_p(b"*** GlobalSetting::OnRunning_Event ***"))
    
    @staticmethod
    def OnDestory_Event():
        LogView.normal(b"*** GlobalSetting::OnDestory_Event ***")
        UtilDLL.Vision3000_Halcon_DestoryWindow(GlobalSetting.windowHandle1)
        UtilDLL.Vision3000_Halcon_DestoryWindow(GlobalSetting.windowHandle2)
        MultiWindowDLL.Release(GlobalSetting.multiWindowHandle)
