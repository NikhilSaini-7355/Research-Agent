Skip to Main content
# Predictive Control
In subject area: Engineering
Model Predictive Control (MPC) is defined as an optimal control algorithm that utilizes a predictive model of a system to forecast future outputs based on past information, enabling rolling optimization and feedback correction. It is particularly suited for complex systems with dynamic changes and uncertainties, effectively managing multi-input, multi-output interactions.
AI generated definition based on: Fuel Cells for Transportation, 2023
How useful is this definition?
Press Enter to select rating, 1 out of 3 starsPress Enter to select rating, 2 out of 3 starsPress Enter to select rating, 3 out of 3 stars
About this page
Add to Mendeley Set alert
## Chapters and Articles
You might find these chapters and articles relevant to this topic.
Chapter
## Industrial control engineering
2010, Advanced Industrial Control Technology Peng Zhang
### (5)Predictive control
Predictive control, or model predictive control (MPC), is one of only a few advanced control methods that are used successfully in industrial control applications. The essence of predictive control is based on three key elements; (a) a predictive model, (b) optimization in range of a temporal window, and (c) feedback correction. These three steps are usually carried continuously by online out programs.
Predictive control is a control algorithm based on a predictive model of the process. The model is used to predict the future output based on historical information about the process, as well as anticipated future input. It emphasizes the function of the model, not the structure of the model. Therefore, a state equation, transfer function, or even a step or impulse response can be used as the predictive model. The predictive model is capable of showing the future behavior of the system. Therefore, the designer can experiment with different control laws to see the resulting system output, using computer simulation.
Predictive control is an algorithm of optimal control. It calculates future control action based on a penalty or a performance function. The optimization of predictive control is limited to a moving time interval and is carried on continuously on-line. The moving time interval is sometimes called a temporal window. This is the key difference from traditional optimal control, which uses a performance function to judge global optimization. This idea works well for complex systems with dynamic changes and uncertainties, since there is no reason in this case to judge optimization performance over the full time range.
Show more
View chapter Explore book
Read full chapter
URL: https://www.sciencedirect.com/science/article/pii/B9781437778076100026
Book\\
2010, Advanced Industrial Control TechnologyPeng Zhang
Review article
## A comprehensive survey on control strategies of distributed generation power systems under normal and abnormal conditions
2019, Annual Reviews in Control Mehmet Emin Meral, Doğan Çelík
### 4.2Predictive control
The predictive control (PC) can be applied to the many applications such as the DGPSs, process control systems and transportation systems (Li & Shi, 2013). The PC is proposed to eliminate forecast errors in order to track properly reference without any error and deals with nonlinearities (Bouzid et al., 2015). The PC also can be minimizing the resonant behaviour under unbalanced conditions (Heo, Choe, & Mok, 2013). The disadvantages of the PC method are based on the mathematical approach, which causes sensitive to parameters changes. The least square method provides the accuracy of control systems for parameter estimation (Baek, Lee, & Hyun, 2009). In Doan, Giselsson, Keviczky, De Schutter, and Rantzer (2013), the PC control based distributed optimization is applied to the power reference tracking problem of system. Generally, the PC method is used for nonlinear system and used to reduce switching frequency of high-power converter devices (Mapari & Wakde, 2013; Rodriguez et al., 2007c). It also provides more robust current control with low harmonic noise. However, it requires a filter, has more computation burden and its applicable is difficult.
Show more
View article
Read full article
URL: https://www.sciencedirect.com/science/article/pii/S1367578818301718
Journal2019, Annual Reviews in ControlMehmet Emin Meral, Doğan Çelík
Review article
## A survey on control of electric power distributed generation systems for microgrid applications
2015, Renewable and Sustainable Energy Reviews Allal M. Bouzid, ... Mustapha Benghanem
### 6.3Predictive control
The predictive control is developed to minimize the forecast error so that the reference current can be tracked properly without any error. Seong et al. \[88\] have proposed predictive active damping method to minimize the resonant behavior during the grid connection, this method is added with the phase and gain compensations. Yang et al. \[89\] have proposed a predictive current control strategy in the inner loop and a fuzzy voltage control strategy in the outer loop that can eliminate the steady-state phase error between the output and reference current, and compensate for the errors caused by sample delays and discretization, with a fixed switching frequency. Yohan et al. \[90\] have used predictive current control strategy based on predictive direct power control strategy and use a symmetrical 4×4 voltage vectors’ sequence which selects two effective and two zero voltage vectors and determines a concatenated voltage vectors’ sequence. The drawback of predictive current control is the mathematical based approach, which is sensitive to parameters changes. The parameter estimation achieved by the least square method improves the accuracy of control systems \[91\]. Rezaei et al. \[92\] have proposed an improved predictive current control strategy for reducing the output current harmonic content of single-phase grid-connected inverters, based on nonlinear filter inductor model. Espi et al. \[93\] present an adaptive robust predictive current control (RPCC) for grid-connected three-phase inverters. The error correction is achieved by means of an adaptive strategy that works in parallel with the deadbeat algorithm, therefore preserving the typical fast response of the predictive law. Jiabing and Zhu \[94\] present a dead-beat predictive direct power control (DPC) strategy and its improved voltage-vector sequences for reversible three-phase grid-connected voltage-source converters (VSCs).
Show more
View article
Read full article
URL: https://www.sciencedirect.com/science/article/pii/S136403211500026X
Journal2015, Renewable and Sustainable Energy ReviewsAllal M. Bouzid, ... Mustapha Benghanem
Chapter
## Predictive control for delay systems: theory and applications
2021, Control Strategy for Time-Delay Systems Sofiane Bououden, Mohammed Chadli
### 6.3.2Predictive control
The main idea of predictive control is to use a model to predict the behavior or state of the system, at least over a certain time horizon, and choose the best decision in terms of a certain cost while respecting the constraints. At each sampling period the use of an explicit model process to calculate the input process, optimizing the desired future plan over an interval, has been called the prediction horizon. Usually, a command set is calculated, but only the first one is taken into account. At the next sampling period the optimization problem is reformulated and solved with the new parameters obtained by the system. Then this procedure is repeated: it is the principle of the slippery or receding horizon. So the optimization problem in general can be either a quadratic program for the linear case or a nonlinear program for the nonlinear case.
Generally, the predictive command consists of the following basic elements:
A prediction model.
A cost function to minimize more constraints.
An optimization algorithm to calculate the future order.
Each element has several options to consider them. This gives a variety of predictive control algorithms.
#### 6.3.2.1Prediction model
The prediction model consists of two parts, one of which describes the input-output relationship and the other describes disturbances and modeling errors. The model must be discrete because the predictive control is a numerical control.
So, depending on the model, there are several forms of predictive control:
Linear predictive control based on a state model, transfer function, and so on.
Nonlinear predictive control based on a nonlinear state model, and so on.
#### 6.3.2.2Cost function
The cost function penalizes the differences between the predicted outputs controlled y(k+t\|k) and the reference trajectory yref(k+t\|k) in addition to the variations of the control vector Δu(k)=u(k)−u(k−1). The reference path may depend on measurements taken at time _k_; in particular, its starting point may be the measurement of output y(k). Thus it may be a set of fixed points or a predetermined path. The cost function is often given in the following form:
(6.9)minu⁡J=∑i=Hp(yref(k+i)−yˆ(k+i\|k))TQ(yref(k+i)−yˆ(k+i\|k))+∑i=HwHp(u(k+i−1)TRu(k+i−1)+Δu(k+i−1)TSΔu(k+i−1)),
where _Q_, _R_, and _S_ are the weighting matrices, with _Q_ is defined as positive, and _R_ and _S_ are semidefinite positive. The parameters Hw, Hp, andHu are the parameters for adjusting the predictive corrector and represent the time of the start of the prediction, the maximum prediction horizon, and the control horizon, respectively.
#### 6.3.2.3Constrained predictive control
As we have previously seen, a small reminder on predictive control was introduced at the beginning of this chapter. For the next step, we will try to make a synthesis of this approach to obtain the control law. For this purpose, we use the following basic discrete-state model to calculate the predictions:
(6.10){x(k+1)=Ax(k)+Bu(k),y(k)=Cx(k),
where x(k)∈Rn is the state vector, u(k)∈Rm is the input vector, and y(k)∈Rl is the output vector. The system is subjected to constrained input u(k) and output y(k):
umin⩽u(k)⩽umax,ymin⩽y(k)⩽ymax.
Then by developing predictions we get:
x(k+1)=Ax(k)+Bu(k)=Ax(k)+Bu(k−1)+BΔu(k),x(k+2)=Ax(k+1)+Bu(k+1)=A2x(k)+(AB+B)u(k−1)+(AB+B)Δu(k)+BΔu(k+1),⋮x(k+n)=Anx(k)+(An−1B+…+B)u(k−1)+(An−1B+…+B)Δu(k)+…+BΔu(k+n−1).
Then we obtain the optimal predictor in the following form:
(6.11)Xˆ=\[xˆ(k)xˆ(k+1)⋮xˆ(k+n−1)\]=Ψ0x(k)+Γ0u(k−1)+ΛΔu,
where
ΔU=\[Δu(k)Δu(k+1)⋮Δu(k+n−1)\],Ψ0=\[AA2⋮An\],Γ0=\[BAB+B⋮An−1B+…+B\],Λ=\[B0…0AB+BB…0⋮⋮⋱⋮An−1B+…+BAn−2B+…+B…B\].
Also, we have:
(6.12)yˆ=Cxˆ=Ψyx(k)+Γyu(k−1)+ΛyΔU
with Ψy=CΨ0, Γy=CΓ, Λy=CΛ
The output predictor (6.12) can be rewritten as follows:
(6.13)yˆ(k+n\|k)=CAnx+∑j=0n−1CAn−j−1B\[u(k−1)+∑i=0jΔu(k+i)\]︸u(k+j).
The next step consists in defining the vector Yˆ(k) of the output predictions in matrix form, considering Eq. (6.13) with the condition Δu(k+i)=0 for i⩾Hu.
Show more
View chapter Explore book
Read full chapter
URL: https://www.sciencedirect.com/science/article/pii/B9780323853477000110
Book\\
2021, Control Strategy for Time-Delay SystemsSofiane Bououden, Mohammed Chadli
Review article
## Review of nuclear power plant control research: Neural network-based methods
2023, Annals of Nuclear Energy Gang Zhou, Da Tan
### 3.6NN predictive control
NN predictive control (NNPC) is an intelligent control method based on the combination of NN modeling and model predictive control (MPC). Predictive control is a model-based control method. The idea of MPC is to predict the future output of the object and then determine the current and future control action or control value at a certain time according to the error between the predicted output, expected output, and optimization algorithm.
Suppose _y_ d( _k_) is the expected output of a controlled system, _y_ P( _k_) ( _k_ = 1, 2, …, _p_) is the output of the controlled system at _p_ time in the future, and _e_( _k_) is the error between the expected output and predicted output of the system.
MPC involves model prediction and dynamic optimization. According to the model of the controlled object, the first step of MPC predicts the output _y_ P( _k_) ( _k_ = 1, 2, …, _p_) of the object in the future and then calculates the control amount _u_( _k_) of the current and future time by optimizing the difference _e_( _k_) between the predicted output and expected output. Therefore, in MPC, the predictive model of the controlled object must be established first. Then, the rolling optimization and feedback correction can be performed.
In NNPC, the common method is to use NN as the predictive model to replace the internal model in the MPC and use the nonlinear optimizer to optimize the calculation. The structure of the NNPC system is shown in Fig. 12.
Fig. 12. Structure of the NNPC system.
In the process control of NPPs, the water level control of SG is a complex problem. To study the effective process control method of SG, the water quality inventory control method of SG was proposed to replace the conventional water level control method of SG (Dong et al., 2008). In this method, feedforward NN, which is used to build the water quality inventory predictor of SG, is combined with the PI controller to form the water quality inventory control system of SG. Theoretical analysis and simulation results show that this method can improve the operation and safety of SG. Thermal power optimization is an important problem in power system research. A model predictive controller based on multi-layer perceptron (MLP) was proposed for the optimization control of thermal power of nuclear superheated steam supply systems (NSSSS) (Dong et al., 2020). In this method, MLP is used to predict the thermal power of NSSSS. The model predictive controller based on MLP and existing NSSSS controller form a cascade feedback control loop, and the model predictive controller based on MLP is used as the outer loop optimization controller. The effectiveness of this method was evident from the simulation results.
The MPC algorithm is generally used in small PWR power control, which has the problem of low identification accuracy. To solve this problem, an NN prediction-based MPC method was proposed (Xiao et al., 2022). Based on the reactor core multi-model system, a global power control system was designed, and the reactor core model was identified by the NN to determine and optimize the core control input. The simulation results show that this method has good load tracking performance and anti-jamming ability.
In the study of PWR core power and outlet temperature monitoring, a gradient descent-based particle swarm optimization NN method was proposed (Ejigu and Liu, 2022). The performance of the controller was tested by the mean square error and integral square error. The results show that compared with other control methods, the proposed method can track the load successfully and has higher stability.
Show more
View article
Read full article
URL: https://www.sciencedirect.com/science/article/pii/S0306454922005436
Journal2023, Annals of Nuclear EnergyGang Zhou, Da Tan
Chapter
## Heat transport and thermal management
2023, Fuel Cells for Transportation Siyuan Wu, ... Jae Wan Park
### 12.3.3.2Model predictive control
MPC, namely, predictive control, is one of the optimal control algorithms that have been successfully used in the industry. The control process consists of a predictive model, rolling optimization, and feedback correction. MPC uses a predictive model of the system to forecast the future output based on past information, showing the future behavior of the system. It emphasizes the function of the model, not the structure of the model. MPC is suitable for complex systems with dynamic changes and uncertainties, which has difficulty building a precise model \[42\]. A PEMFC system possesses hysteresis, nonlinearity, and uncertainty. MPC can deal with multiinput, multioutput systems that may have interactions between the inputs and outputs. Compared to PID control, MPC is advantageous in reduced time to steady state, less oscillation, and stronger robustness. In practice, the time spent on online or on-the-fly calculations is relatively long.
Show more
View chapter Explore book
Read full chapter
URL: https://www.sciencedirect.com/science/article/pii/B9780323994859000010
Book\\
2023, Fuel Cells for TransportationSiyuan Wu, ... Jae Wan Park
Chapter
## Real-time software platform using MRI for navigation of magnetic microrobots
2012, Medical Robotics K. Belharet, ... A. Ferreira
### Predictive control
Predictive control has become an area of significant research interest over the past twenty years. This interest has been powered by a stream of successful industrial applications (Qin and Badgwell, 2003). When focusing on linear (and unconstrained) discrete time transfer function models and quadratic cost functions, some of the best known approaches include the generalized predictive control (GPC) introduced by Clarke _et al._ (1987), and the inner loop stabilizing stable predictive control (Kouvaritakis _et al._, 1992). In particular, in a more general way, model predictive control (MPC) refers to a class of predictive control algorithms that use an explicit process model to predict the future response of the system. One way to design MPC is to use an extended state–space representation, which is classically given by:
\[11.15\]x¨k+1=AXk+BΔukyk=Cxk
where _Δu_ k= _u_ _k_− _u_ k‐1 is the discrete difference operator; and the different matrices _A_, _B_, and _C_ can be simply retrieved from \[equation 11.8\]. The predicted state vector at time _k_ + _i_ is then computed (Camacho and Bordons, 2004):
\[11.16\]x^k+i/k=Aixk/k‐1+∑j=0i‐1AjBuk‐j‐1
The future outputs _y_ k+j/k are than computed based on the real system for future times starting at time _k_ using a recursion procedure, defined by:
\[11.17\]y^k+i/k=CAixk+∑j=1iAi‐j‐1Buk+i‐j/k
The design criterion is defined for a certain interval of predictions (several steps in the future). It includes the part of the control error, in which the model of the system is covered (insertion of equations of prediction \[11.17\]) and the part of control actions, where the input energy (control actions) is weighted. The latter part redistributes control errors to individual steps of predictions and provides coupling within intervals of predictions. The usual form of the criterion for predictive design is written as:
\[11.18\]Jk=∑j=N1+1N2yk+jWK+jTQyyk+jWk+j+∑j=1Nuuk+j‐1TQuuk+j‐1
The criterion is expressed in step _k_, _N_ = _N_ 2 – _N1_ is a horizon of prediction, _Nu_ is the control horizon, _Q_ y and _Q_ u are output and input penalizations, and _y_ k+j and _u_ k+j–1 are output and input (full or incremental) values. Finally, let us note how to construct the real control actions by an incremental algorithm: after computing a vector for the whole horizon, only the first control _u_ k is used; then, to obtain the full control actions, the second line of \[equation 11.15\] is applied. When using MPC in the state–space formulation, and, in general for the use of other state–space controls, it is necessary to solve the question of availability of the state of the system (state vector). If this is not available, and only system output from the measurement are known, then some state–space estimation has to be considered. A suitable well-known solution for such an estimation is the state–space observer based on the Kalman filter.
Show more
View chapter Explore book
Read full chapter
URL: https://www.sciencedirect.com/science/article/pii/B9780857091307500119
Book\\
2012, Medical RoboticsK. Belharet, ... A. Ferreira
Chapter
## Characterization of a Predictive Control Scheme
2018, Experimental Design and Verification of a Centralized Controller for Irrigation Canals Enrique Bonet Gil
### 3.1Introduction
The main focus of predictive control (PC) is to define control actions using input data from a computer model, thus defining the dynamics of a canal system that can be correctly approximated by Saint-Venant’s equations or by another hydraulic approach and the hydraulic model of a check structure (such as a sluice gate and a weir) \[BUY 91, YEV 75\]. On the other hand, physical parameters of the computer model (such as the Manning coefficient) must be calibrated before using the predictive control.
We should follow the next steps in the process of a predictive control algorithm:
estimate the canal flow response during a predictive horizon;
determine the sequence of control actions to control the canal during a predictive horizon.
Canal control is strongly associated with taking more actions, depending on the reference defined by the watermaster; normally this response is to increase or decrease the water level at a setpoint or checkpoint, that is, at a certain cross-section in the canal in which we can measure the water level with pressure transducers or staff gages directly in the canal. Typically, these setpoints are associated with a certain constant value (desired water level) during the irrigation cycle.
A control action to minimize the variation between the desired and simulated/measured behavior is usually made by optimization problems, which seek to minimize an objective function. Minimizing the objective function is equivalent to minimizing the absolute deviation between simulated values and desired values. Before introducing the optimization problem of our predictive control, we are going to introduce a general definition of computer models and objective functions that are also involved in predictive controllers.
Show more
View chapter Explore book
Read full chapter
URL: https://www.sciencedirect.com/science/article/pii/B9781785483073500033
Book\\
2018, Experimental Design and Verification of a Centralized Controller for Irrigation CanalsEnrique Bonet Gil
Review article
## A review of recent developments and technological advancements of variable-air-volume (VAV) air-conditioning systems
2016, Renewable and Sustainable Energy Reviews Godwine Swere Okochi, Ye Yao
### 3.1.2Optimal, predictive, and adaptive controllers
Significant studies in this field were carried out during 1980s and 1990s. The use of optimal control \[118\] or predictive control\[119\] requires building models. Predictive control aims at establishing a model for future disturbances. The disturbances may be from solar gains, presence of occupants etc., \[119–123\]. Also, predictive control improves thermal comfort by reducing overheating through night cooling \[123\]. However, during the application of this method, mathematical analysis of the thermal characteristics of a building results in non-linear models.
Adaptive controllers self-regulate and adapt to the climatic conditions in various conditioned spaces (buildings).These controllers are believed to be the most promising building adaptive control systems \[125\].
Show more
View article
Read full article
URL: https://www.sciencedirect.com/science/article/pii/S1364032115017116
Journal2016, Renewable and Sustainable Energy ReviewsGodwine Swere Okochi, Ye Yao
Review article
## Energy management schemes, challenges and impacts of emerging inverter technology for renewable energy integration towards grid decarbonization
2023, Journal of Cleaner Production Sheikh Tanzim Meraj, ... Hieu Trinh
### 4.1.4Predictive control (PC)
Predictive control (PC) techniques were first developed in 1970s specifically for process industries (Mayne et al., 2000). Later in 1980, it was first utilized to control a 2-level conventional inverter by predicting the ideal switching sequence (Holtz and Stadtfeld, 1983). The predictive control technique employs a system model to forecast future system behavior, after which control measures are chosen based on optimization criteria. The following are the main advantages: (i) a simple and easily comprehensible concept, (ii) has the capacity to handle a system with multiple variables and (iii) system limitations and nonlinearities can be easily evaluated ( _EG8, ER3, IP3_) (Edpuganti and Rathore, 2015a). The major drawback of PC techniques is the requirement of a highly capable and expensive ( _IP1_) microcontroller that can deal with high sampling frequency (Townsend et al., 2013). This is due to the fact that PC techniques generally require high computational power. Thus, the cost of the system can substantially increase. PC techniques can ensure low frequency functionality in MV applications by introducing additional terms in the cost function while ensuring that the best system performance is achieved. PC techniques can be classified into 3 different sub-branches including: model predictive control (MPC), field-oriented control (FOC)and finite control set (FCS).
(Yaramasu and Wu, 2014a) proposed an MPC technique for a grid tied MV NPC inverter in. The entire system is regulated using the proposed MPC which used the discrete time model of the MV NPC inverter to predict the future behavior of the control variables. An independent cost function along with appropriate switching sequences are selected to evaluate the MPC and directly apply it to the grid-side MV NPC. The cost function is as follows:
(25)gi(k)=\[iαg\*(k+1)−iαg(k+1)\]2+\[iβg\*(k+1)−iβg(k+1)\]2+wi\*∑j=1,2∑x=a,b,c\|Sjx(k)−Sjx,op(k)\|
(26)\[iαg\*(k+1)iβg\*(k+1)\]=ejωgTs\[iαg\*(k)iβg\*(k)\]
A non-linear MPC (NMPC) technique is proposed in (Veenstra and Rufer, 2005) for controlling a hybrid MVIT for MV drive applications. The proposed NMPC technique has the ability to optimize the common-mode voltage and thus, power balancing is ensured. As a function of the control inputs, the controller anticipates how the system will evolve. To discover the best control to apply to the system, a cost function and the control variables are iteratively reduced in real time. The cost function is defined as:
(27)V=∑k=1N(εVnp2\[k\]+εV→sub\[k\].εV→sub\[k\]+c0Vcm2\[k\]+c1V˙cm2\[k\]+c2V¨cm2\[k\])
A field-oriented control (FOC) was proposed in (Khambadkone and Holtz, 1992) for high-power MV inverter fed MV drives. The proposed control can effectively eliminate undesired torque harmonics of the MV drive during low frequency operation of the MVIT. In order to make this possible, the switching pulse of the MVIT is made dependent on the orientation of the rotor flux of the MV drive. A model predictive direct torque control (MPDTC) scheme is proposed in (Geyer and Mastellone, 2012) for a 5-level ANPC MVIT. The proposed technique can simultaneously resolve the voltage balancing issues of the diodes and capacitors of the ANPC and provide fast torque and current control. The cost function of MPDTC technique at time-step _k_ can be stated as:
(28)c=1n∑kk+p−1(λsΔSANPC(k)+ΔSFC(k))+λn(vn(k+p−1))2
(29)ΔSANPC,x(k)=sANPC(sx(k−1),sx(k))ε{0,1,2}
(30)ΔSFC,x(k)=sFC(sx(k−1),sx(k))ε{0,1,2}
The schematic diagram of the control diagram is depicted in Fig. 19. A model predictive pulse pattern control (MP3C) technique is proposed in (Geyer et al., 2018) for MVIT. The main objective of this control is the mitigation of harmonics from stator current of a MV drive. The control was able to effectively increase the efficiency of the MVIT and the MV drive by keeping the switching transitions per fundamental cycle to a minimum. The control diagram of the proposed technique is shown in Fig. 20. Other notable PC techniques applied for MVIT in MV applications can be found in (Baidya et al., 2018; Gao et al., 2022; Lezana et al., 2009a; Mahfuz-Ur-Rahman et al., 2020; Narimani et al., 2014b; Nasiri et al., 2019; Ni et al., 2020; Qin and Saeedifard, 2012; Rohten et al., 2021; Rossi et al., 2022; Yang et al., 2020a, 2020b; Yaramasu and Wu, 2014b; Zhou et al., 2020) and their characteristic traits are summarized in Table 13. The line voltage THD of the MVIT reported by these PC techniques are illustrated in Fig. 21 for comparison purposes.
Fig. 19. Schematic control diagram of the MPDTC proposed in (Geyer and Mastellone, 2012).
Fig. 20. Schematic control diagram of the proposed MP3C technique in (Geyer et al., 2018).
Table 13. Characteristic Traits of Various PC techniques for MVIT.
| Ref | _N_ _v_ | MVIT (PC) | Advantages | Limitations | Decarbonization Remarks | Applications |
| Yaramasu and Wu (2014a) | 3 | NPC (MPC) | -<br>reduced switching frequency and switching losses.<br>-<br>active/reactive power management.<br>-<br>capacitor voltages are balanced. | -<br>high system complexity.<br>-<br>presence of significant harmonics in the output current. | Solved: _EG4, EG8, ER1, ER2, ER4, IP3, IP4, IP7, IP9_<br>Endures: _EG6, EG7, IP8_ | Grid-Wind turbine |
| Khambadkone and Holtz (1992) | ns | ns (FOC) | -<br>reduced switching frequency and switching losses substantially. | -<br>dynamic performance is not analyzed.<br>-<br>voltage/current harmonics are not analyzed.<br>-<br>only suitable for low level MVIT | Solved: _IP4_<br>Endures: _IP2, IP8_ | Drive |
| Geyer and Mastellone (2012) | 5 | ANPC (MPDTC) | -<br>fast torque response.<br>-<br>reduced switching frequency and switching losses.<br>-<br>capacitor voltages are balanced. | -<br>output voltage/current contains harmonics and ripples.<br>-<br>high commutations. | Solved: _IP2, IP3, IP4, IP9_<br>Endures: _IP1, IP8_ | Drive |
| Geyer et al. (2018) | ns | NPC (MP3C) | -<br>neutral point voltage is balanced.<br>-<br>reduced switching frequency and switching losses.<br>-<br>current harmonics reduced below IEEE 519 standard.<br>-<br>moderate fault handling ability. | -<br>offline computation is required.<br>-<br>dynamic performance is not analyzed. | Solved: _IP2–IP6, IP8,_ | Drive |
| Lezana et al. (2009a) | 6/8 | FC (MPC) | -<br>the voltage ratios of capacitors are correctly controlled making it suitable for higher level MVIT.<br>-<br>can operate at high power factor. | -<br>presence of significant harmonics in the output voltage/current.<br>-<br>capacitor voltage balancing is not done properly.<br>-<br>high switching frequency and losses. | Solved: _IP1, IP2_<br>Endures: _IP3, IP4, IP8_ | Drive |
| Yaramasu and Wu (2014b) | 4 | NPC (MPC) | -<br>reduced switching frequency and switching losses.<br>-<br>current harmonics reduced below IEEE 519 standard.<br>-<br>power imbalance is resolved.<br>-<br>faster transient response.<br>-<br>capacitor voltages are balanced. | -<br>voltage harmonics did not follow IEEE 519 standard.<br>-<br>high system complexity due to using additional delay compensation. | Solved: _EG4, EG5, EG8, ER1_ – _ER4, IP3, IP4, IP7, IP9_<br>Endures: _EG7, IP8_ | Grid-Wind turbine |
| Narimani et al. (2014b) | 4 | NNPC (MPC) | -<br>capacitor voltages are balanced.<br>-<br>simplified control.<br>-<br>cost-effective system. | -<br>voltage/current harmonics are not analyzed.<br>-<br>only suitable for low level MVIT. | Solved: _IP1–IP3_<br>Endures: _IP4, IP8_ | ns |
| Qin and Saeedifard (2012) | ns | CHB (MPC) | -<br>capacitor voltages are balanced.<br>-<br>active/reactive power management.<br>-<br>high dynamic response.<br>-<br>cost-effective system. | -<br>high switching frequency and losses.<br>-<br>presence of significant harmonics in the output voltage/current. | Solved: _EG1, EG4, EG6, EG8, IP1, IP3, IP9_<br>Endures: _EG7, IP4, IP8_ | Grid |
| Gao et al. (2022) | ns | CHB (MPC) | -<br>capacitor voltages are balanced.<br>-<br>current harmonics reduced below IEE 519 standard.<br>-<br>simplified control. | -<br>high switching frequency and losses. | Solved: _IP1–IP3, IP8_<br>Endures: _IP4_ | Drive |
| Mahfuz-Ur-Rahman et al. (2020) | 9 | ANPC (MPC) | -<br>active/reactive power management.<br>-<br>voltage/current harmonics reduced below IEEE 519 standard.<br>-<br>computational burden reduced.<br>-<br>EMI is reduced. | -<br>high switching frequency and losses.<br>-<br>large and expensive system.<br>-<br>RES power imbalance can cause issue. | Solved: _EG4 – EG8, IP3, IP7 – IP9_<br>Endures: _EG1, ER1, ER3, ER4, IP1_ | Grid-PV |
| Nasiri et al. (2019) | 15 | CHB (FCS) | -<br>computational time is reduced.<br>-<br>active/reactive power management.<br>-<br>transformer-less cost-effective and compact system. | -<br>voltage/current harmonics are not analyzed.<br>-<br>high switching frequency and losses.<br>-<br>RES power imbalance can cause issue. | Solved: _EG1, EG4 – EG6, ER2, IP1, IP7_<br>Endures: _EG7, ER1, ER3, ER4, IP8_ | Grid-Wind turbine |
| Ni et al. (2020) | 7 | CHB (FCS) | -<br>computational time is reduced.<br>-<br>CMV is reduced.<br>-<br>current harmonics recued below IEEE 519 standard.<br>-<br>suitable for high voltage MVIT | -<br>high switching frequency and losses. | Solved: _IP1, IP2, IP8._<br>Endures: _IP4_ | Drive |
| (Yang et al., 2020a, 2020b) | 4, 5 | Hybrid, ANPC (MPC) | -<br>capacitor voltages are balanced.<br>-<br>current harmonics reduced below IEEE 519 standard.<br>-<br>better dynamic performance. | -<br>high computational complexity.<br>-<br>high switching frequency and losses. | Solved: _IP3, IP8._<br>Endures: _IP4_ | ns |
| Baidya et al. (2018) | 5 | CHB (MPC) | -<br>CMV is reduced.<br>-<br>reduced switching frequency and switching losses.<br>-<br>current harmonics reduced below IEEE 519 standard. | -<br>dynamic performance is not analyzed.<br>-<br>high control complexity due to using additional optimization algorithm. | Solved: _IP4, IP8._ | ns |
| Rohten et al. (2021) | 3 | CHB (FCS) | -<br>reduced switching frequency and switching losses.<br>-<br>fast dynamic response.<br>-<br>moderate fault handling ability.<br>-<br>system stability achieved under voltage sag/swell.<br>-<br>economic and compact system | -<br>high sampling per period is required.<br>-<br>high computational complexity due to requiring additional SVM control.<br>-<br>presence of significant harmonics in grid current from experimental results. | Solved: _EG1, EG2, EG4, EG8, IP1, IP4–IP6, IP9_<br>Endures: _EG6, EG7, IP3, IP8_ | Grid |
| Zhou et al. (2020) | 5 | ANPC (HMPC) | -<br>capacitor voltages are balanced.<br>-<br>steady-state performance is improved.<br>-<br>current harmonics reduced below IEEE 519 standard. | -<br>complicated control due to operating switches at 2 switching frequencies.<br>-<br>dynamic performance is not analyzed.<br>-<br>component failure can cause serious damage. | Solved: _IP1, IP2, IP8._<br>Endures: _IP4–IP6_ | ns |
| Rossi et al. (2022) | 3 | NPC (MPC) | -<br>fault-tolerant ability.<br>-<br>voltage/current harmonics reduced below IEEE 519 standard.<br>-<br>reduced switching frequency and losses.<br>-<br>fast dynamic response.<br>-<br>system stability ensured under power imbalance. | -<br>high computational complexity and cost due to optimization problem.<br>-<br>additional filter is required.<br>-<br>large and expensive system.<br>-<br>high EMI in the system. | Solved: _EG2, EG4, EG7, EG8, IP3–IP6, IP8._<br>Endures: _EG1, EG6, IP1, IP9_ | Grid |
Fig. 21. Comparison of current THD and voltage ratings among various PC techniques applied for MVIT.
Show more
View article
Read full article
URL: https://www.sciencedirect.com/science/article/pii/S0959652623011605
Journal2023, Journal of Cleaner ProductionSheikh Tanzim Meraj, ... Hieu Trinh
## Related terms:
- Artificial Neural Network
- Energy Engineering
- Process Control
- Natural Gas
- Battery (Electrochemical Energy Engineering)
- Compressed Natural Gas
- Predictive Control Model
- Energy Conservation
- Control Algorithm
- Control Scheme
View all Topics