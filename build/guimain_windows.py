from tkinter import *
import tkinter.messagebox
import os

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title('CSGO Ping Tester v2.1 by Defirence')

        self.pack(fill=BOTH, expand=1)

        #  button label length determines button size

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=514, y=0)

        ##############################
        # BUTTONS FOR ESEA FUNCTIONS #
        ##############################

        eseagermanytwoButton = Button(self, text="ESEA Germany 2", command=self.esea_germany_two)
        eseagermanytwoButton.place(x=0, y=0)

        gboneButton = Button(self, text="ESEA Great Britain 1", command=self.esea_gbone)
        gboneButton.place(x=0, y=24)

        gbtwoButton = Button(self, text="ESEA Great Britain 2", command=self.esea_gbtwo)
        gbtwoButton.place(x=0, y=48)

        francetwoButton = Button(self, text="ESEA France 2", command=self.esea_francetwo)
        francetwoButton.place(x=0, y=72)

        francethreeButton = Button(self, text="ESEA France 3", command=self.esea_francethree)
        francethreeButton.place(x=0, y=96)

        francefourButton = Button(self, text="ESEA France 4", command=self.esea_francefour)
        francefourButton.place(x=0, y=120)

        netherlandsoneButton = Button(self, text="ESEA Netherlands 1", command=self.esea_netherlandsone)
        netherlandsoneButton.place(x=0, y=144)

        netherlandstwoButton = Button(self, text="ESEA Netherlands 2", command=self.esea_netherlandstwo)
        netherlandstwoButton.place(x=0, y=168)

        swedenButton = Button(self, text="ESEA Sweden", command=self.esea_sweden)
        swedenButton.place(x=0, y=192)

        ##############################
        # FACEIT Matchmaking Buttons #
        ##############################

        faceitgermanyoneButton = Button(self, text="FACEIT Germany 1", command=self.faceitgermanyone)
        faceitgermanyoneButton.place(x=140, y=0)

        faceitgermanythreeButton = Button(self, text="FACEIT Germany 3", command=self.faceitgermanythree)
        faceitgermanythreeButton.place(x=140, y=24)

        faceitgboneButton = Button(self, text="FACEIT Great Britain 1", command=self.faceitgbone)
        faceitgboneButton.place(x=140, y=48)

        faceitgbtwoButton = Button(self, text="FACEIT Great Britain 2", command=self.faceitgbtwo)
        faceitgbtwoButton.place(x=140, y=72)

        faceitfrancetwoButton = Button(self, text="FACEIT France 2", command=self.faceitfrancetwo)
        faceitfrancetwoButton.place(x=140, y=96)

        faceitfrancethreeButton = Button(self, text="FACEIT France 3", command=self.faceitfrancethree)
        faceitfrancethreeButton.place(x=140, y=120)

        faceitnetherlandsoneButton = Button(self, text="FACEIT Netherlands 1", command=self.faceitnetherlandsone)
        faceitnetherlandsoneButton.place(x=140, y=144)

        faceitswedenButton = Button(self, text="FACEIT Sweden", command=self.faceitsweden)
        faceitswedenButton.place(x=140, y=168)

        faceitsouthafricafiveButton = Button(self, text="FACEIT South Africa Five", command=self.faceitsouthafricafive)
        faceitsouthafricafiveButton.place(x=140, y=192)

        faceitsouthafricasevenButton = Button(self, text="FACEIT South Africa Seven",
                                              command=self.faceitsouthafricaseven)
        faceitsouthafricasevenButton.place(x=140, y=216)

        ###################################
        # Valve Matchmaking Relay Buttons #
        ###################################

        valvemm_euw_oneButton = Button(self, text="Valve EU West 1 Relay", command=self.valve_euw_one)
        valvemm_euw_oneButton.place(x=308, y=0)

        valvemm_euw_twoButton = Button(self, text="Valve EU West 2 Relay", command=self.valve_euw_two)
        valvemm_euw_twoButton.place(x=308, y=24)

        valvemm_eue_oneButton = Button(self, text="Valve EU East Relay 1", command=self.valve_eue_one)
        valvemm_eue_oneButton.place(x=308, y=48)

        valvemm_eue_twoButton = Button(self, text="Valve EU East Relay 2", command=self.valve_eue_two)
        valvemm_eue_twoButton.place(x=308, y=72)

        valvemm_sweden_oneButton = Button(self, text="Valve Sweden 1 Relay", command=self.valve_sweden_one)
        valvemm_sweden_oneButton.place(x=308, y=96)

        valvemm_mideastButton = Button(self, text="Valve Middle East Relay", command=self.valve_middleeast)
        valvemm_mideastButton.place(x=308, y=120)

        valvemm_poland_oneButton = Button(self, text="Valve Poland 1 Relay", command=self.valve_poland_one)
        valvemm_poland_oneButton.place(x=308, y=144)

        valvemm_poland_twoButton = Button(self, text="Valve Poland 2 Relay", command=self.valve_poland_two)
        valvemm_poland_twoButton.place(x=308, y=168)

        valvemm_southafrica_oneButton = Button(self, text="Valve South Africa 1 Relay",
                                               command=self.valve_southafrica_one)
        valvemm_southafrica_oneButton.place(x=308, y=192)

        valvemm_southafrica_twoButton = Button(self, text="Valve South Africa 2 Relay",
                                               command=self.valve_southafrica_two)
        valvemm_southafrica_twoButton.place(x=308, y=216)

        ##################
        # ESEA Functions #
        ##################

    def esea_germany_two(self):

        print("Pinging ESEA Germany 2")
        hostname = "85.131.251.5"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_gbone(self):

        print("Pinging ESEA Great Britain 1")
        hostname = "37.122.249.1"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_gbtwo(self):

        print("Pinging ESEA Great Britain 2")
        hostname = "46.166.179.179"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_francetwo(self):

        print("Pinging ESEA France 2")
        hostname = "46.105.104.65"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_francethree(self):

        print("Pinging ESEA France 3")
        hostname = "176.31.234.4"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_francefour(self):

        print("Pinging ESEA France 4")
        hostname = "5.39.72.43"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_netherlandsone(self):

        print("Pinging ESEA Netherlands 1")
        hostname = "77.247.178.10"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_netherlandstwo(self):

        print("Pinging ESEA Netherlands 2")
        hostname = "109.201.133.100"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_sweden(self):

        print("Pinging ESEA Sweden")
        hostname = "37.0.123.1"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_spain(self):

        print("Pinging ESEA Spain")
        hostname = "82.98.141.43"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def esea_turkey(self):

        print("Pinging ESEA Turkey")
        hostname = "31.210.68.1"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    #########################
    # END OF ESEA FUNCTIONS #
    #########################

    ####################
    # FACEIT FUNCTIONS #
    ####################

    def faceitgermanyone(self):

        print("Pinging FACEIT Germany 1")
        hostname = "88.198.52.17"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgermanythree(self):

        print("Ping FACEIT Germany 3")
        hostname = "46.4.35.143"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgbone(self):

        print("Pinging FACEIT Great Britain 1")
        hostname = "82.145.38.91"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgbtwo(self):

        print("Pinging FACEIT Great Britain 2")
        hostname = "185.16.86.1"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitgbthree(self):

        print("Pinging FACEIT Great Britain 3")
        hostname = "87.117.219.99"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitfrancetwo(self):

        print("Pinging FACEIT France 2")
        hostname = "163.172.8.51"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitfrancethree(self):

        print("Pinging FACEIT France 3")
        hostname = "195.154.170.125"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitnetherlandsone(self):

        print("Pinging FACEIT Netherlands 1")
        hostname = "46.166.189.17"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitnetherlandstwo(self):

        print("Pinging FACEIT Netherlands 2")
        hostname = "185.16.84.57"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsweden(self):

        print("Pinging FACEIT Sweden 1")
        hostname = "185.62.207.33"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricafive(self):

        print("Pinging FACEIT South Africa 5")
        hostname = "165.73.240.115"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def faceitsouthafricaseven(self):

        print("Pinging FACEIT South Africa 7")
        hostname = "165.73.240.116"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    ###########################
    # END OF FACEIT FUNCTIONS #
    ###########################

    ###############################
    # VALVE MATCHMAKING FUNCTIONS #
    ###############################

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

        print("Pinging Valve EUW 2 Relay")
        hostname = "146.66.153.12"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_eue_one(self):

        print("Pinging Valve EUE Relay 1")
        hostname = "146.66.155.12"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def valve_eue_two(self):

        print("Pinging Valve EUE Relay 2")
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
        hostname = "155.133.238.163"
        response = os.system("ping " + hostname)
        if response == 0:
            ping = "Ping Successful"
        else:
            ping = "Ping Unsuccessful"

        print(ping)

        return ping

    def client_exit(self):
        sys.exit()


root = Tk()
root.geometry("549x243")
app = Window(root)
root.mainloop()

# Thanks for using my program
