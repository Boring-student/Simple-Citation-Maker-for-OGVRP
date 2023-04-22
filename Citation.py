import tkinter as tk
import pyperclip

# Create a new window
window = tk.Tk()

# Set the window size
window.geometry("800x600")


# Set the window title
window.title("Simple Ctation Maker")

# Create the first text input field
text_field1 = tk.Entry(window)

# Create a list of options
options1 = ["Deputy", "Master Deputy", "Corporal", "Sergeant", "Lieutenant", "Cpatain", "Commander", "Sheriff"]


# Create variables to store the selected options
selected_option1 = tk.StringVar()
selected_option2 = tk.StringVar()


# Create the first text input field
text_field1 = tk.Entry(window)


# Insert the ghost text into the entry widget
text_field1.insert(0, "Your Username")


# Bind the focus and focus out events to the first entry widget
def on_entry_focus1(event):
    if text_field1.get() == "Your Username":
        text_field1.delete(0, tk.END)

def on_entry_focusout1(event):
    if text_field1.get() == "":
        text_field1.insert(0, "Your Username")

text_field1.bind("<FocusIn>", on_entry_focus1)
text_field1.bind("<FocusOut>", on_entry_focusout1)

# Pack the first text input field
text_field1.pack()


# Set the initial values of the variables
selected_option1.set(options1[0])

# Create the first dropdown menu
dropdown1 = tk.OptionMenu(window, selected_option1, *options1)

# Pack the first dropdown menu
dropdown1.pack()


# Create the second text input field
text_field2 = tk.Entry(window)


# Insert the ghost text into the entry widget
text_field2.insert(0, "Suspect Username")

# Bind the focus and focus out events to the second entry widget
def on_entry_focus2(event):
    if text_field2.get() == "Suspect Username":
        text_field2.delete(0, tk.END)

def on_entry_focusout2(event):
    if text_field2.get() == "":
        text_field2.insert(0, "Suspect Username")

text_field2.bind("<FocusIn>", on_entry_focus2)
text_field2.bind("<FocusOut>", on_entry_focusout2)

# Pack the second text input field
text_field2.pack()

# Create a list of options
options2 = ["Citation", "Arrest Report"]

# Set the initial values of the variables
selected_option2.set(options2[0])

# Create the first dropdown menu
dropdown2 = tk.OptionMenu(window, selected_option2, *options2)

# Pack the first dropdown menu
dropdown2.pack()

# Create the second text input field
text_field3 = tk.Entry(window)


# Insert the ghost text into the entry widget
text_field3.insert(0, "Penal Code")

# Bind the focus and focus out events to the second entry widget
def on_entry_focus3(event):
    if text_field3.get() == "Penal Code":
        text_field3.delete(0, tk.END)

def on_entry_focusout3(event):
    if text_field3.get() == "":
        text_field3.insert(0, "Penal Code")

text_field3.bind("<FocusIn>", on_entry_focus3)
text_field3.bind("<FocusOut>", on_entry_focusout3)

# Pack the second text input field
text_field3.pack()

# Create the second text input field
text_field5 = tk.Entry(window)


# Insert the ghost text into the entry widget
text_field5.insert(0, "Amount")

# Bind the focus and focus out events to the second entry widget
def on_entry_focus5(event):
    if text_field5.get() == "Amount":
        text_field5.delete(0, tk.END)

def on_entry_focusout5(event):
    if text_field5.get() == "":
        text_field5.insert(0, "Amount")

text_field5.bind("<FocusIn>", on_entry_focus5)
text_field5.bind("<FocusOut>", on_entry_focusout5)

# Pack the second text input field
text_field5.pack()


# Create the second text input field
text_field4 = tk.Entry(window)


# Insert the ghost text into the entry widget
text_field4.insert(0, "Penal Code")

# Bind the focus and focus out events to the second entry widget
def on_entry_focus4(event):
    if text_field4.get() == "Penal Code":
        text_field4.delete(0, tk.END)

def on_entry_focusout4(event):
    if text_field4.get() == "":
        text_field4.insert(0, "Penal Code")

text_field4.bind("<FocusIn>", on_entry_focus4)
text_field4.bind("<FocusOut>", on_entry_focusout4)

# Pack the second text input field
text_field4.pack()


# Create the second text input field
text_field6 = tk.Entry(window)


# Insert the ghost text into the entry widget
text_field6.insert(0, "Amount")

# Bind the focus and focus out events to the second entry widget
def on_entry_focus6(event):
    if text_field6.get() == "Amount":
        text_field6.delete(0, tk.END)

def on_entry_focusout6(event):
    if text_field6.get() == "":
        text_field6.insert(0, "Amount")

text_field6.bind("<FocusIn>", on_entry_focus6)
text_field6.bind("<FocusOut>", on_entry_focusout6)

# Pack the second text input field
text_field6.pack()

# Create the "Merge and Send to Clipboard" button
def merge_and_send_to_clipboard():
    option1 = selected_option1.get()
    text1 = text_field1.get()
    if text1 == "Your Username":
        text1 = ""
    option2 = selected_option2.get()
    text2 = text_field2.get()
    if text2 == "Suspect Username":
        text2 = ""
    text3 = text_field3.get()
    if text3 == "Penal Code":
        text3 = ""
    text4 = text_field4.get()
    if text4 == "Penal Code":
        text4 = ""
        text5 = text_field5.get()
    if text5 == "Amount":
        text5 = ""
        text6 = text_field6.get()
    if text6 == "Amount":
        text6 = ""
    merged_text = f"{text1} | {option1}\n@{text2}\n \n{option2}\n{text3} - {text5}\n{text4} - {text6}"
    pyperclip.copy(merged_text)

send_button = tk.Button(window, text="Send to Clipboard", command=merge_and_send_to_clipboard)
send_button.pack()


# Define a function to update the preview
def update_preview():
    # Get the current clipboard content
    clipboard_content = pyperclip.paste()

    # Update the preview text
    preview_text.config(state=tk.NORMAL)
    preview_text.delete("1.0", tk.END)
    preview_text.insert(tk.END, clipboard_content)
    preview_text.config(state=tk.DISABLED)

    # Schedule the next update
    preview_text.after(1000, update_preview)

def clear_preview():
    # Clear the clipboard
    pyperclip.copy("")

    # Clear the preview text box
    preview_text.config(state=tk.NORMAL)
    preview_text.delete("1.0", tk.END)
    preview_text.config(state=tk.DISABLED)


# Create a text box for the text
text_box = tk.Text(window, height=1, width=9)

# Insert some text into the text box
text_box.insert(tk.END, "Preview.")

# Pack the text box
text_box.pack()
text_box.pack(side=tk.BOTTOM)

# Create a text box for the preview
preview_text = tk.Text(window, height=10, state=tk.DISABLED)

# Initialize the preview with an empty string
preview_text.insert(tk.END, "")

# Pack the text box
preview_text.pack()
preview_text.pack(side=tk.BOTTOM)

# Update the preview
update_preview()

# Create a button to clear the preview
clear_button = tk.Button(window, text="Clear Preview", command=clear_preview)

# Pack the button
clear_button.pack()


# Display the window
window.mainloop()

