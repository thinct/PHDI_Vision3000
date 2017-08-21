// HalconWindowDlg.cpp : implementation file
//

#include "stdafx.h"
#include "Util.h"
#include "HalconWindowDlg.h"
#include "afxdialogex.h"


// HalconWindowDlg dialog

IMPLEMENT_DYNAMIC(HalconWindowDlg, CDialogEx)

HalconWindowDlg::HalconWindowDlg(CWnd* pParent /*=NULL*/)
: CDialogEx(HalconWindowDlg::IDD, pParent)
, m_hWnd(0)
{

}

HalconWindowDlg::~HalconWindowDlg()
{
}

void HalconWindowDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}


BEGIN_MESSAGE_MAP(HalconWindowDlg, CDialogEx)
	ON_WM_MOUSEWHEEL()
	ON_WM_NCLBUTTONDBLCLK()
END_MESSAGE_MAP()


// HalconWindowDlg message handlers


BOOL HalconWindowDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// TODO:  Add extra initialization here
	InitHalconWindow();

	// 测试
	//HObject img;
	//ReadImage(&img, "D:/_1.tiff");
	//DisplayImage(&img);

	return TRUE;  // return TRUE unless you set the focus to a control
	// EXCEPTION: OCX Property Pages should return FALSE
}

BOOL HalconWindowDlg::OnMouseWheel(UINT nFlags, short zDelta, CPoint pt)
{
	// TODO: Add your message handler code here and/or call default
	CRect rtImage;
	GetDlgItem(IDC_STATIC_ImgWnd)->GetWindowRect(&rtImage);
	if (rtImage.PtInRect(pt) && m_hImage.IsInitialized())
	{
		Hlong  ImagePtX, ImagePtY;
		Hlong  Row0, Col0, Row1, Col1;
		double Scale = 0.1;

		if (zDelta>0)
		{
			ImagePtX = m_dDispImagePartCol0 + (pt.x - rtImage.left) / (rtImage.Width() - 1.0)*(m_dDispImagePartCol1 - m_dDispImagePartCol0);
			ImagePtY = m_dDispImagePartRow0 + (pt.y - rtImage.top) / (rtImage.Height() - 1.0)*(m_dDispImagePartRow1 - m_dDispImagePartRow0);
			Row0 = ImagePtY - 1 / (1 - Scale)*(ImagePtY - m_dDispImagePartRow0);
			Row1 = ImagePtY - 1 / (1 - Scale)*(ImagePtY - m_dDispImagePartRow1);
			Col0 = ImagePtX - 1 / (1 - Scale)*(ImagePtX - m_dDispImagePartCol0);
			Col1 = ImagePtX - 1 / (1 - Scale)*(ImagePtX - m_dDispImagePartCol1);

			m_dDispImagePartRow0 = Row0;
			m_dDispImagePartCol0 = Col0;
			m_dDispImagePartRow1 = Row1;
			m_dDispImagePartCol1 = Col1;
		}
		else
		{
			ImagePtX = m_dDispImagePartCol0 + (pt.x - rtImage.left) / (rtImage.Width() - 1.0)*(m_dDispImagePartCol1 - m_dDispImagePartCol0);
			ImagePtY = m_dDispImagePartRow0 + (pt.y - rtImage.top) / (rtImage.Height() - 1.0)*(m_dDispImagePartRow1 - m_dDispImagePartRow0);
			Row0 = ImagePtY - 1 / (1 + Scale)*(ImagePtY - m_dDispImagePartRow0);
			Row1 = ImagePtY - 1 / (1 + Scale)*(ImagePtY - m_dDispImagePartRow1);
			Col0 = ImagePtX - 1 / (1 + Scale)*(ImagePtX - m_dDispImagePartCol0);
			Col1 = ImagePtX - 1 / (1 + Scale)*(ImagePtX - m_dDispImagePartCol1);

			m_dDispImagePartRow0 = Row0;
			m_dDispImagePartCol0 = Col0;
			m_dDispImagePartRow1 = Row1;
			m_dDispImagePartCol1 = Col1;
		}
		ShowImage();
	}
	return CDialogEx::OnMouseWheel(nFlags, zDelta, pt);
}


