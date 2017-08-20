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


class StraightEdgeForBottom:
    edgeHandle,ROIHandle,OverlayHandle = c_long(0), c_long(0), c_long(0)

    @staticmethod
    def OnCreate_Event():
        Image.read(GlobalSettingExample.imgHandle, r'D:\straight_edge.bmp')
        ImageCtrlWnd.displayImage(GlobalSettingExample.windowHandle, GlobalSettingExample.imgHandle)

        StraightEdgeForBottom.ROIHandle = ROI.init()
        StraightEdgeForBottom.OverlayHandle = Overlay.init()
        StraightEdgeForBottom.edgeHandle = StraightEdge.init()
        direction, type, polarity = 1, 0, 2
        StraightEdge.setDirection(StraightEdgeForBottom.edgeHandle, direction)
        StraightEdge.setType(StraightEdgeForBottom.edgeHandle, type)
        StraightEdge.setPolarity(StraightEdgeForBottom.edgeHandle, polarity)
        def ImageCtrlWnd_OnShapeResizeEvent(wid, ID):
            ImageCtrlWnd.getROI(wid, ID, StraightEdgeForBottom.ROIHandle)
            print ROI.type(StraightEdgeForBottom.ROIHandle)
            if 'rect2' != ROI.type(StraightEdgeForBottom.ROIHandle):
                return
            
            centerX, centerY, width, height, angle = ROI.getRect2(StraightEdgeForBottom.ROIHandle)
            print centerX, centerY, width, height, angle
            startX, startY, endX, endY = StraightEdge.search(StraightEdgeForBottom.edgeHandle, GlobalSettingExample.imgHandle, StraightEdgeForBottom.ROIHandle)

            ImageCtrlWnd.clearAllOverlay(wid)
            Overlay.genLine(StraightEdgeForBottom.OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
            ImageCtrlWnd.drawOverlay(wid, StraightEdgeForBottom.OverlayHandle)
            ImageCtrlWnd.refresh(wid)
         
        ImageCtrlWnd.registeShapeResizeEvent(GlobalSettingExample.windowHandle, ImageCtrlWnd_OnShapeResizeEvent)


    @staticmethod    
    def OnRunning_Event():
        print 'StraightEdgeForBottom.OnRunning_Event'
        startX, startY, endX, endY = StraightEdge.search(StraightEdgeForBottom.edgeHandle, GlobalSettingExample.imgHandle, StraightEdgeForBottom.ROIHandle)
        Overlay.genLine(StraightEdgeForBottom.OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
        ImageCtrlWnd.drawOverlay(GlobalSettingExample.windowHandle, StraightEdgeForBottom.OverlayHandle)
        #ImageCtrlWnd.refresh(GlobalSettingExample.windowHandle)

 
    @staticmethod
    def OnDestory_Event():
        Image.release(GlobalSettingExample.imgHandle)
        ImageCtrlWnd.destory(GlobalSettingExample.windowHandle)
        


#!<AnyLib: Example-Begin>
if __name__ == "__main__":
    QtEngine.startup()
    GlobalSettingExample.OnCreate_Event()
    StraightEdgeForBottom.OnCreate_Event()
    ImageCtrlWnd.looper(GlobalSettingExample.windowHandle)
#!<AnyLib: Example-End>
