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
    t = Thread(target=dll.DeadLoop)

    @staticmethod
    def OnCreate_Event():
        LogView.normal(b"*** Open Camera ***")
        ImageAcqDLL.Init(byref(ReadImage_Threshold_T2.imageAcqHandle))
        ThresholdDLL.InstallLogger(GlobalSetting.logViewHandle)
        ThresholdDLL.Initialize()

    @staticmethod
    def OnRunning_Event():
        if (False != ReadImage_Threshold_T2.t.isAlive()):
            LogView.normal(b"*** busy!!! ***")
            return
        ReadImage_Threshold_T2.lRet = 9
        LogView.normal(b"*** ReadImage ***")
        ReadImage_Threshold_T2.t = Thread(target=dll.DeadLoop, args=(10000, ))
        ReadImage_Threshold_T2.t.start()
        return
        ImageAcqDLL.ReadImage(ReadImage_Threshold_T2.imageAcqHandle, \
                              r'D:\straight_edge.bmp', byref(ReadImage_Threshold_T2.image))
        LogView.normal(b"*** ReadImage 123***")
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

