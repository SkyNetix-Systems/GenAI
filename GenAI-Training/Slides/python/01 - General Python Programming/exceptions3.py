while True:
    try:
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        d = 7
        c = a / b + d

    except ZeroDivisionError as err:
        # Handle division by zero error
        print(f'Division by zero is not permitted: {err.args}')

    except TypeError as err:
        # Handle type mismatch error
        print(f'Operations of different types are not permitted: {err}')

    except Exception as err:
        # Handle any other generic exception
        print(f'A generic exception has occurred: {err}')

    else:
        print(f'c={c}')
        break


age = -1
if age < 0:
    raise Exception('Age below zero is not permitted!')
