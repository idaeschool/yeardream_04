# prac4.py
import os



def read_file(file_name):
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 내용을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''

    folder_path = "."
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print("파일 내용: ")
            print(content)
    else : 
        print("not exist.")

if __name__ == "__main__":
    file_name = input("이름을 내놓으세욤: ")
    read_file(file_name)

