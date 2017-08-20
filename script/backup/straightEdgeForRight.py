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


class StraightEdgeForRight:

    @staticmethod
    def OnCreate_Event():
        Image.read(GlobalSettingExample.imgHandle, r'D:\straight_edge.bmp')
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

        ROIHandle = ROI.init()
        OverlayHandle = Overlay.init()
        edgeHandle = StraightEdge.init()
        direction, type, polarity = 3, 0, 2
        StraightEdge.setDirection(edgeHandle, direction)
        StraightEdge.setType(edgeHandle, type)
        StraightEdge.setPolarity(edgeHandle, polarity)
        def ImageCtrlWnd_OnShapeResizeEvent(wid, ID):
            ImageCtrlWnd.getROI(wid, ID, ROIHandle)
            print ROI.type(ROIHandle)
            if 'rect2' != ROI.type(ROIHandle):
                return
            
            centerX, centerY, width, height, angle = ROI.getRect2(ROIHandle)
            print centerX, centerY, width, height, angle
            startX, startY, endX, endY = StraightEdge.search(edgeHandle, GlobalSettingExample.imgHandle, ROIHandle)
            
            ImageCtrlWnd.clearAllOverlay(wid)
            Overlay.genLine(OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
            ImageCtrlWnd.drawOverlay(wid, OverlayHandle)
            ImageCtrlWnd.refresh(wid)
         
        ImageCtrlWnd.registeShapeResizeEvent(GlobalSettingExample.windowHandle, ImageCtrlWnd_OnShapeResizeEvent)


    @staticmethod    
    def OnRunning_Event():
        print 'StraightEdgeForRight.OnRunning_Event'
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

 
    @staticmethod
    def OnDestory_Event():
        Image.release(GlobalSettingExample.imgHandle)
        ImageCtrlWnd.destory(GlobalSettingExample.windowHandle)
        


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    StraightEdgeForRight.OnCreate_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
    StraightEdgeForRight.OnDestory_Event()
#!<AnyLib: Example-End>
