import pyautogui
import multiprocessing
import pyscreeze
import time
import winsound
import json
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



try:
    with open(resource_path("config.json")) as f:
        config = json.load(f)
except FileNotFoundError:
    print("Missing Config")
except json.JSONDecodeError:
    print("Error decoding JSON")

# Path to the image you want to search for
image_path = resource_path('autismtest.png')

# Path to the audio file you want to play
audio_path = resource_path('SexModeEnabled.wav')
#My values: 1246,1283,64,64
#Left Top Widgth Height
while True:
    # Check if the image is found on the screen
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=config["Confidence"], region=(config["LeftPixelOffset"],config["TopPixelOffset"],config["PixelDimensions"],config["PixelDimensions"]))
        if location:
            print("Image found!")
            winsound.PlaySound(audio_path,winsound.SND_ASYNC)
            time.sleep(24)
    except:
        pass
        print("Image not found, checking again...")
        winsound.PlaySound(None,winsound.SND_PURGE)
        time.sleep(config["Heartbeat"])  # wait for 5 seconds before checking again
