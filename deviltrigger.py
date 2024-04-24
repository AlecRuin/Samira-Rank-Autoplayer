import pyautogui
import pyscreeze
import time
import winsound
import json
import os
import wave
import pyaudio

p = pyaudio.PyAudio()
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

PlayingDefault=False
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    # If len(data) is less than requested frame_count, PyAudio automatically
    # assumes the stream is finished, and the stream stops.
    if len(data)-1<frame_count:
        print("stream finished")
    return (data, pyaudio.paContinue)
# Path to the image you want to search for
SmokingSexyStyleIcon = resource_path('autismtest.png')
stream=None
# Path to the audio file you want to play
audio_path = resource_path('SexModeEnabled.wav')

#My values: 1246,1283,64,64
#Left Top Widgth Height
while True:
    # Check if the image is found on the screen
    try:
        SmokingSexyStyleLocation = pyautogui.locateOnScreen(SmokingSexyStyleIcon, confidence=config["Confidence"], region=(config["LeftPixelOffset"],config["TopPixelOffset"],config["PixelDimensions"],config["PixelDimensions"]))
        if SmokingSexyStyleLocation:
            print("Image found!")
            if stream!=None:
                stream.close()
            wf = wave.open(resource_path("Smoking sexy style.wav"))
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
            stream.start_stream()
    except:
        pass
        print("Image not found, checking again...")
        if stream==None or stream.is_active()==False:
            print("currently not playing default. playing...")
            wf = wave.open(resource_path("Crazy.wav"))
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
            stream.start_stream()
        time.sleep(config["Heartbeat"])  # wait for 5 seconds before checking again
