
#pragma once
#include "stdafx.h"
#include "AnyLib_Types.h"

#define Vision3000(funcFlag) Vision3000_##funcFlag
#define  LOG_NORMAL(info) Vision3000(LogView_Normal(info))
#define  LOG_ERROR(info) Vision3000(LogView_Error(info))

#ifdef WIN32_DLL_EXPORT
#  define DLL_DECLARE(funcFlag) extern "C" __declspec(dllexport) long Vision3000_##funcFlag;
#else
#  define DLL_DECLARE(funcFlag) extern "C" __declspec(dllimport) long Vision3000_##funcFlag;
#endif



DLL_DECLARE(Halcon_CreateWindow(Long parentHandle, Long* winHandle))
DLL_DECLARE(Halcon_ResizeWindow(Long winHandle))
DLL_DECLARE(Halcon_ImageFitWindow(Long imageHandle, Long winHandle))
DLL_DECLARE(Halcon_DisplayObj(Long winHandle, Long objHandle))
DLL_DECLARE(Halcon_DestoryWindow(Long winHandle))
DLL_DECLARE(Halcon_CountSecond(double* second))
DLL_DECLARE(Halcon_ReadImage(const char* fileName, Long* objHandle))

DLL_DECLARE(LogView_Attach(Long logViewHandle))
DLL_DECLARE(LogView_Detach(Long logViewHandle))
DLL_DECLARE(LogView_Normal(const char* info))
DLL_DECLARE(LogView_Error(const char* info))


