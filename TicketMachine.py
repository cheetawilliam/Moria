#01-04-2021 this program is there to allow visitors to buy tickets,
#get a receipt and get tickets. As well as entering relevant data into a
#database so the park gates can check the tickets.
#25-05-2021 Restart project after learning more wxpython.

#Importing Requirements
import wx #WX Python, GUI
from wx.adv import DatePickerCtrl

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
        self.Center() 
        #Make the panel larger than any screen to allow free positioning. 
        self.panel = wx.Panel(self, size=(3000, 3000))
        #Paint background every time the window changes. 
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
        #Load titlepage on startup.
        self.page0()
        #What page is displayed?
        self.page = 0
        
    def OnPaint(self, event):
        #The background image depending on screen.
        if self.page == 0:
            backgroundimage = "Images/MoriaGateBlank.jpg"
        elif self.page == 1 or self.page == 2 or self.page == 4:
            backgroundimage = "Images/MoriaGateBoxed.jpg"
        
        if self.page != 3:
            image = wx.Bitmap(backgroundimage)
            image = wx.Bitmap.ConvertToImage(image)
            #Call screensizer function 
            screensizing = self.screensizer()
            #Unpack result screensizer function
            width, height = screensizing
            #Set the program size to a fraction of the screen size in the right proportions
            self.SetSize(screensizing)
            #Make image the right size as background and draw it.
            image=image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
            image = image.ConvertToBitmap()
            dc=wx.PaintDC(self.panel)
            dc.DrawBitmap(image, 0, 0)
        
    def page0(self):
        #Set page and refresh
        self.page = 0
        self.Refresh()
        #Call screensizer function 
        screensizing = self.screensizer()
        #Unpack result screensizer function
        width, height = screensizing
        #Calculate position for button.
        wpos = width
        hpos = height
        wpos = int(wpos/2-40)
        hpos = int(hpos/10*7)
        #Make button
        orderbutton = wx.Button(self.panel, id=wx.ID_ANY, label="Order Tickets",
            pos=(wpos,hpos))
        orderbutton.Bind(wx.EVT_BUTTON, self.page1)
        #Make background black and letters white.
        orderbutton.SetBackgroundColour("black")
        orderbutton.SetForegroundColour("white")
        #Calculate position for Banner.
        wpos = width
        hpos = height
        wpos = int(wpos/2-90)
        hpos = int(hpos/10*1)
        #Make Banner      
        title = wx.StaticText(self.panel, id=wx.ID_ANY, label="Welcome to Moria",
            pos=(wpos,hpos))
        #Make font larger.
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        title.SetBackgroundColour("black")
        title.SetForegroundColour("white")
        #Set Font to banner
        title.SetFont(font)
    
    def page1(self, event):
        #Write data depending on source page.
        if self.page == 0:
            self.num17tick = 0
            self.num64tick = 0
            self.num65tick = 0
            #self.date = wx.DateTime.Now()
            returning = False
        elif self.page == 2:            
            returning = True       
            
        #Set page and refresh
        self.page = 1
        self.Refresh()
        #Call screensizer function 
        screensizing = self.screensizer()
        #Unpack result screensizer function
        width, height = screensizing
        #Empty last page
        for child in self.panel.GetChildren():
            child.Destroy()
        
        #Position banner
        wpos = width
        hpos = height
        wpos = int(wpos/2-90)
        hpos = int(hpos/10*1)
        #Make Banner
        title = wx.StaticText(self.panel, id=wx.ID_ANY, label="Order your tickets",
            pos =(wpos,hpos))
        #Make font larger.
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        title.SetBackgroundColour("black")
        title.SetForegroundColour("white")
        #Set Font to banner
        title.SetFont(font)
        
        #Position text
        wpos = width
        hpos = height
        wpos = int(wpos/2-70)
        hpos = int(hpos/10*4)
        #Make Banner
        text = wx.StaticText(self.panel, id=wx.ID_ANY, label="How many tickets?",
            pos =(wpos,hpos))
        #Make font larger.
        font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        text.SetBackgroundColour("#030303")
        text.SetForegroundColour("white")
        #Set Font to banner
        text.SetFont(font)
        
        #Create panel for ticket ordering. Make sure to set parent correctly if UI immutable.
        wpos = width
        hpos = height
        wpos = int(wpos/4)
        hpos = int(hpos/10*4.5)
        pwith = int(width/16*9)
        pheight = int(height/10*4)
        
        orderpanel = wx.Panel(parent = self.panel , size=(pwith,pheight),
            pos = (wpos, hpos), style=wx.TRANSPARENT_WINDOW)

        #Create sizer
        gridbox = wx.GridBagSizer(8,5)
                
        #Make age3
        self.text = wx.StaticText(orderpanel, label="Age 0-3 are free:")
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text.SetBackgroundColour("#030303")
        self.text.SetForegroundColour("white")
        #Set Font to age3
        self.text.SetFont(font)

        #Make age17
        self.text1 = wx.StaticText(orderpanel, label="Age 4-17:")
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text1.SetBackgroundColour("#030303")
        self.text1.SetForegroundColour("white")
        #Set Font to age17
        self.text1.SetFont(font)
        
        #Make age64
        self.text2 = wx.StaticText(orderpanel, label="Age 18-64:")
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text2.SetBackgroundColour("#030303")
        self.text2.SetForegroundColour("white")
        #Set Font to age64
        self.text2.SetFont(font)

        #Make age65+
        self.text3 = wx.StaticText(orderpanel, label="Age 65+:")
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text3.SetBackgroundColour("#030303")
        self.text3.SetForegroundColour("white")
        #Set Font to age65+
        self.text3.SetFont(font)
        
        #counter17
        self.counter17 = wx.SpinCtrl(orderpanel, initial=0)
        self.counter17.SetRange(0,100)        
        #counter64
        self.counter64 = wx.SpinCtrl(orderpanel, initial=0)
        self.counter64.SetRange(0,100)
        #counter65+
        self.counter65 = wx.SpinCtrl(orderpanel, initial=0)
        self.counter65.SetRange(0,100)
        
        #Make discount
        self.text4 = wx.StaticText(orderpanel, label="If you buy 5 tickets or "
            "more you get a €5,- discount.", style=wx.TE_MULTILINE,
            size=(-1,-1))
        self.text4.Wrap(int(width/16*5))
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text4.SetBackgroundColour("#030303")
        self.text4.SetForegroundColour("white")
        #Set Font to age65+
        self.text4.SetFont(font)
        
        #Set default price to 0
        self.price = 0
        #Detect change in amount tickets and calculate price.
        self.counter17.Bind(wx.EVT_SPINCTRL, self.calcprice)
        self.counter64.Bind(wx.EVT_SPINCTRL, self.calcprice)
        self.counter65.Bind(wx.EVT_SPINCTRL, self.calcprice)
        
        #Make price
        self.text5 = wx.StaticText(orderpanel, label="The total price will be €"
        + str(self.price) + ",-")
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text5.SetBackgroundColour("#030303")
        self.text5.SetForegroundColour("white")
        #Set Font to price+
        self.text5.SetFont(font)
        
        #Make DateLabel
        self.text6 = wx.StaticText(orderpanel, label="When will you "
        "descend into the depths?")
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text6.SetBackgroundColour("#030303")
        self.text6.SetForegroundColour("white")
        #Set Font to age65+
        self.text6.SetFont(font)
        
        #Create Date widget
        self.calendar = DatePickerCtrl(orderpanel, style=wx.adv.DP_DROPDOWN)
        self.calendar.SetRange(wx.DateTime.Now(),(wx.DateTime.FromDMY(5,5,3000)))
        #Create control date to check if date has changed later.
        self.controldate = wx.DateTime.Now()
        self.controldate = self.controldate.GetDateOnly()

        #Create ticket button
        self.ticketbutton = wx.Button(orderpanel, id=wx.ID_ANY, label="Order Tickets")
        #Make background black and letters white.
        self.ticketbutton.SetBackgroundColour("black")
        self.ticketbutton.SetForegroundColour("white")  
        #Add button function
        self.ticketbutton.Bind(wx.EVT_BUTTON, self.page2)
        
        #Add age3 to sizer
        gridbox.Add(self.text, pos=(0,0), span=(1,2))
        #Add age17 to sizer
        gridbox.Add(self.text1, pos=(1,0))
        #Add age64 to sizer
        gridbox.Add(self.text2, pos=(2,0))        
        #Add age65+ to sizer
        gridbox.Add(self.text3, pos=(3,0))
        #Add counter17 to sizer
        gridbox.Add(self.counter17, pos=(1,1), flag=wx.ALIGN_CENTER)
        #Add counter64 to sizer
        gridbox.Add(self.counter64, pos=(2,1), flag=wx.ALIGN_CENTER)
        #Add counter65 to sizer
        gridbox.Add(self.counter65, pos=(3,1), flag=wx.ALIGN_CENTER)
        #Add discount to sizer
        gridbox.Add(self.text4, pos=(1,2),span=(3,3))
        #Add price to sizer
        gridbox.Add(self.text5, pos=(4,1),span=(1,5))
        #Add DataLabel to sizer
        gridbox.Add(self.text6, pos=(6,0),span=(1,5), flag=wx.ALIGN_CENTER,
            border = 20)
        #Add Calander to sizer
        gridbox.Add(self.calendar, pos=(7,1),span=(1,5))
        #Add ticketbutton to sizer
        gridbox.Add(self.ticketbutton, pos=(8,0), span=(1,5), flag=wx.ALIGN_CENTER)
        
        if returning == True:
            #Set the counters to old values
            self.counter17.SetValue(self.num17tick)
            self.counter64.SetValue(self.num64tick)
            self.counter65.SetValue(self.num65tick)
            #Set date to old value
            print(self.date)
            if self.date != self.controldate:
                self.calendar.SetValue(self.date)
            
        orderpanel.SetSizer(gridbox)
        orderpanel.Layout()

    def page2(self, event):
        #Save the selected date.
        self.date=self.calendar.GetValue()
        #Set page and refresh
        self.page = 2
        self.Refresh()
        #Call screensizer function 
        screensizing = self.screensizer()
        #Unpack result screensizer function
        width, height = screensizing
        #Empty last page
        for child in self.panel.GetChildren():
            child.Destroy()
        #Position banner
        wpos = width
        hpos = height
        wpos = int(wpos/2-90)
        hpos = int(hpos/10*1)
        #Make Banner
        title = wx.StaticText(self.panel, id=wx.ID_ANY, label="Please confirm "
        "your order.", pos =(wpos,hpos))
        #Make font larger.
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        title.SetBackgroundColour("black")
        title.SetForegroundColour("white")
        #Set Font to banner
        title.SetFont(font)        
        
        #Create panel for bounding confirmation information.
        wpos = width
        hpos = height
        wpos = int(wpos/40*9)
        hpos = int(hpos/20*7)
        pwith = int(width/16*9)
        pheight = int(height/10*4)
        confirmpanel = wx.Panel(parent = self.panel , size=(pwith,pheight),
            pos = (wpos, hpos), style=wx.TRANSPARENT_WINDOW)        
        
        #Made date more readable.
        self.displaydate = str(self.date)
        self.displaydate = self.displaydate.split()
        #Confirmation text
        confirmationtext = ("Thank you for braving the deapths of Moria please "
        "confirm all information has been entered correctly. \n"
        "You're welcome on: " + str(self.displaydate[0]) + "\n" +
        str(self.num17tick) + " tickets for people under 18.\n" +
        str(self.num64tick) + " tickets for people under 65.\n" +
        str(self.num65tick) + " tickets for people at or over 65.\n" +
        "The total cost will come to €" + str(self.price) + ",-\n"
        "If this all is correct we hope to see you soon, "
        "If not please return to the previous page.")
        #Make conformation information
        self.text7 = wx.StaticText(confirmpanel, label=confirmationtext,
            style=wx.TE_MULTILINE, size=(-1,-1))
        self.text7.Wrap(int(width/16*8))
        #Make font larger.
        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #Make background black and letters white.
        self.text7.SetBackgroundColour("#030303")
        self.text7.SetForegroundColour("white")
        #Set Font to confirmation text+
        self.text7.SetFont(font)
        
        wpos = int(10)
        hpos = int(height/20*7)
        #Create return button
        self.returnbutton = wx.Button(confirmpanel, id=wx.ID_ANY, 
            label="Change Tickets", pos=(wpos,hpos))
        #Make background black and letters white.
        self.returnbutton.SetBackgroundColour("black")
        self.returnbutton.SetForegroundColour("white")  
        #Add button function
        self.returnbutton.Bind(wx.EVT_BUTTON, self.page1)
        
        bwidth = self.returnbutton.Size.GetWidth()
        wpos = int(bwidth + 20)
        hpos = int(height/20*7)
        #Create pay button
        self.paybutton = wx.Button(confirmpanel, id=wx.ID_ANY, 
            label="Go to Payments", pos=(wpos,hpos))
        #Make background black and letters white.
        self.paybutton.SetBackgroundColour("black")
        self.paybutton.SetForegroundColour("white")  
        #Add button function
        self.paybutton.Bind(wx.EVT_BUTTON, self.page3)
                
        confirmpanel.Layout()
        
    def page3(self, event):
        #Set page and refresh
        self.page = 3
        self.Refresh()
        #Call screensizer function 
        screensizing = self.screensizer()
        #Unpack result screensizer function
        width, height = screensizing
        #Empty last page
        for child in self.panel.GetChildren():
            child.Destroy()
        
        #Create fakepaying button
        self.fakepaybutton = wx.Button(self.panel, id=wx.ID_ANY, 
            label="Change Tickets")
        #Make background black and letters white.
        self.fakepaybutton.SetBackgroundColour("white")
        self.fakepaybutton.SetForegroundColour("black")  
        #Add button function
        self.fakepaybutton.Bind(wx.EVT_BUTTON, self.page4)
    
    def page4(self, event):
        #Set page and refresh
        self.page = 4
        self.Refresh()
        #Call screensizer function 
        screensizing = self.screensizer()
        #Unpack result screensizer function
        width, height = screensizing
        #Empty last page
        for child in self.panel.GetChildren():
            child.Destroy()        
        
    def screensizer(self):
        #Get size of the screen.
        screensize = wx.DisplaySize()
        #If screen ration > 0.5625 limit width, < limit height
        if (screensize[0]/screensize[1])<= 0.5625:
            screensizing=(int((screensize[0]-100)*0.9), 
                int((screensize[0]-100)/0.562*0.9))
        else:
            screensizing=(int((screensize[1]/16*9)*0.9), 
                int(screensize[1]*0.9))
        #Return the width and height for other functions.
        return screensizing
    
    def calcprice(self,event):
        #Calculate price
        #Retrieve amount of tickets
        self.num17tick = self.counter17.GetValue()
        self.num64tick = self.counter64.GetValue()
        self.num65tick = self.counter65.GetValue()
        #Calculate price
        self.price = self.num17tick*5+self.num64tick*10+self.num65tick*8
        if (self.num17tick+self.num64tick+self.num65tick) >= 5:
            self.price -= 5
        #Make price
        self.text5.SetLabel("The total price will be €"
        + str(self.price) + ",-")

def main():
    app=wx.App()
    frm = Moria(None, title="MoriaTickets")
    frm.Show()
    app.MainLoop()

if __name__=="__main__":
    main()
