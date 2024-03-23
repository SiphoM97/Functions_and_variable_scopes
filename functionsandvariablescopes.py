# local usage, refers to a variable declared inside a function.
def add_nums(a, b):
    answer = a + b
    return answer


print(add_nums(40, 40))


# Enclosing scope, a function inside another function also called a nested function.
def add_nums(a, b):
    answer = a + b

    def double_it():
        double = answer * 2
        print(double)
        double_it()
        return answer

    print(add_nums(2, 13))
