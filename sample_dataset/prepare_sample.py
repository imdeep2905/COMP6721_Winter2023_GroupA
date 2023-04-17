import os
import shutil
import random

DATASET_PATH = "./dataset1/"
SAMPLE_DATASET_PATH = "./animal_faces/"
CLASSES = ['cat', 'dog', 'wild']


for type_ in ["train", "test", "val"]:
    for class_ in CLASSES:
        src = os.path.join(DATASET_PATH, type_, class_)
        dest = os.path.join(SAMPLE_DATASET_PATH , type_, class_)
        os.makedirs(dest, exist_ok=True)
        files = os.listdir(src)
        for _ in range(15):
            file = random.choice(files)
            shutil.copy(os.path.join(src, file), os.path.join(dest, file))
