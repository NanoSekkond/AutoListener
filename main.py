from my_modules import GlobalListener, GlobalReplay, ReplayListener
from time import sleep
import ctypes

awareness = ctypes.c_int()
ctypes.windll.shcore.SetProcessDpiAwareness(2)

def main():
    print("Read me: This application captures your keyboard and mouse inputs and movement, providing a convenient way to automate tasks. To launch the program, please enter an integer in the console. This integer determines the mouse movement speed: 1 for slow and precise movement, 10 for faster but less precise movement. You can choose any integer within this range. Once you've entered your chosen integer, wait for 5 seconds. After this brief pause, the program will start recording your inputs until you press the Esc key. After that, further instructions will be provided.")

    try:
        speed = int(input())
    except:
        speed = 1
    
    if (speed > 10):
        speed = 10
    elif (speed < 1):
        speed = 1

    listener = GlobalListener.GlobalListener(speed)
    sleep(5)
    listener.start()
    print("Your inputs are being recorded...")
    while(listener.is_running):
        sleep(0.1)
    print("Great! Your input actions have been recorded. Ensure that all elements are correctly positioned on the screen before initiating the playback, as the process cannot be interrupted. When everything is set, press F10. You can repeat the recorded actions as many times as needed by pressing F10 after each execution. To exit the application, simply press the Esc key.")
    replay = GlobalReplay.GlobalReplay(listener.input_list)
    listener = ReplayListener.ReplayListener(replay)
    listener.start()
    while(listener.is_running):
        sleep(0.1)

if __name__ == "__main__":
    main()