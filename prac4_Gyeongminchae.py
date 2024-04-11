# prac4.py
import os

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input()
    try:
        for f_name in os.listdir('yeardream_04'):
            if file_name in f_name:
                print({file_name})
    except :
        print(f'{file_name} Not Found')
        pass

if __name__ == "__main__":
    read_file()
