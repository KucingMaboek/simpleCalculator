import wx
import sc.Controllers.MainController

app = wx.App()
mainCtrl = sc.Controllers.MainController.MainController(None)
mainCtrl.Show()
app.MainLoop()