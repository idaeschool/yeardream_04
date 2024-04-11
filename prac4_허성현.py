# prac4.py
import os.path
def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 내용을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input()
    l = []
    folder=os.getcwd()

    try:
        for name in os.listdir(folder):
            ext = name
            l.append(ext)
        if file_name in l:
            print(file_name)
        else:
            print("There is no file in this directory.")
    except Exception as Error:
        print(Error)
        # print()

if __name__ == "__main__":
    read_file()
