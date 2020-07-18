import os
import json
from collections import defaultdict

def createDictionary(filename):
    dic = defaultdict(int)
    f = open(filename, 'r')
    contents = f.read()

    for word_tag in contents.split():
        dic[word_tag] += 1

    f.close()
    return dic

def writeDictionary(dic, filepath):
    open(filepath, 'w+').close()
    j = json.dumps(dic)
    with open(filepath, 'w') as f:
        f.write(j)

def main():
    for filename in os.listdir('../Train-corpus/cleaned-files'):
        if '.txt' in filename:
            dic = createDictionary('../Train-corpus/cleaned-files/'+filename)
            writeDictionary(dic, '../Train-corpus/dictionary/'+filename[:-3]+'json')

if __name__ == "__main__":
    main()