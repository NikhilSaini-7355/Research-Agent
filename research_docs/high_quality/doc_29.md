# Machine Learning Methods for Model Predictive Control
**Visibility**: Public
**Uploaded by**: Alberto Bemporad
**Uploaded at**: 2021-07-23
**Published at**:
**Length**: 44:39
**Views**: 10240
**Likes**: 222
**Category**: Science & Technology
## Description
```
Semi-plenary lecture by Alberto Bemporad at the European Control Conference 2021, July 2, 2021.
Slides: http://cse.lab.imtlucca.it/~bemporad/talks/ecc2021.pdf
ABSTRACT:
Machine learning is a set of techniques to extract mathematical models from data that has recently become extremely popular and very successful in many fields, including control. In my talk, I will present several approaches in which machine learning can help design and calibrate model predictive control (MPC) laws and simplify the associated online computations. I will focus on techniques for learning prediction models tailored to nonlinear and hybrid MPC, global and preference-based optimization methods using surrogate functions for actively learning optimal MPC parameters from calibration experiments, and unsupervised and supervised learning techniques for reducing the number of optimization variables in MPC.
```
## Transcript
the title of my presentation is machine
learning methods for modern predictive
control
my name is alberto bemped and i am from
the imt school for advanced studies luca
in italy so what is modern predictive
control
is a control method where a model of the
process that we are controlling is
explicitly used to make predictions
of what would happen in the future if we
apply a certain sequence of manipulative
variables
and among all possible sequences of
manipulated variables that we can
predict
by solving an optimization problem we
choose the best one
where best is expressed in terms of the
performance index
and constraints so let's say now is the
current time
t where we want to compute the control
action
we look at n steps in the future
and optimize a weighted sum of the
tracking errors
so the difference between the predicted
outputs yk and the reference
that we want to track rft and also we
may have some penalties on the inputs
for example
deviations of the inputs from optimal
steady state
values or penalties on input increments
and so on
now the good feature of mpc is that
we can express explicitly in the problem
formulation constraints
constraints on the manipulated variables
the inputs uk
as well as constraints if you want on
the output
the predicted output y okay and the
relation
between the predicted outputs and the
inputs that we command
through the state vector x at prediction
time
k is given by a prediction
so let's say we formulate this optimal
control problem
and this can be recast as a numerical
optimization problem that
let's say we solve this problem at time
t we will get an optimal sequence of
manipulated variables
now we only apply one sample of the
sequence
the sample u of t that we need at time t
because at the next
time step at time t plus one we
again solve the same procedure the
reason why we repeat
um solving the optimization problem at
every time step
is that every time the decision
u t that we apply the monetary
manipulated variable
ut that we apply on the process depends
on the current state
of the system as well as on the current
reference so
indeed mpc is a state feedback strategy
in spite of the fact that it's based on
open loop predictions how the idea is
not new
it was conceived at least in the 60s and
has been used in a process industries
since at least the 80s there are
thousands of applications in the process
industries of
mpc control and nowadays is spreading to
different
industrial sectors in particular to the
automotive industry
and let me mention this result achieved
by general motors
and our company odis who developed
together
a gasoline engine controller that is in
production since
2018 and this as far as we know is the
first
least documented mass production of mpc
uh in the automotive industry is running
on millions
of vehicles
so the question that um we
would like to address now are how to get
good prediction models
from data and uh regarding online
optimization
how can we reduce the size of the
optimization problem
we need to solve and also how can we
help the solver for example providing
a good warm start before solving the
problem
and regarding calibration how to select
the best mpc parameters
for example by running experiments
so how to solve the calibration process
effectively so in my talk i want to show
how machine learning
ideas can help in addressing audio both
questions
so when we want to create a model to use
for predictions in npc
we typically have two approaches one is
to use physics so to write down
equations
to model the process we want to to
control
and the other approach is to completely
rely on data so use
black box modeling by running a linear
or linear system identification
algorithm general machine learning
algorithm on the data to get
a prediction model usually a combination
of the two
is uh is the best uh approach so the
parts that is easy to model we model
users using physics
while the parts that are difficult to
model that we don't want to model or
that we don't know how to model we can
rely on data
and why is the combination usually the
best well think about the following
when you use black box identification
then you choose a modern structure for
example a deep neural network
and you use data and an algorithm to
train
the network and get a model that tries
to explain the data
when we use physics we are basically
basically relying
on on a model that has been
derived by a lot of smart people before
and so the the task that we are left
with is a model structure very well
defined model
structure where we just need to fit in
some parameters and usually the number
of parameters
that we need to fit in a white box model
is much lower
than for example the whole set of
weights and bias terms in neural network
so that's why it's always good to rely
on physics
at least to choose the model structure
if we have enough physical knowledge
and of course we have to keep in mind
that the complexity of the optimization
problem
that we need to solve to implement the
mpc controller
heavily depends on the model that we
choose so if we use a linear model
then we will end up with a simple
probably quadratic programming problem
while if we use nonlinear
model most likely end up to solving on
complex
programming problems how using
machine learning and in particular
neural networks to get
non-linear models from data has been
proposed for
many years i'm studying here
two references from the 90s by hunt and
others and by sukin's van val
vardamur in a book and in particular
non-linear
outer aggressive models are probably the
easiest way
of using data with neural network fit
for neural networks
to get a model so the next output
is expressed as a neural function of the
previous na outputs and previous nb
inputs possibly with input delays
and also we can use neural networks to
estimate
state-based models so if we have states
available then we can fit
two neural networks one for the state of
data equation one for the output
equation
and if we don't have states available
you can
still get states based on your models
using your network for example this is
an idea
in this paper so to get past
inputs and outputs through a neural
networks and then
call the states the values of an inner
layer
of a deep neural network and then
use that to propagate the the model
equation
and an alternative to feed forward
neural networks is
instead to use recurrent neural networks
which are actually more appropriate
to capture relations between variables
that evolve over time
although they are more difficult to
train
an alternative to learning a model
that we then iterate over the prediction
horizon to construct the npc problem
is instead to try to learn the entire
prediction
so regarding the development of
nonlinear state space
models from input output data here's an
idea
that we developed with an elements team
of using
out encoders to construct
state space models not linear state
space models so let me tell you what the
idea about encoder
is very simply so let's say we you have
a neural network
which has an hourglass structure so a
thin
inner layer okay and
you feed data on the input
and the goal is to reconstruct exactly
the same input on the output so this was
proposed for
image processing in particular to get a
non-linear
compression of the image so to extract
features from
image and why you want to do this
because if you are successful in
reproducing the
output on the output the input then the
value
of the inner layer so the value of the
nodes
the inner layer is a good compression of
the original image
because from these few values you can
reconstruct the
entire image so how to use auto encoders
get non-linear state space models
here's the idea so let's say we have
collected
a certain number of pass inputs and
outputs
then we filled the out encoder with the
past
inputs and outputs and the goal is to
reproduce them
on the other side of the encoder
actually we are only interested in
reproducing the past
outputs which is our variables
of interest that you want to reproduce
and the inner layer
of the autoencoder would be our state
vector
so let's say you
write down this structure then you
duplicate the same structure
um by feeding the samples
shifted by one sample step so you want
to reproduce
the same sequence of past inputs and
outputs but
shifted by one time steps so that
the inner layer now represent x k plus
one
then you can introduce another network
that maps x k into x k
plus one okay so you have two times the
copy of the out encoder and another
mapping
to um to map states
together with the input uk into the next
states
xk plus one so with this structure
in mind then we can formulate a training
problem
so our loss function takes into account
the difference between the
past na outputs that we have measured
and the one predicted by
the auto encoder and the same
for the second auto encoder so it's just
one
step ahead shifted also we have the loss
between
the state x star k plus one reproduced
by the f
still update function f and the one x k
plus one that is
uh produced by second out encoder as
well
as loss between
the o star k plus 1
which is the sequence of past outputs
produced by x star k plus 1 and ok plus
1 which is the sequence of past
outputs produced by the autoencoder so
here is a very simple application of the
out encoder
to a data set generated by two tank
system
the model of the two tanks is unknown to
the algorithm
it's just used to generate the data and
with a very simple out encoder
just three hidden layers cc exponential
linear units
as neurons then it's able to learn the
dynamics
and if you close the loop on the model
generated by the out
coder actually you get very good pretty
good
tracking in a closed loop
so now let's see how we can leverage our
machine learning ideas to
learn instead switching modes so hybrid
models
so there are some systems where um the
dynamics where the dynamics
is a switching type logic type
that are better captured by piecewise
linear
models so it is a piecewise linear
system
is a system whose dynamics is described
by a partition
of a set of variables for example z
variables can be the states and the
inputs usually of the system
and the mapping from states and inputs
the next state and the output v
is linear in each affine
in each region of this partition
now piecewise a fine regression has been
studied for
for a while here i put some references
there are there are many others actually
that deal with the problem of learning
at the same
time the partition and the
linear affine gains
in each of the of the procedural cells
of the partition
actually any machine learning methods
that produce a piece piecewise a fine
mapping can be used
for example neural networks based on
relu
activation functions decision trees
linear classifiers like the one obtained
by softmax regression
even k nearest neighbors they can be
used to produce these wi-fi models
although not all of these techniques are
good for
mpc design because you need to optimize
on top
of the model so the representation
should be simple enough that can be
encoded in the mixing integer
programming problem
and that's the reason why i came up
recently with a new algorithm called
parc for piecewise define regression and
classification here the dia it's a quite
a general algorithm
that can be used for hybrid model
identification
so say you have a feature vector z
which contains uh numeric and
categorical
features that have been encoded
in zero one and that you have a target
vector
v that has continuous uh components
numerical components
as well as categorical components so
certain
um targets can take a finite number only
a finite number of values
now what is the idea of the algorithm
the idea is to
take the data set and iteratively
cluster the data set
into k sets where k is the number of
partitions that you want to get
in the end and say you have cluster the
data subdivided the data into clusters
then in each cluster you can fit a
linear function using read regression
as well as fit a classifier
using soft max regression or logistic
regression in case you have binary
targets and then you can fit
a piecewise linear separation function
and
in particular i'm using soft max
regression to fit
the parameters omega and gamma of the
function
okay whose max the argument of the max
of this function
is the index of the region where
the the vector belongs to
and then you keep doing this uh
iteratively by reassigning
um points to clusters
based on a weighted criterion that
contains both
quality of feed and piecewise linear
separability
of the of the cluster and
you can show that the algorithm converts
to a local minimum because it's a block
coordinates
coordinate descent algorithm now in case
you want to use the algorithm to fit
hybrid models uh the future vectors in
state space hybrid models the future
vector will be the collection of
continuous states and inputs and
logic states and inputs and the target
vector would be the next
state continuous and logic state as well
as the current
continuous and binary output
so let's say you have collected a
certain number of these
samples feature target vector samples
then the algorithm will use
read regression to fit the
function leading to the continuous
states and continuous outputs
use logistic regression to fit the
binary
functions for the logic states xl k plus
and the logic outputs as well as a
piecewise a fine partition
obtained from a piecewise linear
separation function fit by using softmax
regression
where the regions are given where each
of the hyperplanes dominates so for
example region i
is a region where the hyperplane
and the hyperplane dominates over the
the remaining hyperplanes
and if you have binary states and
outputs
those regions gets further
subpartitioned
by the the result of the logistic
regression you get
to fit the binary classifiers now let's
see how this works
on a simple example say you generate
data of non-linear function
in this case the 1000 samples from
in a linear function say we use 80 so
800 samples for
training and look for a piecewise
defined partition
over 10 regions that's what you will get
so the algorithm
will automatically generate 10
partitions and in each one of them there
would be a linear
function approximating the given the
linear one so let's see how the park
algorithm would work
to design data-driven hybrid mpc
controller
so i consider this toy example where i
have a mass
moving on a line and there are two
bumpers so the mass
is pushed by force it can only take
values
plus a bar or minus f bar or zero
and when the mass is moving the bumpers
there is
a transfer heat transfer between the
bumper and the mass
so here there is a hot bumper and here
there is a cold
bumper and you have a categorical output
which is the related to the temperature
of the of the mass there are three areas
green
yellow and and red based on the
temperature
and you don't know you don't know
exactly what are those bound you only
know the colors
let's see so i simulated the system for
2000 seconds and collecting 4 000
training samples here the future vector
is the current position
velocity and temperature of the mass as
well as the input
f that is applied to to the mass
and the target that you want to
reconstruct using a piecewise
a fine mapping is the next output
position y k plus one velocity and
temperature as well as the color
which is a categorical target so let's
say we use six
regions this is what you will get so by
running
the algorithm you will get
a discrete time piecewise 5 models
that if you simulate it in open loop
over 500 seconds of new
test data you will see that the fit is
actually
quite quite good resembles a lot what
you had
simulated in open loop with a continuous
time
model with with impacts so we can use
the model to design an npc
controller say here the goal is to
track the yellow color so you would like
to have the categorical output
in the yellow label and also with some
penalty on the force
that you the impulsive force that you
are using
until you if you close the loop you can
recast this as an milp
problem and if you cause close the loop
you will get
that um the controller generates
impulsive force command that push the
mass
touching in this case the hot bumper
so the controller is able to to solve
the color tracking problem that i have
posed
so let's see now how machine learning
can help us reducing the
online computations associated with the
mpc control though
we know that explicit mpc can help us in
this
if the mpc problem can be pre-solved
offline using multi-parametric
programming
so that the resulting control loop can
be rewritten as a piecewise defined
function however the approach is limited
usually we need two small
problems um usually problem with the
small number of constraints so to limit
the number of regions that you get
in the solution if you're okay with
approximate explicit
controllers then you can follow this
simple approach
of generating samples of the
parameter vector x so samples of the
state and reference
signals for each of them solve the
corresponding mpc problem
offline and then fit a function that
approximates the optimizer function and
in order to do this you can use
neural networks or you can use piecewise
affine regression
as we've seen before or nonlinear system
don't see
nonlinear system identification so any
method any functional regression method
can be used in principle
of course you have to be careful that
the original properties of the mpc
controller may be
destroyed by the approximation so that
you
eventually have to later verify a
posteriori whether
the approximation is still stabilizing
and is still providing feasible
solutions now you can also use the
semi-explicit approach
and it is the following in case for
example of linear mpc problems
you can learn attempt to learn offline
the optimal active set
as a function of the state x say the
reference signal
and then online use this to worm start
the qp solver
so get a guess of the optimal set which
is a binary classification problem
because either
constraint is active or or not
okay this could be as proved in this
paper it can
be quite an effective worm starting
method
where you can in case of mixed integer
quadratic programming
within your nonlinear mixing integer
problems that arise from hybrid npc
you can attempt learning the optimal
combination of binary
variables as we have proposed with the
mass in this paper where the idea is
that
offline you learn the binary variables
and
online you fix the binary variables as
at the value given by the classifier
and then instead of solving them iqp or
milp you just solve the qp and the p
since all the remaining variables are
just real variables we've used this in a
micro grid optimization problem
uh together with the bpi and the viral
scooter
and here we have generated 15 about 15
000
solutions of the hybrid mpc problem
and then fit
a classifier using either decision tree
or random force and compare also these
binary variable approximation
you've done offline with the rule-based
controller so what you can show is that
while the milp solution takes
something in the order of a few seconds
if you use the approximation then you
can reduce
online cpu time by almost um
around 96 98
and without a loss too much loss of
performance in particular the random
forest the solution
gave the best results you you
get more or less the same cost
some loss also the solution you get is
most of the time
uh feasible so you don't have to correct
the solution
opposite very to enforce feasibility and
so it can be a valuable substitute for
for the mi online milp solver
and in this case the rule based
controller still works
quite well with a fraction of the
of the computational load because it's
just a rule a set of rules
to compute the control action but the
big difference
is that the root based controller
requires a deep domain specific
knowledge now another
approach that we can take to reduce
in this case the number of variables in
the mpc problem
so to reduce online complexity
is based on this idea so let's let's
consider linear
mpc problems the online optimization can
be recast
as a constraint least squares problem
where the vector to optimize
is the sequence of inputs and states and
the problem depends on the current state
reference and possibly other
varying signals now what is the
standard way of reducing the number of
variables is condensing so to eliminate
the states and only keep the inputs as
optimization variables
in particular if this is an lti
problem this can be quite an effective
method because you can
recompute the matrix if the condense
matrix is offline
however standard condensing in case you
have
uh unstable system but even if the
system is stable is not numerically very
robust so alkyl pre-stabilization has
been proposed to alleviate this
so the idea is to design an lq time
varying lq
control low and then instead of
optimizing inputs
you optimize the deviations from the
lq control low and in this recent paper
here with the john attaching
we have shown that actually an even more
robust approach
is to simply do a qr factorization of
the constraint metrics
and then use it as optim new
optimization variables
this bar this vector s here which is
obtained
is related to the original variables z
by the q uh part of the q factor of the
factorization
so you end up with a number of variables
which is still
the length of the prediction horizon
times the number of inputs
but you get a lot in terms of the
condition number
of the haitian of the
reduced order constraint squares problem
compare not only compared to the
standard condensing especially in the
case
of unstable system but also compared to
lq pre-stabilization
now if you want to reduce the number of
variables even further
one usual way is to introduce a control
horizon
so to limit the number of degrees of
freedom by assuming that the input
becomes constant after a certain time
over the prediction horizon
and here we have proposed a different
approach which is based on a principle
component analysis
so that is the following let's say we
have solved the
constraint b squares problem after doing
the qr
actualization and collect certain number
optimizers sk star for a number
m of samples you can compute a singular
value decomposition of the metrics
obtained by collecting
all the samples after removing their
mean
and then the first m columns of matrix v
would be a basis for a change of
variables
so vector v has the
number m of components you have chosen
to keep
as free variables and the s function
your
original optimization vector will be
expressed in terms of these newbies
you clearly have a complexity versus
solution quality trade-off
so what you see in this picture here we
have an mpc problem with the horizon 20
steps
if we start decreasing m
say 1918 and so on you will observe that
the solution gets
more and more suboptimal and the error
will start growing
and in this case all values of m provide
a feasible feasible solution
now you can do more since the basis is
obtained
as an average of uh on
m different values of theta and we have
introduced
uh an algorithm which is a combination
of uh say k-means
and svd that we call ksvd to get
a basis sorry not just one basis but a
set
of k bases each one
active for a certain set of
parameter vectors theta so
the idea is to alternate svd
and clustering and the algorithm you can
show it converge
to um local minimum
of an optimal uh partition of the
data points into clusters where in each
cluster
you get the basis that gives the the
list um
square approximation error and once you
have created the
clusters you can use a k neural one tool
classifiers to create a non-linear
partition
of the parameter space so let's see an
example here
we have a standard benchmark problem of
controlling
a continuously steer tank reactor
we use linear parameter wiring npc to
control it
so where the model is linear it is
obtained by linearizing
the nonlinear model at each sample step
and then we collect
10 000 samples that we used to run the
ksvd algorithm with k equal 10
to get 10 different bases and what you
see here is the non-linear partition
of the parameter space obtained by the
neural classifiers and the black dots
are
the points visited during a closed loop
simulation so here we compare
the cost obtained by using
23 optimization variables which is equal
to the prediction horizon
in the prediction and then reduce the
number
of variables so say to 10 and 4 the cost
closed loop cost remains roughly the
same
when we reduce to 3 you you see a slight
deterioration of the cost
if we reduce further to only 2 degrees
of freedom so 2 3 moves
in the prediction arise and then the
cost actually change quite dramatically
and you see here in the plots the the
purple one
is the closed loop trajectories that you
get with n equal to
so this may suggest that you should use
three degrees of freedom so
a control horizon of three steps however
if you run the svd algorithm starting
from
the formulation with three free
variables and then use
an svd to reduce the number of variables
to two
you get a much better cost if you use
ksvd you get
even better costs actually very close to
the one
that you get with the exact formulation
practically the same that you get with
the
exact solution based on three three
variables
now let's see how machine learning can
help us calibrating npc controllers
so the mpc problem depends on several
hyper parameters means the weights
and prediction and control horizons
number of free variables sample time a
lot of
choices you have to make or if you want
to automate
the calibration process how how can we
do this
so one approach is to formulate a
performance index
capturing closure performance for
example a weighted sum
of the tracking errors over a certain
simulation or experiment length
and then formulate an optimization
problem where you want to minimize
the closure performance index with
respect to the
mpc hybrid parameters there are very
good global optimization
algorithms derivative free black box
optimization algorithm that you can use
here
i'm listing some of the most used ones
and i recently proposed a new method
called gliese
which is belongs to the class of
surrogate
methods where the idea is to fit um
samples of the functions that you have
collected so far
to fit a function to that so to solve
the function approximation problem
and uh get a surrogate of the function
unknown function that you're trying to
optimize
and based on that function suggest new
points to
to test this algebra is available in
matlab and in python on
our web page you're welcome to download
the code so the idea here
is to say you want to solve a global
optimization problem minimize a function
which you can only sample subject to
also subject to constraints and fit
a surrogate this red curve here
using real basis functions so function
that
pass through the points and tries to
approximate the underlying unknown
function trying to minimize the blue one
so one could use directly the red
function
minimize that to get a new point however
this may
easily miss the global optimum of the
function because you are not exploring
the set of parameters x probably so
rather than and doing this we introduce
an exploration
function which is given by an inverse
distance
weighting function so it's a function
that is zero
at the points that you have already
sampled and grows
in in between so a combination of the
two functions the surrogate
and the expiration function is the
function that you minimize
subject to the given constraints you
have in order to get a new point
um x n plus one
for at which you uh sample the function
so for example you run simulation based
on the mpc parameter
combination given by the inspector and
so you keep
doing this recursively so get a new
point update the surrogate
and find the new point and and so on and
here you see some
comparison of on standard
black box non-linear global optimization
problems
uh comparing the behavior of gliese and
the behavior of bayesian optimization
which is
one of the most used method for solving
this type of black box
global optimization problems the the
results are
comparable in terms of quality
of solution that you get after a certain
number of queries
to the function uh one good property of
of gliese is that it is computationally
lighter
than bayesian optimization but it is
also more flexible in terms of
the possibility to introduce constraints
extra constraints and
the flexibility you have in constructing
the exploration function
now let's see an example of application
of the the gliese
autotuning approach to an mpc problem
so this is a problem of controlling an
inverted pendulum on a cart
and we want to choose 14 different
parameters of the mpc
controller meaning the sample time the
weights
the cost function the prediction control
horizon even the covariance metrics in
the kalman filter
as well as the tolerances of the qp
solver
as a close loop performance index we
consider
a term related to tracking as well as a
term related to
the um inclination
of the of the mass independent during
the simulation that we want to penalize
we consider two platforms um pc and the
raspberry pi
and this is what you will get after
running the
global optimizer to auto tune the
controller
for the tools settings so for the
desktop pc setting you get an optimal
sample time of six
seconds and a certain combination of mpc
parameters
the raspberry pi you will get sample
time optimal sample time of 2
milliseconds and slightly different set
of parameters
now these approaches pros and cons the
pro is that it's totally
automatic um a con is that you need to
quantify
the function f that you want to minimize
and this
sometimes can be hard so for example
sometimes the
calibrator has some quality qualitative
assessments so it's hard to capture
these information these requirements in
a in a function
and often you get multiple objectives
that you want to minimize
and how to blend these different
objectives in a single
scalar function to minimize is not
obvious
so for this reason we have introduced a
new approach called
glissp for active preference learning so
global optimization
using preferences that we have described
in this paper here with diane piga
where that is the following say we don't
know the function not only we don't know
the function but we cannot even measure
the function
the only thing that we can know about
the function
is whether it's given two points
x1 x2 whether the function
is lower in a point x1 then x2 or
is the same or less or it's higher so we
are asking
the calibrator to express some
preferences
whether a value of a combination of
parameters
is better or worse or as good as
another combination and based on this
preference information we construct the
surrogate
of the function f okay that we use to
drive the search for the global solution
so in this case of the problem is to
find vector
x star such that it
is always better or the same as any
other vector
x that you can that you can try
so we have used this to um solve
semi automatic calibration problem for
npc
actually the results of this work are
presented by menja
zhu at this conference on wednesday
so here the latent function that we want
to optimize
is the calibrator's score
unconscious score that it has by
observing experiments
and the algorithm will propose a new
combination of
parameters to test and we'll ask the
calibrator where this new combination is
uh better or worse or the same as the
the current best one
and the idea is that based on the new
preference expressed by the calibrator
the surrogate is updated and together
with an exploration function
uh a global optimization problem is
solved
to find the new vector x and plus 2
to be tested by the calibrator and so on
so here you see an example of
application of this
that makja did by
being here the calibrator trying to tune
an mpc controller for solving a simple
autonomous driving problem so we want to
design an mpc controller
that generates vehicle speed and
steering angle so
to track a certain path on the on the
road
and here the objectives are multiple and
rather vague meaning
avoid obstacles in an optimal way have a
pleasant drive
and keep the cpu time required by npc
small and others
so these are not um easily quantified
probably you could quantify each of them
but you wouldn't know how to
to blend them in a single cos function
what we want to tune here is the
sampling time the prediction and control
horizon
and the weights on the input increments
terms of velocity and steering angle
so the algorithms start by randomly
sampling the
the space of uh of parameters and then
start asking preferences to
to the um calibrator and
for example is this closed loop result
better than this
one on the right the answer can be yes
it's better or no i like more the right
or they are the same
this information is used to update
the surrogate function
and in this case after 50 experiments
which means
49 queries the closed loop result will
look
good and then you can stop the algorithm
and the optimal combination here would
sample time of 85 milliseconds
friction horizon of 16 um
control horizon of 5 and this weighs on
delta v
and delta steering angle and we are
currently
extending these approach tools to handle
unknown constraints
for example certain combination of
parameters may lead to closed loop
instability
you want the calibrator to mark them as
infeasible and keep these feasibility or
infeasibility information
into account when constructing the
acquisition function
so to conclude my presentation um
if you look back in in history of of
control
numerical methods have always
the way of designing control system
think about linear algebra how it has
changed the approach from the frequency
domain to
state space domain with old placement
and kalman filtering lqr or think of
lmi's
how they impacted the way of designing
linear and robust controllers and how
embedded optimization has
have had an impact in control de
particular in other predictive control
techniques now most likely is the turn
on machine learning
so this new set of well-developed and
growing steadily growing quickly growing
set of techniques
that we can learn from and
[Music]
use them to to devise new ways of
designing
control systems what i covered in this
talk
is the use of some machine learning
techniques to improve the way we can
design mpc controllers
in particular to get non-linear or
hybrid
prediction models from data to reduce
the online computations
associated with mpc and also to
automatically or
semi automatically calibrate
mpc controllers by looking at closed
loop experiments
but of course the spectrum of
possibilities
that you have with the machine learning
tools
is is very wide and this has opened
lots really lots of research
opportunities and also
lots of good practices that you can put
in place in order
to design and deploy mpc controllers
and this concludes my talk thanks a lot
for watching this presentation