from torch.utils.data import DataLoader, Dataset

class gpt_dataset(Dataset):
    def __init__(self, init_or_not):
        if init_or_not:
            path1 = r'D:\Python_projection\TransformerCVAE-master\data\post1.txt'
            vocab_path = r'D:\Python_projection\TransformerCVAE-master\data\vocab.txt'
            lines = open(path1, encoding='utf-8').readlines()
            self.data = []
            contents = []
            labels = []
            for line in lines:
                content, label = line.split('\t')[0], line.split('\t')[1].replace('\n', '')
                contents.append(content.split(' '))
                labels.append(label)
            self.data = list(zip(contents, labels))
        # print(self.data[0])

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

if __name__ == '__main__':
    gpt = gpt_dataset(Dataset)
    gpt.__init__(False)
    _10item = gpt.__getitem__(10)
    print(_10item)

