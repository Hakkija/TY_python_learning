import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("House")
root.configure(bg="white")  # Set the background color

# Create the canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw the house
canvas.create_rectangle(50, 150, 350, 300, fill="#FFDAB9",
                        outline="#D2691E", width=4)  # House body
canvas.create_polygon(50, 150, 200, 50, 350, 150,
                      fill="#FFDAB9", outline="#D2691E", width=4)  # Roof
canvas.create_rectangle(120, 180, 180, 400, fill="#6495ED", width=4)  # Door
canvas.create_oval(150, 220, 170, 240, fill="#FFDAB9", width=4)  # Door knob
canvas.create_rectangle(
    80, 200, 110, 250, fill="#FFDAB9", width=4)  # Left window
canvas.create_rectangle(
    290, 200, 320, 250, fill="#FFDAB9", width=4)  # Right window

# Start the main event loop
root.mainloop()
