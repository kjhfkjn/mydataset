import numpy
import pandas
import os
import cv2
import matplotlib as plt
# 获取文件夹下的所有文件名
filename = os.listdir('labels')
# print(filename)

g = []
for name in filename:
    with open('labels/'+name,'r') as f:
        img = cv2.imread('images/'+name[:-4]+'.jpg')

        if img is None:
            continue
        w = img.shape[1]
        h = img.shape[0]
        
        # print(w,h)
        lines = f.readlines()
        for line in lines:
            content = line.split(' ')
            # print(content)
            # print(int(content[0]),float(content[1])*w,float(content[2])*h,float(content[3]),float(content[4]))
            classes = int(content[0])
            x_center = float(content[1])*w
            y_center = float(content[2])*h
            w2 = float(content[3])*w
            h2 = float(content[4])*h
            x = (x_center-w2/2)
            if x<0:
                x = 0
                print(1)
            y = (y_center-h2/2)
            if y<0:
                y = 0
                print(2)
            if x+w2 > w:
                w2 = w-x
                print(3)
            if y+h2 > h:
                h2 = h-y
                print(4)
            new = [name[:-4],w,h,[x,y,w2,h2],classes]
            g.append(new)
           
            box = [int(x),int(y),int(x+w2),int(y+h2)]
            # print(box)
            # print((w,h))
            # cv2.rectangle(img,
            #               (box[0], box[1]),
            #               (box[2], box[3]),
            #               (220, 0, 0), 3)
            # 保存
            # if classes == 3:
            #     cv2.imwrite('images/'+name[:-4]+'.jpg',img)
            #     a= input()

        # # 保存
        # if classes == 3:
        #     cv2.imwrite('images/'+name[:-4]+'.jpg',img)
        #     a= input()

df = pandas.DataFrame(g,columns=['image_id','width','height','bbox','source'])
# df 保存为csv文件
df.to_csv('train.csv',index=False)
print('ok')