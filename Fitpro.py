# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
import codecs
program = True
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
weight_conv = ''
height_conv = ''


#  default behaviour of destroying the: choice language window
def master_pressed_x():
    global program
    program = False
    master.destroy()


#  default behaviour of destroying the: main program window
def window_pressed_x():
    global program
    program = False
    window.destroy()


#  default behaviour of destroying the: description window
def desc_pressed_x():
    global program
    program = False
    description.destroy()


#  on click: clear program window to default
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


#  on click: checking entry widgets(unit test) and assigning numbers to variables + invoke func. calculate
#  + invoke: description window
def calculate_click():
    global age
    global height
    global weight
    global error_test
    global weight_conv
    global height_conv
    age = ''
    height = ''
    weight = ''
    try:
        weight = (float(display_text_weight.get())/weight_conv)
        height = (float(display_text_height.get())/height_conv)
        age = float(display_text_age.get())
        if activity == '':
            if language == 'English':
                display.configure(state="normal")
                display_text.set('Error: Choose activity')
                display.configure(state="disable")
            if language == 'Polish':
                display.configure(state="normal")
                display_text.set('Error: Wybierz aktywność')
                display.configure(state="disable")
        else:
            calculate()

            try:
                if sex_test == '':
                    if language == 'English':
                        display.configure(state="normal")
                        display_text.set('Error: Choose sex')
                        display.configure(state="disable")
                    if language == 'Polish':
                        display.configure(state="normal")
                        display_text.set('Error: Wybierz płeć')
                        display.configure(state="disable")
                else:
                    window.destroy()
                    desc_window()

            except NameError:
                display.configure(state="normal")
                display_text.set('Error: NameError')
                display.configure(state="disable")

    except ValueError:
        if weight == '' and language == 'English':
            error_test = 'input weight'
        elif weight == '' and language == 'Polish':
            error_test = 'Wprowadź wagę'
        elif height == '' and language == 'English':
            error_test = 'input height'
        elif height == '' and language == 'Polish':
            error_test = 'Wprowadź wzrost'
        elif age == '' and language == 'English':
            error_test = 'input age'
        elif age == '' and language == 'Polish':
            error_test = 'Wprowadź wiek'
        display.configure(state="normal")
        display_text.set('Error: ' + error_test)
        display.configure(state="disable")


#  calculate algorithm
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


def list_box_select(index):
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


#  loading text from polish.txt and entering it the list
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


#  loading text from english.txt and entering it the list
def english_language():
    ct_listbox.delete(0, END)
    with open("english.txt", "r") as file:
        line = file.readlines()
        for a in line:
            ct_listbox.insert(6, a)
        ct_listbox.update()


#  button quit action : on click -> will close program window
def quit_click():
    global program
    program = False
    window.destroy()


#  button quit action : on click -> will close description window
def desc_quit_click():
    global program
    program = False
    description.destroy()


#  set global language (from selected)
def ok():
    global language
    global program
    language = str(variable.get())
    master.destroy()


#  invoke: Choice language window
def choice_language():
    global master
    global variable
    global program
    options = ["Polish", "English"]
    master = tk.Tk()
    master.protocol('WM_DELETE_WINDOW', master_pressed_x)
    master.geometry('185x90')
    master.title('Be Fit 1.0')
    variable = StringVar(master)
    variable.set(options[0])
    label_description = tk.Label(master, text="Select language:")
    label_description.pack()
    w = OptionMenu(master, variable, *options)
    w.pack()
    button = Button(master, text="Select", command=ok)
    button.pack()
    master.mainloop()


#  breaking window mainloop and start form beginning program mainloop
def change_language_click():
    global program
    global window
    window.destroy()


