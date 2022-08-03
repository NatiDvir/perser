import os

FOLDER_PATH = r'C:\\Users\\natanel\\Desktop\\GC-MS\\perser\\perses-main-data-new CEF\\data\\new CEF'


def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        name,type = os.path.splitext(fileName)
        print('Folder Name:\n' + os.path.abspath(os.path.join(dir, fileName)), sep='\n')
        print('File Name:\n' + fileName)
        print('Attributes: ')
        print(name.split('_'))
        break;

if __name__ ==  '__main__':
    listDir(FOLDER_PATH)