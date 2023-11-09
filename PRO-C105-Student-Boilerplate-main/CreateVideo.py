import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

data = cv2.imread(images[0])
print (data.shape)
output=cv2.VideoWriter('imageV.avi',cv2.VideoWriter_fourcc(*'XVID'),10,(151,123))
for i in range(0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)
output.release()