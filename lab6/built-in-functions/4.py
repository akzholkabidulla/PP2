import time
import math

print("Input:")
a = int(input())
b = int(input())

time.sleep(b/1000)
print(f"Square root of {a} after {b} miliseconds is {math.sqrt(a)}")

# Вызывает функцию квадратного корня через определенные миллисекунды