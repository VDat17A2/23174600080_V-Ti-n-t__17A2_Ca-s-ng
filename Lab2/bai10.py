def thoi_gian_chieu(phim, thoi_gian):
    if phim == "Tình cảm" and thoi_gian != "tối":
        return "Không có suất chiếu"
    elif phim == "Hoạt hình" and thoi_gian == "tối":
        return "Không có suất chiếu"
    elif phim == "Kinh dị" and thoi_gian != "tối":
        return "Không có suất chiếu"
    else:
        return "Suất chiếu phim {} vào buổi {}".format(phim, thoi_gian)

# Hiển thị các thể loại phim
print("Các thể loại phim: Hành động, Kinh dị, Tình cảm, Hài hước, Hoạt hình")

# Nhập lựa chọn từ người dùng
phim = input("Nhập thể loại phim bạn muốn xem: ")
thoi_gian = input("Nhập thời gian bạn muốn xem phim (sáng, trưa, chiều, tối): ")

# Xác định thời gian chiếu phim
thoi_gian_chiếu = thoi_gian_chieu(phim, thoi_gian)

# In ra kết quả
print(thoi_gian_chiếu)