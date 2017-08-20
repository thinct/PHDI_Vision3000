#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from threading import Thread
from Package.LogView import *

dll = cdll.LoadLibrary(r'D:\dead_loop.dll')
ImageAcqDLL = cdll.LoadLibrary(r"ImageAcq.dll")
ThresholdDLL = cdll.LoadLibrary(r"C:\Users\SUNRISE\Documents\Visual Studio 2013\Projects\Threshold\x64\Debug\Threshold.dll")


class ReadImage_Threshold_T2:
    imageAcqHandle = c_longlong(0)
    image = c_longlong(0)
    lRet = 0
    thread = None

    @staticmethod
    def OnCreate_Event():
        LogView.normal(b"*** Open Camera ***")
        ImageAcqDLL.Init(byref(ReadImage_Threshold_T2.imageAcqHandle))
        ThresholdDLL.InstallLogger(GlobalSetting.logViewHandle)
        ThresholdDLL.Initialize()

    @staticmethod
    def OnRunning_Event():
        ReadImage_Threshold_T2.lRet = 9
        ImageAcqDLL.ReadImage(ReadImage_Threshold_T2.imageAcqHandle, \
                              r'D:\straight_edge.bmp', byref(ReadImage_Threshold_T2.image))

        
        ReadImage_Threshold_T2.thread = Thread(target=ImageAcqDLL.ReadImage, args=(1000,))
        ReadImage_Threshold_T2.thread.start()
        ScriptPlugin.updateThreadInfo('ReadImage_Threshold_T2', 'thread', 'Action()')

    @staticmethod
    def Action():
        LogView.normal(b"*** ReadImage finished***")
        return
        UtilDLL.Vision3000_Halcon_ImageFitWindow(ReadImage_Threshold_T2.image, GlobalSetting.windowHandle2)
        UtilDLL.Vision3000_Halcon_DisplayObj(GlobalSetting.windowHandle2, ReadImage_Threshold_T2.image)
        ThresholdDLL.SetParameter(b'winHandle', GlobalSetting.windowHandle2)
        ThresholdDLL.SetParameter(b'image', ReadImage_Threshold_T2.image)
        ThresholdDLL.SetParameter(b'lowValue', 50)
        ThresholdDLL.SetParameter(b'highValue', 90)
        ThresholdDLL.Action()
     
    
    @staticmethod
    def OnDestory_Event():
        ThresholdDLL.Release()
        ImageAcqDLL.Release(ReadImage_Threshold_T2.imageAcqHandle)


#!<AnyLib: Example-Begin>
        
if __name__ == "__main__":
    pass
#!<AnyLib: Example-End>

