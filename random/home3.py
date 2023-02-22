def einsum(u, v):
    c = 299792.458 # speed of light in km/s
    return (u+v)/(1+(u*v)/(c**2))

u1 = float(input("Enter speed of the first body with respect to the observer: "))
v1 = float(input("Enter speed of the second body with respect to the first: "))
v2 = float(input("Enter speed of the third body with respect to the second: "))
v3 = float(input("Enter speed of the fourth body with respect to the third: "))

sum_of_speeds = einsum(u1, v1)
sum_of_speeds = einsum(sum_of_speeds, v2)
sum_of_speeds = einsum(sum_of_speeds, v3)

print("Sum of speeds is {:.14f} km/s".format(sum_of_speeds))
