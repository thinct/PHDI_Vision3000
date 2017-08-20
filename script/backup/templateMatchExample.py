#!usr/bin/python
# -*- coding: utf-8 -*-


# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ROI import *
from Package.Overlay import *
from Package.ScriptPlugin import *
from Package.ImageCtrlWnd import *
from Package.TemplateMatch import *
#!<AnyLib: GlobalModule-Begin>
from globalSettingExample import *
#!<AnyLib: GlobalModule-End>


class TemplateMatchExample:
    matchHandle,TImgHandle,ROIHandle,OverlayHandle = c_long(0), c_long(0), c_long(0), c_long(0)

    @staticmethod
    def OnCreate_Event():
        Image.read(GlobalSettingExample.imgHandle, r'D:\viewfile.jpg')
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

        TemplateMatchExample.ROIHandle = ROI.init()
        TemplateMatchExample.OverlayHandle = Overlay.init()
        TemplateMatchExample.matchHandle = TemplateMatch.init()
        TemplateMatch.setMaxCount(TemplateMatchExample.matchHandle, 1)
        def ImageCtrlWnd_OnShapeResizeEvent(wid, ID):
            ImageCtrlWnd.getROI(wid, ID, TemplateMatchExample.ROIHandle)
            print ROI.type(TemplateMatchExample.ROIHandle)
            if 'rect1' != ROI.type(TemplateMatchExample.ROIHandle):
                return

            TemplateMatchExample.TImgHandle = ImageProcessor.rect(GlobalSettingExample.imgHandle, TemplateMatchExample.ROIHandle)
            TemplateMatch.buildTemplate(TemplateMatchExample.matchHandle, TemplateMatchExample.TImgHandle)
            centerX,centerY,score,angle = TemplateMatch.match(TemplateMatchExample.matchHandle, GlobalSettingExample.imgHandle)
            TemplateMatch.setMaxCount(TemplateMatchExample.matchHandle, 1)

            arrayLen = VarArray.length(centerX)
            if 1==arrayLen:
                fScore = VarArray.floatVar(score, 0)
                fcenterX = VarArray.floatVar(centerX, 0)
                fcenterY = VarArray.floatVar(centerY, 0)
                fangle = VarArray.floatVar(angle, 0)

                ImageCtrlWnd.clearAllOverlay(wid)
                Overlay.genPoint(TemplateMatchExample.OverlayHandle, c_double(fcenterX), c_double(fcenterY))                
                ImageCtrlWnd.drawOverlay(wid, TemplateMatchExample.OverlayHandle)
                GlobalSettingExample.resultDisplay += "score:%5.2f, center(%5.2f,%5.2f), angle:%5.2f\n"%(fScore,fcenterX,fcenterY, fangle)
                Overlay.genText(TemplateMatchExample.OverlayHandle, c_double(0), c_double(0), GlobalSettingExample.resultDisplay, 10)                
                ImageCtrlWnd.drawOverlay(wid, TemplateMatchExample.OverlayHandle)
                ImageCtrlWnd.refresh(wid)
         
        ImageCtrlWnd.registeShapeResizeEvent(GlobalSettingExample.windowHandle, ImageCtrlWnd_OnShapeResizeEvent)


    @staticmethod    
    def OnRunning_Event():
        centerX,centerY,score,angle = TemplateMatch.match(TemplateMatchExample.matchHandle, GlobalSettingExample.imgHandle)
        if 0 == TemplateMatchExample.TImgHandle.value:
            return
        arrayLen = VarArray.length(centerX)
        if 1==arrayLen:
            fScore = VarArray.floatVar(score, 0)
            fcenterX = VarArray.floatVar(centerX, 0)
            fcenterY = VarArray.floatVar(centerY, 0)
            fangle = VarArray.floatVar(angle, 0)

            ImageCtrlWnd.clearAllOverlay(GlobalSettingExample.windowHandle)
            Overlay.genPoint(TemplateMatchExample.OverlayHandle, c_double(fcenterX), c_double(fcenterY))                
            ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, TemplateMatchExample.OverlayHandle)
            GlobalSettingExample.resultDisplay += "score:%5.2f, center(%5.2f,%5.2f), angle:%5.2f\n"%(fScore,fcenterX,fcenterY, fangle)
            Overlay.genText(TemplateMatchExample.OverlayHandle, c_double(0), c_double(0), GlobalSettingExample.resultDisplay, 35)            
            ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, TemplateMatchExample.OverlayHandle)
            ImageCtrlWnd.refresh(GlobalSettingExample.windowHandle)

 
    @staticmethod
    def OnDestory_Event():
        Image.release(GlobalSettingExample.imgHandle)
        ImageCtrlWnd.destory(GlobalSettingExample.windowHandle)
        


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    TemplateMatchExample.OnCreate_Event()
    TemplateMatchExample.OnRunning_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
#!<AnyLib: Example-End>
