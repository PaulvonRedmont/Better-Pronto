import wx

# Get a more reasonable window size
better_pronto_window_height = 400
better_pronto_window_width = 600

class Pronto_Login(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Better Pronto 1.0 Login', size=(better_pronto_window_width, better_pronto_window_height))
        panel = wx.Panel(frame)

        # Create a BoxSizer for vertical layout
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create TextCtrl for user input
        self.text_ctrl = wx.TextCtrl(panel, size=(75, -1), style=wx.TE_PROCESS_ENTER)
        sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 5)  # Add with padding

        # Create a Submit button
        button = wx.Button(panel, label='Submit')
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)  # Add with padding

        # Set the sizer for the panel
        panel.SetSizer(sizer)

        frame.Show()
        return True

    def on_button_click(self, event):
        wx.MessageBox('Button Clicked!', 'Info')

if __name__ == '__main__':
    app = Pronto_Login()
    app.MainLoop()