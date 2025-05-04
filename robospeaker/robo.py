import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the program speak
def speak_text():
    text = entry.get()  # Get the text from the text entry field
    if text:
        engine.say(text)  # Speak the text
        engine.runAndWait()  # Wait for the speaking to finish

# Create the main window
root = tk.Tk()
root.title("Robo Speaker")  # Set the window title

# Set the window size
root.geometry("400x200")

# Create a label widget
label = tk.Label(root, text="Enter text to speak:", font=("Arial", 14))
label.pack(pady=10)

# Create a text entry widget
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Create a button widget to trigger the speech function
speak_button = tk.Button(root, text="Speak", font=("Arial", 14), command=speak_text)
speak_button.pack(pady=20)

# Run the GUI application
root.mainloop()
