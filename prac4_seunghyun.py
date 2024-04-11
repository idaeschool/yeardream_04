# prac4.py

import os
def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input("file_name을 입력하세요:")
    try:
        if os.path.exists(file_name):
            print(f"파일이 존재합니다: {file_name}")
        else:
            raise FileNotFoundError(f"파일이 존재하지 않습니다: {file_name}")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    read_file()