BOOL HalconWindowDlg::InitHalconWindow()
{
	CWnd *pWnd = GetDlgItem(IDC_STATIC_ImgWnd);
	pWnd->GetClientRect(&m_rtImage);

	if (m_hWnd != 0)
	{
		HalconCpp::CloseWindow(m_hWnd);
	}
	SetWindowAttr("background_color", "black");
	OpenWindow(0, 0, m_rtImage.Width(), m_rtImage.Height(), (INT)pWnd->m_hWnd, "visible", "", &m_hWnd);

	return 0;
}


void HalconWindowDlg::ShowImage()
{
	if (m_hWnd != 0)
	{
		SetSystem("flush_graphic", "false");
		ClearWindow(m_hWnd);
		//显示
		if (m_hImage.IsInitialized())
		{
			SetPart(m_hWnd, m_dDispImagePartRow0, m_dDispImagePartCol0, m_dDispImagePartRow1 - 1, m_dDispImagePartCol1 - 1);
			DispObj(m_hImage, m_hWnd);
		}

		SetSystem("flush_graphic", "true");
		HObject emptyObject;
		emptyObject.GenEmptyObj();
		DispObj(emptyObject, m_hWnd);
	}
}


long HalconWindowDlg::DisplayImage(HObject* hImage)
{
	m_hImage = *hImage;

	////test show
	//DispObj(m_hImage, m_hWnd);


	GetImageSize(m_hImage, &m_hWidth, &m_hHeight);
	//设置窗口
	float fImage = m_hWidth.D() / m_hHeight.D();
	float fWindow = (float)m_rtImage.Width() / m_rtImage.Height();
	float Row0 = 0, Col0 = 0, Row1 = m_hHeight.I() - 1, Col1 = m_hWidth.I() - 1;
	if (fWindow > fImage)
	{
		float w = fWindow * m_hHeight.I();
		Row0 = 0;
		Col0 = -(w - m_hWidth.I()) / 2;
		Row1 = m_hHeight.I() - 1;
		Col1 = m_hWidth.I() + (w - m_hWidth.I()) / 2;
	}
	else
	{
		float h = m_hWidth.I() / fWindow;
		Row0 = -(h - m_hHeight.I()) / 2;
		Col0 = 0;
		Row1 = m_hHeight.I() + (h - m_hHeight.I()) / 2;
		Col1 = m_hWidth.I() - 1;
	}

	m_dDispImagePartRow0 = Row0;
	m_dDispImagePartCol0 = Col0;
	m_dDispImagePartRow1 = Row1;
	m_dDispImagePartCol1 = Col1;

	ShowImage();

	return 0;
}


HTuple HalconWindowDlg::WindowHandle() const
{
	return m_hWnd;
}


void HalconWindowDlg::OnNcLButtonDblClk(UINT nHitTest, CPoint point)
{
	// TODO: Add your message handler code here and/or call default
	if (m_hImage.IsInitialized())
	{
		//设置窗口
		float fImage = m_hWidth.D() / m_hHeight.D();
		float fWindow = (float)m_rtImage.Width() / m_rtImage.Height();
		float Row0 = 0, Col0 = 0, Row1 = m_hHeight.I() - 1, Col1 = m_hWidth.I() - 1;
		if (fWindow > fImage)
		{
			float w = fWindow * m_hHeight.I();
			Row0 = 0;
			Col0 = -(w - m_hWidth.I()) / 2;
			Row1 = m_hHeight.I() - 1;
			Col1 = m_hWidth.I() + (w - m_hWidth.I()) / 2;
		}
		else
		{
			float h = m_hWidth.I() / fWindow;
			Row0 = -(h - m_hHeight.I()) / 2;
			Col0 = 0;
			Row1 = m_hHeight.I() + (h - m_hHeight.I()) / 2;
			Col1 = m_hWidth.I() - 1;
		}

		m_dDispImagePartRow0 = Row0;
		m_dDispImagePartCol0 = Col0;
		m_dDispImagePartRow1 = Row1;
		m_dDispImagePartCol1 = Col1;

		ShowImage();
	}


	CDialogEx::OnNcLButtonDblClk(nHitTest, point);
}