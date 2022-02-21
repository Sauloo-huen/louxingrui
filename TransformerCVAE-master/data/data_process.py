open_path = '../18162371_3.json'
post_path = './post.txt'
response_path = './response.txt'
import json

emotion_dict = {"0":"Other", "1":"Like", "2":"Sadness", "3":"Disgust", "4":"Anger", "5":"Happiness"}
def prepareData():
    f1 = open(post_path, 'w', encoding='utf-8')
    f2 = open(response_path, 'w', encoding='utf-8')
    with open(open_path, encoding='utf-8') as f:
        fileJson = json.load(f)
        cntt = 0   # train dataset size

        for i in fileJson:
            pairs = []
            cntt += 1
            # lines.append(i[0][0].strip())
            # lines.append(i[1][0].strip())
            # f = i[0][0].strip()
            # k = f.split(' ')
            # k = [x for x in k if x != '' and (not x in punctuation)]
            # g = ' '.join(k)
            # w = i[1][0].strip()
            # o = w.split(' ')
            # o = [x for x in o if x != '' and (not x in punctuation)]
            # c = ' '.join(o)
            pairs.append(i[0][0].strip() + '\t' + str(i[0][1]))
            pairs.append(i[1][0].strip() + '\t' + str(i[1][1]))
            f1.write(pairs[0]+'\n')
            f2.write(pairs[1]+'\n')
        f1.close()
        f2.close()

if __name__ == "__main__":
    prepareData()