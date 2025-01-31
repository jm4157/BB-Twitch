# Blood Bowl Snitch Setup

So you want to stream Blood Bowl on Snitch. I'm here to learn you how. Follow the steps.

## Step 1

On this Github page, press the button labeled `<> Code` and select the Download Zip option. Unzip it to the location you want the VSPN files set up.

## Step 2 

Download and install [OBS](https://obsproject.com) and [Python](https://www.python.org/downloads/).

## Step 3

Sign into OBS with the Savage Scrimmage Series Twitch account. Ask Andrew (paradoxical_perception on Discord) for the login details.

## Step 4

In OBS find the **Scene Collection** option and **Import** the file *snitch_scene_collection_import.json*. This will set OBS up with all the SSS scenes and such.

## Step 5

In the Starting Soon scene look at the sources. Change Team1 Name and Team2 Name to the appropriate names, and swap out Team1 Icon and Team2 Icon to the appropriate icons.

## Step 6

Open a terminal in the **Load Text** folder and use the command `py change_load.py`. This will start the code that changes the loading screen tip every 20 seconds. Leave the terminal window open so the code keeps running until the stream is over.

## Step 7

Set the scene change hotkeys. By default, Starting Soon is numpad 7, Coach CAMRA is numpad 8, and Full Gameplay is numpad 9.

## Step 8
Hit Start Streaming to go live!
