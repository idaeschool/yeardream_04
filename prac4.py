# prac4.py

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일의 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input('찾고자 하는 파일의 이름을 확장자까지 입력하세요. e.g. text.txt : ')
    try:
        with open(file_name, 'r') as f:
            print(f'{file_name}은 이곳에 있습니다.')
    except FileNotFoundError:
        print(f'{file_name}은 이곳에 없습니다.')

if __name__ == "__main__":
    read_file()
