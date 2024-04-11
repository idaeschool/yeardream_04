def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    try:
        file_name = input('input file name:')
        with open(file_name, 'r', encoding='utf-8'):
            print(file_name)
    except FileNotFoundError:
        print(f'{file_name} is not exist')

if __name__ == "__main__":
    read_file()
