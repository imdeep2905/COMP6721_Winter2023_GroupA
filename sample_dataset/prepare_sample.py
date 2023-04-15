import os
import shutil
import random

DATASET_PATH = "../dataset/processed/"
SAMPLE_DATASET_PATH = "./awa2/"
CLASSES = ['antelope', 'cow', 'deer', 'elephant', 'giraffe', 'horse', 'lion', 'rabbit', 'sheep', 'squirrel', 'zebra']


for type_ in ["train", "test", "val"]:
    for class_ in CLASSES:
        src = os.path.join(DATASET_PATH, type_, class_)
        dest = os.path.join(SAMPLE_DATASET_PATH , type_, class_)
        os.makedirs(dest, exist_ok=True)
        files = os.listdir(src)
        for _ in range(3):
            file = random.choice(files)
            shutil.copy(os.path.join(src, file), os.path.join(dest, file))
