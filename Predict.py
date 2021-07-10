from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
import glob
from collections import defaultdict
import pandas as pd
import numpy as np
import os
from keras.models import load_model
import tensorflow as tf


def predict():
    window = Tk()
    window.title("Classify Malware")
    window.geometry('1000x700')
    window.configure(background = "white")

    def parser():
        filename = filedialog.askopenfilename(
            initialdir="C://Users//MudassirRiaz//PycharmProjects")
        with open(filename) as datafile:
            data = json.load(datafile)
            data = (data['behavior']['processes'][1]['calls'][1]['api'] + "" + data['behavior']['processes'][1]['calls'][1]['api'])
            print(data)
        def result():
            Categories = ['trojan','backdoor','adware', 'spyware', 'virus', 'worms', 'downloader', 'dropper']
            def result(x):
                return x
            model = tf.keras.models.load_model('C:\\Users\\MudassirRiaz\\PycharmProjects\\Malware Behavior Classification\\Json_Reports\\model.h5')
            prediction = model.predict(result([100]))
            cat = (Categories[int(prediction[0][0])])
            if cat == 'trojan':
                msg = "Trojan misleads users of its true intent"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'backdoor':
                msg = "Backdoor is a technique in which a system security mechanism is bypassed undetectably toaccess a computer or its data"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'adware':
                msg = "Adware hides on your device and serves you advertisements"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'spyware':
                msg = "Spyware enables a user to obtain covert information about another’s computer activities bytransmitting data covertly from their hard drive"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'virus':
                msg = "Virus is designed to spread from host to host and has the ability to replicate itself"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'worms':
                msg = "Worms spreads copies of itself from computer to computer"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'downloader':
                msg = "Downloader share the primary functionality of downloading content"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            elif cat == 'dropper':
                msg = "Dropper surreptitiously carries viruses, back doors and other malicious software so they canbe executed on the compromised machine"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
                classification = Label(window, text=cat, font=('helvatic', 15, 'bold'), fg='green')
                classification.place(x=510, y=370)
            else :
                msg = "Please! try again something went wrong"
                description = Label(window, text=msg, fg="green")
                description.place(x=100, y=400)
        result()
    button_predict = Button(window,
                            text="Browse Files",
                            command=parser)

    button_exit = Button(window,
                         text="Exit",
                         command=exit)

    button_predict.place(x=480, y=190)


    button_exit.place(x=500, y=300)

    window.mainloop()









