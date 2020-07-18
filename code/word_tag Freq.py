import os
import json
from collections import defaultdict

def printTop10(dic):
    i = 0
    for key, value in sorted(dic.items(), key = lambda x : x[1], reverse=True):
    # for key, value in dic.items():    
        print(key, value)
        i = i + 1
        if i == 10: break

def saveDic(word_tagDic, folderpath):
    wordJson = json.dumps(word_tagDic)
    with open(folderpath + 'Word_TagDic.json', 'w+') as f:
        f.write(wordJson)

    # tagJson = json.dumps(tagDic)
    # with open(folderpath + 'TagDic.json', 'w+') as f:
    #     f.write(tagJson)

def addDict(word_tagDic, dic):
    for key, value in dic.items():
        # temp = key.split('_')
        word_tagDic[key] += value
        # tagDic[temp[1]] += value
    return (word_tagDic)

def makedict(filepath):
    dic = defaultdict(int)
    with open(filepath, 'r') as f:
        dic = json.load(f)
    return dic

def main():
    word_tagDic = defaultdict(int)
    # tagDic = defaultdict(int)
    for filename in os.listdir('../Train-corpus/dictionary'):
        if '.json' in filename:
            dic = makedict('../Train-corpus/dictionary/'+filename)
            addDict(word_tagDic, dic)
    saveDic(word_tagDic, '../Train-corpus/freqAnal/')
    print('=============Word_tag=============')
    printTop10(word_tagDic)
    # print('=============Tags==============')
    # printTop10(tagDic)

if __name__ == "__main__":
    main()