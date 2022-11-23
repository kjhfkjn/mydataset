import pandas as pd

# 读取文件
df = pd.read_csv('train.csv')

count = [0,0,0,0]
# df计数
for i in range(len(df)):
    if df['source'][i] == 0:
        count[0] += 1
    elif df['source'][i] == 1:
        count[1] += 1
    elif df['source'][i] == 2:
        count[2] += 1
    elif df['source'][i] == 3:
        count[3] += 1

print(count)