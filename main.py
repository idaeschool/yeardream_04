# main.py
import argparse #library
import prac1 #import == 같은 경로 안에 prac.py를 불러옴
import prac2
import prac3

def main():
    parser = argparse.ArgumentParser(description="Run practice Python scripts.")
    parser.add_argument('script', choices=['prac1', 'prac2', 'prac3'], help='The script to run')
    args = parser.parse_args()

    if args.script == 'prac1':
        prac1.say_hello() #prac1파일의 say_hello()를 실행
    elif args.script == 'prac2':
        prac2.sum_two_numbers()
    elif args.script == 'prac3':
        prac3.calculate_average()

if __name__ == "__main__":
    main()