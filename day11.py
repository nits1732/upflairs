import cv2
# import matplotlib.pyplot as pit
from time import sleep
import numpy as np
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
vid=cv2.VideoCapture(0)
notcaptred=True
while notcaptred:
    flag,img=vid.read()
    if flag:
        # convert to grey
        img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=fd.detectMultiScale(img,1.1,5)
        #  scaleFactor=1.1,
        #     minNeighour=5,
        #     minSize=(50,50)
        np.random.seed(50)
        # colors=[np.random.randint(0,255,(len(faces),3)).tolist()]
        colors=[np.random.randint(0,255,3).tolist() for i in faces]
        i=0
        for x,y,w,h in faces:
            faces=img_grey[y:y+h, x:x+w].copy()
            smiles=sd.detectMultiScale(faces,1.1,5)
            print(len(smiles))
            if len(smiles)==1:
                cv2.imwrite('myselfie1.png',img)
                notcaptred=False
                break
                
            cv2.rectangle(
                img, pt1=(x,y) , pt2=(x+w,y+h) , color=colors[i], thickness=2
            )
            i+=1
        # th, img_bw=cv2.threshold(img_grey,80,255,cv2.THRESH_BINARY_INV)
        # print(type(img_grey))
        cv2.imshow('preview',img)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    else:
        print("No Frames")
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()