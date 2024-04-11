# prac4.py
import os
from os.path import isfile, isdir

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    # 현재 디렉토리의 내용을 가져옵니다.
    # entries = os.listdir()
    file_name = input()

    # if file_name in entries :
    #     print(f"{file_name}파일이 디렉토리에 존재합니다.")
    # else :
    #     print("현재 디렉토리에 해당 파일이 없습니다.")

    try:
        with open(file_name) as file:
            print(f"{file_name}파일이 디렉토리에 존재합니다.")
    except FileNotFoundError :
        print("현재 디렉토리에 해당 파일이 없습니다.")

if __name__ == "__main__":
    read_file()
