def fizzBuzz(n):
    if (n == 0):
        return
    total = ''
    if (n % 3 == 0):
        total + 'Fizz'
    if (n % 5 == 0):
        total + 'Buzz'
    print(total)
    fizzBuzz(n-1)


if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(15)