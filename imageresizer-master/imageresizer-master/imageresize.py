import cv2
import os
import shutil
#source="grogu"
#destination="grog1"
source = input("enter the source:")
destination=input("enter destination:")
source=os.path.join(r"{0}".format(source))
destination=os.path.join(r"{0}".format(destination))
scale = 90
j=0
for i in os.listdir(source):
    src = cv2.imread(os.path.join(source,i))
    #cv2.imshow("image",src)
    new_width = int(src.shape[1] * scale / 100)
    new_height = int(src.shape[0] * scale / 100)
    output = cv2.resize(src, (new_width, new_height))
    des="newimage{0}.jpg".format(j)
    cv2.imwrite(des,output)
    j+=1
images=[f for f in os.listdir() if '.jpg' in f.lower()]
for image in images:
    new_path=destination+"\\"+image
    shutil.move(image,new_path)