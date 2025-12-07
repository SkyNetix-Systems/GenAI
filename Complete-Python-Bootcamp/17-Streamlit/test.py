def my_decorator(f):
    def wrapper(*a, **k):
        print("Before")
        result = f(*a, **k)
        print("After")
        return result
    return wrapper

@my_decorator
def hello():
    print("Hi")
    
hello()
