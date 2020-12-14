#Build exe with pyinstaller
install pyinstaller on PC.
pip install pyinstaller

pyinstaller -w --icon=upload.ico sendToSkynet.py
to create directory

pyinstaller --onefile -w --icon=upload.ico sendToSkynet.py
to create exe only



execute pyinstaller in venv
https://stackoverflow.com/questions/57227191/pyinstaller-hidden-import-not-found