# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class pageUtamaBanget
###########################################################################

class pageUtamaBanget ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 210, 210, 255 ) )

		gSizer6 = wx.GridSizer( 5, 3, 0, 0 )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		gSizer6.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"MyCash", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Baskerville Old Face" ) )

		gSizer6.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer6.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer6.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Aplikasi Kasir Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Baskerville Old Face" ) )

		gSizer6.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer6.Add( self.m_staticText53, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		gSizer6.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.startLogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.startLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		gSizer6.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		gSizer6.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.startRegistrasi = wx.Button( self, wx.ID_ANY, u"Registrasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.startRegistrasi, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		gSizer6.Add( self.m_staticText46, 0, wx.ALL, 5 )


		self.SetSizer( gSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.startLogin.Bind( wx.EVT_BUTTON, self.startLoginOnButtonClick )
		self.startRegistrasi.Bind( wx.EVT_BUTTON, self.startRegistrasiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def startLoginOnButtonClick( self, event ):
		event.Skip()

	def startRegistrasiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pageRegistrasi
###########################################################################

class pageRegistrasi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 217, 217, 255 ) )

		gSizer7 = wx.GridSizer( 4, 2, 0, 0 )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		gSizer7.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.regNama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.regNama, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		gSizer7.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.regUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.regUsername, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer7.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.regPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer7.Add( self.regPassword, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer7.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.btnRegister = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.btnRegister, 0, wx.ALL, 5 )


		self.SetSizer( gSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnRegister.Bind( wx.EVT_BUTTON, self.btnRegisterOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnRegisterOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pageLogin
###########################################################################

class pageLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 213, 213, 255 ) )

		gSizer1 = wx.GridSizer( 5, 3, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang. Silahkan Login!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Baskerville Old Face" ) )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.inputUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.inputUsername, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.inputPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer1.Add( self.inputPassword, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.btnLogin.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer1.Add( self.btnLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnLogin.Bind( wx.EVT_BUTTON, self.btnLoginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnLoginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pageUtama
###########################################################################

class pageUtama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 208, 208, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panelUtama = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelUtama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.panelUtama.SetBackgroundColour( wx.Colour( 223, 223, 255 ) )

		bSizer1.Add( self.panelUtama, 1, wx.EXPAND |wx.ALL, 5 )

		self.panelBawah = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelBawah.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gSizer2 = wx.GridSizer( 0, 6, 0, 0 )

		self.m_staticText44 = wx.StaticText( self.panelBawah, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		gSizer2.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.startKasir = wx.Button( self.panelBawah, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startKasir.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bernard MT Condensed" ) )

		gSizer2.Add( self.startKasir, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.startLihatBarang = wx.Button( self.panelBawah, wx.ID_ANY, u"Lihat Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startLihatBarang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bernard MT Condensed" ) )

		gSizer2.Add( self.startLihatBarang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.startTambahData = wx.Button( self.panelBawah, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startTambahData.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bernard MT Condensed" ) )

		gSizer2.Add( self.startTambahData, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.startEditBarang = wx.Button( self.panelBawah, wx.ID_ANY, u"Edit Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startEditBarang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bernard MT Condensed" ) )

		gSizer2.Add( self.startEditBarang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self.panelBawah, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )


		self.panelBawah.SetSizer( gSizer2 )
		self.panelBawah.Layout()
		gSizer2.Fit( self.panelBawah )
		bSizer1.Add( self.panelBawah, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.startKasir.Bind( wx.EVT_BUTTON, self.startKasirOnButtonClick )
		self.startLihatBarang.Bind( wx.EVT_BUTTON, self.startLihatBarangOnButtonClick )
		self.startTambahData.Bind( wx.EVT_BUTTON, self.startTambahDataOnButtonClick )
		self.startEditBarang.Bind( wx.EVT_BUTTON, self.startEditBarangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def startKasirOnButtonClick( self, event ):
		event.Skip()

	def startLihatBarangOnButtonClick( self, event ):
		event.Skip()

	def startTambahDataOnButtonClick( self, event ):
		event.Skip()

	def startEditBarangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pageKasir
###########################################################################

class pageKasir ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 223, 223, 255 ) )

		gSizer3 = wx.GridSizer( 6, 3, 0, 0 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Kode Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.inputKodeBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputKodeBarang.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer3.Add( self.inputKodeBarang, 0, wx.ALL, 5 )

		self.teksNamaBarang = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teksNamaBarang.Wrap( -1 )

		gSizer3.Add( self.teksNamaBarang, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.inputJmlBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputJmlBarang.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer3.Add( self.inputJmlBarang, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		gSizer3.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.teksTotal = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teksTotal.Wrap( -1 )

		self.teksTotal.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		gSizer3.Add( self.teksTotal, 0, wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		gSizer3.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.inputBayar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputBayar.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer3.Add( self.inputBayar, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		gSizer3.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.btnHitung = wx.Button( self, wx.ID_ANY, u"Hitung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnHitung.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		gSizer3.Add( self.btnHitung, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer3.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Kembalian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_staticText18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.teksKembalian = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teksKembalian.Wrap( -1 )

		self.teksKembalian.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		gSizer3.Add( self.teksKembalian, 0, wx.ALL, 5 )


		self.SetSizer( gSizer3 )
		self.Layout()

		# Connect Events
		self.inputKodeBarang.Bind( wx.EVT_TEXT, self.inputKodeBarangOnText )
		self.inputJmlBarang.Bind( wx.EVT_TEXT, self.inputJmlBarangOnText )
		self.btnHitung.Bind( wx.EVT_BUTTON, self.btnHitungOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def inputKodeBarangOnText( self, event ):
		event.Skip()

	def inputJmlBarangOnText( self, event ):
		event.Skip()

	def btnHitungOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pageDataBarang
###########################################################################

class pageDataBarang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 223, 223, 255 ) )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Data Barang" ), wx.VERTICAL )

		self.tabelBarang = wx.grid.Grid( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelBarang.CreateGrid( 5, 4 )
		self.tabelBarang.EnableEditing( True )
		self.tabelBarang.EnableGridLines( True )
		self.tabelBarang.EnableDragGridSize( False )
		self.tabelBarang.SetMargins( 0, 0 )

		# Columns
		self.tabelBarang.SetColSize( 0, 150 )
		self.tabelBarang.SetColSize( 1, 150 )
		self.tabelBarang.SetColSize( 2, 80 )
		self.tabelBarang.SetColSize( 3, 150 )
		self.tabelBarang.EnableDragColMove( False )
		self.tabelBarang.EnableDragColSize( True )
		self.tabelBarang.SetColLabelSize( 30 )
		self.tabelBarang.SetColLabelValue( 0, u"Kode Barang" )
		self.tabelBarang.SetColLabelValue( 1, u"Nama Barang" )
		self.tabelBarang.SetColLabelValue( 2, u"Stok" )
		self.tabelBarang.SetColLabelValue( 3, u"Harga Jual" )
		self.tabelBarang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelBarang.EnableDragRowSize( True )
		self.tabelBarang.SetRowLabelSize( 80 )
		self.tabelBarang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelBarang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelBarang.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer1.Add( self.tabelBarang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( sbSizer1 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class pageTambahBarang
###########################################################################

class pageTambahBarang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 225, 225, 255 ) )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tambah Barang" ), wx.VERTICAL )

		gSizer4 = wx.GridSizer( 5, 2, 0, 0 )

		self.m_staticText19 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Kode Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer4.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.tambahKodeBrg = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambahKodeBrg.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer4.Add( self.tambahKodeBrg, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer4.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.tambahNamaBrg = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambahNamaBrg.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer4.Add( self.tambahNamaBrg, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer4.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.tambahStok = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambahStok.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer4.Add( self.tambahStok, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Harga Jual", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer4.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.tambahHargaJual = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambahHargaJual.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer4.Add( self.tambahHargaJual, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		gSizer4.Add( self.m_staticText23, 0, wx.ALL, 5 )

		dialogTambahBrg = wx.StdDialogButtonSizer()
		self.dialogTambahBrgSave = wx.Button( sbSizer2.GetStaticBox(), wx.ID_SAVE )
		dialogTambahBrg.AddButton( self.dialogTambahBrgSave )
		self.dialogTambahBrgCancel = wx.Button( sbSizer2.GetStaticBox(), wx.ID_CANCEL )
		dialogTambahBrg.AddButton( self.dialogTambahBrgCancel )
		dialogTambahBrg.Realize();

		gSizer4.Add( dialogTambahBrg, 1, wx.EXPAND, 5 )


		sbSizer2.Add( gSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer2 )
		self.Layout()

		# Connect Events
		self.dialogTambahBrgCancel.Bind( wx.EVT_BUTTON, self.dialogTambahBrgOnCancelButtonClick )
		self.dialogTambahBrgSave.Bind( wx.EVT_BUTTON, self.dialogTambahBrgOnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dialogTambahBrgOnCancelButtonClick( self, event ):
		event.Skip()

	def dialogTambahBrgOnSaveButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pageEditBarang
###########################################################################

class pageEditBarang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 213, 213, 255 ) )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Edit Barang" ), wx.VERTICAL )

		gSizer9 = wx.GridSizer( 5, 3, 0, 0 )

		self.m_staticText34 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cek Kode Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer9.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.cekKode = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cekKode.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer9.Add( self.cekKode, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.teksCekBarang = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teksCekBarang.Wrap( -1 )

		gSizer9.Add( self.teksCekBarang, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Masukkan Nama Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer9.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.editNama = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.editNama.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer9.Add( self.editNama, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText37 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		gSizer9.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Masukkan Stok Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer9.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.editStok = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.editStok.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer9.Add( self.editStok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText39 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		gSizer9.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_staticText40 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Masukkan Harga Jual Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer9.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.editHarga = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.editHarga.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		gSizer9.Add( self.editHarga, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText41 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer9.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		gSizer9.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		gSizer9.Add( self.m_staticText43, 0, wx.ALL, 5 )

		dialogEdit = wx.StdDialogButtonSizer()
		self.dialogEditSave = wx.Button( sbSizer3.GetStaticBox(), wx.ID_SAVE )
		dialogEdit.AddButton( self.dialogEditSave )
		self.dialogEditCancel = wx.Button( sbSizer3.GetStaticBox(), wx.ID_CANCEL )
		dialogEdit.AddButton( self.dialogEditCancel )
		dialogEdit.Realize();

		gSizer9.Add( dialogEdit, 1, wx.EXPAND, 5 )


		sbSizer3.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer3 )
		self.Layout()

		# Connect Events
		self.cekKode.Bind( wx.EVT_TEXT, self.cekKodeOnText )
		self.dialogEditCancel.Bind( wx.EVT_BUTTON, self.dialogEditOnCancelButtonClick )
		self.dialogEditSave.Bind( wx.EVT_BUTTON, self.dialogEditOnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cekKodeOnText( self, event ):
		event.Skip()

	def dialogEditOnCancelButtonClick( self, event ):
		event.Skip()

	def dialogEditOnSaveButtonClick( self, event ):
		event.Skip()


