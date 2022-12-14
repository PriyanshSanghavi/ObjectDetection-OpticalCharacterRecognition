import cv2

img_path='car.jpg'
img=cv2.imread(img_path)

classNames=[]
classFile='coco.objects'

with open(classFile,'rt') as f:
    classNames=f.read().rstrip('\n').split('\n')


configPath='coco.pbtxt'
weightPath='frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320 , 230)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
# clssIds: the returned ids , confs: the confidence , bbox: the drawn box
classIds,confs,bbox=net.detect(img,confThreshold=0.5)
#confThreshold
print(classIds,bbox)
if len(classIds) !=0:
 for classid, confidence, box in zip(classIds.flatten() ,confs.flatten(), bbox):
    cv2.rectangle(img , box ,color=(0,255,0),thickness=2)
    cv2.putText(img , classNames[classid-1] , (box[0]+10 ,box[1]+20 ),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),thickness=2)


   
#show image
img=cv2.resize(img, (800, 600))
cv2.imshow('Detector',img)

cv2.waitKey(0)
