def read_file():
    '''
    file_name에 해당하는 파일이 있다면, 해당 파일에 내용을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = "prac1.py"  # 파일 이름을 직접 입력하거나, 존재하는 파일로 변경
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"파일 '{file_name}'을(를) 찾을 수 없습니다.")

if __name__ == "__main__":
    read_file()

