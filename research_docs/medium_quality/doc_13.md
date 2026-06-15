- Syllabus
- Schedule
- View
- Edit
- History
- Print
# Model Predictive Control
Model predictive control (MPC) is a type of control algorithm that is used to control systems with dynamics. It is a model-based method that uses a predictive model of the system to compute control actions that optimize a performance criterion over a finite horizon.
The basic idea of MPC is to optimize a control policy that minimizes the difference between the desired reference signal and the output of the system, subject to constraints on the control inputs and the states of the system. This optimization problem can be written as follows:
minuk,...,uk+N−1k+N−1∑i=k\|\|ri−yi\|\|2+k+N−1∑i=k\|\|ui−ui−1\|\|2minuk,...,uk+N−1∑i=kk+N−1\|\|ri−yi\|\|2+∑i=kk+N−1\|\|ui−ui−1\|\|2
subject to:
xk+1=f(xk,uk)xk+1=f(xk,uk)
gj(xi,ui)≤0(j=1,2,...,m)gj(xi,ui)≤0(j=1,2,...,m)
where uk,...,uk+N−1uk,...,uk+N-1 are the control inputs at each time step in the horizon, _ri_ is the reference signal at time _i_, _yi_ is the output of the system at time _i_, _f(xk, uk)_ is the model prediction of the state at time _k+1_ given the state at time _k_ and the control input at time _k_, _xk+1_ is the state at time _k+1_, and _gj(xi, ui)_ are the constraints on the states and control inputs at time _i_.
The optimization problem is solved using an optimization algorithm, such as the interior point method, at each time step. The solution of the optimization problem gives the optimal control inputs for the current time step and the next few time steps in the horizon. The control inputs for the current time step are then applied to the system, and the horizon is shifted forward by one time step. The process is then repeated at the next time step.
MPC has several advantages compared to other control algorithms. It allows the control of systems with constraints on the control inputs and states, it can handle a wide range of performance criteria, and it can handle systems with time-varying dynamics. It is widely used in industries such as chemical process control, automotive control, and power systems.
* * *
There are many methods to implement control including basic strategies such as a proportional-integral-derivative (PID) controller or more advanced methods such as model predictive techniques. The purpose of this section is to provide a tutorial overview of potential strategies for control of nonlinear systems with linear models.
Tap to unmute
Model Predictive Control in MATLAB and Excel APMonitor.com
APMonitor.com80.4K subscribers
Watch on
A following section relates methods to implement dynamic control with nonlinear models.
#### Exercise
**Objective:** Design a model predictive controller for an overhead crane with a pendulum mass. Meet specific control objectives by tuning the controller and using the state space model of the crane system. Simulate and optimize the pendulum system with an adjustable overhead cart. _Estimated time: 2 hours._
A pendulum is described by the following dynamic equations:
⎢⎣˙y˙v˙θ˙q⎤⎥
⎥⎦=⎡⎢
⎢⎣010000ϵ0000100−10⎤⎥
⎥⎦⎡⎢
⎢⎣yvθq⎤⎥
⎥⎦+⎡⎢
⎢⎣010−1⎤⎥
⎥⎦u\[y˙v˙θ˙q˙\]=\[010000ϵ0000100−10\]\[yvθq\]+\[010−1\]u
where _m1=10_ is the mass of the cart, _m2=1_ is the mass of the item carried, εε is _m2/(m1+m2)_, _y_ is the position of the overhead cart, _v_ is the velocity of the overhead cart, θθ is the angle of the pendulum relative to the cart, and _q_ is the rate of angle change2.
The objective of the controller is to adjust the force on the cart to move the pendulum mass to a new final position. Ensure that initial and final velocities and angles of the pendulum are zero. The position of the pendulum mass is initially at -1 and it is desired to move it to the new position of 0 within 6.2 seconds. Demonstrate controller performance with changes in the pendulum position and that the final pendulum mass remains at the final position without oscillation. How does the solution change if the mass of the item carried is increased to _m2=5_?
#### Solution
Tap to unmute
Linear MPC with State Space Model APMonitor.com
APMonitor.com80.4K subscribers
Watch on
**Solution with _m2_ =1**
**Solution with _m2_ =5**
#%%Import packages
import numpy as np
from gekko import GEKKO
import matplotlib.pyplotas plt
#%% Build model
#initialize GEKKO model
m = GEKKO()
#time
m.time= np.linspace(0,7,71)
#Parameters
mass1 = m.Param(value=10)
mass2 = m.Param(value=1)
final = np.zeros(np.size(m.time))
for i inrange(np.size(m.time)):
if m.time\[i\]>=6.2:
final\[i\]=1
else:
final\[i\]=0
final = m.Param(value=final)
#Manipulated variable
u = m.Var(value=0)
#Variables
theta = m.Var(value=0)
q = m.Var(value=0)
#Controlled Variable
y = m.Var(value=-1)
v = m.Var(value=0)
#Equations
m.Equations(\[y.dt()== v,\
v.dt()== mass2/(mass1+mass2) \\* theta + u,\
theta.dt()== q,\
q.dt()== -theta - u\])
#Objective
m.Minimize(final \* (y\*\*2 \+ v\*\*2 \+ theta\*\*2 \+ q\*\*2))
m.Minimize(0.001 \\* u\*\*2)
#%% Tuning
m.options.IMODE=6#control
#%% Solve
m.solve()
#%% Plot solution
plt.figure()
plt.subplot(4,1,1)
plt.plot(m.time,u.value,'r-',lw=2)
plt.ylabel('Force')
plt.legend(\['u'\],loc='best')
plt.subplot(4,1,2)
plt.plot(m.time,v.value,'b--',lw=2)
plt.legend(\['v'\],loc='best')
plt.ylabel('Velocity')
plt.subplot(4,1,3)
plt.plot(m.time,y.value,'g:',lw=2)
plt.legend(\['y'\],loc='best')
plt.ylabel('Position')
plt.subplot(4,1,4)
plt.plot(m.time,theta.value,'m-',lw=2)
plt.plot(m.time,q.value,'k.-',lw=2)
plt.legend(\[r'$\\theta$','q'\],loc='best')
plt.ylabel('Angle')
plt.xlabel('Time')
plt.show()
[\[$\[Get Code\]\]](https://apmonitor.com/do/index.php/Main/ControlTypes?action=sourceblock&num=1)
\# Contributed by Everton Colling
import matplotlib.animationas animation
import numpy as np
from gekko import GEKKO
\# requires ffmpeg to save mp4 file
\#  available from https://ffmpeg.zeranoe.com/builds/
\#  add ffmpeg.exe to path such as C:\\ffmpeg\\bin\ in
\#  environment variables
#Defining a model
m = GEKKO()
#################################
#Weight of item
m2 =5
#################################
#Defining the time, we will go beyond the 6.2s
#to check if the objective was achieved
m.time= np.linspace(0,8,100)
#Parameters
m1a = m.Param(value=10)
m2a = m.Param(value=m2)
final = np.zeros(len(m.time))
for i inrange(len(m.time)):
if m.time\[i\]<6.2:
final\[i\]=0
else:
final\[i\]=1
final = m.Param(value=final)
#MV
ua = m.Var(value=0)
#State Variables
theta\_a = m.Var(value=0)
qa = m.Var(value=0)
ya = m.Var(value=-1)
va = m.Var(value=0)
#Intermediates
epsilon = m.Intermediate(m2a/(m1a+m2a))
#Defining the State Space Model
m.Equation(ya.dt()== va)
m.Equation(va.dt()== epsilon\*theta\_a + ua)
m.Equation(theta\_a.dt()== qa)
m.Equation(qa.dt()== -theta\_a -ua)
#Definine the Objectives
#Make all the state variables be zero at time >= 6.2
m.Minimize(final\*ya\*\*2)
m.Minimize(final\*va\*\*2)
m.Minimize(final\*theta\_a\*\*2)
m.Minimize(final\*qa\*\*2)
#Try to minimize change of MV over all horizon
m.Minimize(0.001\*ua\*\*2)
m.options.IMODE=6#MPC
m.solve()#(disp=False)
#Plotting the results
import matplotlib.pyplotas plt
plt.figure(figsize=(12,10))
plt.subplot(221)
plt.plot(m.time,ua.value,'m',lw=2)
plt.legend(\[r'$u$'\],loc=1)
plt.ylabel('Force')
plt.xlabel('Time')
plt.xlim(m.time\[0\],m.time\[-1\])
plt.subplot(222)
plt.plot(m.time,va.value,'g',lw=2)
plt.legend(\[r'$v$'\],loc=1)
plt.ylabel('Velocity')
plt.xlabel('Time')
plt.xlim(m.time\[0\],m.time\[-1\])
plt.subplot(223)
plt.plot(m.time,ya.value,'r',lw=2)
plt.legend(\[r'$y$'\],loc=1)
plt.ylabel('Position')
plt.xlabel('Time')
plt.xlim(m.time\[0\],m.time\[-1\])
plt.subplot(224)
plt.plot(m.time,theta\_a.value,'y',lw=2)
plt.plot(m.time,qa.value,'c',lw=2)
plt.legend(\[r'$\\theta$',r'$q$'\],loc=1)
plt.ylabel('Angle')
plt.xlabel('Time')
plt.xlim(m.time\[0\],m.time\[-1\])
plt.rcParams\['animation.html'\]='html5'
x1 = ya.value
y1 = np.zeros(len(m.time))
#suppose that l = 1
x2 =1\*np.sin(theta\_a.value)+x1
x2b =1.05\*np.sin(theta\_a.value)+x1
y2 = -1\*np.cos(theta\_a.value)+y1
y2b = -1.05\*np.cos(theta\_a.value)+y1
fig = plt.figure(figsize=(8,6.4))
ax = fig.add\_subplot(111,autoscale\_on=False,\
xlim=(-1.5,0.5),ylim=(-1.2,0.4))
ax.set\_xlabel('position')
ax.get\_yaxis().set\_visible(False)
crane\_rail,= ax.plot(\[-1.5,0.5\],\[0.2,0.2\],'k-',lw=4)
start,= ax.plot(\[-1,-1\],\[-1.5,1\],'k:',lw=2)
objective,= ax.plot(\[0,0\],\[-1.5,1\],'k:',lw=2)
mass1,= ax.plot(\[\],\[\],linestyle='None',marker='s',\
markersize=40,markeredgecolor='k',\
color='orange',markeredgewidth=2)
mass2,= ax.plot(\[\],\[\],linestyle='None',marker='o',\
markersize=20,markeredgecolor='k',\
color='orange',markeredgewidth=2)
line,= ax.plot(\[\],\[\],'o-',color='orange',lw=4,\
markersize=6,markeredgecolor='k',\
markerfacecolor='k')
time\_template ='time = %.1fs'
time\_text = ax.text(0.05,0.9,'',transform=ax.transAxes)
start\_text = ax.text(-1.06,-1.1,'start',ha='right')
end\_text = ax.text(0.06,-1.1,'objective',ha='left')
def init():
mass1.set\_data(\[\],\[\])
mass2.set\_data(\[\],\[\])
line.set\_data(\[\],\[\])
time\_text.set\_text('')
return line, mass1, mass2, time\_text
def animate(i):
mass1.set\_data(\[x1\[i\]\],\[y1\[i\]+0.1\])
mass2.set\_data(\[x2b\[i\]\],\[y2b\[i\]\])
line.set\_data(\[x1\[i\],x2\[i\]\],\[y1\[i\],y2\[i\]\])
time\_text.set\_text(time\_template % m.time\[i\])
return line, mass1, mass2, time\_text
ani\_a = animation.FuncAnimation(fig, animate, \
np.arange(1,len(m.time)), \
interval=40,blit=False,init\_func=init)
ani\_a.save('Pendulum\_Control.mp4',fps=30)
plt.show()
[\[$\[Get Code\]\]](https://apmonitor.com/do/index.php/Main/ControlTypes?action=sourceblock&num=2)
Thanks to Everton Colling for the animation code in Python.
import numpy as np
from gekko import GEKKO
import matplotlib.pyplotas plt
mass =\[2,5,10\]
nm =len(mass)
plt.figure()
for j inrange(len(mass)):
m1 =10
m2 = mass\[j\]
eps = m2/(m1+m2)
A = np.array(\[\[0,1,0,0\],\
\[0,0,eps,0\],\
\[0,0,0,1\],\
\[0,0,-1,0\]\])
B = np.array(\[\[0\],\
\[1\],\
\[0\],\
\[-1\]\])
C = np.identity(4)
m = GEKKO()
x,y,u = m.state\_space(A,B,C,D=None)
m.time= np.linspace(0,8,101)
fn =\[0if m.time\[i\]<6.2else1for i inrange(101)\]
final = m.Param(value=fn)
u\[0\].status=1
m.Minimize(final \* ((y\[0\]-1)\*\*2 \+ y\[1\]\*\*2 \+ y\[2\]\*\*2 \+ y\[3\]\*\*2))
m.options.IMODE=6
m.solve()
plt.subplot(len(mass),1,j+1)
plt.ylabel(f'Ball={mass\[j\]} kg')
plt.plot(m.time,y\[0\], label = r"Position ($y$)")
plt.plot(m.time,y\[1\], label = r"Velocity ($v=\\dot y$)")
plt.plot(m.time,y\[2\], label = r"Angle ($\\theta$)")
plt.plot(m.time,y\[3\], label = r"Ang Vel ($q=\\dot \\theta$)")
plt.plot(m.time,u\[0\], label = r"Force Input ($u$)")
plt.legend(loc=1)
plt.show()
[\[$\[Get Code\]\]](https://apmonitor.com/do/index.php/Main/ControlTypes?action=sourceblock&num=3)
Thanks to Derek Prestwich for the state space implementation.
Crane Pendulum Solution Files in MATLAB and Python
Tap to unmute
Pendulum Model Predictive Control with MATLAB and Python APMonitor.com
APMonitor.com80.4K subscribers
Watch on