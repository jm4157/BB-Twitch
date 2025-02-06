# Blood Bowl Snitch Setup

So you want to stream Blood Bowl on Snitch. I'm here to learn you how. Follow the steps.

*Instructions written in italics are only necessary for those who want to set up the loading
tidbit, and can be safely ignored if coding isn't up your alley.*

This version is dated 2/5/2025. It changes some filenames to be more consistent and less confusing,
as well as overhauls the instructions.

## First Time Setup (One Time Only)

### Step 1

Download and install [OBS](https://obsproject.com).

*If you want to change the loading tidbit, you'll need to install 
[Python](https://www.python.org/downloads/) as well.*

### Step 2 

On this Github page, press the button labeled `<> Code` and select the Download Zip option. Unzip 
it to the location you want the VSPN files set up.

### Step 3

Sign into OBS with the Savage Scrimmage Series Twitch account. Ask Andrew (paradoxical_perception 
on Discord) for the login details.

### Step 4

In OBS find the Scene Collection option and Import the file snitch_import.json. This will set 
OBS up with all the SSS scenes.

## Stream Prep (Repeat Every Match)

### Step 5 

Check the repo (this webpage) to make sure your copy of the BB Twitch account is up to date, 
comparing the date written at the top of your instructions file (readme.md) to the one written 
online.

If you're only missing icons *or new tidbits* you can just download those files to your computer.
More drastic changes to the BB Twitch setup will require you to delete your copy and follow steps
2-4 again.

Alternatively, those of you who understand GitHub or are willing to learn can clone the repo and
Pull before each match to keep everything up to date.

### Step 6

In the Starting Soon scene look at the sources. Change Team1 Name and Team2 Name to the names of 
the teams playing and swap out Team1 Icon and Team2 Icon to their respective icons, stored in the
Team Icons folder.

*Also make sure that the Tidbit source refers to the tidbit.txt file in the Load Text folder.*

### *Step 7*

*Open the Load Text folder and right click on the empty space. Select Show More Options, then Open
in Terminal. This will open a command terminal, into which you need to type `py change_load.py`. 
This will start the code that changes the loading screen tip every 20 seconds. Leave the terminal window 
open so the code keeps running until the stream is over.*

### Step 8

Make sure you're ready to use the scene change hotkeys. By default, Starting Soon is numpad 7, 
Coach CAMRA is numpad 8, and Full Gameplay is numpad 9, but you can change these to suit your 
setup.

### Step 9

Hit Start Streaming to go live!
