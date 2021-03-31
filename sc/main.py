import wx
import Controllers.MainController as mc

app = wx.App()
mainCtrl = mc.MainController(None)
mainCtrl.Show()
app.MainLoop()
