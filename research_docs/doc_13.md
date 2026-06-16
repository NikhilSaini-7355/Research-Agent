# Model predictive control technology demystified
### Model predictive control (MPC) is a well-established technology for advanced process control (APC) in many industrial applications like blending, mills, kilns, boilers and distillation columns. This article explains the challenges of traditional MPC implementation and introduces a new configuration-free MPC implementation concept.
MPC technology has the proven ability to provide control solutions using constraints, feed-forward, and feedback to handle multivariable processes with delays and processes with strong interactive loops. These types of control problems have successfully been handled in many industrial applications.
Advanced Process Control and Analytics\\
New tools revolutionize data analysis, reduce modeling effort
## MPC enabling optimization
Using model predictive control brings many benefits.
For example, there is less variation in process variables (PVs), which allows set points to be chosen that are closer to performance boundaries, which in turn leads to an increased throughput and a higher profit. MPC brings a structured approach to solutions that would otherwise consist of combinations of feed-forward and feedback with PID (proportional integral derivative) controllers, possibly with override functions.
Additional benefits of MPC are:
- Increases in process knowledge (estimation of hidden variables)
- Higher levels of automation, freeing operators to focus on more important tasks
- Extended scope of control strategy for optimization of, for example, specific energy consumption.
Optimization is an inherent capability in an MPC controller
Optimization is an inherent capability of MPC
## Make control problems “well behaved” with MPC technology
From a user perspective, the main components in an MPC are:
- The plant model
- An objective function
- A state estimator
- An algorithm for solving constrained optimization problems
The following actions take place on a cyclic basis and are repeated with equidistant intervals, of which the sampling time is chosen with respect to the time scale of the controlled process:
- The actual state of the process is estimated from current and past measurements and from the state at previous sample(s) using a state estimator. Kalman filters and moving horizon estimators are well established methods for this. The estimated state xˇ(k) is assumed to be an accurate approximation of the sometimes unmeasurable state in the true process. It is used as the starting point for the optimization in the next step.
- The plant model can be used to predict the future trajectories of the plant outputs for a given sequence/trajectory of future control signals. Optimization determines the future control signal such that the objective function is minimized. The optimization may also account for constraints on the process inputs and the process outputs.
- Finally, the first instance for each calculated future control signal is applied to the process.
It is worth noting that normally the objective function is a weighted sum of deviations in the plant outputs and in the control signal increments. There may also be linear terms for minimization or maximization of certain variables. Using the square form in the objective function serves to make the control problem “well behaved” .
Past and future trajectories in an MPC
## Configuration challenges of traditional MPC implementation
MPC has been utilized for process control within ABB for a long time, initially using third-party solutions from other vendors. Later, solutions were implemented using the ABB products **Predict & Control**, and **Expert Optimizer**. Typically MPC provides set points for the underlying cascaded PID controllers.
Common for these approaches has been that the MPC has been running on a separate server, which is not part of the DCS (distributed control system). Signal data is then normally exchanged with the DCS using OPC; measurements, consisting of PV and feed-forward (FF) variables, are sent to the MPC, and the MPC outputs, also called manipulated variables (MVs), are then sent to the DCS.
However, for these solutions to work, a number of additional signals need to be exchanged between the DCS and the MPC on the external server. These carry information, eg, about which level-1 PID controllers will accept a set point from the MPC and whether the output from the PID is saturated. It is also necessary to move data between the MPC and the operator displays. Further information that needs to be exchanged is the status of the MPC, where often a “heartbeat” signal is used to indicate that the external MPC is alive. All of this communication needs to be configured before the engineer has even started to deal with the control problem. This must also occur before deciding to add or remove signals from the MPC. There is no question that the threshold to use MPC has been substantial.
There has been a substantial threshold to use traditionally implemented MPC due to challenges with connectivity, safety locks and HMI settings
## Use cases
The typical use cases in the mining, minerals, cement, pulp and paper, oil and gas or marine sectors cover the vertical industries where ABB has a strong footprint.
Mining and minerals processing\\
Grinding and flotation - separation of valuable minerals from waste
Underground mining\\
Optimal mine ventilation with minimum power consumption
Terminals, stockyards at steel plants or mines\\
Stockyard Management
Cement production\\
Kilns, mills, alternative fuel management, material blending
Metals\\
Sintering and pelletizing process stability, quality and output
Aluminium\\
Improvement of thickness tolerances for a two-stand aluminium cold rolling mill
Pulp mills\\
Continuous digester of cellulose fiber or pulp
Paper mills\\
Wet End Control APC that stabilizes paper machine operations
Paper mills\\
Paper machine drives, winder, paper quality, sheet break performance, strength / weight virtual measurement
Industrial steam supply\\
Steam generation for industrial plants
Energy Industries\\
Distillation columns for crude oil separation, active feedback control of unstable wells, emission monitoring
Marine\\
Vessel fuel management
## New configuration-free MPC implementation concept
ABB has developed a new extension to its flagship Extended Automation System 800xA, leading to straightforward design and deployment of APC in ABB’s 800xA DCS: 800xA APC.
800xA APC cleanly splits the work related to modeling and control design from the more usual tasks of connectivity, safety locks, and HMI settings, which effectively happen in a configuration-free manner. The system also facilitates remote commissioning and application support. In addition there is a tool, the Model Builder, for modeling, controller tuning, and simulations.
System 800xA APC also offers a **migration path for Predict & Control (P&C) and Expert Optimizer controllers**.
With this new product the control engineer can now concentrate on the control problem, leaving all other issues to the platform.
System 800xA APC
## Benefits beyond the scope of the process
ABB continues to invest in MPC technology with the aim of increasing the value that the company’s control system delivers to its customers, across the entire ABB global footprint.
The optimization that is inherent to MPC brings not only financial benefits to ABB’s customers, but contributes to an ongoing drive to reduce emissions, and resource use, which delivers benefits beyond the scope of the process under consideration.
More process performance software solutions
- Submit your inquiry and we will contact you
- Quickly find an ABB channel partner
Find a channel partner
PRODUCTS
- Offerings A-Z
- Services
- Where to buy
INDUSTRY SOLUTIONS
- Channel partners
- Buildings and infrastructure
- Industrial automation
- Marine
- Oil & gas
- Power generation
INVESTORS
- Investor & shareholder resources
- Quarterly results & annual reports
- Corporate governance
- Calendar, events and publications
COMPANY
- News & media
- Who we are
- Innovation
- Careers
- Sustainability
- Supplying