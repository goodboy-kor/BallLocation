import os.path


def getFile():
    print("get file")
    folder = os.getcwd()
    print("current directory : %s" % folder)

    i = 0
    for filename in os.listdir(folder):
        print(str(i)+" : %s" % filename)
        i += 1
    return os.listdir(folder)


def saveFile():
    print("save file")
    name = input("파일 이름 입력 : ")
    data = input("저장할 내용 : ")
    f = open(name, 'w')
    f.write(data)
    f.close()
# def saveFile(filename,data):
#     print("save file")
#     f = open(filename, 'w')
#     f.write(data)
#     f.close()


def readFile():
    print("read file")
    file_list = getFile()
    num = int(input("읽을 파일 번호 입력 : "))
    if num > len(file_list)-1:
        print("잘못 입력 했습니다.")
        return
    else:
        f = open(file_list[num], 'r')

    print("==========")
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
    f.close()
    print("==========")
# def readFile(filename):
#     print("read file")
#     file_list = getFile()
#     f = open(filename, 'r')

#     print("==========")
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)
#     f.close()
#     print("==========")


def removeFile():
    print("remove file")
    file_list = getFile()
    num = int(input("삭제할 파일 번호 입력 : "))
    if num > len(file_list)-1:
        print("잘못 입력 했습니다.")
        return
    else:
        os.remove(file_list[num])


def controlFile():
    while(True):
        mode = int(
            input("무엇을 할 것인가요? 1 : 파일 목록 읽기, 2 : 파일저장 3 : 파일읽기 4 : 파일 삭제 0 : 종료 \n"))
        if(mode == 0):
            print("종료")
            break
        elif(mode == 1):
            getFile()
        elif(mode == 2):
            saveFile()
        elif(mode == 3):
            readFile()
        elif(mode == 4):
            removeFile()


controlFile()
