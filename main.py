#Write your code below this line 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
total = 0

def paint_calc() :
    area_total = 0
    area_total = test_h * test_w
    number_cans = round(area_total / coverage)
    print('The number of cans are, '+ str(number_cans))

paint_calc()

