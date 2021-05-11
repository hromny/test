import os

def fun(path, file_name):
    os.chdir(path)
    for each in os.listdir(path):
        if os.path.isfile(each):
            if str(file_name) == str(each):
                print(os.path.join(os.getcwd(), each))
        else:
            next_path = os.path.join(os.getcwd(), each)
            fun(next_path, file_name)
            os.chdir(os.pardir)


path = input('请输入待查找的初始目录：')
file_name = input('请输入需要查找的目标文件：')
fun(path, file_name)



