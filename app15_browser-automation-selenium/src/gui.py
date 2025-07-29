import tkinter as tk
from tkinter import messagebox
from main import WebAutomation

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, 
                 text="Username").grid(row=0, column=0, sticky="w")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, 
                 text="Password").grid(row=1, column=1, sticky="w")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ow")

        # Form submission Frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, 
                 text="Full Name").grid(row=0, column=0, sticky="w")
        self.entry_fullname = tk.Entry(self.login_frame)
        self.entry_fullname.grid(row=0, column=1, sticky="ew")
        
        tk.Label(self.form_frame, 
                 text="Email").grid(row=0, column=0, sticky="w")
        self.entry_email = tk.Entry(self.login_frame)
        self.entry_email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, 
                 text="Current Address").grid(row=0, column=0, sticky="w")
        self.entry_current_address = tk.Entry(self.login_frame)
        self.entry_current_address.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, 
                 text="Permanent Address").grid(row=0, column=0, sticky="w")
        self.entry_permanent_address = tk.Entry(self.login_frame)
        self.entry_permanent_address.grid(row=1, column=1, sticky="ew")

        # Buttons
        self.buttons_frame = tk.Frame()
        self.buttons_frame.pack(padx=10, pady=10)

        tk.Button(self.buttons_frame, text="Submit", 
                  command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.buttons_frame, text="Close browser", 
                  command=self.close_browser).grid(row=0, column=1, padx=5)

    def submit_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        fullname = self.entry_fullname.get()
        email = self.entry_email.get()
        current_address = self.entry_current_address.get()
        permanent_address = self.entry_permanent_address.get()

        self.web_automation = WebAutomation()
        self.web_automation.start()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(fullname, email, 
                current_address, permanent_address)
        self.web_automation.download()

    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("Success")


root = tk.Tk()
app = App(root)
root.mainloop()
