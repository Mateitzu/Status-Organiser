import time
import random
import json
import os
from colorama import Fore, Back, Style
import colorama
from tkinter import messagebox, filedialog

colorama.init()

settings = {}

def loadsettings():
    global settings
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as file:
            settings = json.load(file)
    else:
        settings = {
            "logo_time": 1,
            "author_time": 1,
            "message_time": 1,
            "text_color": "white",
            "password": "12345",
            "fx": False,
            "sud": False,
            "autovm": False
        }
        with open("settings.json", "w") as file:
            json.dump(settings, file, indent=2)

def save_settings():
    global settings
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=2)

def save():
    global data
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

loadsettings()

os.system("cls")
resize = os.get_terminal_size()
if resize.columns < 120:
    print(Fore.RED + "Terminal size is too small! Please resize the terminal to at least 120 columns and 30 lines.")
    time.sleep(3)
    quit()
if resize.lines < 30:
    print(Fore.RED + "Terminal size is too small! Please resize the terminal to at least 190 columns and 30 lines.")
    time.sleep(3)
    quit()
os.system("cls")
os.system("title User Management System")
os.system("chcp 65001")
os.system("cls")

logo_time = settings["logo_time"]
author_time = settings["author_time"]
message_time = settings["message_time"]
text_color = settings["text_color"]
realpass = settings["password"]
fx = settings["fx"]
sud = settings["sud"]
autovm = settings["autovm"]

def intro():
    os.system("cls")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print( Fore.BLUE + "                            ██╗   ██╗███╗   ███╗███╗   ██╗ ██████╗ ███████╗██╗   ██╗███████╗")
    print(Fore.WHITE + "                            ██║   ██║████╗ ████║████╗  ██║██╔════╝ ██╔════╝╚██╗ ██╔╝██╔════╝")
    print(Fore.WHITE + "                            ██║   ██║██╔████╔██║██╔██╗ ██║██║  ███╗███████╗ ╚████╔╝ ███████╗")
    print(Fore.WHITE + "                            ██║   ██║██║╚██╔╝██║██║╚██╗██║██║   ██║╚════██║  ╚██╔╝  ╚════██║")
    print( Fore.BLUE + "                            ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║╚██████╔╝███████║   ██║   ███████║")
    print( Fore.BLUE + "                             ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝")                                                              
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(logo_time)
    os.system("cls")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(Fore.CYAN + "                                                             BY")
    print(Fore.CYAN + "                                                          Mateitzu")
    print("")
    print("")                                                              
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(author_time)
    os.system("cls")
    

intro()
time.sleep(0.5)   

if text_color == "white":
    color = Fore.WHITE
elif text_color == "red":
    color = Fore.RED
elif text_color == "green":
    color = Fore.GREEN
elif text_color == "blue":
    color = Fore.BLUE
elif text_color == "yellow":
    color = Fore.YELLOW
elif text_color == "cyan":
    color = Fore.CYAN
elif text_color == "magenta":
    color = Fore.MAGENTA

password = input(color + "Please enter the password: ")

visualmode = False

data = {}
if not os.path.exists("data.json"):
    with open("data.json", "w") as file:
        json.dump({}, file)

def read():
    global data
    with open("data.json", "r") as file:
        data = json.load(file)

def adduser(user):
    global data
    with open("data.json", "r") as file:
        data = json.load(file)
    data[user] = {"banned": False}
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

def removeuser(user):
    global data
    if user in data:
        del data[user]
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
def banuser(user):
    global data
    if user in data:
        data[user]["banned"] = True
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
def unbanuser(user):
    global data
    if user in data:
        data[user]["banned"] = False
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
def showusers(sleep):
    i=0
    print(color + "Users:")
    for user in data:
        i+=1
        if sud == True:
            if data[user]["banned"]:
                print(Fore.RED + str(i) + "."+  " ->  " + user + " (BANNED)")
            else:
                print(color + str(i) + "."+  " ->  " + user)
        else:
            if data[user]["banned"]:
                print(Fore.RED + " ->  " + user + " (BANNED)")
            else:
                print(color + " ->  " + user)
        time.sleep(sleep)

