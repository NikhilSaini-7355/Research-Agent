Sitemap
Open in app
Medium Logo
Get app
Write
Search
# Model Predictive Control for Dummies
[](https://adityang5.medium.com/?source=post_page---byline--904c0f7e184d---------------------------------------)
Aditya NG
4 min read
Jun 9, 2024
Listen
Share
Controlling a robot, whether in simulation or real life, often requires a robust control strategy. Traditional approaches like PID and bang-bang control have their place, but they come with limitations such as lack of foresight and poor handling of constraints. Enter Model Predictive Control (MPC), a method that brings a sophisticated, forward-looking approach to control problems.
MPC in action. Blue is the Planner’s desired trajectory. Green is the path that the MPC’s was able to fit
## Understanding Model Predictive Control
MPC is a control strategy that predicts the future behavior of a system and optimizes control actions to achieve the best performance. Unlike naive approaches, MPC considers a model of the system, future states, and constraints to make more informed decisions.
### **Advantages of MPC:**
- **Predictive Capability:** MPC uses a model to predict future states, allowing it to anticipate changes and adjust accordingly.
- **Constraint Handling:** MPC can naturally incorporate constraints on inputs and outputs, ensuring safe and feasible operation.
- **Optimal Control:** By solving an optimization problem at each step, MPC finds the best control action to minimize a cost function, leading to optimal performance.
Implementing MPC might seem intimidating, but with the right approach, it can be quite manageable. Let’s walk through an MPC implementation in Python, leveraging the code from the general-navigation repository.
## Implementing MPC in Python
To illustrate how to implement MPC, we’ll follow a structured approach, using the MPC implementation from the general-navigation project as our reference. The main steps involve defining a desired trajectory, selecting a vehicle model, formulating a cost function, choosing an optimizer, and integrating everything into a feedback loop.
### Step 1: Desired Trajectory
We start by defining a desired trajectory that our model aims to follow. For this, we use the General Navigation Model (GNM) from Berkeley AI Research. GNM provides a robust framework for trajectory generation in autonomous systems.
### Step 2: Vehicle Model
The Bicycle Model of a vehicle
We use the bicycle model to represent our vehicle’s dynamics. The bicycle model is a simplified representation of a car, capturing the essential dynamics required for trajectory planning.
```
steering_ratio = 13.4 # steering wheel angle / wheel angle
wheel_base = 2.6 # meters
def bicycle_model(x, u):
"""
x <- (X, Y, theta, velocity)
u <- steering angle
"""
delta = np.radians(u) / steering_ratio
x_next = np.zeros(4)
x_next = x + (velocity / wheel_base * np.tan(delta) * dt) # theta
x_next = x + (velocity * np.cos(x_next) * dt) # x pos
x_next = x + (velocity * np.sin(x_next) * dt) # y pos
x_next = velocity
return x_next
```
## Get Aditya NG’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster
### Step 3: Cost Function
The cost function drives the optimization process by quantifying the error between the desired and actual trajectory. It also includes a term for penalizing aggressive steering, which can be tuned using the inverse\_agressiveness parameter.
```
def cost(u, x, x_des):
"""
u[i] <- steering angle for step i
x <- (X, Y, theta, velocity) initial state
x_des[i] <- (X, Y, theta, velocity) desired state at step i
"""
cost_val = 0.0
for i in range(horizon):
x = bicycle_model(x, u[i])
cost_val += ((x - x_des[i, 0]) ** 2 + (x - x_des[i, 1]) ** 2 + K * u[i] ** 2)
return cost_val
```
**Insights on Cost Function:**
- **Trajectory Matching:** Ensures that the actual trajectory closely follows the desired one by minimizing the positional error.
- **Aggressiveness Penalty:** Penalizes unnecessary steering to maintain smooth control. You can tweak the `inverse_agressiveness` parameter to balance between trajectory accuracy and steering smoothness.
### Step 4: Optimizing the Cost Function
We use `scipy.optimize.minimize` with the Sequential Least Squares Quadratic Programming (SLSQP) method to minimize the cost function. SLSQP is a powerful optimizer for constrained optimization problems, ensuring that our control inputs respect the system's constraints.
```
# initial state and input sequence
x0 = np.array(
trajectory_interp[0, 0],\
trajectory_interp[0, 1],\
current_steering,\
velocity,\
# Incorporate current trajectory
u0 = steering_history.copy()
# bounds on the steering angle
bounds = [(-max_steer, max_steer) for _ in range(horizon)]
res = scipy.optimize.minimize(
cost,
u0,
args=(x0, trajectory_interp.copy()),
method="SLSQP",
bounds=bounds,
options=dict(maxiter=100),
```
### Putting It All Together
Incorporating all these components, we run our MPC controller in the CARLA simulator, guided by the GNM model. The visualization shows the blue trajectory produced by the model and the green trajectory optimized by our MPC controller.
GNMs in action with MPC in the Carla Simulator
If you want to try it out yourself, check out my repository on GitHub!
## Citations
- Dhruv Shah, Ajay Sridhar, et al. “General Navigation Models,” Berkeley AI Research. Link
- “Sequential Least Squares Programming (SLSQP),” SciPy Documentation. Link
- “General Navigation Python Module”, Aditya NG. Link
- “What is Model Predictive Control”, Mathworks. Link
- “Kinematic Bicycle Model”, Mario Theers. Link
Model Predictive Control
General Naigation
Control System
[](https://adityang5.medium.com/?source=post_page---post_author_info--904c0f7e184d---------------------------------------)
[](https://adityang5.medium.com/?source=post_page---post_author_info--904c0f7e184d---------------------------------------)
**Written by Aditya NG**
43 followers
· 3 following
Computer Vision and Autonomous Robotics Research
Help
Status
About
Careers
Press
Blog
Store
Privacy
Rules
Terms
Text to speech
reCAPTCHA
Recaptcha requires verification.
protected by **reCAPTCHA**