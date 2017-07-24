// Util.h : main header file for the Util DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols
#include "UtilAPI.h"


// CUtilApp
// See Util.cpp for the implementation of this class
//

class CUtilApp : public CWinApp
{
public:
	CUtilApp();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
