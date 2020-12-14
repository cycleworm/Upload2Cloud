import os
import sys
import tkinter as tk
import pyperclip
import webbrowser
import threading
import json

import siaskynet as skynet


#from siaskynet import Skynet

PortalList = [
"siasky.net",
"siacdn.com",
"skynet.tutemwesi.com",
"skynet.developmomentum.com",
"skydrain.net",
"sialoop.net",
"skyportal.xyz",
"skynet.luxor.tech",
"skynethub.io"
]


def upload():
    client = skynet.SkynetClient()

    print(str(sys.argv))
    upload.skylink = client.upload_file(str(sys.argv[1]))

    setSkylink(upload.skylink.replace("sia://", "https://"+variable.get()+"/"))
    btnOpenLink['state'] = tk.NORMAL
    btnCopyLink['state'] = tk.NORMAL
    opt['state'] = tk.NORMAL


def openLink():
    url = upload.skylink.replace("sia://", "https://"+variable.get()+"/")
    webbrowser.open(url, new=2)
    print(upload.skylink)


def copyLink():
    pyperclip.copy(upload.skylink.replace("sia://", "https://"+variable.get()+"/"))


def setSkylink(text):
    skylinkEntry.delete(0, "end")
    skylinkEntry.insert(0, text)


def readPortalURL(filename):
    with open(filename) as json_data_file:
        portalURL = json.load(json_data_file)
    print("string value: %s" % portalURL["portal"])
    return portalURL

def initConfigFile(filename):
    data = {}
    data['portal'] = "siasky.net"
    with open(configFilePath, 'x') as json_data_file:
        json.dump(data, json_data_file)
    json_data_file.close()

def callbackDropdown(*args):
    setSkylink("https://{}".format(variable.get())+upload.skylink.replace("sia://", "/"))
    #labelTest.configure(text="The selected item is {}".format(variable.get())+upload.skylink.replace("sia://", "/"))
    print(variable.get())
    portalURL["portal"] = variable.get()
    with open(configFilePath, 'w') as json_data_file:
        json.dump(portalURL, json_data_file)
    json_data_file.close()

# determine if application is a script file or frozen exe
APP_DIRNAME = "Upload2Cloud"
if not os.path.exists(os.path.join(os.environ['APPDATA'],APP_DIRNAME)):
    appDirectory = os.path.join(os.environ['APPDATA'], APP_DIRNAME)
    os.mkdir(appDirectory)
    configFilePath = os.path.join(appDirectory, "config.json")
    initConfigFile(configFilePath)

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

# Read Portal from Config File
appDirectory = os.path.join(os.environ['APPDATA'], APP_DIRNAME)
configFilePath = os.path.join(appDirectory, "config.json")
portalURL = readPortalURL(configFilePath)

# Configure Window
icon_path = os.path.join(application_path, "upload.ico")
root = tk.Tk()
root.title("U2C - Ver. 1.0.1")
root.minsize(1000, 60)
root.iconbitmap(icon_path)
root.resizable(0, 0)
skynetColor = '#57b560'  # or use hex if you prefer
root.configure(bg=skynetColor)

index = 0
for portal in PortalList:
    if portal == portalURL["portal"]:
        break;
    index += 1


print(index)

variable = tk.StringVar(root)
variable.set(PortalList[index])
opt = tk.OptionMenu(root, variable, *PortalList)
opt.config(width=24, font=('Helvetica', 12))
opt.pack(side="right", padx=10)

variable.trace("w", callbackDropdown)
variable.trace

# Add Elements to GUI
tk.Label(root, text="Skylink:", bg=skynetColor, fg="white", font=('helvetica', 16, 'bold')).pack(padx=(10, 0), pady=10, side="left")
skylinkEntry = tk.Entry(root, width=66, font=('helvetica', 15))
skylinkEntry.pack(fill="x", padx=10, pady=10, side="left")
setSkylink("uploading file...")

# Progressbar


# Disable Buttons before as long as upload is not finished
btnOpenLink = tk.Button(root, text="Open Link", state=tk.DISABLED, command=openLink)
btnOpenLink.pack(padx=0, side="left")
btnCopyLink = tk.Button(root, text="Copy Link", state=tk.DISABLED, command=copyLink)
btnCopyLink.pack(padx=10, side="left")
opt.configure(state="disabled")


# Put window in center of screen
positionRight = int(root.winfo_screenwidth() / 2 - 1000 / 2)
positionDown = int(root.winfo_screenheight() / 2 - 100 / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))

root.update_idletasks()
root.update()

# Start upload in separate thread
thread = threading.Thread(target=upload)
thread.start()
root.mainloop()

