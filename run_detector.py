from pathlib import Path
from fastai.vision.all import *
import mss
import os

def grab_screen():
    with mss.mss() as sct:
        sct_img = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
    return img

        
learns = load_learner("/Users/harryhaghani/Downloads/nsfw_dataset_v1/nsfw_model.pkl")

import time

while True:
    img = grab_screen()  
    img = img.resize((128, 128))  
    pred, pred_idx, probs = learns.predict(img)

    print(f"Prediction: {pred} | Probability: {probs[pred_idx]:.2f}")
    
    if pred.lower() in ['nsfw', 'porn', 'unsafe']:
        print("⚠️ NSFW content detected!")
        os.system("osascript -e 'tell application \"System Events\" to keystroke \"q\" using {control down, command down}'")

    
    time.sleep(1)  # wait 1 second before next capture
