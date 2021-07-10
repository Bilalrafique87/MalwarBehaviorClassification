from tkinter import *
from tkinter import ttk
from Classifier import classify
from Predict import predict
from tkinter import filedialog
from Report_parser import parser
window = Tk()
window.title("Classify Malware")
window.geometry('1000x700')

def report_parser():
    filename = filedialog.askopenfilename(initialdir="C://", multiple=True)

    parser(filename)


button_explore = Button(window,
                        text="Browse Files",
                        command=report_parser)

button_classify = Button(window,
                         text="Classify",
                         command=classify)

button_predict = Button(window,
                     text="Predict Malware",
                        command=predict)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

button_explore.place(x=480, y=190)

button_classify.place(x=490, y=250)

button_predict.place(x=475, y=310)

button_exit.place(x=510, y=370)


window.configure(background = "white")
window.mainloop()