if password == realpass:
    print(Fore.GREEN + "Access granted!")
    if autovm == True:
        visualmode = True
    time.sleep(2)
    os.system("cls")
    while True:
        read()
        if visualmode == True:
            showusers(sleep=0)
            print("")
            print("")
        if visualmode == False:
            command1 = input(color + "Enter Command, adduser, adduserlist, removeuser, removeuserlist, banuser, unbanuser, showusers, wipeserver, exit, settings, info, help, entervisualmode| : \n")
        else:
            command1 = input(color + "Enter Command, adduser, adduserlist, removeuser, removeuserlist, banuser, unbanuser, showusers, wipeserver, exit, settings, info, help, exitvisualmode| : \n")
        if command1.lower() == "adduser":
            usertoadd = input(color + "Please enter the username: ")
            adduser(user=usertoadd)
            time.sleep(0.1)
            print(Fore.GREEN + "User " + usertoadd + " added succesfully!")
            time.sleep(message_time)
            os.system("cls")
        elif command1.lower() == "removeuser":
            usertorem = input(color + "Please enter the username or id: ")
            time.sleep(0.1)
            if usertorem.isnumeric():
                if int(usertorem) > len(data):
                    print(Fore.RED + "User ID: " + usertorem + " does not exist!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print(Fore.GREEN + "User " + usertorem + " removed succesfully!")
                    time.sleep(message_time)
                    removeuser(user=list(data.keys())[int(usertorem)-1])
                    os.system("cls")
            else:
                if usertorem not in data:
                    print(Fore.RED + "User " + usertorem + " does not exist!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print(Fore.GREEN + "User " + usertorem + " removed succesfully!")
                    removeuser(user=usertorem)
                    time.sleep(message_time)
                    os.system("cls")
        elif command1.lower() == "banuser":
            usertoban = input(color + "Please enter the username: ")
            
            time.sleep(0.1)
            if usertoban.isnumeric():
                if int(usertoban) > len(data):
                    print(Fore.RED + "User ID: " + usertoban + " does not exist!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print(Fore.GREEN + "User " + usertoban + " banned succesfully!")
                    time.sleep(message_time)
                    banuser(user=list(data.keys())[int(usertoban)-1])
                    os.system("cls")
            else:
                if usertoban not in data:
                    print(Fore.RED + "User " + usertoban + " does not exist!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print(Fore.GREEN + "User " + usertoban + " banned succesfully!")
                    banuser(user=usertoban)
                    time.sleep(message_time)
                    os.system("cls")
        elif command1.lower() == "unbanuser":
            usertounban = input(color + "Please enter the username: ")
            
            time.sleep(0.1)
            if usertounban.isnumeric():
                if int(usertounban) > len(data):
                    print(Fore.RED + "User ID: " + usertounban + " does not exist!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print(Fore.GREEN + "User " + usertounban + " unbanned succesfully!")
                    time.sleep(message_time)
                    unbanuser(user=list(data.keys())[int(usertounban)-1])
                    os.system("cls")
            else:    
                if usertounban not in data:
                    print(Fore.RED + "User " + usertounban + " does not exist!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print(Fore.GREEN + "User " + usertounban + " unbanned succesfully!")
                    unbanuser(user=usertounban)
                    time.sleep(message_time)
                    os.system("cls")
        elif command1.lower() == "showusers":
            print("")
            print("")
            showusers(sleep=0.05)
            print("")
            print("")
        elif command1.lower() == "entervisualmode":
            visualmode = True
            print(color + "Visual mode activated!")
            time.sleep(message_time)
            os.system("cls")
        elif command1.lower() == "exitvisualmode":
            visualmode = False
            print(color + "Visual mode deactivated!")
            time.sleep(message_time)
            os.system("cls")
        elif command1.lower() == "wipeserver":
            answer = input(Fore.MAGENTA + "Are you sure you want to wipe the server? (y/n): ")
            if answer.lower() == "y":
                with open("data.json", "w") as file:
                    json.dump({}, file, indent=2)
                time.sleep(0.5)
                print(color + "Server wiped!")
                time.sleep(message_time)
                os.system("cls")
            else:
                print(color + "Server wipe cancelled!")
                time.sleep(message_time)
                os.system("cls")
        elif command1.lower() == "exit":
            if fx == False:
                intro()
            quit()
        elif command1.lower() == "adduserlist":
            os.system("cls")
            filepath = filedialog.askopenfilename(title="Select a json file", filetypes=[("FILE",".json")])
            if os.path.exists(filepath):
                with open(filepath, "r") as file:
                    toadd = json.load(file)
                for user in toadd:
                    if user not in data:
                        adduser(user=user)
                        print(Fore.GREEN + "User " + user + " added succesfully!")
                    else:
                        print(Fore.RED + "User " + user + " already exists!")
                answer = input(Fore.MAGENTA + "Do you want to save the changes? (y/n): ")
                if answer.lower() == "y":
                    print(Fore.GREEN + "Changes saved!")
                    time.sleep(message_time)
                    os.system("cls")
                else:
                    for user in toadd:
                        if user in data:
                            removeuser(user=user)
                            print(Fore.RED + "User " + user + " removed succesfully!")
                        else:
                            print(Fore.YELLOW + "User " + user + " does not exist!")
                    proceed = input(Fore.MAGENTA + "Do you want to proceed? (y/n): ")
                    if proceed.lower() == "y":
                        os.system("cls")
                        save()
                    else:
                        after = input(Fore.MAGENTA + "Do you want to undo changes? (y/n): ")
                        if after.lower() == "y":
                            for user in toadd:
                                if user not in data:
                                    adduser(user=user)
                                    print(Fore.GREEN + "User " + user + " added succesfully!")
                                else:
                                    print(Fore.RED + "User " + user + " already exists!")
                            proceedagain = input(Fore.MAGENTA + "Do you want to proceed? (y/n): ")
                            if proceedagain.lower() == "y":
                                os.system("cls")
                                save()
                            else:
                                for user in toadd:
                                    if user in data:
                                        removeuser(user=user)
                                print(Fore.RED + "Changes not saved!")
                                time.sleep(message_time)
                                os.system("cls")
                        else:
                            print(Fore.GREEN + "Changes saved!")
                            time.sleep(message_time)
                            os.system("cls")
                            save()
        if command1.lower() == "removeuserlist":
            os.system("cls")
            filepath = filedialog.askopenfilename(title="Select a json file", filetypes=[("FILE",".json")])
            if os.path.exists(filepath):
                with open(filepath, "r") as file:
                    toremove = json.load(file)
                for user in toremove:
                    if user in data:
                        removeuser(user=user)
                        print(Fore.GREEN + "User " + user + " removed succesfully!")
                    else:
                        print(Fore.RED + "User " + user + " does not exist!")
                answer = input(Fore.MAGENTA + "Do you want to save the changes? (y/n): ")
                if answer.lower() == "y":
                    print(Fore.GREEN + "Changes saved!")
                    time.sleep(message_time)
                    os.system("cls")
                else:
                    for user in toremove:
                        if user not in data:
                            adduser(user=user)
                            print(Fore.GREEN + "User " + user + " added succesfully!")
                        else:
                            print(Fore.RED + "User " + user + " already exists!")
                    proceed = input(Fore.MAGENTA + "Do you want to proceed? (y/n): ")
                    if proceed.lower() == "y":
                        os.system("cls")
                        save()
                    else:
                        after = input(Fore.MAGENTA + "Do you want to undo changes? (y/n): ")
                        if after.lower() == "y":
                            for user in toremove:
                                if user in data:
                                    removeuser(user=user)
                                    print(Fore.RED + "User " + user + " removed succesfully!")
                                else:
                                    print(Fore.YELLOW + "User " + user + " does not exist!")
                            proceedagain = input(Fore.MAGENTA + "Do you want to proceed? (y/n): ")
                            if proceedagain.lower() == "y":
                                os.system("cls")
                                save()
                            else:
                                for user in toremove:
                                    if user in data:
                                        adduser(user=user)
                                print(Fore.RED + "Changes not saved!")
                                time.sleep(message_time)
                                os.system("cls")
                        else:
                            print(Fore.GREEN + "Changes saved!")
                            time.sleep(message_time)
                            os.system("cls")
                            save()

        if command1.lower() == "settings":
            while True:
                os.system("cls")
                print(Fore.WHITE + "Settings:")
                print("")
                print(Fore.WHITE + "1. Logo-Time = " + str(logo_time) + " s")
                print(Fore.WHITE + "2. Message-Time = " + str(message_time) + " s")
                print(Fore.WHITE + "3. Text Colour = " + text_color)
                print(Fore.WHITE + "4. Password = " + realpass)
                if fx == True:
                    print(Fore.WHITE + "5. Fast Exit = " + "on")
                else:
                    print(Fore.WHITE + "5. Fast Exit = " + "off")
                if sud == True:
                    print(Fore.WHITE + "6. Show Users IDs = " + "on")
                else:
                    print(Fore.WHITE + "6. Show Users IDs = " + "off")
                if autovm == True:
                    print(Fore.WHITE + "7. Auto Visual Mode = " + "on")
                else:
                    print(Fore.WHITE + "7. Auto Visual Mode = " + "off")
                print(Fore.WHITE + "8. Back")
                print(Fore.WHITE + "9. Save Settings")
                print("")
                setting = input(Fore.WHITE + "Please enter the setting you want to change(1-9): ")
                if setting == "1":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    value = input(Fore.WHITE + "1. Logo-Time = ")
                    logo_time = int(value)
                    os.system("cls")
                elif setting == "2":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    print("")
                    value = input(Fore.WHITE + "2. Message-Time = ")
                    message_time = float(value)
                    os.system("cls")
                elif setting == "3":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    print("")
                    print("")
                    value = input(Fore.WHITE + "3. Text Colour = ")
                    if value.lower() == "white":
                        text_color = "white"
                    elif value.lower() == "red":
                        text_color = "red"
                    elif value.lower() == "green":
                        text_color = "green"
                    elif value.lower() == "blue":
                        text_color = "blue"
                    elif value.lower() == "yellow":
                        text_color = "yellow"
                    elif value.lower() == "cyan":
                        text_color = "cyan"
                    elif value.lower() == "magenta":
                        text_color = "magenta"
                    else:
                        print(Fore.RED + "Invalid color!")
                        time.sleep(1)
                        os.system("cls")
                    os.system("cls")
                elif setting == "4":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    print("")
                    print("")
                    print("")
                    value = input(Fore.WHITE + "4. Password = ")
                    realpass = value
                    os.system("cls")
                elif setting == "5":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    value = input(Fore.WHITE + "5. Fast Exit = ")
                    if value.lower() == "on":
                        fx = True
                    elif value.lower() == "off":
                        fx = False
                    else:
                        print(Fore.RED + "Invalid value!")
                        time.sleep(1)
                        os.system("cls")
                    os.system("cls")
                elif setting == "6":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    value = input(Fore.WHITE + "6. Show Users IDs = ")
                    if value.lower() == "on":
                        sud = True
                    elif value.lower() == "off":
                        sud = False
                    else:
                        print(Fore.RED + "Invalid value!")
                        time.sleep(1)
                        os.system("cls")
                    os.system("cls")
                elif setting == "7":
                    os.system("cls")
                    print(Fore.WHITE + "Settings:")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    value = input(Fore.WHITE + "7. Auto Visual Mode = ")
                    if value.lower() == "on":
                        autovm = True
                    elif value.lower() == "off":
                        autovm = False
                    else:
                        print(Fore.RED + "Invalid value!")
                        time.sleep(1)
                        os.system("cls")
                    os.system("cls")
                elif setting == "8":
                    os.system("cls")
                    break
                elif setting == "9":
                    os.system("cls")
                    settings["logo_time"] = logo_time
                    settings["message_time"] = message_time
                    settings["text_color"] = text_color
                    settings["password"] = realpass
                    settings["fx"] = fx
                    settings["sud"] = sud
                    settings["autovm"] = autovm
                    if autovm == True:
                        visualmode = True
                    save_settings()
                    if text_color == "white":
                        color = Fore.WHITE
                    elif text_color == "red":
                        color = Fore.RED
                    elif text_color == "green":
                        color = Fore.GREEN
                    elif text_color == "blue":
                        color = Fore.BLUE
                    elif text_color == "yellow":
                        color = Fore.YELLOW
                    elif text_color == "cyan":
                        color = Fore.CYAN
                    elif text_color == "magenta":
                        color = Fore.MAGENTA
                    print(Fore.GREEN + "Settings saved!")
                    time.sleep(1)
                    os.system("cls")
                    break
        if command1.lower() == "info":
            os.system("cls")
            print(Fore.WHITE + "Info:")
            print("")
            print(Fore.WHITE + "App Created by: Mateitzu")
            print(Fore.WHITE + "App Published on: GitHub")
            print(Fore.WHITE + "App Version: 1.0")
            print(Fore.WHITE + "App Created date: 2025-05-03")
            print(Fore.WHITE + "App Last Updated: 2025-05-04")
            print("")
            print(Fore.WHITE + "App Description: This is a user management system that allows you to add, remove, ban and unban users.")
            print(Fore.WHITE + "App Features:")
            print(Fore.WHITE + "1.This app has a visual mode that allows you to see the users in a list format." )
            print(Fore.WHITE + "2.This app has a settings section that makes it customisable for everyone." )
            print(Fore.WHITE + "3.This app has a basic saving system, without encrypting or encoding." )
            print(Fore.WHITE + "4.This app has a basic command system that allows you to enter commands." )
            print(Fore.WHITE + "5.This app is protected by a NON-SECURE password, so if you want use this app for fragile data, don't!" )
            print("")
            print(Fore.WHITE + "Note: Updates are coming soon to make the app:" )
            print(Fore.WHITE + "1.More secure" )
            print(Fore.WHITE + "2.More user-friendly" )
            print(Fore.WHITE + "3.More customisable" )
            print(Fore.WHITE + "4.More optimised" )
            print(Fore.WHITE + "5.More useful" )
            print("")
            print(Fore.WHITE + "To support me don't forget to:" )
            print(Fore.WHITE + "1.Follow me on Github" )
            print(Fore.WHITE + "2.Follow me on Youtube" )
            print(Fore.WHITE + "3.Like This project" )
            print(Fore.WHITE + "4.*Optional* Send a feedback at : selescumatei@gmail.com" )
            print("")
            value = input(Fore.WHITE + "Press enter to go back to the main menu.")
            os.system("cls")
        if command1.lower() == "help":
            os.system("cls")
            with open("help.txt", "r") as file:
                help_text = file.read()
                print(Fore.WHITE + help_text)
                print("")
                wait = input(Fore.WHITE + "Press enter to go back to the main menu.")
                os.system("cls")
                    

        
else:
    print(Fore.RED + "Access denied! App closing soon...")
    time.sleep(random.randrange(2,3))
    quit()