import wx
from sc.Views.MainView import MainFrame

class MainController(MainFrame):
    isCalculated = False

    def __init__(self, parent):
        super().__init__(parent)

        # Connect Event
        self.m_button0.Bind(wx.EVT_BUTTON, self.inputCharacter('0'))
        self.m_button1.Bind(wx.EVT_BUTTON, self.inputCharacter('1'))
        self.m_button2.Bind(wx.EVT_BUTTON, self.inputCharacter('2'))
        self.m_button3.Bind(wx.EVT_BUTTON, self.inputCharacter('3'))
        self.m_button4.Bind(wx.EVT_BUTTON, self.inputCharacter('4'))
        self.m_button5.Bind(wx.EVT_BUTTON, self.inputCharacter('5'))
        self.m_button6.Bind(wx.EVT_BUTTON, self.inputCharacter('6'))
        self.m_button7.Bind(wx.EVT_BUTTON, self.inputCharacter('7'))
        self.m_button8.Bind(wx.EVT_BUTTON, self.inputCharacter('8'))
        self.m_button9.Bind(wx.EVT_BUTTON, self.inputCharacter('9'))
        self.m_buttonAdd.Bind(wx.EVT_BUTTON, self.inputCharacter('+'))
        self.m_buttonSubstraction.Bind(wx.EVT_BUTTON, self.inputCharacter('-'))
        self.m_buttonMultiply.Bind(wx.EVT_BUTTON, self.inputCharacter('*'))
        self.m_buttonDel.Bind(wx.EVT_BUTTON, self.delete)
        self.m_buttonCalculate.Bind(wx.EVT_BUTTON, self.calculate)


    def inputCharacter(self, character):
        def OnClick(event):
            if(self.isCalculated):
                self.m_textCtrlResult.SetLabelText("")
                self.isCalculated = False
            self.m_textCtrlResult.LabelText += character
        return OnClick

    def calculate(self, event):
        labelText = self.m_textCtrlResult.GetLabelText()
        try:
            self.m_textCtrlResult.SetLabelText(str(eval(labelText)))
        except Exception as e:
            self.m_textCtrlResult.SetLabelText("Error!! Invalid input: " + str(e))
        self.isCalculated = True


    def delete(self, event):
        labelText = self.m_textCtrlResult.GetLabelText()
        labelText = labelText[:-1]
        self.m_textCtrlResult.SetLabelText(labelText)
