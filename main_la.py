# main.py
import argparse
import prac1_la
import prac2_la
import prac3_la
import prac4_la

def main():
    parser = argparse.ArgumentParser(description="Run practice Python scripts.")
    parser.add_argument('script', choices=['prac1_la', 'prac2_la', 'prac3_la','prac4_la'], help='The script to run')
    args = parser.parse_args()

    if args.script == 'prac1_la':
        prac1_la.say_hello()
    elif args.script == 'prac2_la':
        prac2_la.sum_two_numbers()
    elif args.script == 'prac3_la':
        prac3_la.calculate_average()
    elif args.script == 'prac4_la':
        prac4_la.read_file()

if __name__ == "__main__":
    main()