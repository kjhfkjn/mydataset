import os

path = 'D:/learning/PythonProject/APythonProject/courseDesign/mydatasets'

# 获取文件夹下的所有文件名
filename_face = os.listdir(path+'/face/data/labels/train')+os.listdir(path+'/face/data/labels/valid')+os.listdir(path+'/face/data/labels/test')
filename_drone = os.listdir(path+'/drone/drone_dataset_yolo/dataset_txt')

filename = os.listdir(path+'/mydataset/labels')
error_num = 0
error_num2 = 0

for name in filename:
    if name in filename_face:
        new_lines = []
        need = 0
        with open(path+'/mydataset/labels/'+name,'r') as f:
            lines = f.readlines()
            new_line = []
            for line in lines:
                content = line.split(' ')
                if int(content[0]) != 1:
                    error_num += 1
                    need = 1
                    content[0] = '1'
                    new_line = ' '.join(content)
                    new_lines.append(new_line)
                else: 
                    new_lines.append(line)
                # print(new_line)
        if need:
            with open(path+'/mydataset/labels/'+name,'w') as f:
                for line in new_lines:
                    f.write(line)

print(error_num,error_num2)
