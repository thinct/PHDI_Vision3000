#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from ctypes import *
from Package.LogView import *

class GlobalSetting:
    logViewHandle = 0

    @staticmethod
    def OnCreate_Event():
        LogView.attach(GlobalSetting.logViewHandle)
        LogView.normal(b"*** GlobalSetting::OnCreate_Event ***")

    @staticmethod
    def OnRunning_Event():
        LogView.normal(c_char_p(b"*** GlobalSetting::OnRunning_Event ***"))
    
    @staticmethod
    def OnDestory_Event():
        LogView.normal(b"*** GlobalSetting::OnDestory_Event ***")
