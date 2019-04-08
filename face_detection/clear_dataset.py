import os

def clear(path):
    print(os.listdir(path))
    print(len(os.listdir(path)))
    for image in os.listdir(path):
        print(image)
        os.remove(path+'/'+image)
clear('cropped')