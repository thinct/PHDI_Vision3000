#pragma once
#include "resource.h"

#define HCPP_LEGACY_API
#define HCPP_LEGACY_NAMESPACE
#include "Halconcpp.h"
using namespace HalconCpp;


// HalconWindowDlg dialog

class HalconWindowDlg : public CDialogEx
{
	DECLARE_DYNAMIC(HalconWindowDlg)

public:
	HalconWindowDlg(CWnd* pParent = NULL);   // standard constructor
	virtual ~HalconWindowDlg();

// Dialog Data
	enum { IDD = IDD_DIALOG_HalconWnd };

protected:
	virtual BOOL OnInitDialog();
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

	DECLARE_MESSAGE_MAP()

public:
	long DisplayImage(HObject* hImage);
	HTuple WindowHandle() const;

private:
	afx_msg BOOL OnMouseWheel(UINT nFlags, short zDelta, CPoint pt);
	afx_msg void OnNcLButtonDblClk(UINT nHitTest, CPoint point);

private:
	BOOL InitHalconWindow();
	void ShowImage();

private:
	HTuple   m_hWnd; //ÏÔÊ¾´°¿Ú¾ä±ú
	HObject  m_hImage;//Í¼Ïñ¶ÔÏó
	HTuple   m_hWidth;//Í¼Ïñ¿í
	HTuple   m_hHeight;

	CRect    m_rtImage;
	CString  m_strImagePath;

	double  m_dDispImagePartRow0;
	double  m_dDispImagePartCol0;
	double  m_dDispImagePartRow1;
	double  m_dDispImagePartCol1;
};