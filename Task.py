import tkinter as tk
from playsound import playsound  # You may need to install this module

def set_reminder():
    day = day_var.get()
    time = time_var.get()
    activity = activity_var.get()
    # Logic to schedule the reminder and play a sound at the specified time

# Create the main window
app = tk.Tk()
app.title("Reminder App")

# Dropdown for day of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_var = tk.StringVar()
day_dropdown = tk.OptionMenu(app, day_var, *days)
day_dropdown.pack()

# Dropdown for choosing the time
times = [f"{hour:02d}:00" for hour in range(24)]
time_var = tk.StringVar()
time_dropdown = tk.OptionMenu(app, time_var, *times)
time_dropdown.pack()

# Dropdown for the list of activities
activities = ["Wake up", "Go to gym", "Breakfast", "Meetings", "Lunch", "Quick nap", "Go to library", "Dinner", "Go to sleep"]
activity_var = tk.StringVar()
activity_dropdown = tk.OptionMenu(app, activity_var, *activities)
activity_dropdown.pack()

# Button to set the reminder
set_button = tk.Button(app, text="Set Reminder", command=set_reminder)
set_button.pack()

# Run the application
app.mainloop()
