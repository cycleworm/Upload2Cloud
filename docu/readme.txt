#Build exe with pyinstaller
install pyinstaller on PC.
pip install pyinstaller

pyinstaller -w --icon=upload.ico sendToSkynet.py
to create directory

pyinstaller --onefile -w --icon=upload.ico sendToSkynet.py
to create exe only