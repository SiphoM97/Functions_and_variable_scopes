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

# Global scope is when a variable is declared outside of a function.
global_var = 13
def add_nums(a, b):
    total = a + b
    print("global_var in outer function:", global_var)

    def double_it():
        double = total * 2
        print("global_var in inner function:", global_var)
        return double

    return double_it()  # Return the result of double_it, instead of calling it again


# Call add_nums with arguments
result = add_nums(13, 5)
print("Result:", result)

#Rehashing functions as i dont fully undertand.

#using simple function here

def greet(first_name, last_name):
    print(f"greetings {first_name} {last_name}")
    print("All is well and I wish you the best.")

greet("Sipho", "Mzayiya")