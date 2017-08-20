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


class StraightEdgeForTop:

    @staticmethod
    def OnCreate_Event():
        Image.read(GlobalSettingExample.imgHandle, r'D:\straight_edge.bmp')
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

        StraightEdgeForTop.ROIHandle = ROI.init()
        StraightEdgeForTop.OverlayHandle = Overlay.init()
        StraightEdgeForTop.edgeHandle = StraightEdge.init()
        direction, type, polarity = 0, 0, 2
        StraightEdge.setDirection(StraightEdgeForTop.edgeHandle, direction)
        StraightEdge.setType(StraightEdgeForTop.edgeHandle, type)
        StraightEdge.setPolarity(StraightEdgeForTop.edgeHandle, polarity)
        def ImageCtrlWnd_OnShapeResizeEvent(wid, ID):
            ImageCtrlWnd.getROI(wid, ID, StraightEdgeForTop.ROIHandle)
            print ROI.type(StraightEdgeForTop.ROIHandle)
            if 'rect2' != ROI.type(StraightEdgeForTop.ROIHandle):
                return
            
            centerX, centerY, width, height, angle = ROI.getRect2(StraightEdgeForTop.ROIHandle)
            print centerX, centerY, width, height, angle
            startX, startY, endX, endY = StraightEdge.search(StraightEdgeForTop.edgeHandle, GlobalSettingExample.imgHandle, StraightEdgeForTop.ROIHandle)
            
            ImageCtrlWnd.clearAllOverlay(wid)
            Overlay.genLine(StraightEdgeForTop.OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
            ImageCtrlWnd.drawOverlay(wid, StraightEdgeForTop.OverlayHandle)
            ImageCtrlWnd.refresh(wid)
         
        ImageCtrlWnd.registeShapeResizeEvent(GlobalSettingExample.windowHandle, ImageCtrlWnd_OnShapeResizeEvent)

    @staticmethod    
    def OnRunning_Event():
        print 'StraightEdgeForTop.OnRunning_Event'
        startX, startY, endX, endY = StraightEdge.search(StraightEdgeForLeft.edgeHandle, GlobalSettingExample.imgHandle, StraightEdgeForLeft.ROIHandle)
        Overlay.genLine(StraightEdgeForLeft.OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
        ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, StraightEdgeForLeft.OverlayHandle)
 
    @staticmethod
    def OnDestory_Event():
        Image.release(GlobalSettingExample.imgHandle)
        ImageCtrlWnd.destory(GlobalSettingExample.windowHandle)
        


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    StraightEdgeForTop.OnCreate_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
    StraightEdgeForTop.OnDestory_Event()
#!<AnyLib: Example-End>
