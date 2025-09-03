def gcf(num1, num2):
    smaller = min(num1, num2)
    for i in range(1, smaller + 1):
        if num1 % i ==0 and num2%i == 0:
            gcf = i
    return gcf
print(gcf(12, 16))
            