import os
import json
from collections import defaultdict

def printTop10(dic):
    i = 0
    for key, value in sorted(dic.items(), key = lambda x : x[1], reverse=True):
        print(key, value)
        i = i + 1
        if i == 10: break

def saveDic(wordDic, tagDic, folderpath):
    wordJson = json.dumps(wordDic)
    with open(folderpath + 'WordDic.json', 'w+') as f:
        f.write(wordJson)

    tagJson = json.dumps(tagDic)
    with open(folderpath + 'TagDic.json', 'w+') as f:
        f.write(tagJson)

def addDict(wordDic, tagDic, dic):
    for key, value in dic.items():
        temp = key.split('_')
        wordDic[temp[0]] += value
        tagDic[temp[1]] += value
    return (wordDic, tagDic)

def makedict(filepath):
    dic = defaultdict(int)
    with open(filepath, 'r') as f:
        dic = json.load(f)
    return dic

def main():
    wordDic = defaultdict(int)
    tagDic = defaultdict(int)
    for filename in os.listdir('../Train-corpus/dictionary'):
        if '.json' in filename:
            dic = makedict('../Train-corpus/dictionary/'+filename)
            addDict(wordDic, tagDic, dic)
    saveDic(wordDic, tagDic, '../Train-corpus/freqAnal/')
    print('=============Words=============')
    printTop10(wordDic)
    print('=============Tags==============')
    printTop10(tagDic)

if __name__ == "__main__":
    main()