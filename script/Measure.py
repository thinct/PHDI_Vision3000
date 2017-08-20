#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from Package.LogView import *

MeasureDLL = cdll.LoadLibrary(r"test.dll")


class Measure:

    @staticmethod
    def OnCreate_Event():
        pass

    @staticmethod
    def OnRunning_Event():
        pass
    
    @staticmethod
    def OnDestory_Event():
        pass


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    pass
#!<AnyLib: Example-End>

