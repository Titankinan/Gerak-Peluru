import math
import matplotlib.pyplot as plt
import numpy as np

#Konstanta
g = 9.806
t = 0
delta_t = 0.01
m = 0.15
vo = 50
teta = 35

#Tanpa Hambatan Udara
ax = 0
ay = -g
i = 0
x = np.zeros((600))
y = np.zeros((600))
vx = vo * math.cos(math.radians(teta))
vy = vo * math.sin(math.radians(teta))

#Hambatan Udara
d = 0.0013
vxH = vo * math.cos(math.radians(teta))
vyH = vo * math.sin(math.radians(teta))
v = ((vx**2) + (vy**2))**0.5
axH = -(d/m)*(v*vx)
ayH = -g -(d/m)*(v*vy) 
j = 0
xH = np.zeros((600))
yH = np.zeros((600))


while x[i] >= 0 and y[i] >= 0:
  #x  
  vx = vx + (ax * delta_t)
  x[i+1] = x[i] + (vx * delta_t)
  #y
  vy = vy + (ay * delta_t)
  y[i+1] = y[i] + (vy * delta_t)
  #increment
  t += delta_t
  i+= 1

while xH[j] >= 0 and yH[j] >= 0:
  #xH  
  vxH = vxH + (axH * delta_t)
  xH[j+1] = xH[j] + (vxH * delta_t)
  #yH
  vyH = vyH + (ayH * delta_t)
  yH[j+1] = yH[j] + (vyH * delta_t)
  #increment
  j+= 1

plt.plot(x,y,'r',label="Tanpa Hambatan Udara")
plt.plot(xH,yH,'b',label="Dengan Hambatan Udara")
plt.title("Grafik Gerak Peluru Numerik")
plt.xlabel("Jarak Tempuh Horizontal (m)")
plt.ylabel("Tinggi (m)")
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left', borderaxespad=0.)
plt.show()
