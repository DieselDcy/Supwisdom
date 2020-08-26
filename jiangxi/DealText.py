# 文本数据处理
from StopWords import readFile
from StopWords import seg_doc
import os
import time


# 高效读取文件
# 迭代器类
class loadFolders(object):
    def __init__(self, par_path):
        self.par_path = par_path

    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath = os.path.join(self.par_path, file)
            if os.path.isdir(file_abspath):
                yield file_abspath


class loadFiles(object):
    def __init__(self, par_path):
        self.par_path = par_path

    def __iter__(self):
        folders = loadFolders(self.par_path)
        for folder in folders:  # level1 directory
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):  # level2 directory
                file_path = os.path.join(folder, file)
                # 文件具体操作
                if os.path.isfile(file_path):
                    this_file = open(file_path, 'rb')  # rb读取更快
                    content = this_file.read().decode('utf8')
                yield catg, content
                this_file.close()


if __name__ == '__main__':
    start = time.time()

    filepath = os.path.abspath(r'C:\Users\Chengyu.Dean\Desktop\树维\江西省挖煤\new_江西省报告')
    files = loadFiles(filepath)
    # n = 5  # n表示抽样率
    for i, msg in enumerate(files):
        catg = msg[0]
        content = msg[1]
        content = seg_doc(content)
        print('{t}***{i}\t docs has been dealed'.format(i=i, t=time.
            strftime('%Y-%m-%d %H:%M:%S', time.localtime())), '\n',
            catg, ':\t', content[:20])
    end = time.time()
    print('total cost time: %.2f' % (end-start)+'s')
