# prac4.py
## 수정!
# 파일명 변환 했습니다!!
def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
    file_name = input("파일 이름을 입력해주세요: ")
    try:
        with open(file_name, 'r') as file:
            print("파일 이름:", file.name)
    except FileNotFoundError:
        print("해당 파일이 없습니다.")

if __name__ == "__main__":
    read_file()
