def giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2):
    # Tính định thức
    det = a1 * b2 - a2 * b1
    
    # Tính giá trị x và y
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    
    return x, y

# Nhập các hệ số từ người dùng
a1, b1, c1 = map(float, input("Nhập các hệ số a1, b1, c1 của phương trình thứ nhất (a1x + b1y = c1): ").split())
a2, b2, c2 = map(float, input("Nhập các hệ số a2, b2, c2 của phương trình thứ hai (a2x + b2y = c2): ").split())

# Gọi hàm để giải hệ phương trình
x, y = giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2)

# In kết quả
print("Giá trị của x là:", round(x, 2))
print("Giá trị của y là:", round(y, 2))