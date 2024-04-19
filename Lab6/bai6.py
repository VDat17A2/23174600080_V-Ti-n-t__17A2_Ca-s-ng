m = int(input("Nhập số hàng ma trận 1: "))
n = int(input("Nhập số cột ma trận 1: "))
ma_tran = []
for i in range(m):
  hang = []
  for j in range(n):
    phan_tu = float(input(f"Nhập phần tử [{i},{j}]: "))
    hang.append(phan_tu)
  ma_tran.append(hang)


# In ma trận ra màn hình
for i in range(m):
  for j in range(n):
    print(f"{ma_tran[i][j]:.2f}", end=" ")
  print()
# Tính tổng của ma trận
tong = 0
for i in range(m):
  for j in range(n):
    tong += ma_tran[i][j]

# In tổng ra màn hình
print("Tổng của ma trận 1:", tong)





m2 = int(input("Nhập số hàng ma trận 2: "))
n2 = int(input("Nhập số cột ma trận 2: "))
ma_tran2 = []
for i in range(m2):
  hang2 = []
  for j in range(n2):
    phan_tu2 = float(input(f"Nhập phần tử [{i},{j}]: "))
    hang2.append(phan_tu2)
  ma_tran2.append(hang2)


# In ma trận ra màn hình
for i in range(m2):
  for j in range(n2):
    print(f"{ma_tran2[i][j]:.2f}", end=" ")
  print()
# Tính tổng của ma trận
tong2 = 0
for i in range(m2):
  for j in range(n2):
    tong2 += ma_tran2[i][j]

# In tổng ra màn hình
print("Tổng của ma trận 2:", tong2)





tich = [[0 for _ in range(n2)] for _ in range(m)]
for i in range(m):
  for j in range(n2):
    for k in range(n):
      tich[i][j] += ma_tran[i][k] * ma_tran2[k][j]
print("Tích của 2 ma trận là : ",tich)



# Tạo ma trận chuyển vị
ma_tran_chuyen_vi = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
  for j in range(n):
    ma_tran_chuyen_vi[j][i] = ma_tran[i][j]

# In ma trận chuyển vị ra màn hình
print("Ma trận chuyển vị của m trận ban đầu là :")
for i in range(n):
  for j in range(m):
    print(f"{ma_tran_chuyen_vi[i][j]:.2f}", end=" ")
  print()