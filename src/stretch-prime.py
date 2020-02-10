import sys


def main():
    args_check()

    num = sys.argv[1]
    print_prime_result(num)


def args_check():
    if len(sys.argv) != 2:
        print(
            'Please use this program in this format: python3 src/stretch-prime.py [number]')
        sys.exit()


def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def print_prime_result(num):
    if isPrime(int(num)):
        print(f'{num} is a prime number!')
    else:
        print(f'{num} is not a prime number!')


main()
