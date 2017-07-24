#!usr/bin/python
# -*- coding: utf-8 -*-

# 1. 加载模块
from ctypes import *

LogViewDLL = cdll.LoadLibrary(r'AnyLib_LogView.dll')

class LogView:
    
    @staticmethod
    def attach(handle):
        LogViewDLL.AnyLib_LogView_Attach(c_longlong(handle))
        
    @staticmethod
    def normal(info):
        LogViewDLL.AnyLib_LogView_Normal(info)
        
    @staticmethod
    def error(info):
        LogViewDLL.AnyLib_LogView_Error(info)
        
