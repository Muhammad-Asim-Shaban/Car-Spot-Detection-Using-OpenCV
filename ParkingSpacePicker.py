import cv2
import pickle
try:
    with open('CarParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]

width,height=107,48

def mouseclick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)






while True:
    image = cv2.imread('carParkImg.png')
    #cv2.rectangle(image,(50,192),(157,240),(255,0,255),2)
    for pos in posList:
        cv2.rectangle(image, pos, (pos[0]+width,pos[1]+height), (255, 0, 255), 2)

    cv2.imshow("image",image)
    cv2.setMouseCallback("image",mouseclick)
    cv2.waitKey(1)