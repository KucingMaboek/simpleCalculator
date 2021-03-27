# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyCalculator", pos = wx.DefaultPosition, size = wx.Size( 300,375 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrlResult = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_READONLY|wx.TE_RIGHT )
		bSizer1.Add( self.m_textCtrlResult, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 4, 4, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonMultiply = wx.Button( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonMultiply, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonSubstraction = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonSubstraction, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonAdd = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonAdd, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonBlank = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonBlank, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button0, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonDel = wx.Button( self, wx.ID_ANY, u"del", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonDel, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonCalculate = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonCalculate, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer1, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


