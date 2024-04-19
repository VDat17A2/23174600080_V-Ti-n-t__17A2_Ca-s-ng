def la_so_nguyen_to(number):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def la_so_hoan_hao(number):
    """Kiểm tra xem một số có phải là số hoàn hảo không."""
    if number <= 1:
        return False
    tong_uoc = sum([i for i in range(1, number) if number % i == 0])
    return tong_uoc == number

# Nhập số lượng phần tử của mảng từ người dùng
n = int(input("Nhập số lượng phần tử của mảng: "))
so_nguyen = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    so_nguyen.append(so)

# Tìm và in ra các số nguyên tố trong mảng
so_nguyen_to = [so for so in so_nguyen if la_so_nguyen_to(so)]
if so_nguyen_to:
    print("Các số nguyên tố trong mảng là:", so_nguyen_to)
else:
    print("Không có số nguyên tố trong mảng.")

# Tìm và in ra các số hoàn hảo trong mảng
so_hoan_hao = [so for so in so_nguyen if la_so_hoan_hao(so)]
if so_hoan_hao:
    print("Các số hoàn hảo trong mảng là:", so_hoan_hao)
else:
    print("Không có số hoàn hảo trong mảng.")