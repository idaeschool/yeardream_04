# prac4.py

import os

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 내용(이름)을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input()
    try:
        if os.path.isfile(file_name):
            print(file_name)
        else: 
            raise Exception()
    except Exception:
        print("현재 경로에 해당 파일이 없습니다.")

if __name__ == "__main__":
    read_file()
    