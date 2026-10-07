import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("400x300")
        
        # Timer duration in seconds (3 minutes)
        self.duration = 180
        self.remaining = self.duration
        self.running = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Timer display
        self.time_label = tk.Label(
            self.root, 
            text="03:00", 
            font=("Arial", 48, "bold"),
            fg="blue"
        )
        self.time_label.pack(pady=30)
        
        # Buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Start button
        self.start_button = tk.Button(
            button_frame,
            text="Start",
            command=self.start_timer,
            font=("Arial", 14),
            width=10,
            bg="green",
            fg="white"
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        # Reset button
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_timer,
            font=("Arial", 14),
            width=10,
            bg="red",
            fg="white"
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 12),
            fg="gray"
        )
        self.status_label.pack(pady=10)
        
    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_button.config(state="disabled")
            self.status_label.config(text="Timer running...", fg="green")
            # Start timer in a separate thread
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()
    
    def run_timer(self):
        while self.running and self.remaining > 0:
            self.update_display()
            time.sleep(1)
            self.remaining -= 1
        
        if self.remaining <= 0:
            self.timer_finished()
        
        self.running = False
        self.root.after(0, lambda: self.start_button.config(state="normal"))
    
    def update_display(self):
        time_str = self.format_time(self.remaining)
        self.root.after(0, lambda: self.time_label.config(text=time_str))
    
    def timer_finished(self):
        self.root.after(0, lambda: self.time_label.config(text="00:00", fg="red"))
        self.root.after(0, lambda: self.status_label.config(text="Time's up!", fg="red"))
        
        # Play sound alert
        self.play_alert()
        
        # Show message box
        self.root.after(0, lambda: messagebox.showinfo("Timer", "3 minutes have passed!"))
    
    def play_alert(self):
        # Play system beep sound (Windows)
        try:
            # Play a beep sound at 1000Hz for 500ms, repeated 3 times
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.1)
        except Exception as e:
            print(f"Could not play sound: {e}")
    
    def reset_timer(self):
        self.running = False
        self.remaining = self.duration
        self.time_label.config(text="03:00", fg="blue")
        self.status_label.config(text="Ready", fg="gray")
        self.start_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
