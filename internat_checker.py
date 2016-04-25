#!/usr/bin/python3

import subprocess
import urllib.request
import time

HASHREF = '0b4a8f206e2f5d840fc93557beaa7075'

count = 1

while True:

    url = "http://www.citegeorgespoint.be/Formulaire/Doc/Form_inscription.doc"
    filename = "Form_inscription.doc"

    try:
        with urllib.request.urlopen(url) as response, open(filename, 'wb') as o:
            data = response.read() # a `bytes` object
            o.write(data)
    except:
        print("Site is down or URL Form changed, go check the website! Try " + str(count))
        if (count < 3):
            count += 1
            continue
        else:
            while True:
                subprocess.Popen("paplay /usr/share/sounds/ubuntu/stereo/dialog-warning.ogg".split(), stdout=subprocess.PIPE)
                time.sleep(2)


    count = 1
    bashCommand = "md5sum Form_inscription.doc"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0].decode('utf-8')
    hash = output.split(' ')[0]

    if (HASHREF == hash):
        print("The file is the same! Wait 15 sec")
        time.sleep(15)
    else:
        subprocess.Popen("libreoffice Form_inscription.doc".split(), stdout=subprocess.PIPE)
        while True:
            subprocess.Popen("paplay /usr/share/sounds/ubuntu/stereo/dialog-information.ogg".split(), stdout=subprocess.PIPE)
            time.sleep(2)
