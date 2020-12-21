import tkinter as tk
import random as random
import time

LARGE_FONT = ("verdana", 12)

root = tk.Tk()
root.geometry("400x300")


data = list()
with open("tests.txt") as f:
    for line in f:
        lin = line.rstrip()
        data.append(lin)

print(data)


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    time_label.config(text=hour + ":" + minute + ":" + second)
    time_label.after(1000, clock)


actual_line = ""


def qf(adat):
    global actual_line
    adat = random.choice(adat)

    new_string = "{0} ".format(adat)
    label.config(text=new_string)
    actual_line = adat
    print(actual_line)


# now oky
def delete_element(text):
    global data
    try:
        index_of_element = data.index(actual_line)
        data.pop(index_of_element)
    except Exception:
        pass

    with open("tests.txt", "w") as f:
        for line in data:
            f.write(line + "\n")

    print(text)

    pass


time_label = tk.Label(root, text="", font=("Helvetica", 36) )
time_label.pack(pady=20)
clock()
label = tk.Label(root, text="", font=LARGE_FONT)
label.pack()

button = tk.Button(root, text="get random",font=LARGE_FONT, command=lambda: qf(data))
button.pack()

delete_button = tk.Button(root, text="Tick", font=LARGE_FONT, command=lambda: delete_element(actual_line))
delete_button.pack(padx=20)

root.mainloop()
