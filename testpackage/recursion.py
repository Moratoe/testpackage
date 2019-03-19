def sum_array(array):
    '''Return sum of all items in array'''
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(arrayy[1:])


def fibonacci(n):
    "Returns nth term in fibonacci"


    'Args:'
    'n is the input number'
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):

    '''Created a recursive function that returns the factorial of the nth term'''
    "Args:"
      "n (int): number of top items to return."

    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1

    return result

def reverse(word):
    "Returns the word entered in reverse"

    "Args:"
    'word is the string input that will be used to reverse the word'
    if word =="":
        return word
    else:
        return reverse(word[1:]) + word[0]
