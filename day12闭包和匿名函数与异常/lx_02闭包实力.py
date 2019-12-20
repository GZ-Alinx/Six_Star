def line_conf(a,b):
    def line(x):
        return a*x + b
    return line


line1 = line_conf(3, 2)(5)
print(line1)
line2 = line_conf(4, 5)(3)
print(line2)
