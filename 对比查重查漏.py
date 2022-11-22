import os

# 当前文件所在目录
path = os.path.dirname(os.path.abspath(__file__))
# 获取文件夹下文件名
filename_labels = os.listdir(path+'/labels')
filename_images = os.listdir(path+'/images')

for name_image in filename_images:
    name_label = name_image.split('.')[0] + '.txt'
    if name_label not in filename_labels:
        print(name_label)
