import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class FirstWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # self.configure(fg_color="#202020")
        self.title("Dayily tracker")
        self.geometry("1200x600+400+200")

        self.text_entry = ctk.CTkLabel(self, text="How long you want to track?", 
                                        font=ctk.CTkFont(size=40, weight="bold"))
        self.text_entry.pack(pady=100)

        self.entry = ctk.CTkEntry(self, 
                                    placeholder_text="Must be a number, I don't want have error for this :>",
                                    width=600,
                                    height=50,
                                    corner_radius=10)
        self.entry.pack(pady=30)

        self.botton = ctk.CTkButton(self, text="Start tracking", width=200, height=50, corner_radius=10, command=self.start_tracking)
        self.botton.pack(pady=30)


    def start_tracking(self):
        time = self.entry.get()
        if time.isdigit():
            time = int(time)
            print(f"Start tracking for {time} minutes")
        else:
            print("Please enter a valid number")

if __name__ == "__main__":
    app = FirstWindow()
    app.mainloop()