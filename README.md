<h3><u>Samira Rank Autoplayer</u></h3>

This program scans for an image (provided by user) on the screen within the bounds specified. If it finds the image, it will play a sound (provided by user). Design for use with Samira from League of Legends

>How to package:
>
><ol><li>place any .PNGs you'd like scanned and .wav files you'd like to play inside of imagescans and sounds respectively</li>
><li>run pyinstaller -y SamiraRankAutoplayer.spec in terminal to build exe</li></ol>

>How to use .exe
><ol>
><li>Navigate to dist/SamiraRankAutoplayer/_internal/imagescans</li>
><li>Place .png images of the rank youre scanning for. It MUST be the exact >dimensions (in pixels) that the icon appears IN GAME. It is recommended to take a screenshow of yourself in game and use photoediting software to measure the pixels</li>
><li>Find any sound you want, convert it to .wav, and place inside dist/SamiraRankAutoplayer/_internal/sounds</li>
><li>modify the config.json file found inside dist/SamiraRankAutoplayer/_internal/<ul><li>Currently, the .json file is programmed to cycle through 3 different songs if it finds 3 different images</li></ul></li></ol>

>## JSON configuration guide
>
>    ### Scans
>
>    This is an array of objects that looks like this</br>
>```json
>    "Scans":[{
>        "Priority":0,
>        "ScanImagePath":"CrazyPNG.png",
>        "SongPath":"Crazy.wav",
>        "Confidence":0.7
>    }]
>```
> Each object added to scans is a possible image and sound to play at a given moment.
>><h3>Scans properties</h3>
>><ul> 
>><li> <h4>Priority</h4>
>>When an image is found, or no ScanImagePath was provided, the script will compare priority to the currently-playing song and replace it with the song found in SongPath and begin playing. You cannot have a scan entry share priority, or have negative priority, or use decimals for priority. Keep it simple!</li>
>><li><h4>Confidence</h4>
>>        Every heartbeat, the program will scan for the image provided in ScanImagePath. Confidence is the pyautogui's parameter for how perfect the image found resembles the image provided. 0.7 is 70% likeness and is recommended
>></li>
>><li><h4>ScanImagePath</h4>
>>The name of the .PNG the program should look for. If none is provided, it will play the song found in SongPath constantly in the background. </li>
></ul>
><ul><li><h4>Heartbeat</h4>
>Every Heartbeat (in seconds), the program will wait before scanning again. Default value is 0.1 seconds</li>
><li><h4>LeftPixelOffset</h4>
>Based off of the in-game resolution, the program will scan <b><i><u>this</u></i></b> far (in pixels) from the left side of the screen. Measure the distance in a photoediting app from the left side of the screen to the edge of the ability icon. Do not include the border. </li>
><li><h4>TopPixelOffset</h4>
>Based off of the in-game resolution, the program will scan <b><i><u>this</u></i></b> far (in pixels) from the top side of the screen. Measure the distance in a photoediting app from the top side of the screen to the edge of the ability icon. Do not include the border. </li>
><li><h4>PixelDimensions</h4>
>This is the length and width of the .PNGs. Measure in a photoediting software the dimensions of the ult icon in game to get this value. Ie, mine was 64x64, so I'll put 64</li>
></ul>

Any questions please contact Katlec Valentine aka <b><i><a href="https://discord.gg/p9bR7hc57r">Swoggers</a></i></b>. I will be happy to help out :)