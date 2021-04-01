#01-04-2021 this program is there to allow visitors to buy tickets,
#get a receipt and get tickets. As well as entering relevant data into a
#database so the park gates can check the tickets.

#Importing Requirements
import wx #WX Python, GUI

class MainWindow(wx.Frame):
    """
    Main window
    """
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)
        MainWindow.SizeScreen(self)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnResize)
        
    def SizeScreen(self):
        #Gets size of the screen width/height
        screensize = wx.DisplaySize()
        #If screen ration > 0.5625 limit width, < limit height
        if (screensize[0]/screensize[1])<= 0.5625:
            self.SetSize(wx.Size(int((screensize[0]-100)*0.9), 
                int((screensize[0]-100)/0.562*0.9)))
        else:
            self.SetSize(wx.Size(int((screensize[1]/16*9)*0.9), 
                int(screensize[1]*0.9)))
        
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
            
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("Images\MoriaGate.jpg")
        dc.DrawBitmap(bmp, 0, 0)
    
    def OnResize(self, evt):
        frame_size=self.GetSize()
        image = wx.Image("Images\MoriaGate.jpg")
        image.Rescale(frame_size[0],frame_size[1])
        bmp = image.ConvertToBitmap()
        self.DrawBitmap(bmp, 0, 0)
        
if __name__=="__main__":
    #When the module is run, run the application.
    app = wx.App()
    frm = MainWindow(None, title="MoriaTickets")
    frm.Show()
    app.MainLoop()
