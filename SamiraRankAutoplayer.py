import pyautogui
import pyscreeze
import json
import os
import time
import threading
import winsound
import wave

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

SortedScansArray=[]
#Ensure no song shares same priority
for KeyName in config["Scans"]:
    LocalValue = KeyName["Priority"]
    Instance=0
    if KeyName["Priority"]>len(SortedScansArray):
        SortedScansArray.extend([None]*(KeyName["Priority"]-len(SortedScansArray)+1))
    SortedScansArray[KeyName["Priority"]]=KeyName
    SortedScansArray[KeyName["Priority"]]["Active"]=False
    for Value in config["Scans"]:
        if Value["Priority"]==LocalValue:
            Instance+=1
    if Instance>1:
        raise ValueError("Multiple entries contain the same priority! Ensure non entries share same priority and try again. Aborting...")

print(SortedScansArray)

def SongFinishedDelegate(KeyValue):
    #iterate and find true value
    #switch it to false
    KeyValue["Active"]=False



thread=None
def Playback(Priority,SongPath):
    winsound.PlaySound(resource_path("sounds/"+SongPath),winsound.SND_ASYNC)
    aud_file= wave.open(resource_path("sounds/"+SongPath),"rb")
    duration = aud_file.getnframes()/aud_file.getframerate()
    print(f'duration: {duration}')
    time.sleep(duration)
    SortedScansArray[Priority]["Active"] = False
    thread=None

def PlaySong(KeyValue):
    #iterate over all possible scans
    flag=False
    for item in SortedScansArray:
        #if one is currently playing a song then
        if item["Active"]==True:
            #if the priority of the song playing is less than the priority of the new song, then stop playing
            print(f'item["Priority"]: {item["Priority"]}')
            print(f'KeyValue["Priority"]: {KeyValue["Priority"]}')
            if item["Priority"]<KeyValue["Priority"]:
                item["Active"]=False
                if thread!=None:
                    thread.Terminate()
                    thread=None
            else:
                flag=True
    print("done")
    if KeyValue["Active"]==False and flag==False:
        thread = threading.Thread(target=Playback,args=(KeyValue["Priority"],KeyValue["SongPath"]))
        thread.start()
        KeyValue["Active"]=True

while True:
    #Do scans
    for x in range(len(SortedScansArray)-1,-1,-1):
        if SortedScansArray[x]!=None:
            if "ScanImagePath" in SortedScansArray[x]:
                Confidence=SortedScansArray[x]["Confidence"]
                LeftPixel = config["LeftPixelOffset"]
                TopPixel = config["TopPixelOffset"]
                PixelDimensions = config["PixelDimensions"]
                try:
                    ScannedLocation = pyautogui.locateOnScreen(resource_path("imagescans/"+SortedScansArray[x]["ScanImagePath"]), confidence=Confidence, region=(LeftPixel,TopPixel,PixelDimensions,PixelDimensions))
                    if ScannedLocation:
                        #found image
                        print("Playing song...")
                        PlaySong(SortedScansArray[x])
                except:
                    pass
            else:
                print("Didn't find any reference images")
                #it is probably a default song
                #check SortedScansArray[0] for image
                if ("ScanImagePath" in SortedScansArray[0]) ==False:
                    print("playing default song")
                    PlaySong(SortedScansArray[0])
    print("scanning again...")
    time.sleep(config["Heartbeat"])