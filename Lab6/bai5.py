n = int(input("Nhập số lượng phần tử: "))
day_so = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}: "))
    day_so.append(so)

co_phai_cap_so_cong = True

for i in range(1, n):
    if day_so[i] - day_so[i - 1] != day_so[1] - day_so[0]:
        co_phai_cap_so_cong = False

if co_phai_cap_so_cong:
    print(f"Dãy số {day_so} là cấp số cộng.")
else:
    print(f"Dãy số {day_so} không phải là cấp số cộng.")
    