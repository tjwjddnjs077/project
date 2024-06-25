import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        total_time = int(entry.get())
        count_down(total_time)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def count_down(time_left):
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = f"{mins:02}:{secs:02}"
        label.config(text=time_format)
        root.after(1000, count_down, time_left - 1)
    else:
        label.config(text="00:00")
        messagebox.showinfo("Time's up", "Time's up!")

# GUI setup
root = tk.Tk()
root.title("Simple Timer")

frame = tk.Frame(root)
frame.pack(pady=20)

entry_label = tk.Label(frame, text="Enter time in seconds:")
entry_label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(frame, width=10)
entry.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(frame, text="Start Timer", command=start_timer)
start_button.pack(side=tk.LEFT, padx=5)

label = tk.Label(root, text="00:00", font=("Helvetica", 48))
label.pack(pady=20)

root.mainloop()
