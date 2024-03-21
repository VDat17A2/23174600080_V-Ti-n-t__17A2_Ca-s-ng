def xac_dinh_vi_tri(he_so_goc1, he_so_tu_do1, he_so_goc2, he_so_tu_do2):
    if he_so_goc1 == he_so_goc2:
        return "Hai đường thẳng là đường thẳng song song."
    elif he_so_goc1 * he_so_goc2 == -1:
        return "Hai đường thẳng là đường thẳng vuông góc."
    else:
        return "Hai đường thẳng cắt nhau."

# Nhập thông số của hai đường thẳng từ người dùng
he_so_goc1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
he_so_tu_do1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
he_so_goc2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
he_so_tu_do2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))

# Xác định vị trí tương đối của hai đường thẳng
vi_tri = xac_dinh_vi_tri(he_so_goc1, he_so_tu_do1, he_so_goc2, he_so_tu_do2)

# In ra kết quả
print("Vị trí tương đối của hai đường thẳng là:", vi_tri)