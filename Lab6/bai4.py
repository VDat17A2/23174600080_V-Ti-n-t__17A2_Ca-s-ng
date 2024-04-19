def so_nguyen_to(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1): 
        if number % i == 0:
            return False
    return True
def fibonacci(n):
    fib_list = [0, 1]
    [fib_list.append(fib_list[-1] + fib_list[-2]) for _ in range(2, n)]
    return fib_list[:n]
danh_sach_so_nguyen_to = [num for num in range(2, 100) if so_nguyen_to(num)]
n = int(input("Nhập số lượng số Fibonacci đầu tiên: "))
fibonacci_list = fibonacci(n)
print(f"Danh sách Fibonacci gồm {n} số đầu tiên là:", fibonacci_list)
print("Danh sách số nguyên tố nhỏ hơn 100 là:", danh_sach_so_nguyen_to)