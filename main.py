# main.py
import argparse
import prac1
import prac2
import prac3
import prac4_백봉운

def main():
    parser = argparse.ArgumentParser(description="Run practice Python scripts.")
    parser.add_argument('script', choices=['prac1', 'prac2', 'prac3', 'prac4_백봉운'], help='The script to run')
    args = parser.parse_args()

    if args.script == 'prac1':
        prac1.say_hello()
    elif args.script == 'prac2':
        prac2.sum_two_numbers()
    elif args.script == 'prac3':
        prac3.calculate_average()
    elif args.script == 'prac4_백봉운':
        prac4_백봉운.read_file()

if __name__ == "__main__":
    main()