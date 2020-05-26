import os
import sys
import tkinter as tk
import pyperclip
import webbrowser



from siaskynet import Skynet

def resource_path(relative_path):
#""" Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def openLink():
    url = skylink.replace("sia://","https://www.siasky.net/")
    webbrowser.open(url, new=2)

def copyLink():
    pyperclip.copy(skylink.replace("sia://","https://www.siasky.net/"))
    #spam = pyperclip.paste()

def setSkylink(text):
    skylinkEntry.delete(0, "end")
    skylinkEntry.insert(0, text)

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

icon_path = os.path.join(application_path, "upload.ico")

root= tk.Tk()
root.title("Send to Skynet V 0.0.1")
root.minsize(1000,60)
root.iconbitmap(icon_path)

skynetColor = '#57b560'  # or use hex if you prefer
root.configure(bg=skynetColor)

#canvas1 = tk.Canvas(root, width = 800, height = 100)
#canvas1.pack()
#canvas1.create_window(150, 200, window=label2)

tk.Label(root, text="Skylink:", bg=skynetColor, fg="white", font=('helvetica', 16, 'bold')).pack(padx=(10,0), pady=10, side="left")
skylinkEntry = tk.Entry(root, width=66, font=('helvetica', 15))
skylinkEntry.pack(fill="x", padx=10, pady=10, side="left")

btnOpenLink = tk.Button(root, text="Open Link", command=openLink).pack(padx=0,side="left")
btnCopyLink = tk.Button(root, text="Copy Link", command=copyLink).pack(padx=10, side="left")

setSkylink("file gets uploaded...")

root.update_idletasks()
root.update()

# upload
#print("Uploading", str(sys.argv[1]))
skylink = Skynet.upload_file(str(sys.argv[1]))
setSkylink(skylink.replace("sia://","https://www.siasky.net/"))
#print("Upload successful, skylink: " + skylink)
#os.system("echo " + skylink + " | clip")
#os.system("start https://siasky.net/" + skylink.replace("sia://", ""))

root.mainloop()



#while True:
   # ball.draw()
  #  tk.update_idletasks()
 #   tk.update()