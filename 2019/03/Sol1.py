import math as mathf

def inline(line, point):
    res = True
    if(line[0][0] <= point[0] and line[1][0] >= point[0]) or (line[0][0] >= point[0] and line[1][0] <= point[0]): res = True
    else: return False

    if(line[0][1] <= point[1] and line[1][1] >= point[1]) or (line[0][1] >= point[1] and line[1][1] <= point[1]): return True
    else: return False
    

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return(0,0)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if inline(line1, (x, y)) and inline(line2, (x, y)):
        return (x, y)
    else:
        return(0,0)

f = open("Input1.txt", "r")
t = f.read()
input1 = t.split(",")
f = open("Input2.txt", "r")
t = f.read()
input2 = t.split(",")
wire1=[(0,0)]
for i in input1:
    if(i[0] == "R"):
        wire1.append((wire1[-1][0] + int(i[1:len(i)]), wire1[-1][1]))
    if(i[0] == "L"):
        wire1.append((wire1[-1][0] - int(i[1:len(i)]), wire1[-1][1]))
    if(i[0] == "U"):
        wire1.append((wire1[-1][0], wire1[-1][1] + int(i[1:len(i)])))
    if(i[0] == "D"):
        wire1.append((wire1[-1][0], wire1[-1][1] - int(i[1:len(i)])))
sol = (0,0)
wire2=[(0,0)]
for i in input2:
    if(i[0] == "R"):
        wire2.append((wire2[-1][0] + int(i[1:len(i)]), wire2[-1][1]))
    if(i[0] == "L"):
        wire2.append((wire2[-1][0] - int(i[1:len(i)]), wire2[-1][1]))
    if(i[0] == "U"):
        wire2.append((wire2[-1][0], wire2[-1][1] + int(i[1:len(i)])))
    if(i[0] == "D"):
        wire2.append((wire2[-1][0], wire2[-1][1] - int(i[1:len(i)])))
        
for i in range(1,len(wire1)):
    for j in range(1, len(wire2)):
        intersection = line_intersection((wire1[i-1], wire1[i]),(wire2[j-1], wire2[j]))
        if (intersection != (0,0)):
            if(sol == (0,0)):
                sol = intersection
            elif(abs(intersection[0]) + abs(intersection[1])) < (abs(sol[0]) + abs(sol[1])):
                sol = intersection
print(abs(sol[0]) + abs(sol[1]))
