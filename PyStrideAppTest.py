"""Simple TKinter GUI for PyStride Driver - JSP - 5_23_24"""

from tkinter import *
from PIL import ImageTk, Image
from PyStrideClass import PyStrideAnalog,PyStrideDigital
from time import sleep, time

#Main Function
def main():
    root = Tk()
    mainWindow = Window(root, "PyStride Simple GUI", "Simple GUI To Test PyStride")
    return None

#Create Window Class
class Window:

    def __init__(self, root, title, message):
        self.root = root
        self.root.title(title)

        #Center the GUI in Windows
        self.centerGUI()

        #Create GUI Items and Place On Screen
        self.createGUI(message)

        #Create variables to hold modbus stuff
        self.createModbusData()

        #Update IO
        self.updateIO()

        #Run Main Loop
        self.root.mainloop()
        pass

    def updateIO(self):
        """Update Io every 250 msec"""
        #Read in IO
        if (self.strideConnected):
        #Read In Inputs
            digIn = self.testStride.getAllDigitalInputs()
            if digIn[0]:
                self.digitalInputIndicator1 = Button(self.frameCenter, state=DISABLED,padx=8, bg="green")
            else:
                self.digitalInputIndicator1 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
            self.digitalInputIndicator1.grid(row=0, column=0, padx=5,pady=5)

            if digIn[1]:
                self.digitalInputIndicator2 = Button(self.frameCenter, state=DISABLED,padx=8, bg="green")
            else:
                self.digitalInputIndicator2 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
            self.digitalInputIndicator2.grid(row=1, column=0, padx=5,pady=5)

            if digIn[2]:
                self.digitalInputIndicator3 = Button(self.frameCenter, state=DISABLED,padx=8, bg="green")
            else:
                self.digitalInputIndicator3 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
            self.digitalInputIndicator3.grid(row=2, column=0, padx=5,pady=5)
        
            if digIn[3]:
                self.digitalInputIndicator4 = Button(self.frameCenter, state=DISABLED,padx=8, bg="green")
            else:
                self.digitalInputIndicator4 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
            self.digitalInput4Lbl.grid(row=3,column=1, padx=1, pady=1)

            """Update Digital Outputs"""
            self.testStride.setDigitalOutput(0, self.strideDigitalOut0)
            self.testStride.setDigitalOutput(1, self.strideDigitalOut1)
            self.testStride.setDigitalOutput(2, self.strideDigitalOut2)
            self.testStride.setDigitalOutput(3, self.strideDigitalOut3)

        self.root.after(200, self.updateIO)

    def createModbusData(self):
        """Create Modbus Data"""

        #Create Internal IP to Use
        self.strideIPAddress = ""
        #Bit to Hold If Connected
        self.strideConnected = False

        #Digital Input Status
        self.strideDigitalIn0 = False
        self.strideDigitalIn1 = False
        self.strideDigitalIn2 = False
        self.strideDigitalIn3 = False

        #Digital Output Status
        self.strideDigitalOut0 = False
        self.strideDigitalOut1 = False
        self.strideDigitalOut2 = False
        self.strideDigitalOut3 = False

    def centerGUI(self):
        """Centers the GUI In Windows"""
        self.window_height = 250
        self.window_width = 680
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))

    def createGUI(self, message):
        #Top Label Of Grid - Row 0, Span 3 Col
        self.topLabel = Label(self.root, text=message)
        self.topLabel.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

        #***************Left Side of Screen Frame - Row 1, Col 0******************************************
        self.frameLeft=LabelFrame(self.root, text="Communication", padx=5, pady=5)
        self.frameLeft.grid(row=1, column=0, padx=10,pady=10)
        
        #Ip Address and Form to Enter it In
        self.EnterIPLabel = Label(self.frameLeft, text="Enter IP Address: ")
        self.EnterIPLabel.grid(row=0,column=0, padx=1, pady=1)
        self.IPEntry = Entry(self.frameLeft, width=30, text="192.168.1.100")
        self.IPEntry.grid(row=0, column=1, padx=1, pady=1)
        #Connect Button
        self.connectButton = Button(self.frameLeft, text="Connect", padx=50, command=self.buttonConnect)
        self.connectButton.grid(row=1,column=0,columnspan=2, padx=10, pady=5)
        #Disconnect Button
        self.disconnectButton = Button(self.frameLeft, text="Disconnect", state=DISABLED, padx=50, command=self.buttonDisconnect)
        self.disconnectButton.grid(row=2,column=0,columnspan=2, padx=10, pady=5)
        #Indicator that we are connected, for now just use a button
        self.ModbusConnectedIndicator = Button(self.frameLeft, state=DISABLED,text="Not Connected",fg="white",bg="red", padx=50)
        self.ModbusConnectedIndicator.grid(row=3,column=0,columnspan=2, padx=10, pady=5)

        #***************Middle of Screen Frame - Row 1, Col 1******************************************
        self.frameCenter=LabelFrame(self.root, text="Digital Inputs", padx=5, pady=5)
        self.frameCenter.grid(row=1, column=1, padx=10,pady=10)
        
        #Digital Input Setup
        self.digitalInputIndicator1 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
        self.digitalInputIndicator1.grid(row=0, column=0, padx=5,pady=5)
        self.digitalInput1Lbl = Label(self.frameCenter, text="Digital Input #1")
        self.digitalInput1Lbl.grid(row=0,column=1, padx=1, pady=1)
        self.digitalInputIndicator2 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
        self.digitalInputIndicator2.grid(row=1, column=0, padx=5,pady=5)
        self.digitalInput2Lbl = Label(self.frameCenter, text="Digital Input #2")
        self.digitalInput2Lbl.grid(row=1,column=1, padx=1, pady=1)
        self.digitalInputIndicator3 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
        self.digitalInputIndicator3.grid(row=2, column=0, padx=5,pady=5)
        self.digitalInput3Lbl = Label(self.frameCenter, text="Digital Input #3")
        self.digitalInput3Lbl.grid(row=2,column=1, padx=1, pady=1)
        self.digitalInputIndicator4 = Button(self.frameCenter, state=DISABLED,padx=8, bg="gray")
        self.digitalInputIndicator4.grid(row=3, column=0, padx=5,pady=5)
        self.digitalInput4Lbl = Label(self.frameCenter, text="Digital Input #4")
        self.digitalInput4Lbl.grid(row=3,column=1, padx=1, pady=1)

        #***************Right of Screen Frame - Row 1, Col 2******************************************
        self.frameRight=LabelFrame(self.root, text="Digital Outputs", padx=5, pady=5)
        self.frameRight.grid(row=1, column=2, padx=10,pady=10)
        self.buttonDigitalOut1 = Button(self.frameRight, text="Toggle Digital Output #1",padx=8, bg="gray", command=lambda: self.buttonToggleDO(0))
        self.buttonDigitalOut1.grid(row=0, column=0, padx=5,pady=5)
        self.buttonDigitalOut2 = Button(self.frameRight, text="Toggle Digital Output #2",padx=8, bg="gray", command=lambda: self.buttonToggleDO(1))
        self.buttonDigitalOut2.grid(row=1, column=0, padx=5,pady=5)
        self.buttonDigitalOut3 = Button(self.frameRight, text="Toggle Digital Output #3",padx=8, bg="gray", command=lambda: self.buttonToggleDO(2))
        self.buttonDigitalOut3.grid(row=2, column=0, padx=5,pady=5)
        self.buttonDigitalOut4 = Button(self.frameRight, text="Toggle Digital Output #4",padx=8, bg="gray", command=lambda: self.buttonToggleDO(3))
        self.buttonDigitalOut4.grid(row=3, column=0, padx=5,pady=5)

        self.testStride = 0

    def buttonConnect(self):
        "Button to Connect to Stride"
        #Disable Connect Button If Successful
        self.IPs = self.IPEntry.get()
        #print("The IP Entered is: " + self.IPs)
        
        self.testStride = PyStrideDigital(self.IPs)
        successConnect=TRUE
        self.testStride.connectClient()

        #Test Firmware Version
        self.firmwareVer = self.testStride.getFirmwareVersion()
        print(f"The Firmware Version is: {self.firmwareVer}")
        self.strideConnected = True
        self.connectButton = Button(self.frameLeft, text="Connect",state=DISABLED, padx=50, command=self.buttonConnect)
        self.connectButton.grid(row=1,column=0,columnspan=2, padx=10, pady=10)
        self.disconnectButton = Button(self.frameLeft, text="Disconnect", padx=50, command=self.buttonDisconnect)
        self.disconnectButton.grid(row=2,column=0,columnspan=2, padx=10, pady=5)
        self.ModbusConnectedIndicator = Button(self.frameLeft, state=DISABLED,text="Connected       ",fg="white",bg="green", padx=50)
        self.ModbusConnectedIndicator.grid(row=3,column=0,columnspan=2, padx=10, pady=5)
        #print (self.testStride.client.connected)

    def buttonDisconnect(self):
        "Button to disConnect to Stride"
        if (self.testStride.client.connected):
            """Update Digital Outputs"""
            self.testStride.setDigitalOutput(0, FALSE)
            self.testStride.setDigitalOutput(1, FALSE)
            self.testStride.setDigitalOutput(2, FALSE)
            self.testStride.setDigitalOutput(3, FALSE)

            #Close Connection
            self.testStride.closeClient()
            self.strideConnected = False

            #Dumb Buttons
            self.connectButton = Button(self.frameLeft, text="Connect",padx=50, command=self.buttonConnect)
            self.connectButton.grid(row=1,column=0,columnspan=2, padx=10, pady=10)
            self.disconnectButton = Button(self.frameLeft, text="Disconnect",state=DISABLED, padx=50, command=self.buttonDisconnect)
            self.disconnectButton.grid(row=2,column=0,columnspan=2, padx=10, pady=5)
            self.ModbusConnectedIndicator = Button(self.frameLeft, state=DISABLED,text="Not Connected",bg="red", padx=50)
            self.ModbusConnectedIndicator.grid(row=3,column=0,columnspan=2, padx=10, pady=5)

    def buttonToggleDO(self, number):
        "Button to toggle DO"
        #print("Congrats you clicked the button " + str(number))

        """Toggle Internal Bit"""
        if number == 0:
            if self.strideDigitalOut0==True:
                self.strideDigitalOut0=False
                self.buttonDigitalOut1 = Button(self.frameRight, text="Toggle Digital Output #1",padx=8, bg="gray", command=lambda: self.buttonToggleDO(0))
                self.buttonDigitalOut1.grid(row=0, column=0, padx=5,pady=5)
            else:
                if self.strideConnected==True:
                    self.strideDigitalOut0=True
                    self.buttonDigitalOut1 = Button(self.frameRight, text="Toggle Digital Output #1",padx=8, bg="red", command=lambda: self.buttonToggleDO(0))
                    self.buttonDigitalOut1.grid(row=0, column=0, padx=5,pady=5)
                else:
                    print("Device Not Connected. Failed to Turn On Output")
        if number == 1:
            if self.strideDigitalOut1==True:
                self.strideDigitalOut1=False
                self.buttonDigitalOut2 = Button(self.frameRight, text="Toggle Digital Output #2",padx=8, bg="gray", command=lambda: self.buttonToggleDO(1))
                self.buttonDigitalOut2.grid(row=1, column=0, padx=5,pady=5)
            else:
                if self.strideConnected==True:
                    self.strideDigitalOut1=True
                    self.buttonDigitalOut2 = Button(self.frameRight, text="Toggle Digital Output #2",padx=8, bg="red", command=lambda: self.buttonToggleDO(1))
                    self.buttonDigitalOut2.grid(row=1, column=0, padx=5,pady=5)
                else:
                    print("Device Not Connected. Failed to Turn On Output")
        if number == 2:
            if self.strideDigitalOut2==True:
                self.strideDigitalOut2=False
                self.buttonDigitalOut3 = Button(self.frameRight, text="Toggle Digital Output #3",padx=8, bg="gray", command=lambda: self.buttonToggleDO(2))
                self.buttonDigitalOut3.grid(row=2, column=0, padx=5,pady=5)
            else:
                if self.strideConnected==True:
                    self.strideDigitalOut2=True
                    self.buttonDigitalOut3 = Button(self.frameRight, text="Toggle Digital Output #3",padx=8, bg="red", command=lambda: self.buttonToggleDO(2))
                    self.buttonDigitalOut3.grid(row=2, column=0, padx=5,pady=5)
                else:
                   print("Device Not Connected. Failed to Turn On Output") 
        if number == 3:
            if self.strideDigitalOut3==True:
                self.strideDigitalOut3=False
                self.buttonDigitalOut4 = Button(self.frameRight, text="Toggle Digital Output #4",padx=8, bg="gray", command=lambda: self.buttonToggleDO(3))
                self.buttonDigitalOut4.grid(row=3, column=0, padx=5,pady=5)
            else:
                if self.strideConnected==True:
                    self.strideDigitalOut3=True
                    self.buttonDigitalOut4 = Button(self.frameRight, text="Toggle Digital Output #4",padx=8, bg="red", command=lambda: self.buttonToggleDO(3))
                    self.buttonDigitalOut4.grid(row=3, column=0, padx=5,pady=5)
                else:
                   print("Device Not Connected. Failed to Turn On Output") 
    pass

main()