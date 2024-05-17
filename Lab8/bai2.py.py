def giai_thuat_nhan(n, k):
  """
  Tính giai thừa của một số n.

  Args:
    n: Số nguyên dương.
    k: Số nguyên dương.

  Returns:
    Giai thừa của n.
  """
  if k == 0:
    return 1
  else:
    return n * giai_thuat_nhan(n - 1, k - 1)

def hoan_vi(n, r):
  """
  Tính số hoán vị của n phần tử lấy r phần tử.

  Args:
    n: Số nguyên dương, số lượng phần tử.
    r: Số nguyên dương, số lượng phần tử được lấy.

  Returns:
    Số hoán vị.
  """
  if r > n:
    return 0
  else:
    return giai_thuat_nhan(n, r) / giai_thuat_nhan(n - r, 0)

def to_hop(n, r):
  """
  Tính số tổ hợp của n phần tử lấy r phần tử.

  Args:
    n: Số nguyên dương, số lượng phần tử.
    r: Số nguyên dương, số lượng phần tử được lấy.

  Returns:
    Số tổ hợp.
  """
  return hoan_vi(n, r) // giai_thuat_nhan(r, 0)

n = 5
r = 2
so_hoan_vi = hoan_vi(n, r)
print("Số hoán vị của", n, "phần tử lấy", r, "phần tử:", so_hoan_vi)
so_to_hop = to_hop(n, r)
print("Số tổ hợp của", n, "phần tử lấy", r, "phần tử:", so_to_hop)
