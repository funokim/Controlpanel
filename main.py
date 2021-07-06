import wx

class ControlPanel(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.Centre()

def main():
    app = wx.App()
    control_panel = ControlPanel(None, title = "")
    control_panel.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
