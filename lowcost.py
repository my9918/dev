import cv2
import numpy as np
import math

  
img_origin = cv2.imread("IMG_4122.JPG")
#xyxy to yyxx 
img = img_origin[649:1725,1281:4032]
list_deg=[]  

#エフェクト処理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,90,450,apertureSize = 3)

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=150, minLineLength=300, maxLineGap=70)
for line in lines:
    x1, y1, x2, y2 = line[0]
    rad = math.atan2(y2 - y1, x2 - x1)
    deg = np.rad2deg(rad)
    if(deg<0):##反転
        deg=-deg
    if (10 < deg) or (deg < -10 ):
        # 横縞以外の邪魔な線
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2,lineType=cv2.LINE_AA)
        
    else:
        # 横縞
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2,lineType=cv2.LINE_AA)
        list_deg.append(deg)

cv2.imwrite("result.jpg", img)

list_deg.sort()
print(list_deg)
print(np.mean(list_deg))
