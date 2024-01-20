import tkinter as tk
from tkinter import scrolledtext
import ai


from threading import Lock

send_lock = Lock()


# Function to send and receive messages

def send_message(event=None):

    if send_lock.locked():
        return

    # lock for 20 seconds
    send_lock.acquire(timeout=20)

    user_message = message_field.get()
    if user_message:
        # Display user's message with right bubble style
        chat_box.configure(state='normal')
        chat_box.insert(tk.END, user_message + "\n", "right_bubble")
        chat_box.configure(state='disabled')

        # Get response from OpenAI
        ai_response = ai.get_openai_response(user_message)
        chat_box.configure(state='normal')
        chat_box.insert(tk.END, ai_response + "\n", "left_bubble")
        chat_box.configure(state='disabled')

        message_field.delete(0, tk.END)

    # unlock
    send_lock.release()


# Create main window
root = tk.Tk()
root.title("Spoken Assistant By JXC")

# Create a single chat box
chat_box = scrolledtext.ScrolledText(root, state='disabled')
chat_box.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Configure tags for bubble styles
chat_box.tag_configure("left_bubble", justify='left',
                       lmargin1=20, lmargin2=20, rmargin=10, spacing2=10)
chat_box.tag_configure("right_bubble", justify='right',
                       lmargin1=10, lmargin2=10, rmargin=20, spacing2=10)

# Set the grid layout to be responsive
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create message field and send button
message_field = tk.Entry(root)
message_field.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
message_field.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Set focus to the message field
message_field.focus_set()

# Run the application
root.mainloop()
