
#include "stdafx.h"
#include "UtilAPI.h"
#include <functional>


#define HCPP_LEGACY_API
#define HCPP_LEGACY_NAMESPACE
#include "Halconcpp.h"
using namespace HalconCpp;


#define BEGIN_IMPLEMENT(funcFlag) long Vision3000_##funcFlag { AFX_MANAGE_STATE(AfxGetStaticModuleState());
#define END_IMPLEMENT return 0; }


/************************************************************************/
/* HalconWindow                                                         */
/************************************************************************/
static HWND parentWinHandle = NULL;


BEGIN_IMPLEMENT(Halcon_CreateWindow(Long parentHandle, Long* winHandle))
parentWinHandle = (HWND)parentHandle;
if (0 == parentHandle || !IsWindow(parentWinHandle)) {
	return -1;
}
RECT parentRect{ 0 };
GetClientRect(parentWinHandle, &parentRect);
HTuple* windowHandle = new HTuple(); 
Herror err = open_window(parentRect.top, parentRect.left
	, parentRect.right - parentRect.left, (parentRect.bottom - parentRect.top) 
	, (Hlong)parentWinHandle, "visible", "", windowHandle);
*winHandle = (Long)windowHandle;
END_IMPLEMENT




BEGIN_IMPLEMENT(Halcon_DestoryWindow(Long winHandle))
HTuple htWindow = *((HTuple*)winHandle);
close_window(htWindow);
delete (HTuple*)winHandle;
END_IMPLEMENT


BEGIN_IMPLEMENT(Halcon_ResizeWindow(Long winHandle))
HTuple htWindow = *((HTuple*)winHandle);
RECT parentRect{ 0 };
GetClientRect(parentWinHandle, &parentRect);
set_window_extents(htWindow, 0, 0, parentRect.right - parentRect.left, parentRect.bottom - parentRect.top);
::InvalidateRect(parentWinHandle, &parentRect, TRUE);
END_IMPLEMENT


BEGIN_IMPLEMENT(Halcon_ImageFitWindow(Long imageHandle, Long winHandle))
HTuple htWindow = *((HTuple*)winHandle);
Hobject* img = (Hobject*)imageHandle;
HTuple width, height;
get_image_size(*img, &width, &height);
set_part(htWindow, 0, 0, height - 1, width - 1);
END_IMPLEMENT

BEGIN_IMPLEMENT(Halcon_DisplayObj(Long winHandle, Long objHandle))
HTuple htWindow = *((HTuple*)winHandle);
Hobject* obj = (Hobject*)objHandle;
disp_obj(*obj, htWindow);
END_IMPLEMENT

BEGIN_IMPLEMENT(Halcon_CountSecond(double* second))
HTuple cnt_seconds;
count_seconds(&cnt_seconds);
*second = cnt_seconds.D();
END_IMPLEMENT

/************************************************************************/
/* LogView                                                              */
/************************************************************************/
typedef long(*AttachView)(Long handle);
typedef long(*OutputLog)(const char* info);

HINSTANCE LogView_DLL = NULL;

BEGIN_IMPLEMENT(LogView_Attach(Long logViewHandle))

LogView_DLL = LoadLibrary(L"./AnyLib_LogView.dll");
if (LogView_DLL) {
	AttachView attachView = (AttachView)GetProcAddress(LogView_DLL, "AnyLib_LogView_Attach");
	if (attachView != NULL) {
		attachView(logViewHandle);
	}
}
END_IMPLEMENT



BEGIN_IMPLEMENT(LogView_Detach(Long logViewHandle))
if (LogView_DLL) {
	FreeLibrary(LogView_DLL);
}
END_IMPLEMENT



BEGIN_IMPLEMENT(LogView_Normal(const char* info))
if (LogView_DLL) {
	OutputLog logView_Normal = (OutputLog)GetProcAddress(LogView_DLL, "AnyLib_LogView_Normal");
	if (logView_Normal) {
		logView_Normal(info);
	}
}
END_IMPLEMENT



BEGIN_IMPLEMENT(LogView_Error(const char* info))
if (LogView_DLL) {
	OutputLog logView_Error = (OutputLog)GetProcAddress(LogView_DLL, "AnyLib_LogView_Error");
	if (logView_Error) {
		logView_Error(info);
	}
}
END_IMPLEMENT