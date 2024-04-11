# main.py
import argparse
import prac1
import prac2
import prac3
import prac4_modified
import prac5_modified
import prac6_new

def main():
    parser = argparse.ArgumentParser(description="Run practice Python scripts.")
    parser.add_argument('script', choices=['prac1', 'prac2', 'prac3','prac4', 'prac5', 'prac6'], help='The script to run')
    args = parser.parse_args()

    if args.script == 'prac1':
        prac1.say_hello()
    elif args.script == 'prac2':
        prac2.sum_two_numbers()
    elif args.script == 'prac3':
        prac3.calculate_average()
    elif args.script == 'prac4':
        prac4_modified.read_file()
    elif args.script == 'prac5':
        prac5_modified.main()
    elif args.script == 'prac6':
        prac6_new.game_loop()

if __name__ == "__main__":
    main()