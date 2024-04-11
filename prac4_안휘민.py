# prac4.py

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일의 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''
<<<<<<< HEAD:prac4.py
    file_name = input('file name: ')
    try:
        with open(file_name, 'r') as file:
            print(f"File: {file_name}")
=======

    file_name = input()

    try:
        open(file_name)
        print(file_name)
>>>>>>> f2ed3c6 (prac4_.py 6th):prac4_안휘민.py
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    read_file()
