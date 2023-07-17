import os
import shutil

def detect_duplicate_images(folder1, folder2):
    images1 = [f for f in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, f))]
    images2 = [f for f in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, f))]
    for image1 in images1:
        if image1 in images2:
            image1_path = os.path.join(folder1, image1)
            image2_path = os.path.join(folder2, image1)

            os.remove(image2_path)
            print(f"Deleted image:{image2_path}")

detect_duplicate_images("datasets/drusen/玻璃膜疣100张合格20230712/di2pi", "datasets/drusen/train/1")