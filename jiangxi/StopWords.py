import sys
import jieba
import re


def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
        return str_doc


def textParse(str_doc):
    str_doc = re.sub('\u3000', '', str_doc)
    str_doc = re.sub(r'\s+', ' ', str_doc)
    str_doc = str_doc.replace('\n', ' ')
    # 正则过滤掉特殊符号、标点、英文等。
    r1 = '[a-zA-Z’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    str_doc = re.sub(r1, '', str_doc)
    return str_doc


def get_stop_words(path=r'../dataSet/StopWord/NLPIR_stopwords.txt'):
    file = open(path, 'r', encoding='utf-8').read().split('\n')
    # 返回，删除重复数据
    return set(file)


# 去掉一些停用词和数字
def rm_tokens(words, stwlist):
    words_list = list(words)
    stop_words = stwlist
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words:
            # 去除停用词
            words_list.pop(i)
        elif words_list[i].isdigit():
            words_list.pop(i)
        elif len(words_list[i]) == 1:
            words_list.pop(i)
        elif words_list[i] == ' ':
            words_list.pop(i)
    return words_list


# 利用jieba分词对文本进行分词，返回切词后的List
def seg_doc(str_doc):
    # 1正则处理文本
    sent_list = str_doc.split('\n')
    sent_list = map(textParse, sent_list)
    # 2 获取停用词
    stwlist = get_stop_words()
    # 3分词并去除停用词
    word_2list = [rm_tokens(jieba.cut(part, cut_all=False), stwlist) for part in sent_list]
    # 4合并列表
    word_list = sum(word_2list, [])
    return word_list


if __name__ == '__main__':
    path = r'C:\Users\Chengyu.Dean\Desktop\树维\江西省挖煤\new_江西省报告\江西科技学院.txt'
    str_doc = readFile(path)
    # print(str_doc)
    # print(textParse(str_doc))
    word_list = seg_doc(str_doc)
    print(word_list)
