import os
import sys
import tkinter as tk
import pyperclip
import webbrowser
import threading
import json
import siaskynet as skynet


def upload():
    client = skynet.SkynetClient()
    upload.skylink = client.upload_file(str(sys.argv[1]))
    setSkylink(upload.skylink.replace("sia://", "https://"+variable.get()+"/"))
    btnOpenLink['state'] = tk.NORMAL
    btnCopyLink['state'] = tk.NORMAL
    btnFancyLink['state'] = tk.NORMAL
    opt['state'] = tk.NORMAL


def openLink():
    url = upload.skylink.replace("sia://", "https://"+variable.get()+"/")
    webbrowser.open(url, new=2)
    print(upload.skylink)


def copyLink():
    pyperclip.copy(upload.skylink.replace("sia://", "https://"+variable.get()+"/"))


def createFancyLink():
    file_stats = os.stat(sys.argv[1])
    file_size = sizeof_fmt(file_stats.st_size)
    filename = sys.argv[1]
    skylink = upload.skylink.replace("sia://", "https://" + variable.get() + "/")

    f = open("Webtemplate/original_index.html", 'r')
    web_template = f.read()
    f.close()
    web_template = web_template.replace('__filename__', filename)
    web_template = web_template.replace('__filesize__', file_size)
    web_template = web_template.replace('__skylink__', skylink)

    f = open("Webtemplate/index.html", 'w')
    f.write(web_template)
    f.close()

    client = skynet.SkynetClient()
    upload.skylink = client.upload_directory("Webtemplate")
    setSkylink(upload.skylink.replace("sia://", "https://"+variable.get()+"/"))

def setSkylink(text):
    skylinkEntry.delete(0, "end")
    skylinkEntry.insert(0, text)


def readPortalURL(filename):
    with open(filename) as json_data_file:
        portalURL = json.load(json_data_file)
    print("string value: %s" % portalURL["portal"])
    json_data_file.close()
    return portalURL


def readActivePortals(filename):
    with open(filename) as json_data_file:
        data = json.load(json_data_file)
    activePortalList = data["active_portals"]
    return activePortalList



def callbackDropdown(*args):
    setSkylink("https://{}".format(variable.get())+upload.skylink.replace("sia://", "/"))
    print(variable.get())
    portalURL["portal"] = variable.get()
    with open(configFilePath, 'w') as json_data_file:
        json.dump(portalURL, json_data_file)
    json_data_file.close()


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

APP_DIRNAME = "Upload2Cloud"

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    appDirectory = os.path.join(os.environ['LOCALAPPDATA'], APP_DIRNAME)
    configFilePath = os.path.join(appDirectory, "config.json")
elif __file__:
    application_path = os.path.dirname(__file__)
    configFilePath = "config.json"

# Read Portal from Config File
print("configpath "+configFilePath)
portalURL = readPortalURL(configFilePath)

# Read active portals from config file
activePortalList = readActivePortals(configFilePath)

# Configure Window
icon_path = os.path.join(application_path, "upload.ico")
root = tk.Tk()
root.title("U2C - Ver. 1.0.2")
root.minsize(1000, 60)
root.iconbitmap(icon_path)
root.resizable(0, 0)
skynetColor = '#57b560'  # or use hex if you prefer
root.configure(bg=skynetColor)

# Set Dropdown to portal that is saved in config file
index = 0
for portal in activePortalList:
    if portal == portalURL["portal"]:
        break
    index += 1

# Add Elements to GUI
tk.Label(root, text="Skylink:", bg=skynetColor, fg="white", font=('helvetica', 16, 'bold')).pack(padx=(10, 0), pady=10, side="left")
skylinkEntry = tk.Entry(root, width=66, font=('helvetica', 15))
skylinkEntry.pack(fill="x", padx=10, pady=10, side="left")
setSkylink("uploading file...")

variable = tk.StringVar(root)
variable.set(activePortalList[index])
opt = tk.OptionMenu(root, variable, *activePortalList)
opt.config(width=24, font=('Helvetica', 12))
opt.pack(side="right", padx=10)
opt.configure(state="disabled")

variable.trace("w", callbackDropdown)

# Disable Buttons as long as upload is not finished
btnOpenLink = tk.Button(root, text="Open Link", state=tk.DISABLED, command=openLink)
btnOpenLink.pack(padx=0, side="left")
btnCopyLink = tk.Button(root, text="Copy Link", state=tk.DISABLED, command=copyLink)
btnCopyLink.pack(padx=10, side="left")
btnFancyLink = tk.Button(root, text="Create Fancy Link", state=tk.DISABLED, command=createFancyLink)
btnFancyLink.pack(padx=0, side="left")

# Update Tkinter to get actual window size
root.update()

# Put window in center of screen
positionRight = int(root.winfo_screenwidth() / 2 - root.winfo_width() / 2)
positionDown = int(root.winfo_screenheight() / 2 - (root.winfo_height()+30) / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))

root.update_idletasks()
root.update()

# Start upload in separate thread
thread = threading.Thread(target=upload)
thread.start()
root.mainloop()

