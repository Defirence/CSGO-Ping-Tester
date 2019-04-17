from tkinter import *
import os

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #   define function for tkinter_gui_lib window

    def init_window(self):

        self.master.title("CSGO Ping Tester v2.0 by Defirence")

        self.pack(fill=BOTH, expand=1)

        #   begin adding ESEA Matchmaking (tkinter_gui_lib) buttons
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

        francetwoButton = Button(self, text="ESEA France 2", command=self.esea_francetwo)
        francetwoButton.place(x=0, y=96)

        francethreeButton = Button(self, text="ESEA France 3", command=self.esea_francethree)
        francethreeButton.place(x=0, y=120)

        francefourButton = Button(self, text="ESEA France 4", command=self.esea_francefour)
        francefourButton.place(x=0, y=144)

        netherlandsoneButton = Button(self, text="ESEA Netherlands 1", command=self.esea_netherlandsone)
        netherlandsoneButton.place(x=0, y=168)

        netherlandstwoButton = Button(self, text="ESEA Netherlands 2", command=self.esea_netherlandstwo)
        netherlandstwoButton.place(x=0, y=192)

        swedenButton = Button(self, text="ESEA Sweden", command=self.esea_sweden)
        swedenButton.place(x=0, y=216)

        #   begin adding FACEIT Matchmaking (tkinter_gui_lib) buttons below.

        faceitgermanyoneButton = Button(self, text="FACEIT Germany 1", command=self.faceitgermanyone)
        faceitgermanyoneButton.place(x=140, y=0)

        faceitgermanythreeButton = Button(self, text="FACEIT Germany 3", command=self.faceitgermanythree)
        faceitgermanythreeButton.place(x=140, y=24)

        faceitgboneButton = Button(self, text="FACEIT Great Britain 1", command=self.faceitgbone)
        faceitgboneButton.place(x=140, y=48)

        faceitgbtwoButton = Button(self, text="FACEIT Great Britain 2", command=self.faceitgbtwo)
        faceitgbtwoButton.place(x=140, y=72)

        faceitfranceoneButton = Button(self, text="FACEIT France 1", command=self.faceitfranceone)
        faceitfranceoneButton.place(x=140, y=96)

        faceitfrancetwoButton = Button(self, text="FACEIT France 2", command=self.faceitfrancetwo)
        faceitfrancetwoButton.place(x=140, y=120)

        faceitfrancethreeButton = Button(self, text="FACEIT France 3", command=self.faceitfrancethree)
        faceitfrancethreeButton.place(x=140, y=144)

        faceitnetherlandsoneButton = Button(self, text="FACEIT Netherlands 1", command=self.faceitnetherlandsone)
        faceitnetherlandsoneButton.place(x=140, y=168)

        faceitnetherlandstwoButton = Button(self, text="FACEIT Netherlands 2", command=self.faceitnetherlandstwo)
        faceitnetherlandstwoButton.place(x=140, y=192)

        faceitswedenButton = Button(self, text="FACEIT Sweden", command=self.faceitsweden)
        faceitswedenButton.place(x=140, y=216)

        faceitsouthafricaoneButton = Button(self, text="FACEIT South Africa One", command=self.faceitsouthafricaone)
        faceitsouthafricaoneButton.place(x=140, y=240)

        faceitsouthafricatwoButton = Button(self, text="FACEIT South Africa Two", command=self.faceitsouthafricatwo)
        faceitsouthafricatwoButton.place(x=140, y=264)

        faceitsouthafricathreeButton = Button(self, text="FACEIT South Africa Three",
                                              command=self.faceitsouthafricathree)
        faceitsouthafricathreeButton.place(x=140, y=288)

        faceitsouthafricafourButton = Button(self, text="FACEIT South Africa Four", command=self.faceitsouthafricafour)
        faceitsouthafricafourButton.place(x=140, y=312)

        faceitsouthafricafiveButton = Button(self, text="FACEIT South Africa Five", command=self.faceitsouthafricafive)
        faceitsouthafricafiveButton.place(x=140, y=336)

        faceitsouthafricasixButton = Button(self, text="FACEIT South Africa Six", command=self.faceitsouthafricasix)
        faceitsouthafricasixButton.place(x=140, y=360)

        faceitsouthafricasevenButton = Button(self, text="FACEIT South Africa Seven",
                                              command=self.faceitsouthafricaseven)
        faceitsouthafricasevenButton.place(x=140, y=384)

        #   begin adding valve matchmaking (tkinter_gui_lib) buttons below.

        valvemm_euw_oneButton = Button(self, text="Valve EU West 1", command=self.valve_euw_one)
        valvemm_euw_oneButton.place(x=308, y=0)

        valvemm_euw_twoButton = Button(self, text="Valve EU West 2", command=self.valve_euw_two)
        valvemm_euw_twoButton.place(x=308, y=24)

        valvemm_eue_oneButton = Button(self, text="Valve EU East", command=self.valve_eue_one)
        valvemm_eue_oneButton.place(x=308, y=48)

        valvemm_sweden_oneButton = Button(self, text="Valve Sweden 1", command=self.valve_sweden_one)
        valvemm_sweden_oneButton.place(x=308, y=72)

        valvemm_mideastButton = Button(self, text="Valve Middle East", command=self.valve_middleeast)
        valvemm_mideastButton.place(x=308, y=96)

        valvemm_poland_oneButton = Button(self, text="Valve Poland 1", command=self.valve_poland_one)
        valvemm_poland_oneButton.place(x=308, y=120)

        valvemm_poland_twoButton = Button(self, text="Valve Poland 2", command=self.valve_poland_two)
        valvemm_poland_twoButton.place(x=308, y=144)

        valvemm_spain_oneButton = Button(self, text="Valve Spain 1", command=self.valve_spain_one)
        valvemm_spain_oneButton.place(x=308, y=168)

        valvemm_spain_twoButton = Button(self, text="Valve Spain 2", command=self.valve_spain_two)
        valvemm_spain_twoButton.place(x=308, y=192)

        valvemm_southafrica_oneButton = Button(self, text="Valve South Africa 1", command=self.valve_southafrica_one)
        valvemm_southafrica_oneButton.place(x=308, y=216)

        valvemm_southafrica_twoButton = Button(self, text="Valve South Africa 2", command=self.valve_southafrica_two)
        valvemm_southafrica_twoButton.place(x=308, y=240)

    #   commented out ESEA Spain because it no longer works
    #   and also Valve Sweden 2 because there is no reply on the ping
    #   so that basically leaves a useless function + button

    #   start defining esea server functions below

    def esea_germany_one(self):

        print("Pinging ESEA Germany 1")
        hostname = "85.131.152.1 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Error, Ping Unsuccessful"

        print(ping)

        return ping

    def esea_germany_two(self):

        print("Pinging ESEA Germany 2")
        hostname = "85.131.251.5 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_gbone(self):

        print("Pinging ESEA Great Britain 1")
        hostname = "37.122.249.1 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_gbtwo(self):

        print("Pinging ESEA Great Britain 2")
        hostname = "46.166.179.179 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_francetwo(self):

        print("Pinging ESEA France 2")
        hostname = "46.105.104.65 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_francethree(self):

        print("Pinging ESEA France 3")
        hostname = "176.31.234.4 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_francefour(self):

        print("Pinging ESEA France 4")
        hostname = "5.39.72.43 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_netherlandsone(self):

        print("Pinging ESEA Netherlands 1")
        hostname = "77.247.178.10 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_netherlandstwo(self):

        print("Pinging ESEA Netherlands 2")
        hostname = "109.201.133.100 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_sweden(self):

        print("Pinging ESEA Sweden")
        hostname = "37.0.123.1 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_spain(self):

        print("Pinging ESEA Spain")
        hostname = "82.98.141.43 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_turkey(self):

        print("Pinging ESEA Turkey")
        hostname = "31.210.68.1 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    #   finish defining esea server functions.

    #   start defining faceit server functions below.

    def faceitgermanyone(self):

        print("Pinging FACEIT Germany 1")
        hostname = "88.198.52.17 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    # removed old function to improve run time
    # but I add two comment lines which will impact loading time lol

    def faceitgermanythree(self):

        print("Ping FACEIT Germany 3")
        hostname = "46.4.35.143 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgbone(self):

        print("Pinging FACEIT Great Britain 1")
        hostname = "82.145.38.91 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgbtwo(self):

        print("Pinging FACEIT Great Britain 2")
        hostname = "185.16.86.1 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgbthree(self):

        print("Pinging FACEIT Great Britain 3")
        hostname = "87.117.219.99 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitfranceone(self):

        print("Pinging FACEIT France 1")
        hostname = "62.210.84.115 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitfrancetwo(self):

        print("Pinging FACEIT France 2")
        hostname = "163.172.8.51 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitfrancethree(self):

        print("Pinging FACEIT France 3")
        hostname = "195.154.170.125 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitnetherlandsone(self):

        print("Pinging FACEIT Netherlands 1")
        hostname = "46.166.189.17 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitnetherlandstwo(self):

        print("Pinging FACEIT Netherlands 2")
        hostname = "185.16.84.57 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsweden(self):

        print("Pinging FACEIT Sweden 1")
        hostname = "185.62.207.33 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricaone(self):

        print("Pinging FACEIT South Africa 1")
        hostname = "165.73.240.107"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricatwo(self):

        print("Pinging FACEIT South Africa 2")
        hostname = "165.73.240.108 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricathree(self):

        print("Pinging FACEIT South Africa 3")
        hostname = "165.73.240.118 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricafour(self):

        print("Pinging FACEIT South Africa 4")
        hostname = "165.73.240.110 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricafive(self):

        print("Pinging FACEIT South Africa 5")
        hostname = "165.73.240.115 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricasix(self):

        print("Pinging FACEIT South Africa 6")
        hostname = "165.73.240.109"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricaseven(self):

        print("Pinging FACEIT South Africa 7")
        hostname = "165.73.240.116 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    #   end defining FACEIT server functions here

    #   start defining valve matchmaking server functions below

    def valve_euw_one(self):

        print("Pinging Valve EUW 1 Relay")
        hostname = "146.66.153.12"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_euw_two(self):

        print("Pinging Valve EUW 2")
        hostname = "146.66.153.12"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_eue_one(self):

        print("Pinging Valve EUE 1")
        hostname = "146.66.155.12"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_eue_two(self):

        print("Pinging Valve EUE 2")
        hostname = "146.66.155.1"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_singapore(self):

        print("Pinging Valve Singapore 1")
        hostname = "103.28.54.3"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_singapore_two(self):

        print("Pinging Valve Singapore 2")
        hostname = "103.10.124.9"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_singapore_three(self):

        print("Pinging Valve Singapore 3")
        hostname = "45.121.184.1"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_middleeast(self):

        print("Pinging Valve Middle-East")
        hostname = "185.25.183.4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_sweden_one(self):

        print("Pinging Valve Sweden 1")
        hostname = "146.66.156.211"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_sweden_two(self):

        print("Pinging Valve Sweden 2")
        hostname = "146.66.180.211"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_poland_one(self):

        print("Pinging Valve Poland One")
        hostname = "155.133.228.100"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_poland_two(self):

        print("Pinging Valve Poland 2")
        hostname = "155.133.241.24"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_spain_one(self):

        print("Pinging Valve Spain 1")
        hostname = "155.133.246.13"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_spain_two(self):

        print("Pinging Valve Spain 2")
        hostname = "155.133.247.16"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_southafrica_one(self):

        print("Pinging Valve South Africa 1")
        hostname = "155.133.238.162"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_southafrica_two(self):

        print("Pinging Valve South Africa 2")
        hostname = "155.133.238.163 -c 4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        elif response == 2:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def client_exit(self):
        sys.exit()


root = Tk()
root.geometry("550x450")
app = Window(root)
root.mainloop()
