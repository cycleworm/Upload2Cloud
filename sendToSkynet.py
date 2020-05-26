import os
import sys
import tkinter as tk
import pyperclip
import webbrowser
import threading

from siaskynet import Skynet


def upload():
    upload.skylink = Skynet.upload_file(str(sys.argv[1]))
    setSkylink(upload.skylink.replace("sia://", "https://www.siasky.net/"))
    btnOpenLink['state'] = tk.NORMAL
    btnCopyLink['state'] = tk.NORMAL


def openLink():
    url = upload.skylink.replace("sia://", "https://www.siasky.net/")
    webbrowser.open(url, new=2)


def copyLink():
    pyperclip.copy(upload.skylink.replace("sia://", "https://www.siasky.net/"))


def setSkylink(text):
    skylinkEntry.delete(0, "end")
    skylinkEntry.insert(0, text)


# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

# Configure Window
icon_path = os.path.join(application_path, "upload.ico")
root = tk.Tk()
root.title("Send to Skynet V 0.0.1")
root.minsize(1000, 60)
root.iconbitmap(icon_path)
root.resizable(0, 0)
skynetColor = '#57b560'  # or use hex if you prefer
root.configure(bg=skynetColor)

# Add Elements to GUI
tk.Label(root, text="Skylink:", bg=skynetColor, fg="white", font=('helvetica', 16, 'bold')).pack(padx=(10, 0), pady=10, side="left")
skylinkEntry = tk.Entry(root, width=66, font=('helvetica', 15))
skylinkEntry.pack(fill="x", padx=10, pady=10, side="left")
setSkylink("uploading file...")

# Disable Buttons before as long as upload is not finished
btnOpenLink = tk.Button(root, text="Open Link", state=tk.DISABLED, command=openLink)
btnOpenLink.pack(padx=0, side="left")
btnCopyLink = tk.Button(root, text="Copy Link", state=tk.DISABLED, command=copyLink)
btnCopyLink.pack(padx=10, side="left")

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

