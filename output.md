Skip to main content
Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain
the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in
Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles
and JavaScript.
An adaptive model predictive control approach for robust load frequency control under renewable energy disturbances
Download PDF
Download PDF
### Subjects
- Energy science and technology
- Engineering
- Mathematics and computing
## Abstract
This paper presents an Adaptive Model Predictive Control (AMPC) strategy for robust load–frequency control (LFC) in single-area and double-area power systems under load variations, parameter uncertainty, and renewable energy disturbances. The controller integrates online system identification using Recursive Least Squares (RLS) with a receding-horizon optimization framework to ensure real-time model adaptation and constraint-aware predictive regulation. Simulation results demonstrate that the proposed AMPC significantly improves transient and steady-state performance compared with conventional PI/PID controllers. In single-area systems, the AMPC achieves settling times of 0.5–1 s, compared with 30 s for PI, and eliminates overshoot while reducing undershoot from 4.5 × 10⁻³ to 1 × 10⁻³. Under dynamic and wind disturbances, peak-to-peak deviations are reduced to **≈ 0**, whereas PI exhibits deviations up to 26.5 × 10⁻³. In double-area systems, the AMPC reduces settling time from 20 to 40 s (PID) to 1–2 s and minimizes undershoot by up to an order of magnitude. Comparative studies further confirm the proposed AMPC’s superiority over Harmony Search (HS), Sine–Cosine Algorithm (SCA), Teaching–Learning-Based Optimization (TLBO)-optimized PID/PIDA controllers and the Marine Predator Algorithm (MPA)-based cascaded PIDA, establishing AMPC as an effective and scalable solution for low-inertia grids with high renewable penetration.
### Similar content being viewed by others
### Robust fractional-order adaptive cascaded strategy for mitigating load frequency deviations in renewable thermal hybrid systems
ArticleOpen access09 October 2025
### Optimized PID controller and model order reduction of reheated turbine for load frequency control using teaching learning-based optimization
ArticleOpen access30 January 2025
### Cascaded adaptive model predictive and PID control for integrated LFC–AVR enhancement
ArticleOpen access18 April 2026
## Introduction
The modern electrical power system is one of the most complex and critical infrastructures ever developed, serving as the backbone of industrial, commercial, and residential activities worldwide. Its primary objective is to ensure a continuous and high-quality supply of electrical energy to consumers. A fundamental indicator of this quality is the stability of the system’s operating frequency. In any interconnected Alternating Current (AC) power grid, frequency serves as a global indicator of the real-time balance between active power generation and consumption. Maintaining this frequency close to its nominal value is essential, as significant deviations can degrade the performance of sensitive equipment, trigger protective relays leading to load shedding, or even cause cascading failures that result in widespread blackouts1."), 2."). The core mechanism responsible for maintaining this balance is the Load Frequency Control (LFC) system. LFC has two main objectives: first, to minimize transient frequency deviations and restore nominal frequency in a stable and timely manner after load or generation disturbances; and second, in interconnected systems, to maintain scheduled power exchanges between control areas. Each area continuously calculates its Area Control Error (ACE), a signal combining frequency deviation and tie-line power deviation. The LFC system then issues corrective control signals to participating generators to drive the ACE toward zero, thereby restoring both frequency and power exchange to their scheduled values2."), 3."), 4."). Traditionally, power grids were dominated by large synchronous generators (thermal and hydro), whose substantial rotational inertia naturally buffered frequency fluctuations. However, the global transition toward de-carbonization has led to the large-scale integration of Renewable Energy Sources (RES) such as wind and solar photovoltaics. These sources, typically interfaced through power electronic converters, lack inherent inertia, thereby reducing overall system stability and making grids more susceptible to frequency excursions. Moreover, the stochastic and intermittent behavior of RES introduces additional uncertainty, compounded by emerging dynamic load patterns—such as those caused by electric vehicle charging—and the complexities of deregulated electricity markets5."), 6, 344–353 (2009)."). Recent studies have emphasized the importance of considering wind-penetration uncertainty in LFC design7, 2004–2023 (2024)."). demonstrates the worst-case of wind-penetration modeling significantly enhances robustness and damping performance in multi-area hybrid systems. Conventional Proportional–Integral (PI) and Proportional–Integral–Derivative (PID) controllers have long been the standard approach for LFC due to their simplicity, ease of implementation, and low computational cost. However, as these controllers are designed based on linearized system models around specific operating points, their performance deteriorates under large disturbances or varying conditions due to nonlinearities and parameter uncertainties. In modern low-inertia grids, the fixed-gain nature of these controllers often results in large overshoots, slow settling times, and poor disturbance rejection8, 1135–1141 (2010)."). Disturbance-observer (DOB) techniques have also been introduced to improve frequency regulation under uncertainties and communication delays9."). achieves faster disturbance rejection and improved robustness compared to classical PI-based methods. To overcome these challenges, researchers have explored advanced and intelligent control paradigms. Notable approaches include Fuzzy Logic Controllers (FLC) and Artificial Neural Networks (ANN), which handle nonlinearities without precise mathematical modeling, and robust control methods such as Sliding Mode Control (SMC) and H-infinity (H∞) control, which ensure stability across uncertainties. More recently, Fractional-Order PID (FOPID) controllers have gained attention for their ability to fine-tune dynamic responses using fractional calculus, achieving greater robustness and flexibility than traditional controllers10, 1–24. (2018)."), 11."), 12, 346–357 (2005)."), 13."), 14."). The increasing complexity of these advanced controllers makes manual tuning impractical, motivating the integration of metaheuristic optimization algorithms for optimal LFC design. These population-based algorithms efficiently navigate complex, non-convex search spaces to find near-global optimal controller parameters that minimize predefined performance indices, such as time-domain error criteria. Over time, optimization techniques have evolved from classical methods like Genetic Algorithms (GA) and Particle Swarm Optimization (PSO) to more recent and powerful approaches, including the Grey Wolf Optimizer (GWO), Whale Optimization Algorithm (WOA), Ant Lion Optimizer (ALO), and Slap Swarm Algorithm (SSA), which have demonstrated excellent performance in designing high-quality LFC schemes for multi-area, multi-source power systems15, 2416–2424 (2018)."), 16."), 17."), 18, 438–457 (2010)."), 19, 2132–2141 (2014)."), 20."), 21, 1188–1200 (2018).").
### Research gap and contribution
Traditional LFC strategies based on fixed-gain PI or PID controllers are inadequate for modern power systems characterized by high renewable penetration and dynamic operating conditions. These conventional methods fail to adapt to system nonlinearities and time-varying parameters, resulting in degraded frequency response under disturbances or changing operating points. Although several intelligent and robust control techniques have been proposed, most lack real-time adaptability and model-based predictive capability. The present study addresses this gap by developing an Adaptive Model Predictive Controller (AMPC) that continuously updates its internal model using online RLS-based system identification. This adaptation enables precise prediction and control of system dynamics, maintaining frequency stability even under significant load variations and renewable-induced disturbances. Thus, the proposed AMPC bridges the gap between robustness, adaptability, and predictive control in modern interconnected grids.
## Proposed adaptive model predictive controller (AMPC)
### Overview and motivation
In many practical applications, system parameters vary over time due to nonlinearities, load changes, or environmental conditions. A conventional Model Predictive Controller (MPC) assumes a fixed linear model, which can lead to poor control performance when the real plant deviates from this model.
The proposed Adaptive Model Predictive Controller (AMPC) is designed to overcome this limitation by continuously updating the prediction model according to the current operating conditions. This allows the controller to maintain accurate predictions, satisfy system constraints, and achieve robust performance under parameter variations22."), 23.").
### Time-varying state-space model
The AMPC framework uses a discrete-time, linear time-varying (LTV) state-space representation of the plant as follows in Eqs. ( 1)&( 2)24, Zürich, Switzerland, pp. 1–6. (2013)."):
$$\\:\\text{x}\\left(\\text{k}+1\\right)={\\text{A}}\_{\\text{k}}\\text{}\\text{x}\\left(\\text{k}\\right)+{\\text{B}}\_{\\text{k}}\\text{}\\text{u}\\left(\\text{k}\\right)+{\\text{E}}\_{\\text{k}}\\text{}\\text{d}\\left(\\text{k}\\right)\\:\\text{}$$
(1)
$$\\:\\text{y}\\left(\\text{k}\\right)={\\text{C}}\_{\\text{k}}\\text{}\\text{x}\\left(\\text{k}\\right)$$
(2)
where
- \\(\\:x\\left(k\\right)\\:\\)is the state vector,
- \\(\\:u\\left(k\\right)\\:\\)is the control input,
- \\(\\:d\\left(k\\right)\\:\\)represents measurable or unmeasurable disturbances,
- \\(\\:y\\left(k\\right)\\:\\)is the plant output.
- The matrices \\(\\:{A}\_{k}\\text{},{B}\_{k}\\text{},{C}\_{k}\\text{},{E}\_{k}\\)​ are updated at each sampling instant to reflect the current dynamics of the plant.
The model parameters are identified online using recursive estimation techniques (e.g., Recursive Least Squares or Extended Kalman Filter) to capture time-varying system behavior25.").
Only the latest model \\(\\:\\left({A}\_{k}\\text{},{B}\_{k}\\text{},{C}\_{k\\text{}}\\right)\\:\\)is used during the current prediction horizon, following the receding-horizon principle of MPC.
### Online RLS-based system identification
To enable continuous adaptation of the predictive model, the plant parameters are identified online using the Recursive Least Squares (RLS) algorithm. The RLS estimator updates a parameter vector \\(\\:\\theta\\:\\left(k\\right)\\) that represents the dominant coefficients of the governor–turbine–generator subsystem. The algorithm follows the standard recursive update Eqs. ( 3),( 4),(5)&(6)24, Zürich, Switzerland, pp. 1–6. (2013)."), 25."):
$$\\:\\text{e}\\left(\\text{k}\\right)=\\text{y}\\left(\\text{k}\\right)-{{\\upvarphi\\:}}^{\\text{T}}\\left(\\text{k}\\right){\\uptheta\\:}(\\text{k}-1)$$
(3)
$$\\:\\text{K}\\left(\\text{k}\\right)=\\frac{\\text{P}\\left(\\text{k}-1\\right){\\upvarphi\\:}\\left(\\text{k}\\right)}{{\\uplambda\\:}+{{\\upvarphi\\:}}^{\\text{T}}\\:\\left(\\text{k}\\right)\\text{P}\\left(\\text{k}-1\\right){\\upvarphi\\:}\\left(\\text{k}\\right)}\\text{}$$
(4)
$$\\:{\\uptheta\\:}\\left(\\text{k}\\right)={\\uptheta\\:}(\\text{k}-1)+\\text{K}\\left(\\text{k}\\right)\\text{e}\\left(\\text{k}\\right)$$
(5)
$$\\:\\text{P}\\left(\\text{k}\\right)=\\frac{1}{{\\uplambda\\:}}\\text{}\\left\[\\text{P}\\right(\\text{k}-1)-\\text{K}\\left(\\text{k}\\right){{\\upvarphi\\:}}^{\\text{T}}(\\text{k}\\left)\\text{P}\\right(\\text{k}-1\\left)\\right\]$$
(6)
The forgetting factor \\(\\:\\lambda\\:\\) typically (\\(\\:0.98\\le\\:\\lambda\\:\\le\\:1\\)) determines how fast the estimator tracks time-varying parameters. The identified parameter vector is mapped to the time-varying state-space matrices (\\(\\:A\\left(k\\right),B\\left(k\\right),C\\left(k\\right)\\)), which are updated at each sampling instant to provide the AMPC with an accurate prediction model25."). Parameter bounding and covariance resetting are applied to enhance robustness under noise and sudden variations25.").
### Nominal deviation form
For constraint handling, the plant model is written in deviation form with respect to a nominal operating point\\(\\:({x}\_{0}\\text{},{u}\_{0}\\text{},{y}\_{0}\\text{})\\) as in Eqs. ( 7)&( 8) :
$$\\:{\\Delta\\:}\\text{x}(\\text{k}+1)={\\text{A}}\_{\\text{k}}\\text{}{\\Delta\\:}\\text{x}\\left(\\text{k}\\right)+{\\text{B}}\_{\\text{k}}\\text{}{\\Delta\\:}\\text{u}\\left(\\text{k}\\right)$$
(7)
$$\\:{\\Delta\\:}\\text{y}\\left(\\text{k}\\right)={\\text{C}}\_{\\text{k}}\\text{}{\\Delta\\:}\\text{x}\\left(\\text{k}\\right)$$
(8)
Where
$$\\:{\\Delta\\:}\\text{x}\\left(\\text{k}\\right)=\\text{x}\\left(\\text{k}\\right)-{\\text{x}}\_{0}\\text{},\\:\\varDelta\\:u\\left(k\\right)=u\\left(k\\right)-{u}\_{0}\\:,\\:\\text{a}\\text{n}\\text{d}\\:\\varDelta\\:y\\left(k\\right)=y\\left(k\\right)-{y}\_{0}.$$
This formulation simplifies the control optimization problem and ensures that the controller reacts only to deviations from nominal conditions24, Zürich, Switzerland, pp. 1–6. (2013).").
### Receding-horizon optimization
At each sampling instant k, the AMPC computes a control sequence that minimizes a finite-horizon cost function as in Eq. ( 9):
$$\\:\\text{J}=\\sum\\limits\_{\\text{i}=1}^{\\text{N}\\text{p}}\\parallel\\:\\text{y}\\left(\\text{k}+\\text{i}\\right)-\\text{r}\\left(\\text{k}+\\text{i}\\right){\\parallel\\:}\_{\\text{Q}}^{2}\\text{}\\text{}+\\sum\\limits\_{\\text{i}=0}^{\\text{N}\\text{c}-1}\\parallel\\:{\\Delta\\:}\\text{u}\\left(\\text{k}+\\text{i}\\right){\\parallel\\:}\_{\\text{R}}^{2}\\text{}$$
(9)
where \\(\\:{N}\_{p}\\)​ is the prediction horizon, \\(\\:{N}\_{c}\\)​ is the control horizon,
\\(\\:Q\\) and \\(\\:R\\) are weighting matrices, and \\(\\:r\\left(k\\right)\\) is the reference signal.
The optimization is subject to the following constraints such as:
$$\\:{\\text{u}}\_{min}\\:\\text{}\\le\\:\\text{u}\\left(\\text{k}+\\text{i}\\right)\\le\\:{\\text{u}}\_{max}\\:\\text{},{\\Delta\\:}{\\text{u}}\_{min}\\text{}\\le\\:{\\Delta\\:}\\text{u}\\left(\\text{k}+\\text{i}\\right)\\le\\:{\\Delta\\:}{\\text{u}}\_{max}\\:\\text{},\\:{\\text{y}}\_{min}\\text{}\\le\\:\\text{y}(\\text{k}+\\text{i})\\le\\:{\\text{y}}\_{max}$$
Only the first control move \\(\\:u\\left(k\\right)\\) is applied, while the optimization problem is solved again at the next time step using the updated plant model (receding-horizon principle)22."), 26, 4969 (2024).").
### State estimation (time-varying kalman filter)
Since all system states are not directly measurable, the AMPC uses a linear time-varying Kalman filter (LTVKF) to estimate them23.").
At each time step k, the filter updates the state estimate \\(\\:x\\left(k\\right)\\) and the covariance matrix \\(\\:P\\left(k\\right)\\) according to the current plant model.
The key recursive equations are:
1. 1.
Prediction step as in Eq. ( 10)
$$\\:{\\text{P}}\_{\\text{k}\|\\text{k}-1}={\\text{A}}\_{\\text{k}}{\\text{P}}\_{\\text{k}-1\|\\text{k}-1}{\\text{A}}\_{\\text{k}}^{\\text{T}}+\\text{Q}$$
(10)
1. 2.
Kalman gains as in Eqs. ( 11)&( 12)
$$\\:{\\text{L}}\_{\\text{k}}=\\:\\left({\\text{A}}\_{\\text{k}}{\\text{P}}\_{\\text{k}\|\\text{k}-1}\\:{\\text{C}}\_{\\text{k}}^{\\text{T}}+\\:\\text{N}\\right){\\left({\\text{C}}\_{\\text{k}}{\\text{P}}\_{\\text{k}\|\\text{k}-1}\\:{\\text{C}}\_{\\text{k}}^{\\text{T}}+\\:\\text{R}\\right)}^{-1}\\:$$
(11)
$$\\:{\\text{M}}\_{\\text{k}}\\:=\\:{\\text{P}}\_{\\text{k}\|\\text{k}-1}\\:\\:\\:{\\text{C}}\_{\\text{k}}^{\\text{T}}\\:{\\left({\\text{C}}\_{\\text{k}}\\:{\\text{P}}\_{\\text{k}\|\\text{k}-1}\\:\\:{\\text{C}}\_{\\text{k}}^{\\text{T}}\\:+\\:\\text{R}\\right)}^{-1}\\:$$
(12)
1. 3.
Covariance update as in Eq. ( 13)
$$\\:{\\text{P}}\_{\\text{k}+1\|\\text{k}}\\:\\:=\\:{\\text{A}}\_{\\text{k}}\\:{\\text{P}}\_{\\text{k}\|\\text{k}-1}\\:{\\text{A}}\_{\\text{k}}^{\\text{T}}\\:-\\:{\\left({\\text{A}}\_{\\text{k}}\\:{\\text{P}}\_{\\text{k}\|\\text{k}-1}\\:{\\text{C}}\_{\\text{k}}^{\\text{T}}\\:+\\:\\text{N}\\right)\\text{L}}\_{\\text{k}}^{\\text{T}}\\:+\\:\\text{Q}$$
(13)
Here, \\(\\:Q,R\\) and \\(\\:N\\) are covariance matrices representing process noise, measurement noise, and cross-correlation, respectively.
When the model remains constant, the LTVKF converges to the traditional steady-state Kalman filter used in standard MPC23."), 25.").
### Stability and robustness
The AMPC maintains recursive feasibility and closed-loop stability by updating model parameters gradually and ensuring constraint satisfaction at all times.
Robustness is achieved by:
- Applying tightened constraint sets around the nominal trajectory24, Zürich, Switzerland, pp. 1–6. (2013).").
- Monitoring model parameter changes and triggering conservative fallback control if large deviations occur25.").
- Including terminal costs and stability constraints in the optimization problem26, 4969 (2024).").
This ensures stable operation even under significant system variations and modeling uncertainty.
### Implementation steps of the adaptive control strategy
The complete implementation of the proposed AMPC strategy follows the steps below:
1. 1.
**Initialization**:
- The initial state-space model \\(\\:({A}\_{0},\\:{B}\_{0},\\:{C}\_{0})\\), RLS parameters \\(\\:{\\theta\\:}\_{0}\\)​, forgetting factor \\(\\:\\lambda\\:\\), and the MPC horizons (\\(\\:{N}\_{p}\\),\\(\\:{N}\_{c}\\)) are initialized at \\(\\:k=0\\).
1. 2.
**State Measurement**:
- At each sampling instant, the measurable outputs (frequency deviation and tie-line power deviation) are fed back to the controller.
1. 3.
**Online Identification (RLS)**:
- The RLS estimator updates the parameter vector \\(\\:\\theta\\:\\left(k\\right)\\) and regenerates the time-varying state-space matrices \\(\\:(A\\left(k\\right),B\\left(k\\right),C\\left(k\\right))\\).
1. 4.
**State Estimation**:
- The updated model is used by the time-varying Kalman filter to obtain the estimated states \\(\\:x\\left(k\\right)\\).
1. 5.
**MPC Optimization**:
- Using the updated model, the AMPC solves the constrained finite-horizon optimization problem and computes the optimal control sequence.
1. 6.
**Control Application**:
- Only the first element of the optimal sequence is applied to the plant (“receding horizon”), ensuring closed-loop operation.
1. 7.
**Model Update**:
- Steps 2–6 repeat at every sampling instant, allowing the controller to adapt to parameter variations, disturbances, and nonlinear operating conditions.
This implementation ensures real-time adaptability and explains how the proposed controller differs fundamentally from conventional MPC and fixed-gain PI/PID strategies24, Zürich, Switzerland, pp. 1–6. (2013)."), 25.").
### AMPC tuning procedure
The prediction horizon \\(\\:Np\\)​, control horizon \\(\\:Nc\\), and weighting matrices \\(\\:Q\\) and \\(\\:R\\) were selected following a structured tuning methodology commonly adopted in AMPC practice23."). Several candidate combinations were evaluated under step and dynamic load disturbances. The final parameters were selected based on minimizing the ITAE index while ensuring a trade-off between overshoot, settling time, and control effort.
### AMPC integration with LFC
The Adaptive Model Predictive Controller (AMPC) was implemented and integrated into the overall system model using MATLAB/Simulink to ensure real-time regulation and robust tracking performance. The controller operates within a closed-loop configuration, where it continuously receives the measured plant outputs (\\(\\:mo\\)) and the reference signal (ref) from the system. These signals represent, respectively, the actual plant response and the desired operating point.
An external function block, labeled “Update Plant Model” is responsible for supplying the controller with the time-varying state-space matrices \\(\\:{A}\_{K}\\),\\(\\:{B}\_{k},\\:{C}\_{k}\\),\\(\\:{D}\_{k}\\) that define the current linearized plant dynamics. This mechanism allows the adaptive MPC to modify its internal prediction model at each control interval according to the instantaneous operating conditions of the plant. The updated model is then used by the controller to compute the optimal manipulated variable (\\(\\:mv\\)), which drives the system toward the desired reference while minimizing the defined cost function.
The computed control action (\\(\\:mv\\)) is fed back into the simulated plant subsystem, forming a feedback loop that dynamically compensates for disturbances and parameter variations. The disturbance input and frequency deviation output shown in the Simulink diagram enable continuous monitoring of system performance and facilitate adaptive correction in real time.
This configuration ensures that the Adaptive MPC can maintain system stability and high-quality transient performance even under nonlinear behavior or significant changes in plant characteristics. Compared to a conventional MPC scheme, the adaptive structure provides enhanced robustness and flexibility, as the prediction model is continuously updated to match the true plant dynamics, ensuring accurate state estimation and optimal control performance throughout the simulation.
## Model overview
### Single area power system
The single-area load–frequency control (LFC) loop is shown in Fig. 1. A disturbance in electrical demand (ΔP) enters at the generator–load interface. The measured frequency deviation is processed by a secondary controller whose command is combined with the primary droop contribution before driving the governor. The governor and turbine convert this command into mechanical power, which opposes the disturbance through the generator–load swing dynamics. A frequency-bias term closes the loop to achieve zero steady-state frequency error for step loads while coordinating area control28, 739–756 (2018).").
**Fig. 1**
The alternative text for this image may have been generated using AI.
Full size image
Model of single area system.
In the single-area load–frequency control (LFC) system, the PI controller shapes the closed-loop dynamics and eliminates the steady-state frequency error. The governor converts the control command into a valve position, subject to a first-order lag and practical constraints, while the turbine translates valve motion into mechanical power with an additional lag. A change in electrical load (ΔP) acts as an external disturbance that excites the control loop for disturbance-rejection evaluation. The generator and load dynamics are represented by the swing equation, which couple’s mechanical and electrical power to frequency. The droop characteristic provides a static proportional relationship between frequency and power, enabling power sharing among generating units. Finally, the frequency bias adjusts the measured frequency deviation (Δf) within the Automatic Generation Control (AGC) path to prevent the accumulation of area control errors and ensure stable system operation4."). The model transfer functions are given in Eqs. ( 14),( 15),( 16),( 17) & ( 18) :
$$\\:\\text{G}\\text{o}\\text{v}\\text{e}\\text{r}\\text{n}\\text{o}\\text{r}\\:\\text{m}\\text{o}\\text{d}\\text{e}\\text{l}\\:=\\frac{1}{\\left(1\\:+\\:\\text{S}\\text{T}\\text{g}\\right)\\:}$$
(14)
$$\\:\\text{T}\\text{u}\\text{r}\\text{b}\\text{i}\\text{n}\\text{e}\\:\\text{m}\\text{o}\\text{d}\\text{e}\\text{l}\\:=\\frac{1}{\\left(1\\:+\\:\\text{S}\\text{T}\\text{t}\\right)}\\:$$
(15)
$$\\:\\text{G}\\text{e}\\text{n}\\text{e}\\text{r}\\text{a}\\text{t}\\text{o}\\text{r}\\:\\text{a}\\text{n}\\text{d}\\:\\text{l}\\text{o}\\text{a}\\text{d}\\:\\text{m}\\text{o}\\text{d}\\text{e}\\text{l}\\:=\\frac{1}{\\text{M}\\text{S}\\:+\\:\\text{D}}$$
(16)
$$\\:\\text{D}\\text{r}\\text{o}\\text{o}\\text{p}\\:=\\frac{1}{\\text{R}}\\:$$
(17)
$$\\:\\text{G}\\text{o}\\text{v}\\text{e}\\text{r}\\text{n}\\text{o}\\text{r}\\:\\text{f}\\text{r}\\text{e}\\text{q}\\text{u}\\text{e}\\text{n}\\text{c}\\text{y}\\:\\text{b}\\text{i}\\text{a}\\text{s}\\:=\\:\\text{B}.\\:\\text{D}\\:\\:$$
(18)
Where
R is the speed regulation of the governor.
M is the inertia constant.
B is governor frequency bias.
### Double area power systems
We model two power areas, each with its own controller, governor, turbine, generator-load model and droop/frequency-bias feedback. The areas are linked by a tie-line, so a load step in one area changes the other area’s frequency and the tie-line power.
Each controller acts on an Area Control Error (ACE) that blends loc