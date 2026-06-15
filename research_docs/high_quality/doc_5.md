Skip to main content Skip to article
- View **PDF**
- Download full issue
Search ScienceDirect
[](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence "Go to Engineering Applications of Artificial Intelligence on ScienceDirect")
## Engineering Applications of Artificial Intelligence
Volume 123, Part A, August 2023, 106211
[](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence/vol/123/part/PA)
# Optimization of the model predictive control meta-parameters through reinforcement learning
Author links open overlay panelEivindBøhna, SebastienGrosb, SigneMoec, Tor ArneJohansenbd
Show more
Add to Mendeley
Cite
https://doi.org/10.1016/j.engappai.2023.106211 Get rights and content
Under a Creative Commons license
Open access
## Abstract
Model predictive control (MPC) is increasingly being considered for control of fast systems and embedded applications. However, MPC has some significant challenges for such systems, such as its high computational complexity. Further, the MPC parameters must be tuned, which is largely a trial-and-error process that affects the control performance, the robustness, and the computational complexity of the controller to a high degree. This paper presents a multivariate optimization method based on reinforcement learning (RL) that automatically tunes the control algorithm’s parameters from data to achieve optimal closed-loop performance. The main contribution of our method is the inclusion of state-dependent optimization of the meta-parameters of MPC, i.e. parameters that are non-differentiable wrt. the MPC solution. Our control algorithm is based on an event-triggered MPC, where we learn when the MPC should be re-computed, and a dual-mode MPC and linear state feedback control law applied in between MPC computations. We formulate a novel mixture-distribution RL policy determining the meta-parameters of our control algorithm and show that with joint optimization we achieve improvements that do not present themselves with univariate optimization of the same parameters. We demonstrate our framework on the inverted pendulum control task, reducing the total computation time of the control system by 36% while also improving the control performance by 18.4%.
- Previousarticle in issue
- Nextarticle in issue
## Keywords
Reinforcement learning
Model predictive control
Event-triggered control
Linear quadratic regulator
Recommended articles
## Data availability
Code and data are available at the URL provided in the article.
© 2023 The Author(s). Published by Elsevier Ltd.