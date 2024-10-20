import PySimpleGUI as sg
sg.theme("LightBlue7")
sg.theme_text_color("#E0EEEE")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM   : 2210010748 ")],
                           [sg.Text("Nama  : Muhammad Fajar Fitrianto ")],
                           [sg.Text("Kelas : 5B NonReg Banjarmasin ")]
                           ],
                   size=(510,200),
                   font=("Times New Roman", 18))
window()
window.close()