
def tinh_tien_dien(gio_dung, von, hien_tai, gia_dien):
    # Tính công suất (đơn vị watt)
    cong_suat = von * hien_tai
    
    # Tính năng lượng tiêu thụ (đơn vị kWh)
    nang_luong_tieu_thu = (cong_suat * gio_dung) / 1000
    
    # Tính số tiền điện phải trả
    tien_dien = nang_luong_tieu_thu * gia_dien
    
    return tien_dien

# Giá điện (đồng/kWh)
gia_dien = 5000

# Nhập số giờ sử dụng từ người dùng
so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))

# Thông số điện của máy lọc không khí
dien_ap = 220  # Hiệu điện thế (V)
dong_dien = 1.5  # Cường độ dòng điện (A)

# Tính toán tổng số tiền điện phải trả
tong_tien_dien = tinh_tien_dien(so_gio_su_dung, dien_ap, dong_dien, gia_dien)

# In kết quả
print("Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí là: {:.2f} đồng".format(tong_tien_dien))