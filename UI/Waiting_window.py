import customtkinter as ctk

class TimerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Progress Bar 1 Phút")
        self.geometry("400x200")

        # Cấu hình giao diện
        self.label = ctk.CTkLabel(self, text="Thời gian còn lại: 60s", font=("Arial", 16))
        self.label.pack(pady=20)

        # Tạo Progress Bar
        self.progress = ctk.CTkProgressBar(self, orientation="horizontal", width=300)
        self.progress.set(0) # Bắt đầu từ 0
        self.progress.pack(pady=10)

        # Nút bắt đầu
        self.start_button = ctk.CTkButton(self, text="Bắt đầu", command=self.start_timer)
        self.start_button.pack(pady=20)

        # Biến điều khiển
        self.duration = 60  # 60 giây
        self.remaining = self.duration

    def start_timer(self):
        self.start_button.configure(state="disabled")
        self.remaining = self.duration
        self.update_progress()

    def update_progress(self):
        if self.remaining >= 0:
            # Tính toán tỷ lệ phần trăm (từ 0.0 đến 1.0)
            percentage = (self.duration - self.remaining) / self.duration
            self.progress.set(percentage)
            
            # Cập nhật chữ
            self.label.configure(text=f"Thời gian còn lại: {int(self.remaining)}s")
            
            # Giảm thời gian (mỗi bước là 100ms để mượt hơn)
            self.remaining -= 0.1
            
            # Gọi lại hàm sau 100ms (0.1 giây)
            self.after(100, self.update_progress)
        else:
            self.label.configure(text="Hoàn thành!")
            self.start_button.configure(state="normal")

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()