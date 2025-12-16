function dodt = f(t,o)

l = 1;

a = 0.1;

g = 9.8;

f = sqrt(l/g)/4/pi/pi;

dodt = [o(2); (-a*f*f/l)*sin(f*t)*cos(o(1)) - (g/l)*sin(o(1))];

