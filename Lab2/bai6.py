def tim_so_lon_thu_hai(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return b
        else:
            return c
    elif b >= a and b >= c:
        if a >= c:
            return a
        else:
            return c
    else:
        if a >= b:
            return a
        else:
            return b

# Nhập 3 số nguyên từ bàn phím
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

# Gọi hàm để tìm số lớn thứ hai và in ra kết quả
so_lon_thu_hai = tim_so_lon_thu_hai(a, b, c)
print("Số lớn thứ hai trong các số là:", so_lon_thu_hai)