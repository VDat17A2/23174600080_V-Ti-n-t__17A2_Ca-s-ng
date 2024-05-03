kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
hoa_don = []
def tinh_hoa_don(mua_hang):
    tong_tien = 0
    for mat_hang, so_luong in mua_hang.items():
        if mat_hang in kho and mat_hang in gia_tien:
            don_gia = gia_tien[mat_hang]
            if kho[mat_hang] >= so_luong:
                tien_mat_hang = don_gia * so_luong
                tong_tien += tien_mat_hang
                kho[mat_hang] -= so_luong
                hoa_don.append({
                    'Mat hang': mat_hang,
                    'So luong': so_luong,
                    'Don gia': don_gia,
                    'Tien mat hang': tien_mat_hang
                })
            else:
                print(f"Không đủ hàng trong kho cho '{mat_hang}'")
        else:
            print(f"Không có thông tin giá hoặc số lượng cho '{mat_hang}'")
    return tong_tien

mua_hang = {
    "banana": 2,
    "apple": 3,
    "orange": 5,
    "pear": 1
}

tong_tien_hoa_don = tinh_hoa_don(mua_hang)
print("Hóa đơn mua hàng:")
for item in hoa_don:
    print(item)

print(f"\nTổng tiền hóa đơn: {tong_tien_hoa_don}")
print("\nSố lượng của các mặt hàng trong kho sau khi mua hàng:")
print(kho)