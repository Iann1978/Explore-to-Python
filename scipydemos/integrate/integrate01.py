# https://www.tutorialspoint.com/scipy/scipy_integrate.htm

print("integrate01")

import numpy as np
from scipy.integrate import quad, dblquad
from scipy.constants import pi

#Return the double (definite) integral of func(y, x) from x = a..b and y = gfun(x)..hfun(x).
f = lambda x: np.exp(-x**2)
i = quad(f, 0, 1)
print(i)

f1 = lambda y, x: 1
i1 = dblquad(f1, 0, pi/4, np.sin, np.cos)
print(i1)

f2 = lambda y, x, a: a*x*y
i21 = dblquad(f2, 0,1, lambda x:2-x, lambda x:x, args=(1,))
print(i21)
i23 = dblquad(f2, 0, 1, lambda x:2-x, lambda x:x, args=(3,))
print(i23)