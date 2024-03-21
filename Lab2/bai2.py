def chu_so_hang_nghin(so_nguyen):
    if len(str(so_nguyen)) < 4:
        return 0
    else:
        return int(str(so_nguyen)[0])

# Nhập số nguyên từ người dùng
so_nguyen = int(input("Nhập một số nguyên: "))

# Xuất chữ số hàng nghìn
print("Chữ số hàng nghìn của số là:", chu_so_hang_nghin(so_nguyen))