import os

FOLDER_PATH = r'C:\\Users\\natanel\\Desktop\\GC-MS\\perser\\perses-main-data-new CEF\\data\\new CEF'


def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        name,type = os.path.splitext(fileName)
        # print('Folder Name:\n' + os.path.abspath(os.path.join(dir, fileName)), sep='\n')
        # print('File Name:\n' + fileName)
        # print('Attributes: ')
        # print(name.split('_'))
        break;

    fileArray = name.split('_')
    fileDic = {
        "tube_sn": fileArray[0],
        "analyzer_id": fileArray[1],
        "internal_standards_set_id": fileArray[2],
        "injection_pos": fileArray[3],
        "time_analysis": fileArray[4],
        "tube_sn": fileArray[5],
    }
    return fileDic;


if __name__ == '__main__':
    fileDic = listDir(FOLDER_PATH)
    print(fileDic)