# author : @jhhalls

# import the entire module
import module

# import specific function or classes
from module import add, Greeter

# use the functions
result_add = module.add(2,4)
result_subtract = module.subtract(10,5)

print(f"Addition results : {result_add}")
print(f"Subtraction results : {result_subtract}")

# use the class
greeter = Greeter("Alice")
print(greeter.greet())
