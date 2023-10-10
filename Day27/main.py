# import tkinter as tk
# window = tk.Tk()
# window.title("My First GUI Program")

# window.minsize(500, 300)

# my_label=tk.Label(text="I am a label", font=("Arial", 24, "bold", "italic"))

# my_label.pack(expand=True)

# window.mainloop()

def add(*args):
    sum=0
    for arg in args:
      sum+=arg
    return sum

print(add(2, 3, 5, 6, 7))

