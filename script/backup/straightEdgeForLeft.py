#!usr/bin/python
# -*- coding: utf-8 -*-


# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ROI import *
from Package.Overlay import *
from Package.ScriptPlugin import *
from Package.ImageCtrlWnd import *
from Package.StraightEdge import *
#!<AnyLib: GlobalModule-Begin>
from globalSettingExample import *
#!<AnyLib: GlobalModule-End>


class StraightEdgeForLeft:
    edgeHandle,ROIHandle,OverlayHandle = c_long(0), c_long(0), c_long(0)
    centerX, centerY, width, height, angle = 0,0,0,0,0

    @staticmethod
    def OnCreate_Event():
        Image.read(GlobalSettingExample.imgHandle, r'C:/Users/sunrise/Desktop/DianJi.png')
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

        StraightEdgeForLeft.ROIHandle = ROI.init()
        ROI.genRect2(StraightEdgeForLeft.ROIHandle,
                     StraightEdgeForLeft.centerX, StraightEdgeForLeft.centerY, StraightEdgeForLeft.width, StraightEdgeForLeft.height, StraightEdgeForLeft.angle)
        StraightEdgeForLeft.OverlayHandle = Overlay.init()
        StraightEdgeForLeft.edgeHandle = StraightEdge.init()
        direction, type, polarity = 2, 0, 2
        StraightEdge.setDirection(StraightEdgeForLeft.edgeHandle, direction)
        StraightEdge.setType(StraightEdgeForLeft.edgeHandle, type)
        StraightEdge.setPolarity(StraightEdgeForLeft.edgeHandle, polarity)
        def ImageCtrlWnd_OnShapeResizeEvent(wid, ID):
            ImageCtrlWnd.getROI(wid, ID, StraightEdgeForLeft.ROIHandle)
            print ROI.type(StraightEdgeForLeft.ROIHandle)
            if 'rect2' != ROI.type(StraightEdgeForLeft.ROIHandle):
                return
            
            StraightEdgeForLeft.centerX, StraightEdgeForLeft.centerY, StraightEdgeForLeft.width, StraightEdgeForLeft.height, StraightEdgeForLeft.angle = ROI.getRect2(StraightEdgeForLeft.ROIHandle)
            print StraightEdgeForLeft.centerX, StraightEdgeForLeft.centerY, StraightEdgeForLeft.width, StraightEdgeForLeft.height, StraightEdgeForLeft.angle
            startX, startY, endX, endY = StraightEdge.search(StraightEdgeForLeft.edgeHandle, GlobalSettingExample.imgHandle, StraightEdgeForLeft.ROIHandle)

            ImageCtrlWnd.clearAllROI(wid)
            ImageCtrlWnd.clearAllOverlay(wid)
            Overlay.genLine(StraightEdgeForLeft.OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
            ImageCtrlWnd.drawOverlay(wid, StraightEdgeForLeft.OverlayHandle)
            GlobalSettingExample.resultDisplay += 'edge line: (%5.2f, %5.2f, %5.2f, %5.2f)\n'%(startX, startY, endX, endY)
            Overlay.genText(StraightEdgeForLeft.OverlayHandle, c_double(0), c_double(0), GlobalSettingExample.resultDisplay, 15)
            ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, StraightEdgeForLeft.OverlayHandle)
            ImageCtrlWnd.refresh(wid)
         
        ImageCtrlWnd.registeShapeResizeEvent(GlobalSettingExample.windowHandle, ImageCtrlWnd_OnShapeResizeEvent)


    @staticmethod    
    def OnRunning_Event():
        print StraightEdgeForLeft.centerX, StraightEdgeForLeft.centerY, StraightEdgeForLeft.width, StraightEdgeForLeft.height, StraightEdgeForLeft.angle
        print 'straightEdgeForLeft.OnRunning_Event'
        startX, startY, endX, endY = StraightEdge.search(StraightEdgeForLeft.edgeHandle, GlobalSettingExample.imgHandle, StraightEdgeForLeft.ROIHandle)
        ImageCtrlWnd.clearAllOverlay(GlobalSettingExample.windowHandle)
        Overlay.genLine(StraightEdgeForLeft.OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
        ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, StraightEdgeForLeft.OverlayHandle)
        GlobalSettingExample.resultDisplay += 'edge line: (%5.2f, %5.2f, %5.2f, %5.2f)\n'%(startX, startY, endX, endY)
        Overlay.genText(StraightEdgeForLeft.OverlayHandle, c_double(0), c_double(0), GlobalSettingExample.resultDisplay, 35)
        ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, StraightEdgeForLeft.OverlayHandle)
        ImageCtrlWnd.refresh(GlobalSettingExample.windowHandle)

 
    @staticmethod
    def OnDestory_Event():
        Image.release(GlobalSettingExample.imgHandle)
        ImageCtrlWnd.destory(GlobalSettingExample.windowHandle)
        


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    StraightEdgeForLeft.OnCreate_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
    StraightEdgeForLeft.OnDestory_Event()
#!<AnyLib: Example-End>
