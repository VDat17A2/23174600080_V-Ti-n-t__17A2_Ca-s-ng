# Tính số tiền sau 5 năm
so_tien_ban_dau = 10000
lai_suat_hang_nam = 0.06
nam = 5
amount_after_5_years = so_tien_ban_dau * (1 + lai_suat_hang_nam) ** nam

# Tính số tiền sau 10 năm
nam = 10
amount_after_10_years = so_tien_ban_dau * (1 + lai_suat_hang_nam) ** nam

# Tính tỷ lệ tăng trưởng
toc_do_tang_truong = (amount_after_10_years - so_tien_ban_dau) / so_tien_ban_dau

# In kết quả
print("Số tiền sau 5 năm: ${:.2f}".format(amount_after_5_years))
print("Số tiền sau 10 năm: ${:.2f}".format(amount_after_10_years))
print("Tỷ lệ tăng trưởng sau 10 năm so với 5 năm: {:.2f}%".format(toc_do_tang_truong * 100))