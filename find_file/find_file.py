import os

def find_file(path = 'path', file_name = 'name'):
    file_list = os.listdir(path)
    for i in file_list:
        if i.find(file_name)>=0:
            print('file '+i+' founded')
            return 1
    print(file_name+' not founded')
    return 0

if __name__ == '__main__':
    path = 'FILE' # file path
    name = 'file_004' # file want to be founded
    find_file(path, name)
    