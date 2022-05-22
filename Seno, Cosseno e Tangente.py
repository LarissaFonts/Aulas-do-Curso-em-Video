from math import radians, sin, cos, tan
ang = float(input('angulo? '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print("seno {:.2f}, cosseno {:.2f} e tangente {:.2f}".format(s, c, t))