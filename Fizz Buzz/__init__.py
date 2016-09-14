fizzbuzz = range(1,30)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')

    elif num % 3 == 0:
        print('Fizz')

    elif num %5 == 0:
        print('Buzz')

    else:
        return str(num)

