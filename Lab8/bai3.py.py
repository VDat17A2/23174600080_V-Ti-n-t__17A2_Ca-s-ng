def cubesum(n):
  sum = 0
  while n > 0:
    digit = n % 10
    sum += digit**3
    n //= 10
  return sum

print(cubesum(156))  
print(cubesum(5873)) 
print(cubesum(-7))  
