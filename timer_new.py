import tkinter as tk

window=tk.Tk()
window.title("Timer")
window.geometry("350x250")
window.config(bg="#ffd6e7")

seconds=0
running=False

def update_timer():
    global seconds,running

    if running and seconds>0:
        mins, secs=divmod(seconds,60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        seconds-=1
        window.after(1000,update_timer)
    
    elif seconds==0:
        timer_label.config(text="✨Time's Up!✨")
        running = False
    else:
        pass
     

def start_timer():
    global seconds,running
    if running:
        return
    if seconds==0:
         seconds=int(entry.get())
    running=True
    update_timer()


def pause_timer():
    global running
    running=False

def reset_timer():
    global seconds, running
    running=False
    seconds=0
    timer_label.config(text="00:00")
    entry.delete(0,tk.END)


title_label=tk.Label(
    window,
    text="🌸Cute Study Timer🌸",
    font=("Comic Sans MS",16,"bold"),
    bg="#ffd6e7"
    )

title_label.pack(pady=10)

entry=tk.Entry(window,font=("Arial",14))
entry.pack(pady=5)

timer_label=tk.Label(
    window, 
    text="00:00",
    font=("Arial",40,"bold"),
    bg="#ffd6e7"
)
timer_label.pack(pady=15)
start_button=tk.Button(
    window,
    text="▶️Start",
    font=("Arial",12),
    command=start_timer
)
start_button.pack()

pause_button=tk.Button(
    window,
    text="⏸️Pause",
    font=("Arial",12),
    command=pause_timer
)
pause_button.pack(pady=5)

reset_button=tk.Button(
    window, 
    text="🔁Reset",
    font=("Arial",12),
    command=reset_timer
)
reset_button.pack(pady=5)

window.mainloop()