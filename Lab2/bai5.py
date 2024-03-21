def tinh_tong_tien(so_nguoi):
    gia_ve = 120000  # Giá vé cho 1 người
    tong_tien = so_nguoi * gia_ve
    
    # Áp dụng các chiết khấu
    if 2 <= so_nguoi <= 4:
        tong_tien *= 0.95  # Giảm 5%
    elif 4 < so_nguoi <= 10:
        tong_tien *= 0.9  # Giảm 10%
    elif so_nguoi > 10:
        tong_tien *= 0.8  # Giảm 20%
    
    return tong_tien

# Nhập số lượng người từ bàn phím
so_nguoi = int(input("Nhập số lượng người: "))

# Tính tổng số tiền phải trả
tong_tien = tinh_tong_tien(so_nguoi)

# In ra tổng số tiền phải trả
print("Tổng số tiền phải trả là:", tong_tien, "đồng")