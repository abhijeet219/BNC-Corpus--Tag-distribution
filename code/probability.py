import os
import json
from collections import defaultdict

def printTop10(dic):
    i = 0
    # for key, value in sorted(dic.items(), key = lambda x : x[1], reverse=True):
    for key, value in dic.items():    
        for k,v in value.items():
            print(k, v)
        print("\n")    
                
def saveDic(Dict, folderpath):
    wordJson = json.dumps(Dict)
    with open(folderpath + 'probability.json', 'w+') as f:
        f.write(wordJson)

def makedict(filepath):
    dic = defaultdict(int)
    with open(filepath, 'r') as f:
        dic = json.load(f)
    return dic

def main():
    Dict = defaultdict(lambda: defaultdict(int))
    word_tagDic = makedict('../Train-corpus/freqAnal/Word_TagDic.json')
    wordDic = makedict('../Train-corpus/freqAnal/WordDic.json')

    for key, v1 in word_tagDic.items():
        temp = key.split('_')
        v2 = wordDic[temp[0]]
        Dict[temp[0]][temp[1]] = v1/v2
        print(temp[0], temp[1], v1, v2)
    saveDic(Dict, '../Train-corpus/freqAnal/')

    # printTop10(Dict)


if __name__ == "__main__":
    main()