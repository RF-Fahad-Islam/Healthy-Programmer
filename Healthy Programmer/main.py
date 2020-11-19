from pygame import mixer
from datetime import datetime
from time import time
import os
os.chdir(os.path.join(os.getcwd(), "Healthy Programmer"))
def mainsongloop(musicpath, stopper):
    mixer.init()
    mixer.music.load(musicpath)
    mixer.music.play(10)
    while True:
        print(f"Enter \"{stopper}\"")
        a = input("Enter the stopper code : ")
        if a == stopper:
            mixer.music.stop()
            break
def log_file(msg):
    print(msg)
    with open("mylog.log", "a") as f:
        f.write(f"{msg} [{datetime.now()}]\n")
        
if __name__ == "__main__":
    print("Welcome to Healthy Programmer Software")
    initial_water = time()
    initial_eyes = time()
    initial_exercise = time()
    waterTime = 60
    water_level = 0
    eyesTime = 40
    exerciseTime = 100
    while True:
        if time() - initial_water > waterTime:
            mainsongloop("water.wav", "drank")
            log_file("Drink Water")
            initial_water = time()
            
        if time() - initial_eyes > eyesTime:
            mainsongloop("eyes.wav", "eydone")
            log_file("Relax eyes")
            initial_eyes = time()
            
        if time() - initial_exercise > exerciseTime:
            mainsongloop("exercise.wav", "phydone")
            log_file("Physical exercise")
            initial_exercise = time()