import math

def tinh_khoang_cach_duong_den_diem(he_so_goc, he_so_tu_do, x, y):
    return abs(he_so_goc * x - y + he_so_tu_do) / math.sqrt(he_so_goc**2 + 1)

def xac_dinh_vi_tri(he_so_goc, he_so_tu_do, x_tam, y_tam, ban_kinh):
    khoang_cach = tinh_khoang_cach_duong_den_diem(he_so_goc, he_so_tu_do, x_tam, y_tam)
    
    if khoang_cach < ban_kinh:
        return "Đường thẳng cắt đường tròn."
    elif khoang_cach == ban_kinh:
        return "Đường thẳng tiếp xúc đường tròn."
    elif khoang_cach > ban_kinh:
        return "Đường thẳng nằm ngoài đường tròn."
    else:
        return "Đường thẳng nằm trong đường tròn."

# Nhập thông số của đường thẳng từ người dùng
he_so_goc = float(input("Nhập hệ số góc của đường thẳng: "))
he_so_tu_do = float(input("Nhập hệ số tự do của đường thẳng: "))

# Nhập thông số của đường tròn từ người dùng
x_tam = float(input("Nhập tọa độ x của tâm đường tròn: "))
y_tam = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))

# Xác định vị trí tương đối giữa đường thẳng và đường tròn
vi_tri = xac_dinh_vi_tri(he_so_goc, he_so_tu_do, x_tam, y_tam, ban_kinh)

# In ra kết quả
print("Vị trí tương đối giữa đường thẳng và đường tròn là:", vi_tri)