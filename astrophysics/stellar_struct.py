#Stellar Structure Code (written in Python 2)
'''outputs plots describing the relationship between star variables
ex: pressure vs mass'''

import numpy as np
import matplotlib.pyplot as plt
import math

#Differential equations of stellar structure (solved below using Runge-Kutta method)

#dq/dx
def dq(x,f,p,t,q):
    return (p*(x**2))/t

#dp/dx
def dp(x,f,p,t,q):
    return (-p*q)/(t*(x**2))

#df/dx
def df(x,f,p,t,q):
    return (p**2)*(t**2)*(x**2)

#dt/dx
def dt(x,f,p,t,q):
    return ((p**2)*q)/((t**8.5)*((x**2)))
    #return (((p**2)*q)/((t**8.5)*((x**2))))*(-1)
  
def rk4(dq,dp,df,dt,x0,x1,n,pc):
    
    #initializing lists
    vx = [0] * (n+1)
    rq = [0] * (n+1)
    rp = [0] * (n+1)
    rf = [0] * (n+1)
    rt = [0] * (n+1)
    u = [0] * (n+1)
    v = [0] * (n+1)
    nplus1 = [0] * (n+1)
    
    h = (x1 - x0)/float(n)
    
    #initial conditions 
    #single series expansion since undefined at x = 0
    vx[0] = x = x0
    rq[0] = q = 1/3*((pc)*(x**3))
    rp[0] = p = pc - 1/6*((pc**2)*(x**3))
    rf[0] = f = 1/3*((pc**2)*(x**3))
    rt[0] = t = 1 - 1/6*((pc**4)*(x**4))
    
    for i in range(1, n + 1):    
        
        j0 = h*dq(x, f, p, t, q)
        k0 = h*dp(x, f, p, t, q)
        l0 = h*df(x, f, p, t, q)
        m0 = h*dt(x, f, p, t, q)
        
        j1 = h*dq(x+0.5*h, f+0.5*j0, p+0.5*k0, t+0.5*l0, q+0.5*m0)
        k1 = h*dp(x+0.5*h, f+0.5*j0, p+0.5*k0, t+0.5*l0, q+0.5*m0)
        l1 = h*df(x+0.5*h, f+0.5*j0, p+0.5*k0, t+0.5*l0, q+0.5*m0)
        m1 = h*dt(x+0.5*h, f+0.5*j0, p+0.5*k0, t+0.5*l0, q+0.5*m0)
        
        j2 = h*dq(x+0.5*h, f+0.5*j1, p+0.5*k1, t+0.5*l1, q+0.5*m1)
        k2 = h*dp(x+0.5*h, f+0.5*j1, p+0.5*k1, t+0.5*l1, q+0.5*m1)
        l2 = h*df(x+0.5*h, f+0.5*j1, p+0.5*k1, t+0.5*l1, q+0.5*m1)
        m2 = h*dt(x+0.5*h, f+0.5*j1, p+0.5*k1, t+0.5*l1, q+0.5*m1)
        
        j3 = h*dq(x+0.5*h, f+0.5*j2, p+0.5*k2, t+0.5*l2, q+0.5*m2)
        k3 = h*dp(x+0.5*h, f+0.5*j2, p+0.5*k2, t+0.5*l2, q+0.5*m2)
        l3 = h*df(x+0.5*h, f+0.5*j2, p+0.5*k2, t+0.5*l2, q+0.5*m2)
        m3 = h*dt(x+0.5*h, f+0.5*j2, p+0.5*k2, t+0.5*l2, q+0.5*m2)
        
        #solutions
        vx[i] = x = x0 + i*h
        rq[i] = q = q + (1/float(6))*(j0 + 2*j1 + 2*j2 + j3)
        rp[i] = p = p + (1/float(6))*(k0 + 2*k1 + 2*k2 + k3)
        rf[i] = f = f + (1/float(6))*(l0 + 2*l1 + 2*l2 + l3)
        rt[i] = t = t + (1/float(6))*(m0 + 2*m1 + 2*m2 + m3)
        
        #calculate U and V at each point
        u[i] = ((p)*(x**3))/(t*q)
        v[i] = q/(t*x)
    
        nplus1[i] = ((t**8.5)*(q))/((p**2)*f)      
        
    return vx, rq, rp, rf, rt, u, v, nplus1, h, pc

vx,rq,rp,rf,rt,u,v,nplus1,h,pc = rk4(dq,dp,df,dt,0.01,34,67,0.71263901928)
print 'step size =', h
print 'pc =', pc

alp = u[66]+u[67]
bet = alp/2
print 'U at intersection for my model is',bet


