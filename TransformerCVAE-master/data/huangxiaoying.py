

emotion_dict = {"0":"<Other>", "1":"<Like>", "2":"<Sadness>", "3":"<Disgust>", "4":"<Anger>", "5":"<Happiness>"}
path2 = r'D:\Python_projection\TransformerCVAE-master\data\response.txt' # 下句
path1 = r'D:\Python_projection\TransformerCVAE-master\data\post.txt' # 上句
path3 = r'D:\Python_projection\TransformerCVAE-master\data\post1.txt'
lines2 = open(path2, encoding='utf-8').readlines()
lines1 = open(path1, encoding='utf-8').readlines()
f1 = open(path3, 'w', encoding='utf-8')
# print(type(lines1[0])) # 一个数组里装了很多个str
for i in range(len(lines1)):
    label = lines2[i].split('\t')[-1]
    content = lines1[i].split('\t')[0]
    # label = label.strip('\n') # 用replace更好
    # print(label)
    label = label.replace('\n', '')
    # print(label)
    if label in emotion_dict:
        label = emotion_dict[label]
    # print(label)
    f1.write(content + '\t' + label + '\n')
f1.close()

