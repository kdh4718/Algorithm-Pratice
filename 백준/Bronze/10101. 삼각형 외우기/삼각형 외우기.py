tri = []
for i in range(3):
    tri.append(int(input()))

if sum(tri) != 180:
    print("Error")
elif min(tri) == max(tri):
    print("Equilateral")
elif tri[0] != tri[1] and tri[1] != tri[2] and tri[0] != tri[2]:
    print("Scalene")
else:
    print("Isosceles")