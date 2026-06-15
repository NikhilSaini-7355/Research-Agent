Question
Asked 4 June 2026
[](https://www.researchgate.net/profile/Tunda-Olembe-Djamba)
Tunda-Olembe Djamba
- University of Lubumbashi
# How can machine learning be integrated into Model Prédictive Control without losing the stability guarantees of processus identification models ?
This reads really well — clear, academic, and it frames the problem precisely.
I am working on the integration of machine learning models into Model Predictive Control for industrial dynamic systems. Classical process identification provides the stability guarantees required for control design but struggles to capture strong nonlinearities. Neural models offer greater flexibility, yet currently lack the formal certificates needed for safety-critical deployment.
I am interested in current approaches and ongoing research aimed at closing this certification gap for neural models within a predictive control framework.
Neural Modeling
Model Predictive Control
Certificate of Need
Machine Learning
Dynamic Systems
Share
* * *
**Get help with your research**
Join ResearchGate to ask questions, get input, and advance your work.
Join for free
## All Answers (1)
[](https://www.researchgate.net/profile/Mohammad-Heidar-Khamsehei-Fadaei-2)
Mohammad Heidar Khamsehei Fadaei
Self-employed
Integrating machine learning into MPC while preserving stability can be done effectively by **enforcing Lyapunov constraints during learning or training an explicit backup plan**. The key is to never fully rely on the black-box model without a formal safety net.
Here are the most prominent research pathways closing the certification gap:
- **🔒 Certified Neural Policies**: **End-to-end learning of Lyapunov-stable MPC** simultaneously trains neural policies and a control Lyapunov function (CLF), providing rigorous stability certificates. **ReLU-based NN approximation of MPC** pre-computes optimal control laws for linear systems offline, using ReLU neural networks with explicit bounds to guarantee stability.
- **📊 Gaussian Process (GP) & Uncertainty Quantification**: These methods propagate model uncertainty to establish **probabilistic stability guarantees** and learn unknown dynamics while quantifying prediction variance. A **sampling-based GP-MPC scheme** ensures closed-loop safety and stability with high probability.
- **🌐 Koopman Operator Methods**: These identify a **linear representation of nonlinear dynamics**, enabling the use of standard linear MPC with theoretical guarantees. New approaches like **Input-to-State Stable (ISS) Bundle Koopman Neural ODEs** can guarantee global convergence.
- **🛡️ Layered Safety Filters (Control Barrier Functions)**: A supervisor (CBF) overrides the neural MPC's decision to **rigorously enforce safety**. A **Physics-informed RNN for CLBF-MPC** uses an RNN to predict a CLBF as an MPC constraint to guarantee stability and safety.
In practice, the most reliable solutions for safety-critical systems combine multiple elements from these pathways. A powerful and increasingly common industrial approach is the **"MPC dataset + Lyapunov stability check"**: you train a neural network on data from a proven, safe (but computationally heavy) MPC. The NN acts as a fast policy, but if its control action threatens stability (checked via a Lyapunov constraint), you **fall back to a simple, safe controller** to guard against NN errors.
To close the certification gap, you must always anchor learning to a formal mathematical guarantee—Lyapunov, CBF, or robust uncertainty bounds—to ensure safety.
I hope this structured overview helps you position your work. Do any of these specific pathways—such as the practical details of the Lyapunov-constrained fallback method or the implementation of GP-MPC—align closely with your specific application? I can provide further details on any of them.
Cite
1 Recommendation
## Similar questions and discussions
Techniques for MPC optimization using Machine learning ?\\
Question\\
4 answers\\
- Asked 31 October 2018\\
- Muhammad Asad\\
How to optimize Model predictive controller using machine learning ? e.g. using Neural Network or fuzzy systems\\
View
How should I represent input variables for recurrent neural network design?\\
Question\\
5 answers\\
- Asked 14 February 2019\\
- Ali Kamali Mohammadzadeh\\
Dear colleagues,\\
I am trying to design a recurrent neural network to predict patients' length of stay as output. I have different types of data (numeric, categorical, free text, etc..) and I want to present the data as a time series( to capture the temporal dynamic of the system). It means I want the model to know when each piece of information is collected.\\
Here is my question:\\
1- What are the methods to feed the data into the model?\\
2- What are the advantages and disadvantages of each method? \\
View
Call for Papers - MDPI Energies - Special Issue: Model Predictive Control-Based Approach for Microgrids\\
Discussion\\
Be the first to reply\\
- Asked 25 January 2024\\
- Valerio Mariani
Dear network,\\
I am co-editing the Special Issue _"Model Predictive Control-Based Approach for Microgrids"_ with deadline on 20 July 2024.
If you are interested in the topic, please, checkout the attachments for further information (either, just click on https://lnkd.in/gA23Dvzb). I'd be really glad to have your wonderful next article submitted to it. Cheers!
PS: For any question, please don't heasitate to contact me!
View
HWho can help me GEKKO Python Based Optimization for my code ?\\
Question\\
2 answers\\
- Asked 13 February 2023\\
- Siye Kahsay
Dear sir/Madam\\
I am trying the foolowing idea:\\
Data\_Driven multi-objective optimization:
https://gekko.readthedocs.io/en/latest/ml.html
Machine Learning
Gekko specializes in optimization, dynamic simulation, and control.
The ML module in GEKKO interfaces compatible machine learning algorithms into the optimization suite
to be used for data-based optimization. Trained models from scikit-learn, gpflow, nonconformist,
and tensorflow are imported into Gekko for design optimization, model predictive control,
and physics-informed hybrid modeling.
"""
My main Target is I have 4 decison variable data and two column objective function data.
and I want to train first and then interfacing with GEKKO OptimiZation suite with following link ML models
link: https://gekko.readthedocs.io/en/latest/ml.html
Please help me fro problem of data-driven Multi-objective optimization using GEKKO and ML model trainings.
I can attach the code if someone willing to help me.
with best regards
View
How would you do a sensitivity analysis of a simple regression predictive model with two input parameters?\\
Question\\
4 answers\\
- Asked 1 February 2014\\
- Elliot Haruna Alhassan\\
Comments are welcome.\\
View
Is there anyway to reduce the propagated error during Multi step ahead prediction with recurrent neural network? \\
Question\\
3 answers\\
- Asked 19 February 2018\\
- Pezhman Kazemi\\
Hi guys,\\
As you know when predicting multi step ahead if there is even a small error between actual and predicted one at the beginning, this error will be propagated through all predicted values so i want to know if there is any way to reduce this error.\\
Thanks\\
View
Is there any free standard dataset for wind turbines to predict the power production?\\
Question\\
1 answer\\
- Asked 15 March 2014\\
- Vahid Nouri\\
I want to predict the power production of a wind turbine based on the weather of turbine place with an algorithm. Is there any standard or valid dataset for this application?\\
View
What is the benefit of using recurrent neural network over simple MLP neural network for dynamic system?\\
Question\\
7 answers\\
- Asked 12 February 2018\\
- Pezhman Kazemi\\
Hello Guys,\\
Suppose that we have a data from a chemical process. There are some inputs and one output, the output depends on those inputs and also the time. I am gonna identify this process. So what is the difference between using simple MLP with Lagged output as an input (lagging the output as an input to the model, like 5 step before) and using recurrent neural network such as ELMAN or JORDAN without lagging the output, because i know JORDAN is just feeding back one step before as an input. \\
Thanks\\
View
Neural Network Inputs\\
Question\\
4 answers\\
- Asked 24 June 2017\\
- Buddhi Wimarshana\\
Hi everyone,\\
I am trying to build an artificial neural network for some load predictions. So, as one of the inputs, I have selected the actual load at the (t-1) time to predict the load at time 't'. By doing that results seems great, which lead me to the following questions.\\
My question is, is there any theoretical problem in this kind of approach? Is this similar to the moving window approach ? if it's possible, could anyone point me to a paper where this kind of approach (target at t-1 is used as an input) is used?\\
I really appreciate your help regarding this.\\
Thanks in advance.\\
View
## Related Publications
Neural Modeling and Parameter Estimation
Chapter
- Feb 2021
- \\
Majeed Mohamed
- \\
Vikalp Dongare
The neural modeling of a dynamic system is presented in this chapter. The former literature reported that ordinary differential equations can be solved by an neural-network-based approach (Lagaris et al. 1998).
View
Guaranteed tracking and regulatory performance of nonlinear dynamic systems using fuzzy neural networks
Article
- Oct 1999
- \\
L. Behera
- \\
K.K. Anand
A new technique for the design of stable tracking and regulatory
control systems for nonlinear systems using fuzzy neural networks is
described. A class of nonlinear systems is considered where a few of the
input variables can be controlled while the rest are considered as
disturbances. System dynamics are modelled using a fuzzy neural network
wher...
View
Neuronale Modelle nichtlinearer dynamischer Systeme mit Anwendung auf Musiksignale (Neural Models of Nonlinear Dynamical Systems and their Application to Musical Signals)
Thesis
- Jan 1993
- \\
Axel Roebel
View
**Got a technical question?**
Get high-quality answers from experts.
Ask a question