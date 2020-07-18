import os
import xml.etree.ElementTree as ET

def parse(xmlfile):

    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # path of file for storing cleaned file
    filepath = xmlfile[:-7] + 'cleaned-files/' + xmlfile[-7:-3] + 'txt'

    # clean file
    open(filepath, 'w+').close()

    # open file in append mode
    f = open(filepath, 'a')

    # recursively find all <w> tags
    for word in root.iter('w'):
        f.write(word.text.replace(' ', '') + '_' + word.attrib['pos'] + ' ')

    # close file
    f.close()

def main():

    # clean the Training corpus
    for filename in os.listdir('../Train-corpus'):
        if '.xml' in filename:
            parse('../Train-corpus/'+filename)

    # clean the Test corpus
    for filename in os.listdir('../Test-corpus'):
        if '.xml' in filename:
            parse('../Test-corpus/'+filename)

if __name__ == "__main__":
    main()