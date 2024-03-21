def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao ** 2)
    return bmi

def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi < 25:
        return "Bình thường"
    elif 25 <= bmi < 30:
        return "Hơi béo"
    else:
        return "Béo"

# Nhập chiều cao và cân nặng từ người dùng
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))

# Tính chỉ số BMI
bmi = tinh_bmi(chieu_cao, can_nang)

# Phân loại BMI
phan_loai = phan_loai_bmi(bmi)

# In kết quả
print("Chỉ số BMI của bạn là:", bmi)
print("Phân loại BMI của bạn là:", phan_loai)