#  invoke: description window
#  loading data from variables to entry
def desc_window():
    global total
    global description

    description = tk.Tk()
    description.protocol('WM_DELETE_WINDOW', desc_pressed_x)
    description.geometry('510x460')
    description.title('Be Fit 1.0')
    desc_label_kcaltarget = tk.Label(description, text=label_kcaltarget_lang)
    desc_label_kcaltarget.place(x=220, y=5)
    desc_display_text = tk.StringVar()
    desc_display = tk.Entry(description, textvariable=desc_display_text)
    desc_display.place(x=380, y=5)
    desc_display.configure(state="disable")
    desc_display_text.set(total)

    desc_menu = Menu(description)
    desc_filemenu = Menu(desc_menu, tearoff=0)
    desc_filemenu.add_command(label="Save",)
    desc_filemenu.add_separator()
    desc_filemenu.add_command(label="Exit", command=desc_quit_click)
    desc_menu.add_cascade(label="File", menu=desc_filemenu)
    description.config(menu=desc_menu)

    desc_label_weight = tk.Label(description, text=label_weight_lang)
    desc_label_weight.place(x=5, y=40)
    desc_display_text_weight = tk.StringVar()
    desc_display_weight = tk.Entry(description, width=11, textvariable=desc_display_text_weight)
    desc_display_weight.place(x=56, y=40)
    desc_label_weight_unit = tk.Label(description, text=label_weight_unit_lang)
    desc_label_weight_unit.pack()
    desc_label_weight_unit.place(x=125, y=40)
    desc_display_weight.configure(state="disable")
    desc_display_text_weight.set(weight)

    desc_label_height = tk.Label(description, text=label_height_lang)
    desc_label_height.place(x=5, y=70)
    desc_display_text_height = tk.StringVar()
    desc_display_height = tk.Entry(description, width=11, textvariable=desc_display_text_height)
    desc_display_height.place(x=56, y=70)
    desc_label_height_unit = tk.Label(description, text=label_height_unit_lang)
    desc_label_height_unit.pack()
    desc_label_height_unit.place(x=125, y=70)
    desc_display_height.configure(state="disable")
    desc_display_text_height.set(height)

    desc_label_age = tk.Label(description, text=label_age_lang)
    desc_label_age.place(x=5, y=10)
    desc_display_text_age = tk.StringVar()
    desc_display_age = tk.Entry(description, width=11, textvariable=desc_display_text_age)
    desc_display_age.place(x=56, y=10)
    desc_display_age.configure(state="disable")
    desc_display_text_age.set(age)

    desc_label_separate = tk.Label(description, text=99 * '-')
    desc_label_separate.place(x=5, y=90)

    global label_sex_lang
    global desc_activity_lang
    if language == 'Polish':
        label_sex_lang = 'Płeć:'
        desc_activity_lang = 'Aktywność:'
    else:
        label_sex_lang = 'Sex:'
        desc_activity_lang = 'Activity:'
    desc_label_sex = tk.Label(description, text=label_sex_lang)
    desc_label_sex.place(x=220, y=70)

    desc_label_activity = tk.Label(description, text=desc_activity_lang)
    desc_label_activity.place(x=220, y=45)

    global label_sex_text_lang
    if sex_test == 'female' and language == 'English':
        label_sex_text_lang = 'Female'
    if sex_test == 'female' and language == 'Polish':
        label_sex_text_lang = 'Kobieta'
    if sex_test == 'male' and language == 'English':
        label_sex_text_lang = 'Male'
    if sex_test == 'male' and language == 'Polish':
        label_sex_text_lang = 'Mężczyzna'
    desc_label_sex_text = tk.Label(description, text=label_sex_text_lang)
    desc_label_sex_text.place(x=260, y=70)

    desc_label_activity_value = tk.Label(description, text=activity)
    desc_label_activity_value.place(x=290, y=45)

    description.mainloop()


#  start mainloop
while program is True:
    try:
        if program is True:
            choice_language()
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
                label_weight_unit_lang = 'kg'
                label_height_unit_lang = 'cm'
                weight_conv = float('1')
                height_conv = float('1')
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
                label_weight_unit_lang = 'lbs'
                label_height_unit_lang = 'ft'
                weight_conv = float('2.2046226218')
                height_conv = float('0.032808399')

            window = tk.Tk()
            window.protocol('WM_DELETE_WINDOW', window_pressed_x)
            window.geometry('510x460')
            window.title('Be Fit 1.0')
            C = tk.Canvas(window, bg="blue", height=250, width=300)
            filename = tk.PhotoImage(file="fit.png")
            background_label = tk.Label(window, image=filename)
            background_label.place(x=1, y=210)

            menu = Menu(window)
            filemenu = Menu(menu, tearoff=0)
            filemenu.add_command(label="Change language", command=change_language_click)
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=quit_click)
            menu.add_cascade(label="File", menu=filemenu)
            window.config(menu=menu)

            button_quit = tk.Button(window, text=button_quit_lang, command=quit_click, width=7)
            button_quit.pack()
            button_quit.place(x=445, y=5)

            label_kcaltarget = tk.Label(window, text=label_kcaltarget_lang)
            label_kcaltarget.place(x=30, y=40)
            display_text = tk.StringVar()
            display = tk.Entry(window, textvariable=display_text, width=50)
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
            label_weight_unit = tk.Label(window, text=label_weight_unit_lang)
            label_weight_unit.pack()
            label_weight_unit.place(x=150, y=90)

            label_height = tk.Label(window, text=label_height_lang)
            label_height.place(x=30, y=120)
            display_text_height = tk.StringVar()
            display_height = tk.Entry(window, width=11, textvariable=display_text_height)
            display_height.place(x=81, y=120)
            label_height_unit = tk.Label(window, text=label_height_unit_lang)
            label_height_unit.pack()
            label_height_unit.place(x=150, y=120)

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
            ct_listbox.bind('<<ListboxSelect>>', list_box_select)

            if language == 'Polish':
                polish_language()
            elif language == 'English':
                english_language()
            window.mainloop()
        else:
            break
    except NameError:
        program = False
