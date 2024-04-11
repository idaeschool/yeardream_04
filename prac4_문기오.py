# prac4.py

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 내용 or 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input("file_name을 입력 하세요 : ")
    try:
        with open(file_name,"r") as file:
            print(file.read())
    except FileNotFoundError: 
        print("없는 파일명 입니다.")

if __name__ == "__main__":
    read_file()
