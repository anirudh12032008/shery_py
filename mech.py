# By Anirudh Sahu
import threading
import time
import pygame
from pynput import keyboard
from pynput.keyboard import KeyCode,Key
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

print(KeyCode)

# Load audio file
pygame.mixer.init()

# Load the audio file once
pygame.mixer.music.load("soundh.ogg")

print("Made By Anirudh Sahu Star the repository if you like it")

#audio configuration
audio_config = {
    KeyCode.from_char('1'): [2078, 176],
    KeyCode.from_char('\x1a'): [2078, 176],
    KeyCode.from_char('2'): [9291, 164],
    KeyCode.from_char('3'): [9702, 153],
    KeyCode.from_char('4'): [10097, 140],
    KeyCode.from_char('5'): [10459, 165],
    KeyCode.from_char('6'): [10859, 165],
    KeyCode.from_char('7'): [11250, 165],
    KeyCode.from_char('8'): [11648, 159],
    KeyCode.from_char('9'): [12014, 150],
    KeyCode.from_char('0'): [12414, 136],
    KeyCode.from_char('q'): [12826, 137],
    KeyCode.from_char('w'): [13227, 138],
    KeyCode.from_char('e'): [13625, 134],
    KeyCode.from_char('r'): [14035, 137],
    KeyCode.from_char('t'): [15707, 163],
    KeyCode.from_char('y'): [16114, 157],
    KeyCode.from_char('u'): [16515, 150],
    KeyCode.from_char('i'): [16889, 147],
    KeyCode.from_char('o'): [17253, 161],
    KeyCode.from_char('p'): [17630, 156],
    KeyCode.from_char('a'): [18024, 140],
    KeyCode.from_char('s'): [18416, 134],
    KeyCode.from_char('d'): [18815, 140],
    KeyCode.from_char('f'): [19229, 128],
    KeyCode.from_char('g'): [19632, 127],
    KeyCode.from_char('h'): [20024, 131],
    KeyCode.from_char('j'): [20438, 131],
    KeyCode.from_char('k'): [27154, 171],
    KeyCode.from_char('l'): [33678, 163],
    KeyCode.from_char('z'): [22850, 160],
    KeyCode.from_char('x'): [23243, 156],
    KeyCode.from_char('c'): [23645, 155],
    KeyCode.from_char('v'): [24034, 152],
    KeyCode.from_char('b'): [24445, 146],
    KeyCode.from_char('n'): [24824, 148],
    KeyCode.from_char('m'): [25181, 164],
    KeyCode.from_char(','): [25593, 145],
    KeyCode.from_char('.'): [25993, 139],
    KeyCode.from_char('/'): [26393, 136],
    KeyCode.from_char('<97>'): [26393, 136],
    Key.f1: [26801, 128],
    Key.f2: [8869, 181],
    Key.f3: [28061, 186],
    Key.f4: [20858, 129],
    Key.f5: [28466, 161],
    Key.f6: [28845, 151],
    Key.f7: [29208, 156],
    Key.f8: [29571, 144],
    Key.f9: [29926, 159],
    Key.f10: [30248, 139],
    Key.f11: [30598, 140],
    Key.f12: [30981, 130],
    Key.up: [8372, 140],
    Key.left: [34451, 164],
    Key.right: [34906, 168],
    Key.down: [22462, 166],
    Key.space: [34906, 168],      
    Key.tab: [2919, 177],
    Key.caps_lock: [3307, 185],
    Key.shift: [3700, 176],
    Key.ctrl: [4164, 148],
    Key.alt: [4613, 155],
    Key.enter: [5024, 150],
    Key.backspace: [5438, 147],
    Key.esc: [5862, 149],
    Key.print_screen: [6270, 138],     
    Key.scroll_lock: [7547, 134],
    Key.pause: [7957, 141],
    Key.insert: [14524, 141],
    Key.delete: [14949, 119],
    Key.home: [15311, 143],
    Key.end: [13227, 138],
    Key.page_up: [21286, 113],
    Key.page_down: [21671, 146],
    Key.cmd: [36919, 119],
    Key.menu: [36419, 121],
    Key.shift: [3700, 176],
    Key.shift_r: [3700, 176],
    Key.ctrl_l: [4164, 148],
    Key.ctrl_r: [4164, 148],
    Key.alt_l: [4613, 155],
    Key.alt_r: [4613, 155],
}

# Keyboard event listener
# Function to play audio
def play_audio(start_time, duration):
    pygame.mixer.music.play(start=start_time / 1000.0)  # Convert milliseconds to seconds
    time.sleep(duration / 1000.0)  # Convert milliseconds to seconds
    pygame.mixer.music.stop()

# Keyboard event listener
def on_key_press(key):
    if key in audio_config:
        start_time, duration = audio_config[key]
        threading.Thread(target=play_audio, args=(start_time, duration)).start()

# Start keyboard listener in a separate thread
keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()
# Keep the application running
try:               
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    keyboard_listener.stop()
    keyboard_listener.join()
