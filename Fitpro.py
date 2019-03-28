# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
import codecs

male = 66.5
female = 665
over = ''
choose = ''
activity = ''
sex_test = ''
choice = ''
score = ''
total = ''
activity_choice = str('')
language = ''
error_test = ''


def clear():
    display_text.set('')
    display_text_age.set('')
    display_text_weight.set('')
    display_text_height.set('')
    display.configure(state="disable")


def male_click():
    global sex_test
    global choose
    sex_test = ''
    sex_test = 'male'
    choose = ''
    choose = male
    pass


def female_click():
    global sex_test
    global choose
    sex_test = ''
    sex_test = 'female'
    choose = ''
    choose = female
    pass


def calculate_click():
    global age
    global height
    global weight
    global error_test
    age = ''
    height = ''
    weight = ''
    try:
        weight = float(display_text_weight.get())
        height = float(display_text_height.get())
        age = float(display_text_age.get())
        calculate()
    except ValueError:
        if weight == '':
            error_test = 'input weight'
        elif height == '':
            error_test = 'input height'
        elif age == '':
            error_test = 'input age'
        display.configure(state="normal")
        display_text.set('Error: ' + error_test)
        display.configure(state="disable")


def calculate():
    global score
    global sex_test
    global total
    try:
        if sex_test == 'male':
            score = eval('choose+(13.7*weight)+(5*height)-(6.8*age)')
            total = eval('score*activity')
            display_text.set(total)
            display.configure(state="normal")
        if sex_test == 'female':
            score = eval('choose+(9.6*weight)+(1.85*height)-(4.7*age)')
            total = eval('score*activity')
            display_text.set(total)
            display.configure(state="normal")
        if sex_test == '':
            display.configure(state="normal")
            display_text.set('Error: choose Sex')
            display.configure(state="disable")
    except ValueError:
        display.configure(state="normal")
        display_text.set('Error')
        display.configure(state="disable")
    except TypeError:
        display.configure(state="normal")
        display_text.set('Error')
        display.configure(state="disable")


def listboxselect(index):
    global activity_choice
    global activity
    activity_choice = ct_listbox.get(ct_listbox.curselection())
    if activity_choice == ct_listbox.get(ct_listbox.index([0])):
        activity = float('1.0')
    if activity_choice == ct_listbox.get(ct_listbox.index([1])):
        activity = float('1.2')
    if activity_choice == ct_listbox.get(ct_listbox.index([2])):
        activity = float('1.4')
    if activity_choice == ct_listbox.get(ct_listbox.index([3])):
        activity = float('1.6')
    if activity_choice == ct_listbox.get(ct_listbox.index([4])):
        activity = float('1.8')
    if activity_choice == ct_listbox.get(ct_listbox.index([5])):
        activity = float('2.0')


def polish_language():
    try:
        ct_listbox.delete(0, END)
        with codecs.open("polish.txt", "r", "utf8") as file:
            line = file.readlines()
            for a in line:
                ct_listbox.insert(6, a)
            ct_listbox.update()
    except UnicodeDecodeError:
        print("error")


def english_language():
    ct_listbox.delete(0, END)
    with open("english.txt", "r") as file:
        line = file.readlines()
        for a in line:
            ct_listbox.insert(6, a)
        ct_listbox.update()


def quit_click():
    window.quit()


def ok():
    global language
    language = str(variable.get())
    master.destroy()


OPTIONS = ["Polish", "English"]
master = tk.Tk()
master.geometry('185x90')
master.title('Be Fit 1.0')
variable = StringVar(master)
variable.set(OPTIONS[0])
label_description = tk.Label(master, text="Select language:")
label_description.pack()
w = OptionMenu(master, variable, *OPTIONS)
w.pack()
button = Button(master, text="Select", command=ok)
button.pack()
master.mainloop()

if language == 'Polish':
    label_activity_lang = 'Wybierz rodzaj aktywności:'
    button_clear_lang = 'Wyczyść'
    button_calculate_lang = 'Oblicz'
    label_age_lang = 'Wiek'
    label_weight_lang = 'Waga'
    label_height_lang = 'Wzrost'
    button_male_lang = 'Mężczyzna'
    button_female_lang = 'Kobieta'
    label_kcaltarget_lang = 'Zapotrzebowanie kaloryczne'
    button_quit_lang = 'Zamknij'
if language == 'English':
    label_activity_lang = 'Choose your activity level:'
    button_clear_lang = 'Clear'
    button_calculate_lang = 'Calculate'
    label_age_lang = 'Age'
    label_weight_lang = 'Weight'
    label_height_lang = 'Height'
    button_male_lang = 'Male'
    button_female_lang = 'Female'
    label_kcaltarget_lang = 'CALORIES/DAY'
    button_quit_lang = 'Close'
window = tk.Tk()
window.geometry('510x460')
window.title('Be Fit 1.0')
C = tk.Canvas(window, bg="blue", height=250, width=300)
filename = tk.PhotoImage(file="fit.png")
background_label = tk.Label(window, image=filename)
background_label.place(x=1, y=210)

button_quit = tk.Button(window, text=button_quit_lang, command=quit_click, width=7)
button_quit.pack()
button_quit.place(x=445, y=5)

label_kcaltarget = tk.Label(window, text=label_kcaltarget_lang)
label_kcaltarget.place(x=30, y=40)
display_text = tk.StringVar()
display = tk.Entry(window, textvariable=display_text)
display.configure(state="disabled")
display.place(x=190, y=40)

button_male = tk.Button(window, text=button_male_lang, command=male_click, width=8)
button_male.pack()
button_male.place(x=30, y=60)

button_female = tk.Button(window, text=button_female_lang, command=female_click, width=6)
button_female.pack()
button_female.place(x=99, y=60)

label_weight = tk.Label(window, text=label_weight_lang)
label_weight.place(x=30, y=90)
display_text_weight = tk.StringVar()
display_weight = tk.Entry(window, width=11, textvariable=display_text_weight)
display_weight.place(x=81, y=90)

label_height = tk.Label(window, text=label_height_lang)
label_height.place(x=30, y=120)
display_text_height = tk.StringVar()
display_height = tk.Entry(window, width=11, textvariable=display_text_height)
display_height.place(x=81, y=120)

label_age = tk.Label(window, text=label_age_lang)
label_age.place(x=30, y=150)
display_text_age = tk.StringVar()
display_age = tk.Entry(window, width=11, textvariable=display_text_age)
display_age.place(x=81, y=150)

button_calculate = tk.Button(window, text=button_calculate_lang, command=calculate_click, width=7)
button_calculate.pack()
button_calculate.place(x=30, y=180)

button_clear = tk.Button(window, text=button_clear_lang, command=clear, width=7)
button_clear.pack()
button_clear.place(x=93, y=180)

label_activity = tk.Label(window, text=label_activity_lang)
label_activity.pack()
label_activity.place(x=180, y=70)

ct_listbox = tk.Listbox(window, width=52, height=6, exportselection=False)
ct_listbox.pack()
ct_listbox.place(x=180, y=88)
ct_listbox.bind('<<ListboxSelect>>',  listboxselect)

if language == 'Polish':
    polish_language()
elif language == 'English':
    english_language()
window.mainloop()
