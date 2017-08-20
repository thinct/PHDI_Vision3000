#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from Package.LogView import *

InitCameraDLL = cdll.LoadLibrary(r"test.dll")


class InitCamera:
    image = c_long(0)

    @staticmethod
    def OnCreate_Event():
        LogView.normal(b"*** 打开相机 ***")

    @staticmethod
    def OnRunning_Event():
        LogView.normal(b"***  ***")
    
    @staticmethod
    def OnDestory_Event():
        pass


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    pass
#!<AnyLib: Example-End>

