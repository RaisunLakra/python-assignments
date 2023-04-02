# Write a recursive python function to find the Nth term of the Fibonacci series.

def fab(num):
    if num<=1:return num
    return fab(num-1)+fab(num-2)

print(fab(6))