import win32gui
import win32con
import win32api

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1),0)


import get_picture , os , time
import threading

camera=get_picture.init()
def get_mugshot():
    thread=threading.Thread(target=get_picture.get_pic(camera))
    thread.start()

def get_input(question,type_input, clear_line=False, questions=[]):  
    """Question : a string
    Type : int, str, etc..."""
    if clear_line==True: os.system('cls')
    while True:
        user_input = input(question)
        try:
            user_input = type_input(user_input)
            if user_input not in questions and questions:
                print(f"input not in the list {questions}")
            else:
                return(user_input)
        except ValueError:
            print("input a valid type please")



Users={"Admin":["123456789",2],"Utilisateur":["987654321",1],"DEBUG":["MDP",3]}

def login():
    os.system("cls")
    menu_text=("""
    ██╗░░░░░░█████╗░░██████╗░░██████╗  ██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
    ██║░░░░░██╔══██╗██╔════╝░██╔════╝  ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
    ██║░░░░░██║░░██║██║░░██╗░╚█████╗░  ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
    ██║░░░░░██║░░██║██║░░╚██╗░╚═══██╗  ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
    ███████╗╚█████╔╝╚██████╔╝██████╔╝  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
    ╚══════╝░╚════╝░░╚═════╝░╚═════╝░  ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝
    Welcome to your computer
    Is it yours anyways ?    """)

    def print_menu():
        time.sleep(2.5)
        os.system("cls")
        print(menu_text)
    print_menu()
    running=True
    while running:
        user = get_input(question="Username : ",type_input=str,clear_line=False)
        if user in Users:
            password = get_input(question="Password : ",type_input=str,clear_line=False)
            if Users[user][0] == password:
                print("Succesful login ",user)
                os.system("TITLE LogsLoggerSuccess")
                get_input("Press <enter> to quit",type_input=str,clear_line=False)
                exit()
            else:
                print("Password uncorrect")
                get_mugshot()
                print_menu()
                
        else:
            print("no users of this name")
            get_mugshot()
            if get_input("Leave Y/N : ",str,clear_line=False,questions=["Y","N"]) == "Y":
                running=False
            else: print_menu()
no_bypass=False
if no_bypass:
    login()
else:
    os.system('start pythonw no_bypass.py')
    no_bypass=True
    login()