print("Welcome to your own geometry calclator for basic calculations")
import math
pie = 3.1416
shape = input('Please enter the geometric shape you want to know the calculation about like triangle, sphere etc.').lower()
if shape == "triangle":
    para = input('Enter the parameter like area, surface area.').lower()
    if para == "area":
        b = input('Enter the breadth')
        h = input('Enter the height')
        Tarea = 0.5*(float(b)*float(h))
        print(f"Area of triangle is {area}")
    elif para == "peri":
        a = input('Enter the side')
        peri = float(a)*3
        print(f"Perimeter of the triangle is {peri}")
    elif para == "altitude":
        num = 3
        a = input('Side lenght')
        sqrt = num**(0.5)
        alti = (float(sqrt)*float(a))/2
        print(f"Altitude of triangle {alti}")
elif shape == "sphere":
    para = input('Enter the parameter like area, surface area.').lower()
    if para == "area":
        r = input('Enter the radius')
        Sarea =  (4*pie*float(r)**2)
        print(f"Area of sphere is {Sarea}")
    elif para == "peri":
        r = input('Enter the radius')
        Speri = (2*pie*float(r))
        print(f"Perimeter of sphere is {Speri}")
    elif para == "sa":
        r = input('Enter the radius')
        sa = (4*pie*float(r)**2)
        print(f"Surface area of sphere is {sa}")
    elif para == "v":
        r = input('Enter the radius')
        Vol = ((4/3)*pie*float(r)**3)
        print(f"Volume is {Vol}")
elif shape == "cylinder":
    para = input('Enter the parameter like area, surface area.').lower()
    if para == "peri":
        r = input('Enter the radius')
        h = input('Enter the height')
        peri = 2((2*float(r)) + float(h))
        print(f"Perimeter of cylinder is {peri}")
    elif para == "area":
        r = input('Enter the radius')
        h = input('Enter the height')
        area = 2*pie*float(r)*(flaot(r)+float(h))
        print(f"Area of cylinder is {area}")
    elif para == "v":
        r = input('Enter the radius')
        h = input('Enter the height')
        vol = pie*float(r)**2*float(h)
        print(f"Vol of cylinder is {vol}")
    elif para == "csa":
        r = input('Enter the radius')
        h = input('Enter the height')
        csa = 2*pie*float(r)*float(h)
        print(f"Csa of cylinder is {csa}")
    elif para == "lsa":
        r = input('Enter the radius')
        h = input('Enter the height')
        lsa = 2*pie*float(r)*float(h)
        print(f"Lateral surface area of cylinder is {lsa}")
    elif para == "tsa":
        r = input('Enter the radius')
        h = input('Enter the height')
        tsa = 2*pie*float(r)*(float(h)+float(r))
        print(f"Lateral surface area of cylinder is {tsa}")
elif shape == "cone":
    para = input('Enter the parameter like area, surface area.').lower()
    if para == "area":
        r = input('Enter the radius')
        h = input('Enter the height')
        area = pie*float(r)*(float(r)+ math.sqrt((float(h)**2)+(float(r)**2)))
        print(f"The area of cone is {area}")
    elif para == "vol":
        r = input('Enter the radius')
        h = input('Enter the height')
        vol = pie*float(r)**2*(float(h)/3)
       
   
       
