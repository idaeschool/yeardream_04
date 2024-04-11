# prac4.py


def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input("파일 이름을 입력하세요: ")   
    try:
    # 파일 열기 시도
        with open(file_name, 'r') as file:
        # 파일 내용 읽고 출력
            print(file.read())
    except FileNotFoundError:
    # 파일이 존재하지 않는 경우의 예외 처리
        print(f"파일이 존재하지 않습니다: {file_name}")

read_file()