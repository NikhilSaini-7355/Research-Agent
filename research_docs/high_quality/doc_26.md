Skip to main content Skip to article
- Access through **your organization**
- Purchase PDF
Search ScienceDirect
## Article preview
- Abstract
- Introduction
- Section snippets
- References (188)
- Cited by (125)
[](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence "Go to Engineering Applications of Artificial Intelligence on ScienceDirect")
## Engineering Applications of Artificial Intelligence
Volume 120, April 2023, 105878
[](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence/vol/120/suppl/C)
# Survey paper Integrating Machine Learning and Model Predictive Control for automotive applications: A review and future directions
Author links open overlay panelArminNorouzia, HamedHeidarifara, HoseinaliBorhanb, MahdiShahbakhtia, Charles RobertKocha
Show more
Add to Mendeley
Cite
https://doi.org/10.1016/j.engappai.2023.105878 Get rights and content
## Abstract
In this review paper, the integration of Machine Learning (ML) and Model Predictive Control (MPC) in Automotive Control System (ACS) applications are discussed. ACS can be divided into these three main subsystems: enhancing safety, improving comfort, and reducing fuel consumption and emissions. Due to the development of new technologies such as advancing autonomous and connected vehicles the complexity of these subsystems is increasing. The ACS is meant to encompass the vehicle dynamics, powertrain control, passenger comfort, and accessories. Since vehicle manufacturers must meet stringent performance and emission requirements, optimal control methods for ACS applications are seen as a promising technology. MPC is an optimal control method for closed-loop control applications that allows constraints to be enforced in real-time while an objective function is minimized. The application of MPC in the automotive industry has been shown in the past decade. An important challenge in the design and real-time implementation of MPC is having a accurate predictive model that also does not require excessive real-time computation. Using ML to provide an accurate model at decreased computational cost improves MPC performance of ACS and is the main focus of this paper. How MPC in ML-based ACS applications ensures stability while meeting constraint is also discussed. Method to combine MPC and ML for the ACS subsystems of vehicle dynamics and powertrain control are reviewed and an outlook on future ACS is discussed.
## Introduction
Methods of Machine Learning (ML) and Model Predictive Control (MPC) integration in Automotive Control System (ACS) applications are reviewed. Integration of ML and MPC is an emerging area that can enhance performance for the control and optimization of ACS. In the following subsections, the scope of the paper, including main contributions, will be discussed. Then, motivation and review methodology will be provided.
The main scope of this paper includes the ML method exclusively used in MPC implementation to reduce MPC computational cost or MPC model requirement in ACS. In this review, two main components of ACS, including Vehicle Dynamics Control (VDC) and Powertrain Control (PTC), will be analyzed. As such, occupant comfort control and accessory control, including adaptive front lighting control, hill-hold control, and windshield wiper control, are outside of the scope of this paper. In addition, some fields in autonomous driving, such as driver condition monitoring, vision enhancement/night vision systems, human interaction, decision-making, video/image recognition, and sensor fusion, are also outside of the scope of this paper. The focus is on those subsystems that MPC has been implemented, and ML can be integrated with them. This will include a wide range of automotive powertrain (electric, hybrid electric, combustion engine, fuel cell) system.
The main contributions of this review paper are:
- •
Identification and description of five main streams of integrating machine learning and MPC in the literature;
- •
Comprehensive review of MPC applications in the automotive area and updating the prior review (Hrovat et al., 2012) by including emerging fields of MPC and artificial intelligence integration;
- •
Classification of ML methods utilized in MPC based on automotive control applications;
- •
Providing outlook and future directions for using ML-enriched MPC and safe learning control for automotive applications;
- •
Classification of automotive control systems and the application areas that MPC has provided successful results.
In the United States it is predicted that 70.1 percent of the licensed drivers will be driving a connected car by 2025 (Fulford et al., 2021). Several automotive Original Equipment Manufacturers (OEMs) have announced large-scale programs for deploying autonomous vehicles (ranging from SAE Level 2 to 5) over the next ten years. For example, Mercedes-Benz level 3 automated package, DRIVE PILOT, is available in S-Class and EQS models in 2022. Availability of data, through connected vehicles and infrastructure, provides the opportunity of using data-driven approaches.
Furthermore, road accidents cause a significant number of injuries and fatalities (wor, 2018). While fast and effective transportation are essential to maintain quality of living, improving vehicle safety is also essential. Vehicle manufacturers must simultaneously reduce the emissions, improve ride quality and comfort, and provide safety for passengers and pedestrians. Additionally, Electric Vehicle (EV) sales are predicted to reach about 15 million cars in 2025 and over 25 million vehicles in 2030, accounting for 10% and 15% of total road vehicle sales (Outlook, 2021). This level of market share makes it worthwhile for OME’s to optimize battery usage, range estimation of EVs, and optimal battery state of health and charge.
Along with data availability, centralized cloud computing and advancements in edge computing, such as multi-core ECUs, have made the implementation of many ML-based approaches possible. The nonlinear dynamics of ACS combined with additional real world driving emissions and safety regulations, have created a need for data-driven multi-objective constrained optimization. MPC can address these needs and perform real-time optimization. MPC has been used on ACS since the mid-1990s with an increasing trend in recent years and is now being integrated with ML approaches. This increase has been enabled by the advances in the (i) V2X connectivity, (ii) availability of onboard and cloud computation, and (iii) accessibility to large amounts of vehicle and environmental data that can be used in optimizing vehicle performance, reducing emissions and decreasing fuel consumption. When MPC is integrated with ML, MPC drawbacks such as high computational resources and the need for substantial effort to develop an accurate plant and disturbance models can be mitigated.
MPC was first introduced in the early 70s in process control, and since then, it has been developed in different variants (Norouzi et al., 2021b, Borrelli et al., 2017). A time line of MPC development, including the combination with ML is shown in Fig. 1. The time line of MPC application to ACS is presented in Fig. 2. The utilization of different solvers and packages designed for time-critical real-time operation make MPC suitable in ACS applications (Tøndel et al., 2003, Salem and Mosaad, 2015, Hrovat et al., 2012, Di Cairano and Kolmanovsky, 2019). Despite these advantages, MPC has two main challenges. The first one is the high computational demand and the second is the requirement of a system model embedded in the MPC optimizer. To meet theses challenges there is an opportunity for augmentation of AI/ML with MPC. Next, the main structure of this paper will be described.
A systematic review process, shown in Fig. 3, was followed to identify the key articles for this study. The initial keywords to determine a base set of research articles were “Machine Learning and MPC Integration”, “ML-based MPC”, “Deep MPC”, “Deep Learning Control”, “ML-based Optimal Control”, “Deep Learning Optimal Control”, “Deep Learning Predictive Control” and “Machine Learning Predictive Control”. The search only included articles written in the English language and no restriction was considered for the publication year. This initial search resulted in more than 500 research articles. Next, based the abstract of each article was screened and articles where MPC and ML are integrated were kept while articles that centered on non-predictive optimal control methods were excluded. Then, based on the full-text of each articles, only articles that apply to the domain of ML and MPC integration were kept. This led to reducing the number of articles to 130 papers. Out of 130 selected articles, 47 articles were within the ACS domain. In this review paper, ML and MPC integration methodology and results are described based on these 47 articles with detailed discussions and illustrations for implementation of each method.
Although 47 articles form the core references for this study, over 200 additional articles are added to this review paper to include and provide context of state-of-the-art ACS technology and MPC.
This paper is organized into these sections:
- 1.
Introduction: This section provides background information and motivation for MPC and MPC-ML.
- 2.
State-of-the-art Automotive Control System (ACS): MPC challenges in ACS and the opportunity to use the ML method are discussed.
- 3.
Classification of ML and MPC integration methods: Different ML and MPC integration approaches are introduced and a graphical summary of the ACS domain and the ML method used in each approach is given.
- 4.
ML in model structure of MPC: ML in the model structure of MPC is presented focusing on the MPC modeling using ML approaches for ACS applications. This method address the model requirement of MPC using ML.
- 5.
ML as an add-on controller to MPC: ML and MPC integration by focusing on ML for the outer loop of a multi-layer control structure in ACS is discussed. How MPC performance could be enhanced in interaction with the ML controller in the outer/inner loop is described.
- 6.
ML in imitation of MPC: Imitation of MPC is used to replace a well-designed ACS MPC with an ML controller that mimics the MPC behavior is described. This method reduces MPC computational time by approximating optimal solutions using ML.
- 7.
MPC for safe ML learning: The application of MPC as a safety filter for a learning-based controller such as Reinforcement Learning (RL) in ACS is discussed. This method addresses the controller constraints enforcement problem for pure learning-based control.
- 8.
ML in optimization of MPC: The application of ML in MPC optimization are discussed. This method is used to decrease computational time of MPC solver.
- 9.
Summary and Conclusions: A summary of key publications and the main conclusions are listed.
- 10.
Future Directions: Future directions, based on the literature survey, are discussed.
Sections 4 to 8 form the core sections of this paper. In each of these sections, the main methods of ML-MPC integration are discussed first. Then, examples of implementation from key publications in VDC and PTC literature are presented. To conclude each Sections 4 to 8 the main highlight and key takeaways are presented.
Before proceeding to Sections 4 to 8 the details of state-of-the-art ACS are discussed in the next in Section 2. Then methods of ML-MPC integration in different ACS subsystems will be introduced in Section 3.
## Access through your organization
Check access to the full text by signing in through your organization.
Access through **your organization**
## Section snippets
## Automotive control systems: Introduction and challenges
Automotive Control Systems (ACS) can be divided into main subsystems to improve comfort and safety while reducing fuel consumption and emissions. Emerging technologies such as connectivity among vehicles and autonomous driving has resulted in these subsystems getting more complex over time.
## Classification of ML and MPC integration methods
Combining ML and MPC started in the early 2000s but has steadily increased in the last five years. ML integration with MPC, which sometimes refer as learning MPC (Hewing et al., 2020), or Data-driven MPC (Piga et al., 2019), is divided into three main categories of: (1) ML in modeling; (2) ML in computational reduction; and (3) MPC in safe learning. Due to the amount of published work in category (2), this has been further subdivided into: (2.1) Optimization of MPC; (2.2) Imitation of MPC; and
## ML in model structure of MPC in ACS
In this section, ML in the model structure of MPC in VDC and PTC subsystems of ACS will be discussed. In Section 4.1, learning techniques including offline and online learning will be addressed by presenting block diagrams of these methods. In Section 4.2, different ML models from the ACS literature to model a system for MPC implementation will be discussed. Different models of ML in the ACS literature, including neural network, deep learning, support vector machine, Gaussian process
## ML in the control structure of MPC in ACS: ML as an add-on controller
Here ML is integrated as a separate high or low level controller. Different ML methods have been applied as add-on controllers in ACS application such as ANN (Ira et al., 2018), linear regression (Mahalingam and Agrawal, 2016), ELM (Jiang et al., 2020), integrated K-means with Probabilistic Neural Network (PNN) (Gao et al., 2020), DNN (Wang et al., 2020a, Drews et al., 2017), RL (Fehér et al., 2020), Iterative Learning Control (ILC) (Brunner et al., 2017), and Hidden Markov (Joševski and Abel,
## ML in imitation of MPC in ACS
Imitation of MPC using ML methods can be divided into offline imitation and online imitation. Fig. 20 shows offline imitation where the controller input and output are collected, and a data-driven approach is used to fit a model of the controller that mimics the behavior of the MPC. Fig. 21 shows online imitation where the controller switches between ML and MPC subsystems depending on the performance of the controller. The reasons ML methods are used to mimic the MPC system’s behavior are to
## MPC for safe learning controller in ACS
ML to enhance MPC performance or to compensate for MPC drawbacks has already been described. In this section, a combination of MPC and ML in which MPC helps learning-based controllers to ensure constraint satisfaction. Although learning-based techniques have a great potential for optimizing the control law, most of these learning techniques cannot guarantee hard safety constraints, such as physical limitations which are often essential for engineering applications. Since violation of
## ML in optimization of MPC
MPC could be realized by solving an optimization problem using numerical methods. Different optimization problems that can be formed to solve an Optimal Control Problem in MPC have been listed in Table 5.
As can be seen in Table 5, in most of the MPC applications a Non Linear programming need to be solved. To tackle this problem a variety of algorithms such as First Order Methods (FOM), Active Set (AS) methods, Interior Point (IP) methods, and Sequential Quadratic Programming (SQP) methods have
## Summary
Methods of ML and MPC integration in ACS applications including the main categories of ML and MPC integration are reviewed in detail in this paper. Based on the current state of technology, ML and MPC integration is divided into five main categories as shown in Fig. 29. The red highlighted blocks indicate methods that have been implemented in ACS and, including “ML in the model structure of MPC”, “ML as an add-on controller to MPC”, “ML in imitation of MPC”, and “MPC for safe learning
## Future directions
Based on the reviewed papers and summary presented in Section 9, the following future direction of ML and MPC integration in ACS are postulated:
- 1.
**ML in the model structure of MPC**:
- (a)
**Offline learning:** Offline modeling has been used in (i) engine emission modeling such as estimating soot and HC pollutants under steady-state conditions (Norouzi et al., 2021a, Aliramezani et al., 2020b, Shahpouri et al., 2021a, Shahpouri et al., 2021b) , (ii) modeling vehicle dynamics for steering control problem (
## CRediT authorship contribution statement
**Armin Norouzi:** Conceptualization, Methodology, Writing – original draft, Visualization, Investigation. **Hamed Heidarifar:** Writing – original draft, Investigation. **Hoseinali Borhan:** Writing – review & editing. **Mahdi Shahbakhti:** Writing – review & editing. **Charles Robert Koch:** Supervision, Writing – review & editing.
## Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
## Acknowledgments
This study was supported by the Cummins R&T, USA, Natural Sciences and Engineering Research Council (NSERC) of Canada and Canada First Research Excellence Fund, Canada
. The authors would like to thank Dr. Lisa A. Farrell for her insightful technical discussions during this study.
Recommended articles
- AlcalaE. _et al._
### TS-MPC for autonomous vehicle using a learning approach
### IFAC-PapersOnLine
(2020)
- AliramezaniM. _et al._
### A grey-box machine learning based model of an electrochemical gas sensor
### Sensors Actuators B
(2020)
- BradfordE. _et al._
### Stochastic data-driven model predictive control using Gaussian processes
### Comput. Chem. Eng.
(2020)
- ChenZ. _et al._
### Stochastic model predictive control for energy management of power-split plug-in hybrid electric vehicles based on reinforcement learning
### Energy
(2020)
- ChenW. _et al._
### Extension coordinated control of four wheel independent drive electric vehicles by AFS and DYC
### Control Eng. Pract.
(2020)
- ChenY. _et al._
### Transfer learning with deep neural networks for model predictive control of HVAC and natural ventilation in smart buildings
### J. Clean. Prod.
(2020)
- ChenS. _et al._
### Decentralized machine-learning-based predictive control of nonlinear processes
### Chem. Eng. Res. Des.
(2020)
- DahlJ. _et al._
### Model predictive control of a diesel engine with turbo compound and exhaust after-treatment constraints
### IFAC PapersOnLine
(2018)
- DaudW. _et al._
### PEM fuel cell system control: A review
### Renew. Energy
(2017)
- de MoraisG.A. _et al._
### Vision-based robust control framework based on deep reinforcement learning applied to autonomous ground vehicles
### Control Eng. Pract.
(2020)
DerbeliM. _et al._
### Robust high order sliding mode control for performance improvement of PEM fuel cell power systems
### Int. J. Hydrogen Energy
(2020)
DrgoňaJ. _et al._
### Approximate model predictive building control via machine learning
### Appl. Energy
(2018)
García-NietoS. _et al._
### Nonlinear predictive control based on local model networks for air management in diesel engines
### Control Eng. Pract.
(2008)
HannanM. _et al._
### A review of lithium-ion battery state of charge estimation and management system in electric vehicle applications: Challenges and recommendations
### Renew. Sustain. Energy Rev.
(2017)
HongS. _et al._
### Development and application of a comprehensive soot model for 3D CFD reacting flow studies in a diesel engine
### Combust. Flame
(2005)
HsiehM.-F. _et al._
### Development and experimental studies of a control-oriented SCR model for a two-catalyst urea-SCR system
### Control Eng. Pract.
(2011)
HuY. _et al._
### Nonlinear model predictive controller design based on learning model for turbocharged gasoline engine of passenger vehicle
### Mech. Syst. Signal Process.
(2018)
JanakiramanV.M. _et al._
### An ELM based predictive control method for HCCI engines
### Eng. Appl. Artif. Intell.
(2016)
KakoeeA. _et al._
### Modeling combustion timing in an RCCI engine by means of a control oriented model
### Control Eng. Pract.
(2020)
KhanW.Z. _et al._
### Edge computing: A survey
### Future Gener. Comput. Syst.
(2019)
KlaučoM. _et al._
### Machine learning-based warm starting of active set methods in embedded model predictive control
### Eng. Appl. Artif. Intell.
(2019)
Lamnabhi-LagarrigueF. _et al._
### Systems & control for the future of humanity, research agenda: Current and future roles, impact and grand challenges
### Annu. Rev. Control
(2017)
LautenschlagerB. _et al._
### Data-driven iterative learning for model predictive control of heating systems
### IFAC-PapersOnLine
(2016)
AliM.U. _et al._
### Towards a smarter battery management system for electric vehicle applications: A critical review of lithium-ion battery state of charge estimation
### Energies
(2019)
AliramezaniM. _et al._
### Support vector machine for a diesel engine performance and NOx emission control-oriented model
Aliramezani, M., Norouzi, A., Koch, C.R., Hayes, R.E., 2019. A control oriented diesel engine NOx emission model for on...
AlizadehF. _et al._
### Second-order cone programming
### Math. Program.
(2003)
AndersenE.D. _et al._
### The MOSEK interior point optimizer for linear programming: an implementation of the homogeneous algorithm
ArabA. _et al._
### Safety-guaranteed learning-predictive control for aggressive autonomous vehicle maneuvers
BabaieM. _et al._
### Supervised learning model predictive control trained by ABC algorithm for common-mode voltage suppression in NPC inverter
### IEEE J. Emerg. Sel. Top. Power Electron.
(2021)
BaoY. _et al._
### An online transfer learning approach for identification and predictive control design with application to RCCI engines
BasinaA. _et al._
### Data-driven modeling and predictive control of maximum pressure rise rate in RCCI engines
BhatP.K. _et al._
### Generation of optimal velocity trajectory for real-time predictive control of a multi-mode PHEV
BidarvatanM. _et al._
### Energy management control of a hybrid electric vehicle by incorporating powertrain dynamics
BiekerK. _et al._
### Deep model predictive flow control with limited sensor data and online learning
### Theor. Comput. Fluid Dyn.
(2020)
BilginB. _et al._
### Making the case for electrified transportation
### IEEE Trans. Transp. Electr.
(2015)
BillingsS.A.
### Nonlinear System Identification: NARMAX Methods in the Time, Frequency, and Spatio-Temporal Domains
(2013)
BorrelliF. _et al._
### Predictive Control for Linear and Hybrid Systems
(2017)
Bromnick, P., 1999. Development of a Model Predictive Controller for Engine Idle Speed using CPower. SAE Paper No....
BroomheadT. _et al._
### Economic model predictive control and applications for diesel generators
### IEEE Trans. Control Syst. Technol.
(2016)
BrunnerM. _et al._
### Repetitive learning model predictive control: An autonomous racing example
CeraB. _et al._
### Multi-cable rolling locomotion with spherical tensegrities using model predictive control and deep learning
ChenS. _et al._
### Machine learning-based distributed model predictive control of nonlinear processes
### AIChE J.
(2020)
ChiangC.-J. _et al._
### Model predictive control of SCR aftertreatment system
CortesC. _et al._
### Support-vector networks
### Mach. Learn.
(1995)
CuiY. _et al._
### Reinforcement learning boat autopilot: A sample-efficient and model predictive control based approach
CuiY. _et al._
### Autonomous boat driving system using sample-efficient model predictive control-based reinforcement learning approach
### J. Field Robotics
(2020)
Da RochaF.H.M. _et al._
### Model predictive control of a heavy-duty truck based on Gaussian process
DahunsiO. _et al._
### Neural network-based model predictive control of a servo-hydraulic vehicle suspension system
DalamagkidisK. _et al._
### Nonlinear model predictive control with neural network optimization for autonomous autorotation of small unmanned helicopters
### IEEE Trans. Control Syst. Technol.
(2010)
- ### Real-time decision-making for Digital Twin in additive manufacturing with Model Predictive Control using time-series deep neural networks
2025, Journal of Manufacturing Systems
Show abstract
Digital Twin – a virtual replica of a physical system enabling real-time monitoring, model updating, prediction, and decision-making – combined with recent advances in machine learning, offers new opportunities for proactive control strategies in autonomous manufacturing. However, achieving real-time decision-making with Digital Twins requires efficient optimization driven by accurate predictions of highly nonlinear manufacturing systems. This paper presents a simultaneous multi-step Model Predictive Control (MPC) framework for real-time decision-making, using a multivariate deep neural network, named Time-Series Dense Encoder (TiDE), as the surrogate model. Unlike conventional MPC models which only provide one-step ahead prediction, TiDE is capable of predicting future states within the prediction horizon in one shot (multi-step), significantly accelerating the MPC. Using Directed Energy Deposition (DED) additive manufacturing as a case study, we demonstrate the effectiveness of the proposed MPC in achieving melt pool temperature tracking to ensure part quality, while reducing porosity defects by regulating laser power to maintain melt pool depth constraints. In this work, we first show that TiDE is capable of accurately predicting melt pool temperature and depth. Second, we demonstrate that the proposed MPC achieves precise temperature tracking while satisfying melt pool depth constraints within a targeted dilution range (10%–30%), reducing potential porosity defects. Compared to Proportional–Integral–Derivative (PID) controller, the MPC results in smoother and less fluctuating laser power profiles with competitive or superior melt pool temperature control performance. This demonstrates the MPC’s proactive control capabilities, leveraging time-series prediction and real-time optimization, positioning it as a powerful tool for future Digital Twin applications and real-time process optimization in manufacturing.
- ### Optimal design of an adaptive energy management strategy for a fuel cell tractor operating in ports
2023, Applied Energy
Citation Excerpt :
More recently, also Reinforcement Learning (RL) approaches are being proposed for fuel cell/battery hybrid vehicles to cope with the inherent duty-cycle dependency of the online EMSs available in literature. These algorithms present good real-time performance and adaptability to the variability of the vehicle duty cycle, at the cost of the need of a huge amount of data for the training phase \[28,29\]. In fact, if a limited number of driving missions is used to train a RL agent, this method may lead to a far-from-the-optimum EMS performance.
Show abstract
As World trade is growing rapidly, the reduction of the environmental impact of in-port operations towards a low or zero-emission scenario is becoming a paramount issue. To this aim, replacing Diesel engines of cargo handling equipment used in port logistics (e.g. reach stackers, forklifts, yard tractors, etc.) with cleaner propulsion alternatives may play a major role. In this study, a robust rule-based energy management strategy is proposed for a newly developed fuel cell/battery hybrid powertrain of a yard tractor used for roll-on and roll-off in-port operations. As typical port operations are characterized by mission profiles that can vary significantly in terms of driving and duty cycles during the same work-shift, the proposed strategy, built upon the observation of the powertrain behavior under the application of an optimal controller, dynamically adapts the operation of fuel cell and battery in order to track a predefined battery state of charge trajectory, while minimizing the hydrogen consumption. The use of an optimal model-based approach as a reference for the design of an online implementable energy management strategy is indeed particularly suitable in the present case: despite their inherent high variability, the yard tractor mission profiles can be regarded as the combination of a set of predictable parameters. Results show that the application of the proposed control strategy allows the hybrid powertrain to achieve excellent performance, by leading its components to run efficiently and across suitable operative conditions. The achieved hydrogen consumption, for the considered missions, is only 2%–3% higher than that of the optimal controller, despite a quite different evolution of the battery state of charge, that is the feedback control variable. By means of this strategy, the transient loading of the fuel cell is prevented, while the battery pack ensures the fulfillment of the peak power requests, with beneficial effects in terms of on-board stored energy exploitation. The key advantage of the developed rule-based approach lies in its robustness, reliability and online applicability in real-time powertrain control.
- ### Data-driven learning-based Model Predictive Control for energy-intensive systems
2023, Advanced Engineering Informatics
Citation Excerpt :
It is noted that RL is used to learn the linear model of DCs, although the actual physical system model is non-linear. Similarly, in recent years, the integration of Machine Learning (ML) and MPC has been popular, especially to use ML in the model structure of MPC, where modeling is done offline or online \[38\]. An example in \[39\] combined supervised learning and particle swarm algorithm via MPC framework to solve the scheduling of water pumping units, where the system dynamics is based on an offline well-trained model.
Show abstract
Efficient control of energy-intensive systems is essential for reducing energy consumption and realizing sustainable development. However, considering the complex inter-dependent energy-consumption devices, numerous control parameters, and dynamic environments, the energy-efficient control of energy-intensive system is always challenging. To address such problems, this paper proposes a data-driven learning-based Model Predictive Control (MPC) method for the integrated control of various devices in energy-intensive systems. Specifically, a hybrid prediction model based on two variants of RNN is integrated with the MPC scheme to learn and predict the system dynamics based on massive time-series sensing data. Then an efficient tree-based prioritized group control model for heterogeneous devices is developed with a rolling optimization and feedback correction mode. A real-life case study is provided to evaluate the performance of the proposed method, which demonstrates its superiority over existing methods on saving the energy consumption.
- ### Regenerative Braking Systems in Electric Vehicles: A Comprehensive Review of Design, Control Strategies, and Efficiency Challenges
2025, Energies
- ### An optimization-centric review on integrating artificial intelligence and digital twin technologies in manufacturing
2025, Engineering Optimization
- ### Autonomous Vehicles: Evolution of Artificial Intelligence and the Current Industry Landscape
2024, Big Data and Cognitive Computing
View all citing articles on Scopus
View full text
© 2023 Elsevier Ltd.