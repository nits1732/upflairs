import cv2
import skimage
vid=cv2.VideoCapture(0)
while True:
    flag,img=vid.read()
    if flag:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_p=cv2.subtract(img[:,:,-1], cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
        th,img_p2= cv2.threshold (img_p, 60, 255,cv2.THRESH_BINARY)
        img_p3=skimage.morphology.remove_small_objects(img_p2.astype(bool),0)
        img_p4=cv2.dilate(img_p3.astype('uint8'),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))).astype(bool)
        img_p5=skimage.morphology.remove_small_holes(img_p4,180)
        rp=skimage.measure.regionprops(skimage.measure.label(img_p5))
        img_preview=img.copy()
        if len(rp)>0:
            (y1,x1,y2,x2)=rp[0].bbox
            img_preview=img.copy()
            cv2.rectangle(
                img_preview,
                pt1=(x1,y1),pt2=(x2,y2),color=(255,255,0),
                thickness=10
            )
    cv2.imshow('preview', img_preview[:,:,::-1])
    key = cv2.waitKey(1)
    if key == ord('k'):
        break
cv2.destroyAllWindows()
cv2.waitKey(1)
vid.release()