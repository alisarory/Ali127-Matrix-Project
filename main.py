import ali127 as al

print("=== AliMatrix Library Project ===")
print("The library calculates determinant of a 2x2 matrix.")

print("\nMatrix form:")
print("[ a  b ]")
print("[ c  d ]")

a = float(input("\nEnter value a: "))
b = float(input("Enter value b: "))
c = float(input("Enter value c: "))
d = float(input("Enter value d: "))

matrix = al.Ali127(a, b, c, d)
determinant = matrix.determinant_2x2()
print("\nYour Matrix:")
print("[", a, b, "]")
print("[", c, d, "]")

print("\nDeterminant:")
print(determinant)
