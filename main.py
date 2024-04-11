# main.py
import argparse
import prac1    # prac1.py를 불러오겠다!
import prac2
import prac3
import prac4

def main():
    parser = argparse.ArgumentParser(description="Run practice Python scripts.")
    parser.add_argument('script', choices=['prac1', 'prac2', 'prac3', prac4], help='The script to run')
    args = parser.parse_args()

    if args.script == 'prac1':
        prac1.say_hello()
    elif args.script == 'prac2':
        prac2.sum_two_numbers()
    elif args.script == 'prac3':
        prac3.calculate_average()
    elif args.script == 'prac4':
        prac3.calculate_average()    

if __name__ == "__main__":
    main()