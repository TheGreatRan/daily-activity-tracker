import customtkinter as ctk
import threading
import time 


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Daily tracker")
        self.geometry("1200x600+400+200")

        self.is_time_up = False
        self.Start1()

    def Start1(self):
        self.FirstFrame = FirstFrame(self)
        self.FirstFrame.pack(fill="both", expand=True)

    def Start2(self, track_time):
        self.SecondFrame = LoadingFrame(self, track_time)
        self.SecondFrame.pack(fill="both", expand=True)

    def Start3(self):
        self.ThirdFrame = LoadingFrame(self)
        self.ThirdFrame.pack(fill="both", expand=True)

    def CorrectClock(self, track_time):
        time.sleep(track_time * 60)
        self.is_time_up = True

class FirstFrame(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.text_entry = ctk.CTkLabel(self, text="How long do you want to track?", font=ctk.CTkFont(size=40))
        self.text_entry.pack(pady=100)

        self.entry = ctk.CTkEntry(self, 
                                  placeholder_text="Must be a number, I don't want have error for this",
                                  width=600, 
                                  height=50,
                                  corner_radius=10)
        self.entry.pack()

        self.buttom = ctk.CTkButton(self, 
                                    text="Start working", 
                                    width=200,
                                    height=50, 
                                    corner_radius=10, 
                                    command=self.press_bottom)
        self.buttom.pack(pady=60)

    def press_bottom(self):
        track_time = self.entry.get()
        if track_time.isdigit():
            track_time = int(track_time)
            self.pack_forget()
            threads = []
            threads.append(threading.Thread(target=self.master.Start2, args=(track_time,)))
            threads.append(threading.Thread(target=self.master.CorrectClock, args=(track_time,)))
            threads[0].start()
            threads[1].start()
            

class LoadingFrame(ctk.CTkFrame):
    def __init__(self, root, track_time):   
        super().__init__(root)

        self.track_time = track_time * 60
        self.cur_time = 0 
        self.process = ctk.CTkProgressBar(self, width=800,
                                           height=50,
                                           border_width=2, 
                                           mode="determinate", 
                                           determinate_speed=0)
        self.process.pack(pady=200)
        self.process.set(0)
        self.update_time()

    def update_time(self):
        self.cur_time += 1 
        self.process.set(self.cur_time / self.track_time)
        if not self.master.is_time_up and self.cur_time < self.track_time:
            self.after(1000, self.update_time)
        else: 
            self.pack_forget()
            self.master.ThirdFrame = FinishFrame(self.master)
            self.master.ThirdFrame.pack(fill="both", expand=True)

class FinishFrame(ctk.CTkFrame):
    def __init__(self, root): 
        super().__init__(root)

        self.entry = ctk.CTkEntry(self,
                                  placeholder_text="Tell me what you do",
                                  width=600,
                                  height=50,
                                  corner_radius=10)
        self.entry.pack(pady=150)

        self.buttom = ctk.CTkButton(self,
                                    text="OK",
                                    width=300,
                                    height=50,
                                    corner_radius=10,
                                    command = self.press_key)
        self.buttom.pack()
        
    def press_key(self): 
        pass



if __name__ == "__main__":
    app = App()
    app.mainloop()

