import os
from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #   define function for tkinter window

    def init_window(self):

        self.master.title("CSGO Ping Tester v1.4 by Defirence")

        self.pack(fill=BOTH, expand=1)

        #   start adding esea (tkinter) buttons
        #   button label length determines button size

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=514, y=0)

        eseagermanyoneButton = Button(self, text="ESEA Germany 1", command=self.esea_germany_one)
        eseagermanyoneButton.place(x=0, y=0)

        eseagermanytwoButton = Button(self, text="ESEA Germany 2", command=self.esea_germany_two)
        eseagermanytwoButton.place(x=0, y=24)

        gboneButton = Button(self, text="ESEA Great Britain 1", command=self.esea_gbone)
        gboneButton.place(x=0, y=48)

        gbtwoButton = Button(self, text="ESEA Great Britain 2", command=self.esea_gbtwo)
        gbtwoButton.place(x=0, y=72)

        franceoneButton = Button(self, text="ESEA France 1", command=self.esea_franceone)
        franceoneButton.place(x=0, y=96)

        francetwoButton = Button(self, text="ESEA France 2", command=self.esea_francetwo)
        francetwoButton.place(x=0, y=120)

        francethreeButton = Button(self, text="ESEA France 3", command=self.esea_francethree)
        francethreeButton.place(x=0, y=144)

        francefourButton = Button(self, text="ESEA France 4", command=self.esea_francefour)
        francefourButton.place(x=0, y=168)

        netherlandsoneButton = Button(self, text="ESEA Netherlands 1", command=self.esea_netherlandsone)
        netherlandsoneButton.place(x=0, y=192)

        netherlandstwoButton = Button(self, text="ESEA Netherlands 2", command=self.esea_netherlandstwo)
        netherlandstwoButton.place(x=0, y=216)

        swedenButton = Button(self, text="ESEA Sweden", command=self.esea_sweden)
        swedenButton.place(x=0, y=240)

        spainButton = Button(self, text="ESEA Spain", command=self.esea_spain)
        spainButton.place(x=0, y=264)

        #   start adding faceit (tkinter) buttons below

        faceitgermanyoneButton = Button(self, text="FACEIT Germany 1", command=self.faceitgermanyone)
        faceitgermanyoneButton.place(x=140, y=0)

        faceitgermanytwoButton = Button(self, text="FACEIT Germany 2", command=self.faceitgermanytwo)
        faceitgermanytwoButton.place(x=140, y=24)

        faceitgermanythreeButton = Button(self, text="FACEIT Germany 3", command=self.faceitgermanythree)
        faceitgermanythreeButton.place(x=140, y=48)

        faceitgboneButton = Button(self, text="FACEIT Great Britain 1", command=self.faceitgbone)
        faceitgboneButton.place(x=140, y=72)

        faceitgbtwoButton = Button(self, text="FACEIT Great Britain 2", command=self.faceitgbtwo)
        faceitgbtwoButton.place(x=140, y=96)

        faceitfranceoneButton = Button(self, text="FACEIT France 1", command=self.faceitfranceone)
        faceitfranceoneButton.place(x=140, y=120)

        faceitfrancetwoButton = Button(self, text="FACEIT France 2", command=self.faceitfrancetwo)
        faceitfrancetwoButton.place(x=140, y=144)

        faceitfrancethreeButton = Button(self, text="FACEIT France 3", command=self.faceitfrancethree)
        faceitfrancethreeButton.place(x=140, y=168)

        faceitnetherlandsoneButton = Button(self, text="FACEIT Netherlands 1", command=self.faceitnetherlandsone)
        faceitnetherlandsoneButton.place(x=140, y=192)

        faceitnetherlandstwoButton = Button(self, text="FACEIT Netherlands 2", command=self.faceitnetherlandstwo)
        faceitnetherlandstwoButton.place(x=140, y=216)

        faceitswedenButton = Button(self, text="FACEIT Sweden", command=self.faceitsweden)
        faceitswedenButton.place(x=140, y=240)

        faceitsouthafricaoneButton = Button(self, text="FACEIT South Africa One", command=self.faceitsouthafricaone)
        faceitsouthafricaoneButton.place(x=140, y=264)

        faceitsouthafricatwoButton = Button(self, text="FACEIT South Africa Two", command=self.faceitsouthafricatwo)
        faceitsouthafricatwoButton.place(x=140, y=288)

        faceitsouthafricathreeButton = Button(self, text="FACEIT South Africa Three",
                                              command=self.faceitsouthafricathree)
        faceitsouthafricathreeButton.place(x=140, y=312)

        faceitsouthafricafourButton = Button(self, text="FACEIT South Africa Four", command=self.faceitsouthafricafour)
        faceitsouthafricafourButton.place(x=140, y=336)

        faceitsouthafricafiveButton = Button(self, text="FACEIT South Africa Five", command=self.faceitsouthafricafive)
        faceitsouthafricafiveButton.place(x=140, y=360)

        faceitsouthafricasixButton = Button(self, text="FACEIT South Africa Six", command=self.faceitsouthafricasix)
        faceitsouthafricasixButton.place(x=140, y=384)

        faceitsouthafricasevenButton = Button(self, text="FACEIT South Africa Seven",
                                              command=self.faceitsouthafricaseven)
        faceitsouthafricasevenButton.place(x=140, y=408)

        #   start adding valve matchmaking (tkinter) buttons below

        valvemm_euw_oneButton = Button(self, text="Valve EU West 1", command=self.valve_euw_one)
        valvemm_euw_oneButton.place(x=284, y=0)

        valvemm_euw_twoButton = Button(self, text="Valve EU West 2", command=self.valve_euw_two)
        valvemm_euw_twoButton.place(x=284, y=24)

        valvemm_eue_oneButton = Button(self, text="Valve EU East 1", command=self.valve_eue_one)
        valvemm_eue_oneButton.place(x=284, y=48)

        valvemm_sweden_oneButton = Button(self, text="Valve Sweden 1", command=self.valve_sweden_one)
        valvemm_sweden_oneButton.place(x=284, y=72)

        valvemm_sweden_twoButton = Button(self, text="Valve Sweden 2", command=self.valve_sweden_two)
        valvemm_sweden_twoButton.place(x=284, y=96)

        valvemm_mideastButton = Button(self, text="Valve Middle East", command=self.valve_middleeast)
        valvemm_mideastButton.place(x=284, y=120)

        valvemm_poland_oneButton = Button(self, text="Valve Poland 1", command=self.valve_poland_one)
        valvemm_poland_oneButton.place(x=284, y=144)

        valvemm_poland_twoButton = Button(self, text="Valve Poland 2", command=self.valve_poland_two)
        valvemm_poland_twoButton.place(x=284, y=168)

        valvemm_spain_oneButton = Button(self, text="Valve Spain 1", command=self.valve_spain_one)
        valvemm_spain_oneButton.place(x=284, y=192)

        valvemm_spain_twoButton = Button(self, text="Valve Spain 2", command=self.valve_spain_two)
        valvemm_spain_twoButton.place(x=284, y=216)

        valvemm_southafrica_oneButton = Button(self, text="Valve South Africa 1", command=self.valve_southafrica_one)
        valvemm_southafrica_oneButton.place(x=284, y=240)

        valvemm_southafrica_twoButton = Button(self, text="Valve South Africa 2", command=self.valve_southafrica_two)
        valvemm_southafrica_twoButton.place(x=284, y=264)

    #   it would actually help to remember to write the Button syntax correctly
    #   leaving this comment as a reminder to check the
    #   syntax for buttons and button.place

    #   start defining esea server functions below

    @staticmethod
    def esea_germany_one():

        hostname = "85.131.152.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_germany_two():

        hostname = "85.131.251.5"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_gbone():

        hostname = "37.122.249.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_gbtwo():

        hostname = "46.166.179.179"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_franceone():

        hostname = "37.187.68.60"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_francetwo():

        hostname = "46.105.104.65"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_francethree():

        hostname = "176.31.234.4"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_francefour():

        hostname = "5.39.72.43"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_netherlandsone():

        hostname = "77.247.178.10"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_netherlandstwo():

        hostname = "109.201.133.100"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_sweden():
        hostname = "37.0.123.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_spain():

        hostname = "82.98.141.43"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def esea_turkey():

        hostname = "31.210.68.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    #   finish defining esea server functions

    #   start defining faceit server functions below

    #   I only realized very far into this project that function values (?)
    #   or strings can be defined with numbers like so
    #   def faceitgermany1(self):
    #   def faceitgermany2(self): etc
    #   it does still work if you want to rather optimize/change the code to run like that
    #   if I do have to change the function naming convention to numbers I'd have to edit the entire code
    #   to reflect this, I'll probably do it at a later stage

    @staticmethod
    def faceitgermanyone():

        hostname = "88.198.52.17"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitgermanytwo():

        hostname = "148.251.124.133"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitgermanythree():

        hostname = "46.4.35.143"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitgbone():

        hostname = "82.145.38.91"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitgbtwo():

        hostname = "185.16.86.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitgbthree():

        hostname = "87.117.219.99"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitfranceone():

        hostname = "62.210.84.115"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitfrancetwo():

        hostname = "163.172.8.51"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitfrancethree():

        hostname = "195.154.170.125"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitnetherlandsone():

        hostname = "46.166.189.17"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitnetherlandstwo():

        hostname = "185.16.84.57"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsweden():

        hostname = "185.62.207.33"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricaone():

        hostname = "165.73.240.107"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricatwo():

        hostname = "165.73.240.108"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricathree():

        hostname = "165.73.240.118"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricafour():

        hostname = "165.73.240.110"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricafive():

        hostname = "165.73.240.115"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricasix():

        hostname = "165.73.240.109"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def faceitsouthafricaseven():

        hostname = "165.73.240.116"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    #   end defining FACEIT server functions here

    #   start defining valve matchmaking server functions below

    @staticmethod
    def valve_euw_one():

        hostname = "146.66.153.12"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_euw_two():

        hostname = "146.66.153.12"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_eue_one():

        hostname = "146.66.155.12"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_eue_two():

        hostname = "146.66.155.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_singapore():

        hostname = "103.28.54.3"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_singapore_two():

        hostname = "103.10.124.9"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_singapore_three():

        hostname = "45.121.184.1"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_middleeast():

        hostname = "185.25.183.4"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_sweden_one():

        hostname = "146.66.156.211"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_sweden_two():

        hostname = "146.66.180.211"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_poland_one():

        hostname = "155.133.228.100"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_poland_two():

        hostname = "155.133.241.24"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_spain_one():

        hostname = "155.133.246.13"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_spain_two():

        hostname = "155.133.247.16"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_southafrica_one():

        hostname = "155.133.238.162"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def valve_southafrica_two():

        hostname = "155.133.238.163"
        response = os.system("ping " + hostname)
        if response == 0:
            pingstatus = "Active"
        else:
            pingstatus = "Error"

        print("Ping Test Complete")

        return pingstatus

    @staticmethod
    def client_exit():
        sys.exit()


root = Tk()
root.geometry("545x430")
app = Window(root)
root.mainloop()
