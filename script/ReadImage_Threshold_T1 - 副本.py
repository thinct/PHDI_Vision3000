#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from threading import Thread
from Package.LogView import *

ImageAcqDLL = cdll.LoadLibrary(r"ImageAcq.dll")
ThresholdDLL = cdll.LoadLibrary(r"C:\Users\SUNRISE\Documents\Visual Studio 2013\Projects\Threshold\x64\Debug\Threshold.dll")

class ReadImage_Threshold_T1:


    imageAcqHandle = c_longlong(0)
    image = c_longlong(0)
    lRet = 0

    @staticmethod
    def OnCreate_Event():
        LogView.normal(b"*** ReadImage_Threshold::Open Camera ***")
        ImageAcqDLL.Init(byref(ReadImage_Threshold_T1.imageAcqHandle))
        ThresholdDLL.InstallLogger(GlobalSetting.logViewHandle)
        ThresholdDLL.Initialize()

    @staticmethod
    def OnRunning_Event():
        ReadImage_Threshold_T1.lRet = 9
        LogView.normal(b"*** ReadImage_Threshold::ReadImage ***")
        ImageAcqDLL.ReadImage(ReadImage_Threshold_T1.imageAcqHandle, \
                              r'D:\Image\WD\FL130130-R-02 WD-5mm.bmp', byref(ReadImage_Threshold_T1.image))
        UtilDLL.Vision3000_Halcon_ImageFitWindow(ReadImage_Threshold_T1.image, GlobalSetting.windowHandle1)
        UtilDLL.Vision3000_Halcon_DisplayObj(GlobalSetting.windowHandle1, ReadImage_Threshold_T1.image)
        ThresholdDLL.SetParameter(b'winHandle', GlobalSetting.windowHandle1)
        ThresholdDLL.SetParameter(b'image', ReadImage_Threshold_T1.image)
        ThresholdDLL.SetParameter(b'lowValue', 50)
        ThresholdDLL.SetParameter(b'highValue', 90)
        t = Thread(target=ThresholdDLL.Action)
        t.start()
        #t.join()
        ThresholdDLL.Action()
    
    @staticmethod
    def OnDestory_Event():
        LogView.normal(b"*** ReadImage_Threshold::OnDestory_Event ***")
        ThresholdDLL.Release()
        ImageAcqDLL.Release(ReadImage_Threshold_T1.imageAcqHandle)


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    pass
#!<AnyLib: Example-End>