print '\nThese are the variable values at intersection'

char = vx[66] + vx[67]
det = char/2
x_real = math.log(det)
print 'x =',x_real

ech = (rq[66]+rq[67])/2
q_real = math.log(ech)
print 'q =',q_real

eq = (rp[66]+rp[67])/(2)
p_real = math.log(eq)
print 'p =',p_real

fep = (rt[66]+rt[67])/2
t_real = math.log(fep)
print 't =',t_real

geo = (rf[66]+rf[67])/2
f_real = math.log(geo)
print 'f =',f_real

print '\nThese are the values of ()star after manipulating eqns 1,4,5,6'
print 'AKA log(a) = A --> a = 10^A'
xstar=-0.270
xstar1=10**(xstar)
print 'xstar =',xstar1

qstar=0.03729
qstar1=10**(qstar)
print 'qstar =',qstar1

pstar=-0.34841
pstar1=10**(pstar)
print 'pstar =',pstar1

tstar=-0.47740
tstar1=10**(tstar)
print 'tstar =',tstar1

fstar = 1
print 'fstar = 1'

print '\nThese are the original values of ()star from T1513 in Schwarz.'
print 'xstar =',xstar
print 'qstar =',qstar
print 'pstar =',pstar
print 'tstar =',tstar

x0 = (xstar1/det)
q0 = qstar1/ech
p0 = pstar1/eq
t0 = (tstar1/fep)
f0 = fstar/f_real

print '\nEvaluating ()0 values'
print 'x0 = xstar/x ...'
print 'x0 =', x0
print 'q0 =', q0
print 'p0 =', p0
print 't0 =', t0
print 'f0 =', f0

#using (14) in structeqns.pdf
print'Evaluating C and D constants'
c = (x0*(t0)**9.5)/((p0**2)*(f0))
print 'C =',c

d = f0/((p0**2)*(t0**2)*(x0**3))
print 'D =',d

#calculating R, T, P, L for 8 different masses
print 'Total stellar radius\n'
m = 0.7
k = 1.38*(10**-10)
a = 7.5657*(10**-11)
light = 3*(10**8)
pi = 3.14159
rg = 8.31*(10**7)
mu = 1.30
grav = 6.67*(10**-11)

rad = ((m**0.5)/((c*d))*(3*k/(4*a*light))*1/((4*pi)**4)*((rg/mu)**3.5)*1/(grav**3.5))**(1/6.5)

print 'R =',rad/1000,'km'

temp = tstar1*((mu*grav*m)/(rg*rad))
print temp

pres = pstar1*((grav*(m**2)/(4*pi*(rad**4))))
print pres

lumi = ((mu/rg)**4)*(grav**4/(4*pi))*((m**6)/(d*(rad**7)))
print lumi

#plotting UV plane
uvint = np.loadtxt("T1506.dat", skiprows=1)
a = uvint[:,0]
b = uvint[:,1]
#print a,b
plt.plot(a,b)

uvint = np.loadtxt("T1507.dat", skiprows=1)
c = uvint[:,0]
d = uvint[:,1]
plt.plot(c,d)

uvint = np.loadtxt("T1508.dat", skiprows=1)
e = uvint[:,0]
f = uvint[:,1]
plt.plot(e,f)

uvint = np.loadtxt("T1509.dat", skiprows=1)
g = uvint[:,0]
h = uvint[:,1]
plt.plot(g,h)

uvint = np.loadtxt("T1510.dat", skiprows=1)
i = uvint[:,0]
j = uvint[:,1]
plt.plot(e,f)

uvint = np.loadtxt("T1511.dat", skiprows=1)
k = uvint[:,0]
l = uvint[:,1]
plt.plot(k,l)

uvint = np.loadtxt("T1512.dat", skiprows=1)
m = uvint[:,0]
n = uvint[:,1]
plt.plot(m,n)

uvint = np.loadtxt("T1513.dat", skiprows=1)
o = uvint[:,0]
p = uvint[:,1]
plt.plot(o,p)

plt.plot(u,v)
plt.xlabel('U')
plt.ylabel('V')
plt.xlim(0,3)
plt.ylim(2,10)
plt.show()

#lum vs mass
plt.plot(rq,rf) 
plt.title('Luminosity vs. Mass')
plt.xlabel('M')
plt.ylabel('L')
plt.show()

#pressure vs mass
plt.plot(rq, rp)
plt.title('Pressure vs. Mass')
plt.xlabel('M')
plt.ylabel('P')
plt.show()

#temp vs mass
plt.plot(rt, rq)
plt.title('Temperature vs. Mass')
plt.xlabel('M')
plt.ylabel('T')
plt.show()
