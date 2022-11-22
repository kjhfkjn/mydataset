import os

# Current file directory
path = os.path.dirname(os.path.abspath(__file__))
# Get file names in the folder
filename = os.listdir(path)
for name in filename:
    new_lines = []
    with open(path+'/'+name,'r') as f:
        lines = f.readlines()
        for line in lines:
            new_line = []
            text = line.split(' ')
            if int(text[0]) == 44:
                print(name)
                new_line.append('0')
            elif int(text[0]) == 57:
                print(name)
                new_line.append('1')
            new_lines.append(new_line)

    if new_lines == []:
        # 删除空文件
        os.remove(path+'/'+name)
        image_name = name.split('.')[0] + '.jpg'
        os.remove(path+'/'+image_name)
    else:
        with open(path+'/'+name,'w') as f:
            for line in new_lines:
                f.write(line)
