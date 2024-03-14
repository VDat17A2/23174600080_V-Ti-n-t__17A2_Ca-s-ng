

def tinh_bieu_thuc(x, z):
    # Tính giá trị của từng phần trong biểu thức
    phan1 = (math.sin(x)) ** 2 / (1 + math.atan(x))
    phan2 = math.log(x) / (x - z)
    phan3 = (x * z) / (z * math.exp(1))
    
    # Tổng hợp giá trị của các phần
    ket_qua = phan1 + phan2 + phan3
    
    return round(ket_qua, 2)

# Nhập số thực x và z từ người dùng
x = float(input("Nhập giá trị của x: "))
z = float(input("Nhập giá trị của z: "))

# Tính giá trị của biểu thức
gia_tri = tinh_bieu_thuc(x, z)

# In kết quả
print("Giá trị của biểu thức là:", gia_tri)