#!usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *

AnyLib_ScriptPlugin = cdll.LoadLibrary("AnyLib_VMDataBuffer.dll")

class ScriptPlugin:

    @staticmethod
    def registerIntItem(varFullName, ref):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_RegisterIntItem(varFullName, c_longlong(ref))

    @staticmethod
    def registerLongItem(varFullName, ref):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_RegisterLongItem(varFullName, c_longlong(ref))

    @staticmethod
    def registerFloatItem(varFullName, ref):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_RegisterFloatItem(varFullName, c_longlong(ref))

    @staticmethod
    def registerStringItem(varFullName, ref):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_RegisterStringItem(varFullName, c_longlong(ref))
        
    @staticmethod
    def unregisterItem(varFullName):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_UnregisterItem(varFullName)
        
    @staticmethod
    def updateIntItem(varFullName, number):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_UpdateIntItem(varFullName, c_int(number))
        
    @staticmethod
    def updateLongItem(varFullName, number):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_UpdateLongItem(varFullName, c_long(number))
        
    @staticmethod
    def updateFloatItem(varFullName, number):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_UpdateFloatItem(varFullName, c_float(number))
        
    @staticmethod
    def updateStringItem(varFullName, str):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_UpdateStringItem(varFullName, str)

    @staticmethod
    def updateThreadInfo(groupName, threadName, labelName):
        AnyLib_ScriptPlugin.AnyLib_VMDataBuffer_UpdateThreadInfo(\
            groupName, threadName, labelName if labelName is not None else b"")


        
# 示例
if __name__ == "__main__":
    iNum = c_int(123)
    ScriptPlugin.registerIntItem("test.iNum", byref(iNum))
    ScriptPlugin.updateIntItem("test.iNum", 321)
    print 'iNum={}'.format(iNum)

    str = create_string_buffer(b'Hello', 512)
    ScriptPlugin.registerStringItem('test.String', str)
    ScriptPlugin.updateStringItem('test.String', b'Hello, Sunrise!')
    print 'str={}'.format(str.value)
    
    


