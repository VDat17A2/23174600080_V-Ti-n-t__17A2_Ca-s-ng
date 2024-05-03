van_ban = input("Nhập văn bản: ")
cac_tu = van_ban.split()
so_luong_tu = {}
for tu in cac_tu:
    tu_sach = tu.lower().strip('.,!?:;"')
    if tu_sach:
        if tu_sach in so_luong_tu:
            so_luong_tu[tu_sach] += 1
        else:
            so_luong_tu[tu_sach] = 1
tu_nhieu_nhat = max(so_luong_tu, key=so_luong_tu.get)
tu_it_nhat = min(so_luong_tu, key=so_luong_tu.get)
print(f"Từ có số lượng nhiều nhất: '{tu_nhieu_nhat}' ({so_luong_tu[tu_nhieu_nhat]} lần)")
print(f"Từ có số lượng ít nhất: '{tu_it_nhat}' ({so_luong_tu[tu_it_nhat]} lần)")