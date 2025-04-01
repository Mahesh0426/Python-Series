# CReate a function that return the area and circumferences of  a circle given its radious
import math
def circle(radious):
    area=  math.pi * radious ** 2 
    circumferences= 2 * math.pi * radious
    return area, circumferences

a,c = circle(3)
print(f"Area:", round(a,2), "\n" "Circumference:", round(c, 2))
    