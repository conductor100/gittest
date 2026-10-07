import time
import winsound

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"

def play_alert():
    """Play sound alert when timer finishes"""
    try:
        # Play beep sound at 1000Hz for 500ms, repeated 3 times
        for _ in range(3):
            winsound.Beep(1000, 500)
            time.sleep(0.1)
    except Exception as e:
        print(f"Could not play sound: {e}")

def timer(duration_minutes=3):
    """Simple timer with countdown display and sound alert"""
    duration_seconds = duration_minutes * 60
    remaining = duration_seconds
    
    print(f"Starting {duration_minutes}-minute timer...")
    print("Press Ctrl+C to stop the timer\n")
    
    try:
        while remaining > 0:
            # Clear line and display time
            print(f"\rTime remaining: {format_time(remaining)}", end="", flush=True)
            time.sleep(1)
            remaining -= 1
        
        # Timer finished
        print(f"\rTime remaining: 00:00", end="", flush=True)
        print("\n\nTime's up!")
        
        # Play sound alert
        play_alert()
        
    except KeyboardInterrupt:
        print("\n\nTimer stopped by user")

if __name__ == "__main__":
    timer(3)  # 3-minute timer
