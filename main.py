import os
import tkinter as tk
from tkinter import filedialog, messagebox, Checkbutton, Entry, Label, Button
from datetime import datetime

# Task list
tasks = ['ST1', 'ST2', 'DTAN', 'DTF', 'DTV', 'DTS1', 'DTS7', 'DTCT']


def rename_files():
    # Get the participant number
    subject = subject_entry.get()
    subject = subject.zfill(3)  # Ensure the subject has three digits

    # Get the selected tasks
    selected_tasks = [task for task, var in zip(tasks, tasks_vars) if var.get() == 1]

    # Get the folder path
    folder = filedialog.askdirectory()

    # Get all files in the folder
    files = os.listdir(folder)

    # Filter .csv and .mp4 files
    csv_files = [file for file in files if file.endswith('.csv')]
    mp4_files = [file for file in files if file.endswith('.mp4')]

    # Sort files by creation date
    csv_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    mp4_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))

    # Rename files
    for i, task in enumerate(selected_tasks):
        task_files = csv_files[i*2:i*2+2] + [mp4_files[i]]
        for j, file in enumerate(task_files):
            extension = os.path.splitext(file)[1]
            if j < 2:  # .csv files
                sensor = "F6F2" if j == 0 else "03F5"
                new_name = f"Sub-SAN{subject}_ses_V0_task_{task}_{sensor}{extension}"
            else:  # .mp4 file
                new_name = f"Sub-SAN{subject}_ses_V0_task_{task}_video{extension}"
            os.rename(os.path.join(folder, file), os.path.join(folder, new_name))

    messagebox.showinfo("Information", "The files have been successfully renamed.")

# Create the application window
root = tk.Tk()

# Create the entry for the participant number
Label(root, text="Enter the participant number:").pack()
subject_entry = Entry(root)
subject_entry.pack()

# Create the checkboxes for the tasks
Label(root, text="Select the tasks that were NOT performed:").pack()
tasks_vars = [tk.IntVar(value=1) for _ in tasks]
for task, var in zip(tasks, tasks_vars):
    Checkbutton(root, text=task, variable=var).pack()

# Create the button to start the process
Button(root, text="Start", command=rename_files).pack()

# Start the application
root.mainloop()
