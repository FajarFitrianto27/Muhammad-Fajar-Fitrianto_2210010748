import PySimpleGUI as sg
sg.theme("LightBrown3")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM     : 2210010748")],
                           [sg.Text("Nama    : Muhammad Fajar Fitrianto")],
                           [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                           [sg.Text("Matkul  : Pemrograman Visual 3")],
                           ],
                        size=(400,200))
window()
window.close()
   
                   