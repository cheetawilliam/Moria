#01-04-2021 this program is there to allow visitors to buy tickets,
#get a receipt and get tickets. As well as entering relevant data into a
#database so the park gates can check the tickets.
#25-05-2021 Restart project after learning more wxpython.

#Importing Requirements
import wx #WX Python, GUI

class Moria(wx.Frame):
    """
    Main window
    """
    def __init__(self, *args, **kw):
        super(Moria,self).__init__(*args, **kw)
        self.initFrame()
    
    def initFrame(self):
        #Create title in top bar.
        self.SetTitle("Moria")
        self.Centre() 
        #Make the panel larger than any screen to allow free positioning. 
        self.panel = wx.Panel(self, size=(3000, 3000))
        #Paint background every time the window changes. 
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
        #Load titlepage on startup.
        self.page0()
        
    def OnPaint(self, event):
        #The background image
        image = wx.Bitmap("Images/MoriaGate.jpg")
        image = wx.Bitmap.ConvertToImage(image)
        #Call screensizer function 
        screensizing = self.screensizer()
        width, height = screensizing
        self.SetSize(screensizing)
        image=image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        image = image.ConvertToBitmap()
        dc=wx.PaintDC(self.panel)
        dc.DrawBitmap(image, 0, 0)
        
    def page0(self):
        screensizing = self.screensizer()
        width, height = screensizing
        wpos = width
        hpos = height
        wpos = int(wpos/2-40)
        hpos = int(hpos/10*7)
        button = wx.Button(self.panel, id=wx.ID_ANY, label="Order Tickets",
            pos=(wpos,hpos))
        button.SetBackgroundColour("black")
        button.SetForegroundColour("white")
        wpos = width
        hpos = height
        wpos = int(wpos/2-90)
        hpos = int(hpos/10*1)       
        title = wx.StaticText(self.panel, id=wx.ID_ANY, label="Welcome to Moria",
            pos=(wpos,hpos))
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetBackgroundColour("black")
        title.SetForegroundColour("white")
        title.SetFont(font)
    
    def screensizer(self):
        screensize = wx.DisplaySize()
        #If screen ration > 0.5625 limit width, < limit height
        if (screensize[0]/screensize[1])<= 0.5625:
            screensizing=(int((screensize[0]-100)*0.9), 
                int((screensize[0]-100)/0.562*0.9))
        else:
            screensizing=(int((screensize[1]/16*9)*0.9), 
                int(screensize[1]*0.9))
        return screensizing
        
if __name__=="__main__":
    #When the module is run, run the application.
    app = wx.App()
    frm = Moria(None, title="MoriaTickets")
    frm.Show()
    app.MainLoop()
