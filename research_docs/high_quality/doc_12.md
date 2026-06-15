# Model Predictive Control
**Visibility**: Public
**Uploaded by**: Steve Brunton
**Uploaded at**: 2018-06-11
**Published at**:
**Length**: 12:13
**Views**: 348517
**Likes**: 6754
**Category**: Science & Technology
## Description
```
This lecture provides an overview of model predictive control (MPC), which is one of the most powerful and general control frameworks. MPC is used extensively in industrial control settings, and can be used with nonlinear systems and systems with constraints on the state or actuation input.
Sparse identification of nonlinear dynamics for model predictive control in the low-data limit
E. Kaiser, J. N. Kutz, and S. L. Brunton, arxiv 2017.
https://arxiv.org/abs/1711.05501
Code: https://github.com/eurika-kaiser/SINDY-MPC
https://www.eigensteve.com/
This video was produced at the University of Washington
```
## Transcript
welcome back today I want to tell you
about a powerful optimization strategy
for feedback control called model
predictive control also known as MPC so
MPC fits right here in this feedback
control diagram and essentially what MPC
does it's a very flexible procedure
where if you have a system model you run
a set of you run forecasts of this model
forward in time for different actuation
strategies you and you optimize over the
control and put you over a short time
period and essentially determine your
immediate next control action based on
that optimization once you've applied
that immediate next control action then
you reinitialize your optimization over
you move your window over you re
optimized to find your next control
inputs you enact that and this thing
essentially keeps marching that that
window forward and forward in time so
it's an optimization strategy based on a
model of the system I'm going to kind of
explain a little bit how it works here
so the the basic idea let's say I have
some time and I have let's say that this
is my desired output and this is my
control signal u and let's say that
there's some kind of a set point that
I'm trying to reach so there's some kind
of goal that I'm trying to reach I want
my system to go up up here and let's say
I start here okay so essentially what
I'll do with model predictive control if
I am starting at some point let's call
this let's say that I have the whole
state X and this is at time K so X at K
and let's say y equals x just to make
this easier then what I'll do is I will
start my system I'll initialize it at
time at X at time K XK and then I'll run
an optimization procedure over the
inputs to try to find what is the best u
over some short window that gets any
closer to my desired objective okay so
there will be some some window of
hi and let's call this my horizon that's
what we call this in MPC so I've got
some time horizon and what I'm going to
do is I'm going to optimize you over
that time horizon okay and maybe what
that looks like is some kind of strategy
like this maybe I'm just making
something up maybe that's the you that
comes out of the optimization procedure
that I run here then what I do is I
essentially just lock in the first value
of that optimizing control law and I see
where my system goes so now my system
maybe goes there then what I do is I
shift my horizon over one delta T and I
realize so now maybe maybe this system
didn't go exactly where I thought so
instead of doing this now I think that
my optimal control should be a little
bit more aggressive something like this
I'm just making this up again okay and
so then what you do is you essentially
pick that next optimizing control lock
that in and see where your system goes
and so over time you can essentially
watch your system step forward and at
every new time step you reassess what
the optimal optimizing control input you
should be over some kind of moving
horizon and you only enact that next
instant control law that next step of
control and see where your system goes
and you can essentially get very very
very good control even for strongly
nonlinear systems that that achieve your
desired objective okay so if I write
this control down you would actually say
that my control K my control signal K at
time a little X K would be whatever my
optimal can control U is at time step K
plus-1
based on time step K ok so I'm going to
decode this for you because I found I
found this a little confusing I found
this a little confusing the first time
so u K plus 1 of X K basically means
this is my optimal
short time control strategies short time
control starting at XK okay so I
initialize this optimization at XK I
figure out this long trajectory of use
that would optimize my objective
function starting at that initial
condition given this model and then I
only implement the first time step this
is the first time step so I run a
simulation and I optimize my control
over many time steps but I only
implement the first time step
that's my control law at time K then my
X moves to XK plus 1 I realize an entire
new control trajectory starting at XK
plus 1 and again I implement the first
time step of that new optimized control
strategy it steps me forward and so on
and so forth so every time step I'm
rerunning this entire optimization
forward in time over some short time
window to see what is the best possible
you given my new state and what the
dynamics actually did ok so that's the
basic idea of model predictive control
now why is this so powerful I think I
think this is so powerful for a number
of reasons one is that you can impose
constraints so I can have constraints on
the state of my system so basically I
can do a control so that I never hit
some boundary so I stay within some
bounds but I can also constrain my input
which is very very important so in a lot
of control strategies that we've seen up
until now the actuation is this kind of
continuous variable and often times your
your controller would make unrealistic
demands on what you could do so for
example if I'm you know designing a
cruise controller if I design my
controller badly then it might command
use which are unphysical it might say go
a million miles an hour for a fraction
of a second and then slow down what
model predictive control can do is it
can essentially put bounds
what your control signal can actually do
so when it's running this optimization
loop for every time step when this
optimisation is running it can
essentially constrain the optimization
to not hit these these max or min values
okay so that's really cool it can run
these these hard constraints or soft
constraints on the state or on the input
it works for nonlinear systems and
there's a few ways you can think about
this so let's imagine that I had a
linear system but there were some
disturbances or noise or something like
that so I can I can determine the
optimal control signal for a linear
system using something like linear
quadratic regulator and and I could use
that for my MPC short-time optimization
and then if there's some disturbance or
some changing parameters of my system
those will compensate over time if I
have a nonlinear system what I could do
is I could take my nonlinear model and I
could linearize it about that particular
state and then I could do kind of linear
optimization so maybe what I'm trying to
get at here is that optimization is the
heart of MPC and PC is built around an
optimization every single time step I'm
Ryo maizing this control strategy U and
then just picking the first time step
and reinitializing and starting over so
this is a little bit expensive because
I'm optimum running this full
optimization at every time step okay and
this is enabled by increasingly fast
computers and fast Hardware okay so this
is essentially relies on fast Hardware
to be able to run this optimization loop
instead of usually if I do something
like a linear quadratic regulator or a
common filter I run my optimization
offline on a you know a big computer and
then I take those results and I
hard-code them on my my fast online
control system NPC is different it
relies on the fact that you have fast
computational hardware to run this
optimization
online at every time step okay now we
know that there are known optimal
solutions for you for linear systems so
oftentimes model predictive control will
be applied to linearized equations of
motion even if I have a nonlinear system
maybe I'll compute the linearized
dynamics and every point X and I'll feed
that into a linear optimization because
that's fast but increasingly now that
computers are getting faster and faster
and faster it's becoming increasingly
possible to actually directly optimize
the nonlinear equations of motion if you
have them okay so kind of the big
picture here is that now instead of
doing our control optimization one time
offline like we used to do with linear
quadratic regulator x' we can do this
optimization continuously at every time
step of our system and we can modify our
control behavior if our system starts to
deviate or if the dynamics start to
change now this has driven a tremendous
amount of interest in system
identification because this relies on
having a system model so because of the
power of model predictive control we're
very very interested in getting good
system models that we can actually use
so non linear and linear models of our
system that we can control linear is the
easiest and fastest to optimize so a lot
of model predictive controls are wrapped
around linear models and of course
there's this feedback so if my system
doesn't do what my model says then I
just reinitialize and make a new
prediction so model predictive control
is more flexible than traditional linear
control methods because if the system
starts to move or deviate or doesn't do
what you what you think it should you
reinitialize your optimization at every
new time step okay so that's really
important is that this is more flexible
sometimes what people do is linear
parameter varying so essentially what I
do is I have a family of linear models
so instead of just X dot equals
X plus bu what I'll do is I'll have a
sum parameter mu and B of some parameter
mu and as my parameter mu changes in
time I can still run a linear
optimization but I'm running this linear
optimization on different a and B
matrices as my trajectory of all's in
time okay and then now of course since
we're getting faster and faster
computers and our latency is is getting
lower and lower it's actually becoming
feasible in some situations to run this
online optimization on the full
nonlinear dynamical system okay so
that's the overview of model predictive
control in a nutshell what we're going
to talk about later is how we can use
modern system identification techniques
so kind of based on data-driven
optimization and machine learning to
build these models from data and then
use those with model predictive control
to stabilize and track reference
trajectories for strongly nonlinear
systems okay thank you