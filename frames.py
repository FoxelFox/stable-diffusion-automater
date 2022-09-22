import imp
from subprocess import run
import glob
import os
import shutil

outputFolder = "output"

if os.path.exists(outputFolder) and os.path.isdir(outputFolder):
    shutil.rmtree(outputFolder)

promt = "close up ground - level view of a futuristic bladerunner building and sidewalk busy with activity with of signages and billboards street venders and carts very narrow streets aliens and people with a floating cars on the streets by craig mullins, neil blevins, dylan cole, james paick, hyper - realistic, night, environment fog, cinematic lighting, 8 k, vray render, artstation, deviantart, "

run([
    "python", "frame2.py", "--prompt", promt, "--strength", "0.3", "--n_samples", "1", "--n_iter", "1", "--skip_grid", "--ddim_eta", "0.9", "--ddim_steps", "100",  "--seed", "23409", "--scale", "8.0", "--precision", "full", "--explore"])
#"--precision", "full"
#"--scale", "19.0"
#"--explore"
