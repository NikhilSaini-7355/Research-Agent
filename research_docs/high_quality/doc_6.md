Technische Universität München Fakultät für Elektrotechnik und Informationstechnik Lehrstuhl für Energiewirtschaft und Anwendungstechnik
**Comparison of optimization methods for model predictive control: An application to a compressed air energy storage system**
## Dipl.-Ing. Dennis Atabay
Vollständiger Abdruck der von der Fakultät für Elektrotechnik und Informationstechnik der Technischen Universität München zur Erlangung des akademischen Grades eines **Doktor-Ingenieurs (Dr.-Ing.)** genehmigten Dissertation.
**Vorsitzender:** Prof. Dr. rer. nat. Thomas Hamacher **Prüfer der Dissertation:**
1. Prof. Dr.-Ing. Ulrich Wagner
2. Prof. Dr.-Ing. Gunther Reinhart Die Dissertation wurde am 27.07.2017 bei der Technischen Universität München eingereicht und durch die Fakultät für Elektrotechnik und Informationstechnik am 13.04.2018 angenommen.
* * *
* * *
Für Motte ii
**Abstract**
In energy systems with a high share of renewable energy sources, electrical energy storage plays an important role in balancing energy production and demand. The optimal operation times of a storage can depend on locally available energy production (e.g. distributed solar battery storage) or external signals such as a time-sensitive electricity price (e.g. pumped hydroelectric energy storage). Model Predictive Control (MPC) is a modern control strategy that allows one to consider forecasts of future parameters, such as power production or electricity prices, and therefore has been widely applied to energy systems and storages in the last years. A model of the energy storage system is used to define and solve an optimization problem and find the optimal charging and discharging times. Since MPC is not a unique technique but rather a set of methodologies, different models and optimization methods can be used to solve the optimal control problem. In this thesis, a compressed air energy storage system is used to compare different opti- mization methods for MPC. Based on experimental investigations, the system parameters, such as the electrical round-trip efficiency, are calculated. A linear, a mixed-integer-linear and a nonlinear model of the system are developed and used for MPC. To compare the different optimization methods, MPC is used to minimize operational costs covering a given 24-hour air demand using a time-sensitive electricity price as an incentive. The experiments are performed for several scenarios with variations in air demand, electricity price, optimization timestep size and forecast quality. The results indicate that dynamic programming demonstrates the most cost savings throughout all performed experiments. For this application, it shows better results than the other two nonlinear optimization methods used in this thesis, genetic algorithms and mixed-integer nonlinear programming. Due to its detailed model, dynamic programming also clearly outperforms the linear programming method. The results using mixed-integer linear programming are only slightly different than with dynamic programming and even better in some specific cases.
* * *
iii
**Zusammenfassung**
In Energiesystemen mit einem hohen Anteil fluktuierender erneuerbarer Energien spielen Energiespeicher eine wichtige Rolle zum Ausgleich von Angebot und Nachfrage. Der optimale Einsatz von einzelnen Speichern kann dabei von vorhandenen lokalen Erzeu- gungsprofilen und Lasten (z.B. dezentrale PV Speicher) sowie variablen Strompreissig- nalen (z.B. Pumpspeicher) abhängen. Prädiktive Regelstrategien erlauben es zukünftige Ereignisse, wie die Vorhersage von Verbrauch und Erzeugung oder Strompreisverläufe, mit einzubeziehen und sind somit für die Regelung von Energiespeichern prädestiniert. Die modellprädiktive Regelung (Model Predictive Control, MPC) verwendet hierbei ein Modell zur Vorhersage des zukünftigen Verhaltens des Systems. Durch Lösen eines Optimierungsproblems basierend auf diesem Modell, können die zu wählenden Lade- und Entladezeitpunkte für den Speicher für die nächsten Minuten, Stunden oder Tage ermittelt werden. MPC beschreibt keinen exakten Algorithmus, sondern ein generelles Verfahren zur prädiktiven Regelung von Systemen. Dabei wurden im Rahmen einer modellprädiktiven Regelung von Energiespeichern bereits eine Vielzahl verschiedener Optimierungsmethoden angewendet. Diese Arbeit vergleicht verschiedene Optimierungsmethoden zur modellprädiktiven Rege- lung am Anwendungsbeispiel eines Druckluftspeichers. Auf Basis von messtechnischen Untersuchungen und der Bestimmung von verschiedenen Systemparametern, wie dem elektrischen Speichernutzungsgrad, wird ein lineares, ein gemischt-ganzzahlig lineares und ein nichtlineares Modell der Anlage entwickelt. Mit Hilfe dieser Modelle wird eine modellprädiktive Regelung des Speichers für einen Zeitraum von 24 Stunden durchgeführt. Ziel ist dabei die Deckung eines vorgegebenen Bedarfs mit minimalen Stromkosten. Für die drei Methoden werden jeweils mehrere Szenarien mit verschiedenen Verbrauchs- und Strompreisprofilen betrachtet. Zudem wird auch der Einfluss der Optimierungsschrittweite sowie der Genauigkeit der Verbrauchsprognose auf die Ergebnisse untersucht. Die Ergebnisse zeigen, dass bei Betrachtung aller durchgeführten Experimente mit Hilfe der dynamischen Programmierung die größten Kosteneinsparungen erreicht werden können. Für den untersuchten Anwendungsfall zeigt sich, dass die dynamische Pro- grammierung besser geeignet ist als die beiden anderen untersuchten nichtlinearen Optimierungsmethoden, der genetische Algorithmus und die gemischt-ganzzahlige nicht- lineare Programmierung. Aufgrund der genaueren Modellierung des System können auch im Vergleich zur linearen Programmierung deutlich bessere Ergebnisse erzielt werden. Die Kosteneinsparungen, die mit Hilfe der gemischt-ganzzahligen linearen Programmierung er- reicht werden können, sind im Vergleich zur dynamischen Programmierung nur geringfügig schlechter. Für bestimmte Szenarien werden hier sogar bessere Ergebnisse erzielt.
* * *
**Danksagung**
Die vorliegende Arbeit entstand im Rahmen meiner Tätigkeit als wissenschaftlicher Mi- tarbeiter am Lehrstuhl für Energiewirtschaft und Anwendungstechnik der Technischen Universität München. Ich habe diese Zeit sehr genossen und durfte viele Erfahrungen sammeln. Daher möchte ich mich an dieser Stelle bei allen bedanken, die mich in den letzten Jahren während meiner Promotion begleitet haben. Mein Dank gilt Herrn Prof. Dr.-Ing. Ulrich Wagner für das jederzeit sehr angenehme Betreuungsverhältnis und die große Freiheit in der Umsetzung meiner eigenen Ideen. Bei Herrn Prof. Dr.-Ing. Gunther Reinhart möchte ich mich für die Übernahme des Korreferats bedanken. Mein besonderer Dank gilt Herrn Prof. Dr. rer. nat. Thomas Hamacher für die lehrreiche gemeinsame Zeit am Lehrstuhl sowie für die Übernahme des Prüfungsvorsitzes. Ich bedanke mich bei allen Kollegen, mit denen ich während meiner Zeit an der TUM zusammenarbeiten durfte. Vielen Dank für die große Unterstützung in allen Bereichen, die zahlreichen Diskussionen und Gespräche sowie die sehr angenehme Atmosphäre am Lehrstuhl. Mein besonderer Dank gilt meiner Familie und meinen Freunden. Ich danke meinen Eltern für die große Unterstützung in allen Lebenssituationen, für die Möglichkeiten die sie mir dadurch in meinem Leben eröffnet haben und das in mich gesetzte Vertrauen. Ganz besonders danke ich meiner Frau, Verena Atabay, für ihr großes Verständnis und ihre Unterstützung während des gesamten Zeitraums meiner Arbeit.
Hamburg im Mai 2018
Dennis Atabay
* * *
Contents
1 Introduction 1
1.1 Introduction to Model Predictive Control..................... 2
1.2 Motivation..................................... 3
1.3 Objective and outline of this thesis........................ 3
2 Optimization methods for Model Predictive Control5
2.1 Linear programming............................... 5
2.2 Mixed-integer linear programming........................ 6
2.3 Mixed-integer nonlinear programming...................... 6
2.4 Genetic algorithm.................................. 7
2.5 Dynamic programming.............................. 8
2.6 Overview of the optimization methods used in this thesis............ 9
3 Compressed air energy storage system11
3.1 Compressed air constants and definitions..................... 11
3.2 Design of the compressed air energy storage system............. 12
3.3 Operation of the compressed air energy storage system............. 14
3.4 Experimental investigations............................ 17
3.4.1 Power consumption of the compressors.................. 17
3.4.2 Power consumption of the booster.................... 19
3.4.3 Round-trip efficiency........................... 20
3.5 Economic evaluation of the compressed air energy storage system...... 23
4 Optimization Models25
4.1 Objective function, sets, parameters, and variables............... 25
4.2 Linear programming model............................ 26
4.3 Mixed-integer linear programming model.................... 30
4.4 Nonlinear model................................. 35
4.5 Validation of the models............................. 42
4.5.1 Validation data.............................. 42
4.5.2 Results.................................. 43
5 Model Predictive Control of the compressed air energy storage system45
5.1 Implementation.................................. 45
5.1.1 Air demand time-series and forecast scenarios............. 46
5.1.2 Electricity price scenarios........................ 49
5.1.3 Optimization timestep size........................ 50
* * *
5.2 Preliminary investigations and optimization parameters............ 50
5.2.1 Reference values............................. 50
5.2.2 Influence of measurement inaccuracy and operation.......... 50
5.2.3 Optimization parameters.......................... 51
5.2.4 Comparison of the nonlinear optimization methods........... 52
5.2.5 Differences of the models in completely charging/discharging the storage 55
5.3 Results....................................... 57
5.3.1 Perfect air demand forecast........................ 57
5.3.2 Imperfect air demand forecast....................... 61
5.3.3 Influence of the optimization timestep size............... 65
5.3.4 Result summary............................. 73
6 Conclusion 75
ACompressed air energy storage system specifications77
BMathematical description of the models79
CValues of the constant model parameters103
List of Figures109
List of Tables 110
Bibliography 111
* * *
Chapter 1
Introduction
Reducing the worldwide greenhouse gas emissions in order to mitigate global warming is one
of the biggest challenges of today’s generation. To achieve its goal to reduce CO2 emissions
by 80 % compared to 1990 \[14\], one main part of Germany’s concept is to increase the share
of renewable energies in the electricity sector to 80 % by 2050 \[12\].
{\\mathrm O\_{2}}
In 2015, wind turbines and photovoltaic (PV) systems provided more than half of the renewable
electric energy in Germany \[15\]. Subsidized by the government, both have already shown
tremendous growth in the last years. Because of the fluctuation of wind and solar generation,
which cannot be accurately predicted, the need for flexibility in the power system increases
with their installation. Energy storages are one approach to provide this flexibility.
There are different concepts and subsidy programs to integrate energy storages in Germany’s
energy system. Large-scale electric energy storages that are directly connected to the grid,
such as pumped hydro storages, are exempt from demand charges and EEG surcharges \[12\].
In May 2016, a subsidy program for small-scale battery storages combined with a PV system,
which are mainly installed in the residential sector, was launched \[17\]. Also, for heat storages
in combination with acombined heat and power (CHP)unit \[13\] or a heat pump \[16\], subsidy
programs were initiated. Heat storages can provide flexibility to the electric power sector by
decoupling electricity production (CHP) or consumption (heat pump) and heat supply.
The optimal operation to maximize revenues or minimize costs of such storage (and generation)
The optimal operation to maximize revenues or minimize costs of such storage (and generation)
systems over a certain time horizon can depend on the given demand that has to be covered,
the availability of a variable energy resource and the electricity price curve.Model Predictive
Control (MPC)is an advanced method of system control that allows one to consider these
future parameters when calculating the next control action. MPC has been widely used for the
control of energy systems including storages in many recent publications.
* * *
1.1 Introduction to Model Predictive Control
Model Predictive Control(MPC), also known as model-based predictive control or recedinghorizon control, is a modern control strategy for the operation of systems. While this section
provides a short introduction toMPC, a detailed overview of the topic and its applications can
be found in the books \[89,19,87,36,55\] and survey papers \[72,67,26\].
The general idea ofMPCis to use an internal model of a system to predict its future behavior
over a given time horizon. The output of the system for each time sample t = 1:::N in this
horizon is calculated based on previous system inputs, outputs, states, and the proposed
optimal future control actions. This control sequence is calculated by solving an optimization
problem taking into account the objective function (e.g. minimizing costs) as well as constraints
for the system operation (e.g. covering the demand). At each instant, the first control signal of
the sequence is applied to the system and the new outputs and states are measured. Then the
horizon is displaced one timestep towards the future and the optimization problem is solved
again using the new information (receding strategy). The general structure ofMPCis shown in
Figure1.1\[19\].
Figure 1.1: General structure ofMPC
In contrast to classical control methods, such as PID controllers, in which the next control action
is calculated only based on previous measured inputs and outputs,MPCadditionally allows one
to consider predicted or already known future parameters. Because of its systematic account
for constraints and its feed-forward design,MPCshows better performance than non-predictive
control methods \[89, p. 5-6\]. Therefore, it has become the most widely accepted modern
control strategy \[55, p. 2\] and theMPCtechnology can be found in a wide variety of industrial
application areas \[84\].
* * *
1.2. Motivation
# 1.2 Motivation
Model Predictive Controlis a control strategy in which an optimal operation problem is repeat- edly solved over a rolling horizon in real time with updated information. Thus,MPCis not a unique technique, but rather a set of different methodologies that can be applied to control a system \[19, p. 4\]. Thereby, the model, which describes the dynamic behavior of the system, is the cornerstone ofMPC. The chosen model defines not only the accuracy of the prediction of the system behavior, but also the optimization method that can be used to calculate the control sequence. While linear or quadratic (convex) models are limited in their accuracy of predicting the system outputs, fast and reliable solvers are available to solve the optimization problem. In contrast, nonlinear models are able to predict the system outputs more accurately, but the implied optimization is computationally more intensive and, moreover, the convergence to a global optimum cannot be assured \[72\]. In the last years, several reviews of optimization methods for the (model predictive) control of energy systems containing storages, such as electric power systems \[5, 34, 102, 4, 41\], microgrids \[77, 31, 69, 37\], tri-generation systems \[99\],heating, ventilation, and air conditioning (HVAC)systems \[1\], and thermal energy storages \[79\] have been published. The commonly used optimization methods in these studies are linear programming (LP), mixed-integer linear programming (MILP), mixed-integer nonlinear programming (MINLP), dynamic programming (DP) and evolutionary computation algorithms1. All of these methods have already been applied to energy storage systems for experimental investigations. So far, however, there are no studies comparing the performance of the model predictive control of an energy storage using different optimization methods.
# 1.3 Objective and outline of this thesis
The objective of this thesis is to evaluate the influence of the model’s accuracy versus the computational effort and reliability of the optimization problem’s solution for the model predictive control of an energy storage. Therefore, different optimization methods for the MPC of an energy storage system are evaluated. They are applied to a compressed air energy storage (CAES) system to compare their performance under different scenarios. In chapter2 the optimization methods used in this thesis are introduced. For each method an overview of publications where they were used for the model predictive control of energy storage systems is given. **Chapter3 describes the design and operation of the compressed air energy storage (CAES)** system. As for typical compressed air systems in the industry, the CAES system consists of compressors, air treatment devices, and an air receiver tank. An additional booster is used to raise the pressure of the compressed air delivered by the compressors and store it in a high pressure storage tank. In this way, the electricity consumption and air supply can be decoupled. Based on experimental results a method for calculating the electrical round-trip efficiency of
1 There exist various different evolutionary computation algorithms that have been used for optimal control of energy system, such as particle swarm optimization or ant colony optimization. In this thesis the genetic algorithm (GA) is applied because it is the most commonly used method.
* * *
1. Introduction
the storage system is presented. Additionally, the specific storage costs of the CAES system are calculated and compared to battery storage systems. In chapter4 the mathematical descriptions of the CAES system models for each optimization method used in this thesis are given. Simulation results of the models are used to validate and compare them to measured data. In chapter5 these optimization models are used for the model predictive control of the CAES system, with the objective to cover a given air demand over 24 hours with minimal costs. The experiments are performed with different air demand and electricity price scenarios. Additionally, the influences of the optimization timestep size and the quality of the air demand forecast are investigated. **Chapter6 concludes the thesis.**
* * *
## Chapter 2
# Optimization methods for Model Predictive Control
In this chapter the optimization methods used in this thesis are introduced. For each method a literature overview of their application to Model Predictive Control (MPC) of energy systems including storage is given.
### 2.1 Linear programming
Linear programming(LP) problems are a subclass of convex optimization problems, where the objective function and all constraints are linear. As for all convex optimization problems, a local minimum of the objective functions is also a global minimum. In the last decades several effective methods for solvinglinear programming (LP)problems where developed, such as the simplex method and the interior point method. They can easily solve very big problems with hundreds of variables and thousands of constraints. The main drawback ofLPis that the behavior of many real-world systems can only be approximated, since all variables have to be real-numbered and all constraints and the objective function have to be linear. A general linear program, where the vector x is the optimization variable and the matrices A, G and the vectors _b, c, d, h are problem parameters that specify the objective and constraint functions, can be_ stated as follows. A detailed insight into the theory and practice oflinear programmingis given in \[8\] and \[86\].
minimize _c_ _T_ _x + d_ subject to _Gx h_ (2.1) _Ax = b_
In the last years various articles usingLPforMPCor optimal control of energy systems including storages have been published. Xie and Ilic \[103\] usedLPfor model predictive control of a small electric energy system containing intermittent renewable resources. An application of LPfor optimal scheduling of aCHPsystem with a battery unit and a thermal energy storage unit is presented by Majic et al. \[63\]. Ma et al. \[61\] propose aMPCtechnique usingLPto reduce costs for the operation of aHVACsystem. Further examples can be found in \[85,20,60,78\].
* * *
2.2 Mixed-integer linear programming
Mixed-integer linear programming(MILP) is a special case of the more general mixed-integer
programming. In MILP the objective function and constraints are linear. Some of the decision
variables are integers whereas others are continuous variables. Using integer or binary
variables allow a more detailed representation of energy systems than with LP by considering
e.g. start-up costs and part-load performance. State-of-the-art MILP solvers use a combination
of algorithms, such as branch-and-bound, cutting plane and heuristics. Although, they are
able to solve large problems with regard to the number of variables and constraints, the
computational effort compared to LP rises significantly due to the addition of integers to the
problem. An imporant advantage of these algorithms is that they provide an assessment of
the current solution. The time for solving a MILP depends upon the specific structure of the
problem and is thus hard to be estimated in general terms. Equation2.2states the general
formulation of a MILP with the integer variable vector y and the real variable vector x. The
matrices G, A, M, N and the vectors c, w, d, h, b are problem parameters that specify the
objective and constraint functions. Detailed mathematical foundations of integer programming
are presented in the textbook of Conforti \[22\].
\\begin{array}{r l r}{\ mathsf\ m i i i z e}&{c^{T}x+w^{T}y+d}\ {\\mathsf\ s u b j e c t,t\ }&{G x+M y\\leq h}\ &{}&{A x+N y=b}\ &{x\\in\\mathbb{R},y\\in\\mathbb{Z}}\\end{array}
(2.2)
Recently, MILP models have been used widely for the optimal control of energy systems
containing energy storages. They were used for the model predictive control of microgrids
including battery storage systems by Parisio et al. \[81, 82\], Palma-Behnke et al. \[80\], Bracco
et al. \[11\], and Kriett et al. \[56\]. An application of MPC using a MILP model for active load
management in a distributed power system containing a battery storage is presented by Zong
et al. \[107\]. Zhang et al. used MILP for model predictive control of industrial loads and energy
storage for demand response \[106\]. Stadler et al. used a MILP model for MPC of an energy
system in a building including heat and electric storages \[95\]. A MILP approach for model
predictive control of a residential HVAC system with a thermal energy storage is presented by
Fiorentini et al. \[28, 29\]. Further applications of MPC to energy systems with energy storages
using MILP can be found in \[70,68,10,65,66,101\]
2.3 Mixed-integer nonlinear programming
Mixed-integer nonlinear programming(MINLP) covers a wide range of mathematical optimization problems. In this thesis, MINLP refers to exact methods for solving problems where
the objective and constraint functions include non-convexities and the decision variables are
integers and continuous. There are some exact approaches to solve non-convex MINLP
problems, such as spatial branch-and-bound, branch-and-reduce and-branch-and-bound.
Although there are software packages available that can solve non-convex MINLPs to proven
optimality, relative small problems can still cause existing methods to run into serious difficulties.
* * *
2.4. Genetic algorithm Compared to MILP, solving MINLP problems requires a much higher computational effort and are much more time consuming. The survey paper by Burer and Letchford gives a good overview of non-convex MINLP \[18\]. The general formulation of a MINLP is given in equation
2.3, where the objective function f (x;y) is to be minimized finding the optimal values of the integer variable vector y and the real variable vector x. The constraints are defined by a number of inequality functions c _i_ and equality functions c _j_. Here, I and E are two disjoint sets of integers defining the number of constraints.
minimize _f (x;y)_ subject to _ci_(x;y) 0 8i 2 I (2.3) _c_ _j_ (x;y) = 0 8j 2 E _x 2 R;y 2 Z_
Compared to other optimization methods, mixed-integer nonlinear programming is rarely used for MPC of energy systems. Sachs et al. used MINLP for model predictive control of island energy systems including a battery storage \[90\]. A MINLP model for MPC of an energy storage system in the smart grid environment is used by Nojavan et al. \[76\]. Shirazi et al. \[92\] used a MINLP model for optimal scheduling of residential HVAC system including a battery system. Ma et al. \[62, 105\] used a nonlinear programming for model predictive control of a thermal energy storage in building cooling systems.
# 2.4 Genetic algorithm
Agenetic algorithm(GA) is a meta-heuristic optimization method inspired by biological evolution and the most popular technique within the more general class of evolutionary algorithms. The basic idea of GA is to create a population of candidate solutions (individuals) for the optimization problem. Each candidate solution is evaluated based on the value of the objective function (fitness). The best candidates are selected and used to create a new generation by crossover (creating a new child candidate by combining two or more parent candidates) and mutation (small random changes to an individual to explore the whole search space). The new generation population is then again evaluated and the loop continues until the last population meets a certain stopping criteria. GA can be applied to almost every optimization problem, such as non-convex, discrete, mixed-integer and black-box problems and only needs rough information of the objective function. Major disadvantages of GA are that solving big problems requires tremendously high time and that it gives no information about the quality of a solution. A detailed introduction to genetic algorithms is given in \[93\]. Because of its easy implementation, the genetic algorithm is often used for optimal control of energy systems. Jungwirth applied MPC with a GA to control heating and cooling of buildings, using the thermal building mass as heat storage \[42\]. Lipp used a GA for model predictive control of a micro CHP unit with a thermal energy storage \[43\]. Lujano-Rojas et al. used GA for optimizing the daily operation of battery energy storage systems under real-time pricing schemes. A MPC approach using GA for the operation of an energy smart home lab including an energy storage system is presented by Kochanneck et al. \[54\]. Further examples of using genetic algorithm for MPC can be found in \[3,64,73\]
* * *
2.5 Dynamic programming
Dynamic programming(DP) is an optimization technique introduced by Richard Bellman \[6\],
that can be applied to multistage decision problems requiring a sequence of interrelated
decisions. It is based on Bellman’s principle of optimality which states that a sub-policy of an
optimal policy for a given problem must itself be an optimal policy of the sub-problem. For a
given discrete-time dynamic system
x\_{t+1}=f\_{t}(x\_{t},u\_{t}),\ \ \ \ \ t=0,1,...,N-1
(2.4)
where xtrepresents the state of the system and utthe control (decision) at time period t, DP is
able to find the optimal policy = fu0;u1;:::;u g that minimizes the total costs given by
N 1
x\_{t}
u\_{t}
\\pi^{ _}=\\left{u\_{0}^{\\pi^{_}},u\_{1}^{\\pi^{ _}},...,u\_{N-1}^{\\pi^{_}}\\right}
\\mathcal{J} _{\\pi}(x_{0})=g\_{N}(x\_{N})+\\sum\_{t=0}^{N-1}g\_{t}(x\_{t},u\_{t}^{\\pi})
(2.5)
for the given starting state x0and the given cost functions gt.
\ {cal g\_{t}}
x\_{0}
To calculate the optimal policy, the DP algorithm proceeds backward1 in time (from t = N 1
to t = 0) and calculates the optimal decision utto minimize the current (gt) and following
(Jt+1) costs for each possible state xt.
\\pi^{\*}
t=N-1
\ boldsymbol u{}\_{t}^{\*}
\ g()
t=0)
(\\mathcal{J}\_{t+1})
x\_{t}
J\_{N}(x\_{N})=g\_{N}(x\_{N})
(2.6)
J\_{t}(x\_{t})=\\operatorname\*{{m n n}} _u u{t}(x_{t},u\_{t})+J\_{t+1}\\left(f\_{t}(x\_{t},u\_{t})\\right)
(2.7)
\\mathcal{J} _{\\pi}^{\*}(x_{0})
\\pi^{\*}
x\_{0}
step of this algorithm.
DP can deal with every problem given in this form, including non-convex, non-continuous,
non-differentiable and black-box functions and is able to find the global optimal solution of a
problem. If the state space is not already a finite set, it has to be discretized, which may lead
to suboptimal solutions. The computational requirements are depending on the number of
possible values of x and the number of possible decisions u as well as on the number of time
periods t. Therefore, DP can become quite time-consuming for very big problems (known as
Bellman’s curse of dimensionality). A detailed insight into the theory and practice of dynamic
programming is given by Bertsekas in \[7\].
A forward in time implementation of the DP algorithm is also possible
* * *
2.6 Overview of the optimization methods used in this thesis
Table2.1summarizes the optimization methods used for MPC in this thesis with their advantages and disadvantages. Linear programming is very limited in the available expression
to model the system, but is able to solve the optimization problem fast and reliable. With
mixed-integer linear programming the accuracy of the model, as well as the computational
effort of solving the problem, increases. The nonlinear optimization models, MINLP, GA and
DP, are able to represent complex interactions of the system very detailed, but require a very
high computational effort to solve the problem.
Table 2.1: Optimization methods used in this thesis with their advantages and disadvantages
(based on \[57,25,86\])
| Method | Advantages | Disadvantages |
| Linear programming(LP) | -Scales well to big problems- Globally optimal solution attainable | -Very limited expressions available- Complex interactions difficult or impossible to represent |
| Mixed-integer linear programming(MILP) | -Can scale well to big problems-Complex interactions representable-Quality of solutions can be assessed | -Bad worst-case complexity-Global optimum often not attainable |
| Mixed-integer nonlinear programming(MINLP) | -Complex interactions fully representable-High freedom of expression | -Scales horribly to big problems |
| Dynamic programming(DP) | -Full freedom of expression(can also be used with"black box" models)-Globally optimal solution of the discretized system attainable | -Scales horribly to big problems(Bellman's"curse of dimensionality")-Continuous variables must be discretized which may lead to a suboptimal solution |
| Genetic algorithm(GA) | -Full freedom of expression(can also be used with"black box" models) | -Scales horribly to big problems-Quality of solutions impossible to assess |
* * *
* * *
## Chapter 3
# Compressed air energy storage system
To evaluate the different methods of control optimization, they are applied to a real energy storage test system. Therefore, a small-scalecompressed air energy storagesystem is used. It represents a typical compressed air system in the industry that is used to cover a given air demand. An additional booster allows one to store compressed air in high-pressure storage tanks. The air from these tanks can then be used to cover the air demand without the compressors running. Thereby, the electricity consumption of the system can be influenced and adapted to a given incentive. In this chapter at first the design and the operation modes of thecompressed air energy storage (CAES)system are introduced. Then the results for different experimental investigations are shown. These results are used to calculated the specific costs of the CAES system and compare them with battery storage systems.
### 3.1 Compressed air constants and definitions
Pressure is defined as force per unit area. There are three different categories for pressure measurement. The absolute pressure p _a_ is zero referenced to a complete vacuum, while the gauge pressure p _g_ is defined as the pressure referenced against the atmospheric pressure. The differential pressure p _d_ measures the difference between two unknown pressures \[9, p. 145\]. Although the SI unit of pressure is Pascal (Pa), in the compressed air industry the pressure is usually depicted in bar gauge pressure. The pressure sensors used in the compressed air system also have bar gauge pressure as output. In this thesis p _a_ indicates the absolute pressure and is given in Paaor bara, while p _g_ given in the units Pagor bargshall indicate the gauge pressure. Compressed air flow, like thefree air delivery(FAD) of the compressors or the compressed kg air demand represent the mass flow m\_ of the air with the SI unit s . In the compressed air industry air flow is usually given as normal (or standard) volumetric flow V\_ _n_ with the unit m3n standard (or normal) cubic meters per minute ( min ). This represents a volumetric flow of the air converted to standardized conditions of temperature T _n_ and pressure p _n_, often referred as normal temperature and pressure or standard temperature and pressure. Using the ideal gas
equation of state (3.2) \[71, p.127\], where p is the pressure, V the Volume, m the mass, Rsthe
specific gas constant and T the temperature of the gas, the mass flow m\_ can be converted to
the normal volumetric flow V\_n(and vice versa) given the standard conditions pnand Tn.
R\_{s}
\\dot{v}\_{n}
p\_{n}
T\_{n}
p\\cdot V=m\\cdot R\_{s}\\cdot T
(3.1)
\\dot{V} _{n}=\\dot{m}\\cdot\\frac{R_{s}\\cdot T\_{n}}{p\_{n}}
(3.2)
There are a variety of normal or standard conditions for temperature and pressure established
by different organizations. In this thesis these reference values are defined to pn= 1:0 bara
and Tn= 273:15 K as per ISO 8778:2003. The specific gas constant of air is defined as
Rs;air= 287:0 \[71, p.123\]. All constants used for compressed air calculations are shown
kgJ K
in table3.1
T\_{n}=273.15,\\mathsf{K}
p\_{n}=1.0,{\\sf b a r}\_{}
\\begin{array}{r}{R\_{s,a i r}=287.0,\\frac{\\mathsf{J}}{\\mathsf{k a}.\\mathsf{K}},\[7mathsf{1},\\mathsf{p}.1\ {23}\]}\\end{array}
Table 3.1: Constants used for compressed air calculations
| Symbol | Value | Unit | Description |
| $p\_{n}$ | 1.0 | bar $a$ | Normal condition for pressure |
| $T\_{n}$ | 273.15 | K | Normal condition for temperature |
| $R\_{s,air}$ | 287.0 | J/kg·K | Specific gas constant of air |
p\_{n}
\ _T_{n}
\\mathsf{K}
R\_{s,\ \\it a i r}
\\frac{\\textbf{J}}{\\mathfrak{K g}\\cdot\\mathfrak{K}}
3.2 Design of the compressed air energy storage system
The compressed air energy storage system is located at the Technical University of Munich and
represents a typical compressed air system in the industry with an additional high-pressure
compressed air storage. Figure3.1shows the structure of the test system. The compressed
air is produced by three rotary screw compressors with a total maximumfree air delivery(FAD)
of 2.53 and a maximum output pressure of 11 bar. The air treatment consists of two dryers
min
and two filters. The air receiver tank, with a volume of 2 m, is used to reduce compressor
cycling. To simulate an arbitrary compressed air demand, a control valve is used, through
which the air is released into the ambient. A reciprocating compressor (booster) that is able to
boost the compressed air from the rotary screw compressors up to a pressure of 38 bar allows
one to store the air in two high-pressure storage tanks with a volume of 2 m, each. The air
from these tanks can be fed back into the system by opening the outlet valve. To prevent a
pressure increase in the low-pressure part of the system when the the outlet valve is open, a
pressure regulator is used.
The electric power consumption of the compressors and the booster as well as the temperature
The electric power consumption of the compressors and the booster as well as the temperature
and the gauge pressure at three different positions is measured and stored with a time
resolution of one second. Table3.2provides an overview of all measured and calculated values
of theCAESsystem.
The technical data of the compressors are shown in table3.3, information about the other
2.53,\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i}}
The technical data of the compressors are shown in table3.3, information about the other
components can be found in appendixA.
2,m^{3}.
* * *
Figure 3.1: Schematic representation of the compressed air energy storage test system
| Symbol | Unit | Description |
| $p\_{1}$ | bar $g$ | Gauge pressure at compressors output |
| $p\_{2}=p\_{sys}$ | bar $g$ | System gauge pressure(after dryer and filter) |
| $p\_{3}=p\_{sto}$ | bar $g$ | Gauge pressure in high-pressure storage |
| $T\_{1}$ | K | Temperature at compressors output |
| $T\_{2}$ | K | Temperature after dryer and filter |
| $T\_{3}$ | K | Temperature in high-pressure storage |
| $P\_{1}$ | kW | Electric power consumption of compressor C1 |
| $P\_{2}$ | kW | Electric power consumption of compressor C2 |
| $P\_{3}$ | kW | Electric power consumption of compressor C3 |
| $P\_{4}=P\_{bo}$ | kW | Electric power consumption of booster |
| $P\_{co}$ | kW | Sum of electric power consumption of compressors C1,C2andC3 |
| $P\_{tot}$ | kW | Sum of electric power consumption of compressors and booster |
| $E\_{tot}$ | kWh | Sum of electric energy consumption of compressors and booster |
p\_{1}
b a r\_{9}
T\_{1}
p\_{2}=p\_{s y s}
b a l\_{9}
\ {cal Gamma\_\_{2}}
p\_{3}=p\_{s t o}
b a l\_{9}
\ 7}\_{3}
P\_{1}
P\_{2}
P\_{3}
Table 3.3: Technical specifications of the compressors from manufacturer KAESER
P\_{4}=P\_{b o}
P\_{c o}
(\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i n}})
P\_{t o t}
E\_{t o t}
* * *
3.3 Operation of the compressed air energy storage system
As shown in figure3.2, thecompressed air energy storagesystem is controlled by two different
components. TheSigma Air Manager (SAM)from KAESER Compressors controls the three
screw compressors, such that the system pressure psysstays above the setpoint of the
system pressure p^syswithin a given pressure range ^psys(p^syspsysp^sys+ ^psys). It
decides which compressors are running to cover the actual air demand. The control software
implemented in LabVIEW directly controls the outlet valve, the control valve and the booster.
Additionally, it communicates with theSAMand is able to specify the setpoint of the system
pressure p^sysand to turn off all compressors.
p\_{s y s}
\\hat{p}\_{s y s}
\\Delta\\hat{\\rho} _{s y s}\ (\\hat{\\rho}_{s y s},\\leq,p\_{s y s},\\leq,\\hat{\\rho} _{s y s}+\\Delta\\hat{\\rho}_{s y s})
\\hat{p}\_{s y s}
Figure 3.2: Control of the compressed air energy storage test system
Figure3.3shows an example of the system behavior of all three operation modes, based on
the time curves of measured system pressure psysand storage pressure pstoas well as power
consumption of the compressors Pco, of the booster Pboand the total power consumption Ptot.
Additionally, the target operation mode ^ applied by the control schedule and the concrete
operation mode assigned by the superior mode controller are shown. For this example, the
compressed air demand is kept constant at 0.9.
min
In normal operation mode (t < t1, t2 t < t3 and t > t4), the complete air demand V\_ is
p\_{s y s}
P\_{c o}
\\Theta
\\Theta
\\hat{\\Theta}
\\hat{\\Theta}
0.9,\ {frac\\{{{sfsf m}} _{n}^{3}}{\ {\\sf m}_{n}^{3}}}
min
In normal operation mode (t < t1, t2 t < t3 and t > t4), the complete air demand V\_dis
\\dot{V}\_{d}
(t<t\_{1},,t\_{2}\\leq t<t\_{3}
t>t\_{4}, r
3.3. Operation of the compressed air energy storage system a
covered by the compressors that are controlled by theSAM. The booster is switched off and
the outlet valve of the storage is closed. The setpoint of the system pressure p^sysis set to the
norm
normal setpoint pressure p^sys.
During the operation mode charge (t1 t < t2), the booster is running and the high-pressure
sys
During the operation mode charge (t1 t < t2), the booster is running and the high-pressure
storage is filled. The compressors are controlled by theSAMand have to cover the complete
air demand V\_dand the air consumption of the booster. If the sum of the air demand and the
flow rate of the booster exceeds the maximumfree air delivery (FAD)of the compressors, this
will lead to a pressure decrease in the system. To avoid this, a system-pressure-dependent
hysteresis is implemented in thesuperior mode controller (SMC). If the system pressure drops
under the value of the lower bound of the hysteresis psys, the concrete operation mode is
set to normal by theSMC. TheCAESsystem stays in this mode until the upper bound of the
hysteresis psysis reached or a new target operation mode is applied.
When the storage pressure reaches the maximum pressure level p, the concrete operation
\\dot{v}\_{d}
\\bar{p}\_{\\mathrm{c v s}}^{c h}
hysteresis psysis reached or a new target operation mode is applied.
When the storage pressure reaches the maximum pressure level psto, the concrete operation
mode is set to normal. The state of the storage is set to full until the operation mode
mode is set to normal. The state of the storage is set to full until the operation mode
discharge is applied, even if the pressure drops below the maximum pressure p
a temperature decrease or leakage losses. When the target operation mode =
applied while the storage is in the full state, the concrete operation mode
theSMC(t2 t < t2).
The state of the storage is set to full until the operation mode
discharge is applied, even if the pressure drops below the maximum pressure pstobecause of
a temperature decrease or leakage losses. When the target operation mode = ^ charge is
applied while the storage is in the full state, the concrete operation mode is set to normal by
\ \_{s y s}^{c h}
(t\_{2}\\leq t<t\_{?}^{\*})
Since the booster has a maximum compression ratio of rbo= 4, the input pressure of the
booster (which is the system pressure psys) has to be adapted during charge mode. If the
storage pressure pstois greater than the system pressure psysmultiplied by the compression
ratio rbominus an offset of 1 bar for safety, the setpoint of the system pressure p^sysis calculated
by dividing the actual storage pressure pstoby the compression ratio rboand adding an offset
\\overline{{p}}\_{s t o}
\\overline{{p}} _{s t_{0}}
\\Theta
p\_{s t o}
r\_{b o}
p\_{s t o}
r\_{b o} of 0.5 bar (t1 t < t20). Otherwise the setpoint of the system pressure is set to the normal
norm
system pressure p^sys(t1 t < t20). For a maximum compression ratio of rbo= 4 the system
pressure has to be adapted for storage pressures psys> 23 bar .
(t\_{1}\\leq t<t\_{2}^{\\prime})
\\hat{p} _{s y s}^{n o r m}\\left(t_{1}\\leq t<t\_{2}^{\\prime}\\right)
r\_{b o}=4
p\_{s y s}>23,\\mathsf{b a r}
\\hat{p} _{s y s}=\\begin{cases}{p_{s t o}/r\_{b o}+0.5,\\mathsf{b a r}\\quad\\mathrm{i f}\\quad\\quad p\_{s t o}>p\_{s y s}\\cdot r\_{b o}-1,\\mathsf{b a r},}\ {\\hat{\\beta}\_{s y s}^{n o r m}\\qquad\\qquad\\mathsf{e l s e}.}\\end{cases}
(3.3)
Depending on which value is higher, the setpoint of the system pressure is either set to the
norm
normal system pressure p^sys= p^sys(t1 t < t20) or calculated depending on the actual
storage pressure p^sys= psto=rbo+ 0:5 bar (t20 t < t2).
In discharge operation mode (t3 t < t4), all compressors and the booster are turned
\\hat{p} _{s y s}=\\hat{p}_{s y s}^{n o r m}\\left(t\_{1}\\leq t<t\_{2}^{\\prime}\\right)
\\hat{p} _{s y s}=p_{s t o}/r\_{b o}+0.5
(t\_{2}^{\\prime}\\leq t<t\_{2})
In discharge operation mode (t3 t < t4), all compressors and the booster are turned
off. The outlet valve is opened and the complete air demand V\_dis covered by the air in the
high-pressure storage. When the storage pressure reaches the minimum pressure level psto,
the outlet valve is closed and theCAESsystem is set to normal operation mode. The state of
the storage is set to empty until the operation mode charge is applied, even if the pressure
exceeds the minimum pressure again because of a temperature increase. When the storage
is in the empty state and the target operation mode ^ is set to discharge, theSMCassigns
the concrete operation mode = normal and prevents the system from being discharged
(t4 t < t4).
Table3.4shows the control parameters of theCAESsystem used for all experiments in this
(t\_{3},\\leq,t,<,t\_{4})
\\dot{V}\_{d}
\\hat{\\Theta}
(t\_{4}\\leq t<t\_{4}^{\*})
Table3.4shows the control parameters of theCAESsystem used for all experiments in this
thesis.
Table 3.4: Control parameters of theCAESsystem used in this thesis
| Symbol | Value | Unit | Description |
| $\\hat{p}\_{sys}^{norm}$ | 6 | bar$\_{g}$ | Normal setpoint pressure |
| $\\Delta \\hat{p}\_{sys}$ | 0.5 | bar | Pressure range of the SAM |
| $\\bar{p}\_{sto}$ | 38 | bar$\_{g}$ | Maximum storage pressure |
| $\\underline{p}\_{sto}$ | 7 | bar$\_{g}$ | Minimum storage pressure |
| $\\underline{p}\_{sys}^{ch}$ | 5.9 | bar$\_{g}$ | Lower bound of the SMC system pressure hysteresis during charge |
| $\\bar{p}\_{sys}^{ch}$ | 6.4 | bar$\_{g}$ | Upper bound of the SMC system pressure hysteresis during charge |
\\hat{p}\_{s y s}^{n o r m}
\\mathsf{b a r}\_{\\mathsf{g}}
\\Delta\\hat{p}\_{s y s}
\\overline{{p}}\_{s t o}
\\underline{{p\_{s t o}}}
\ a r\_{9}
\ a a r\_9
\\mathsf{b a r}\_{\\mathsf{g}}
\\underline{{p\_{s y s}^{c h}}}
\ a{mathfrak r}\_{9
\\bar{p}\_{s y s}^{c h}
* * *
3.4 Experimental investigations
To investigate the behavior of thecompressed air energy storage(CAES) system, several
experiments measuring the power consumption of the compressors and the booster for different
operating conditions were performed. The obtained results are used for the calculation of the
parameters needed to identify different models of theCAESsystem (see chapter4) as well as
for an economic evaluation of the system (see section3.5).
3.4.1 Power consumption of the compressors
The electric power consumption of the compressors was measured during normal operation
mode for different air flows and system pressures. For each measurement the operating
state was kept constant for three hours and the mean power consumption was calculated.
Each measurement was performed three times and the mean value was calculated to reduce
the influence of measurement errors. As shown in figure3.4the power consumption of the
compressors increases monotonically with the air flow. The compressors also consume more
power for higher system pressures. The influence of the system pressure depends on the air
flow. For very small air flows, there is only little difference of the power consumption between
the different system pressures, while for high air flows the influence of the system pressure
increases.
The results also show that the maximumfree air delivery(FAD) of the compressors decreases
The results also show that the maximumfree air delivery(FAD) of the compressors decreases
for higher output pressures \[45, 46, 47\]. For a setpoint pressure of 8 bargand higher, the
compressors are not capable of covering an air demand over 2.5.
min
8,{\\tt b a a}\_{mathfrak g}
2.5,\ {\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i n}}}
Figure 3.4: Power consumption of the compressors for different air flows and system pressures in
In figure3.5the specific power consumption of the compressors is illustrated. The specific
power consumption can be calculated by dividing the electric power consumption of the com-n
pressors by the air flow.m
Figure 3.5: Specific power consumption of the compressors for different air flows and pressures
For very small air flows, the system has a high specific power consumption. The reason is
that for an air demand which is lower than the minimumFADof each compressor, one or
that for an air demand which is lower than the minimumFADof each compressor, one or
more compressors are repeatedly switched on and off to cover the demand. This generates
additional losses during start-up and shut-down. As shown in figure3.6, for a constant air
demand of V\_d= 0:2 theSAMcontroller regulates the compressors differently depending
min
on the setpoint pressure. While for setpoint pressures of p^
mostly just the smallest compressor SX6 is used, for a setpoint pressure of p^
always the compressors SX6 and SM12 SFC are switched on and off together. Because of
this, the specific power consumption for p^sys= 10 bar
For increasing air flows, the specific electric power consumption of the system generally
decreases. But as shown in figure3.5, this descent is not monotonic. For a constant setpoint
pressure of p^sys= 6 bargand an air flow of 0.9
flow of 1.3. The reason is the part-load efficiency curve of the variable frequency drive
min
compressor SM12 SFC. The SM12 SFC is constructed to have its best efficiency at a frequency
of 50 Hz, which corresponds to aFADof about 0.9
\[53\]. If theFADdiffers from this value, the specific power consumption of the SM12 SFC
increases. As shown in figure3.6, for p^sys= 6 bar
air for the operation points V\_d=0.7 and V\_d
min
SFC compared to its best operation point leads to an increase of the specific electric power of
that for an air demand which is lower than the minimumFADof each compressor, one or
more compressors are repeatedly switched on and off to cover the demand. This generates
additional losses during start-up and shut-down. As shown in figure3.6, for a constant air
theSAMcontroller regulates the compressors differently depending
on the setpoint pressure. While for setpoint pressures of p^sys= 6 bargand p^sys= 10 barg
mostly just the smallest compressor SX6 is used, for a setpoint pressure of p^sys= 7 barg
always the compressors SX6 and SM12 SFC are switched on and off together. Because of
= 10 bargis lower than for p^sys= 7 barg.
For increasing air flows, the specific electric power consumption of the system generally
decreases. But as shown in figure3.5, this descent is not monotonic. For a constant setpoint
and an air flow of 0.9 the specific power is lower than for an air
min
. The reason is the part-load efficiency curve of the variable frequency drive
compressor SM12 SFC. The SM12 SFC is constructed to have its best efficiency at a frequency
of 50 Hz, which corresponds to aFADof about 0.9 at a system pressure of p^sys= 6 barg
min
If theFADdiffers from this value, the specific power consumption of the SM12 SFC
= 6 bargthe SM12 SFC delivers less than 0.9
min
= 1:3. The efficiency decrease of the SM12
min
SFC compared to its best operation point leads to an increase of the specific electric power of
min min
SFC compared to its best operation point leads to an increase of the specific electric power of
the system.
\ sin\\alpha=\\cos
\\hat{p} _{s y s}=10,\\mathsf{b a r}_{9}
\\begin{array}{r}{\\dot{V} _{d}=0.2\\frac{\\mathfrak{m}_{mathsf n}^33}{\ {\\sf m i}}}\\end{array}
\\hat{p} _{s y s}=7,\\mathsf{b a r_{9}}
\\boldsymbol{\\cdot}\\hat{p} _{s y s}=10,\\mathsf{b a r}_{\\up{}}
\\hat{p} _{s y s}=7,\\mathsf{b a r}_{9}
\\hat{p} _{s y s}=6,\\mathsf{b a r_{9}}
\ 10.9,\\frac{\\mathsf{m} _{mathsf{n}}^{3}}{\\mathsf{m}_{\\mathsf{n}}^{3}}
\\hat{p} _{s y s}=6,\\mathsf{b a r}_{9}
1.3,\ {frac\\{{{mathsfmathfrak m m}}^{3}}{,{\\mathrm{m i n}}}}
0.9,\\frac{\\mathsf{m}^{3}}{\\mathsf{m}^{3}}
\\hat{p} _{s y s}=6,\\mathsf{b a r}_{9}
\\dot{V} _{d}=1.3,\\frac{\\mathsf{m}_{\\mathsf{n}}^{3}}{\\mathsf{m n}}
* * *
3.4. Experimental investigations For a system pressure of p^ _sys_ = 10 bargthe best efficiency at a frequency of 50 Hz of the
mn SM12 SFC corresponds to aFADof about 0.8 min \[53\]. Together with a reduced maximum air delivery for higher system pressures this causes a different operation of the compressors by theSAMcontroller as for lower system pressure (see figure3.6). Therefore, in contrast to _p^sys_ = 6 barg, the specific electrical power consumption increases with the air flow for values m3nm3n between 0.7 min and 1.3 min for a system pressure of p^ _sys_ = 10 barg, as shown in figure3.5. Thus the specific electrical power consumption of the system for a certain operation point depends on how the three compressors are controlled by theSAM. The combination of three different compressor models and the part-load dependent efficiency of the variable frequency drive compressor SM12 SFC causes a nonlinear dependence of the electrical power consumption on the air demand and the system pressure. g ) r a SM12 SFC SM12 SX6 b W 3 3 3 3 (k _Vd_ = 0\. 2 m i _V_ n _d_ = 0\. 7 m i _V_ n _d_ = 0\. 9 m _V_ i n _d_ = 1\. 3 m 0i n mnmnmnmn
r10 1 e = w5 r _ysg_ o a _s_ p 0 _pb_ l a 10 7 ic = r t 5 _ysg_ r _s_ lc a e l 0 _pb_
E 6 10 = 5 _ys_ _s_ 0 _p_ 0 10 20 0 10 20 0 10 20 0 10 20 Time (minutes)
Figure 3.6: Measured power consumption of the individual compressors for different exemplary
air flows and system pressures
## 3.4.2 Power consumption of the booster
The electric power consumption of the booster was measured with a resolution of one second, while the high pressure storage was completely charged from an empty state (p _sto_ = 7 barg) to the maximum pressure of p _sto_ = 38 barg. To reduce the influence of measurement errors, the experiment was performed five times. Figure3.7shows the power consumption of the booster in relation to the storage pressure. The illustrated mean value was calculated for linear discretized pressure ranges of 0.1 bar. The increase of the system pressure at a storage pressure of 23 bar (see eq.3.3) results in a change of the power curve. The few points with a higher power consumption at a storage pressure of 7 bar are caused by the start-up of the booster.
* * *
Figure 3.7: Power consumption of the booster
3.4.3 Round-trip efficiency
The round-trip efficiency of an energy storage is described by the ratio of energy a full energy
storage can deliver until it is empty (discharge energy Edch) to the energy needed to completely
charge an empty storage (charge energy Ech).
\\gamma=\\frac{E\_{d c h}}{E\_{c h}}
(3.4)
Thecompressed air energy storagesystem described in this chapter, is used to shift the
electrical energy demand. To describe theCAESsystem as an electrical energy storage, the
electrical efficiencyelhas to be calculated.
\\eta\_{e f}
electrical efficiencyelhas to be calculated.
The electrical power consumed by the compressed air system during charging, is used to
deliver the air needed to charge the storage as well as to cover the air demand V\_d. To calculate
the power that is used only for charging the storage, the reference power Prefneeded to
deliver the air demand has to be subtracted from the measured power Ptotof the system.
Thereby Prefis the power the compressors would consume in normal operation mode to
cover the air demand V\_d, which corresponds to the power consumption of the compressors
norm
for p^sys= p^sys= 6 barg(see figure3.4). The charge energy Echcan be calculated by
integrating the difference of Ptotand Prefover the charging time (t0chto t1ch), as shown in
figure3.8.
\\dot{v}\_{d}
P\_{r e f}
P\_{r e f}
P\_{t o t}
\\hat{p} _{s y s}=\\hat{p}_{s y s}^{n o r m}=6,\\up{\\sf b a r}\_{9}
P\_{t o t}
(3.5)
P\_{r e t}
E\_{c h}=\\int\_{t\_{0}^{c h}}^{t\_{1}^{c h}}\\left(P\_{t o t}\\left(t\\right)-P\_{r e f}\\left(t\\right)\\right)d t
t\_{1}^{c h}
* * *
3.4. Experimental investigations
TheCAESsystem is not able to deliver electrical energy during discharging. But because the
air demand V\_dis covered by the air out of the storage, the compressors are turned off, which
leads to a reduction of the power consumption of theCAESsystem by Pref. The reference
power Prefhere again is the power the compressors would consume in normal operation mode
to cover the air demand. When the compressors are turned off, they still consume electrical
power because of their stand-by losses which correspond to the measured total electrical
power Ptot. Thus the charge energy Edchcan be calculated by integrating the difference of
Prefand Ptotover the discharging time (t0dchto t1dch, see figure3.8).
\\dot{V}\_{d}
P\_{r e f}
P\_{r e f}
P\_{t o t}
E\_{d c h}
(t\_{0}^{d c h}
P\_{t o t}
P\_{r e f}
t\_{1}^{d c h}
E\_{d c h}=\\int\_{t\_{0}^{d c h}}^{t\_{1}^{d c h}}\\left(P\_{r e f}\\left(t\\right)-P\_{t o t}\\left(t\\right)\\right)d t
(3.6)
Figure 3.8: Charge and discharge energy for one full cycle of the storage with a constant air
demand
When theCAESsystem is charged, the setpoint of the system pressure p^syshas to be increased for high storage pressures (see section3.3). As shown in figure3.4, an increased
system pressure leads to a higher electrical power consumption of the compressors, depending
on the air flow. During charging, the compressors have to cover the air flow into the storage
as well as the air demand V\_d. Therefore, the CAES system cannot be charged for high air
demands. Since the air flow into the storage is constant when the booster is running, the power
consumption of the compressors during charging and therefore the charge energy Echof the
CAESsystem depends on the air demand. To determine the influence of V\_don the charge
energy Ech, measurements for different air demands where performed. Therefore, V\_dwas
kept constant while the empty storage was completely charged. For each air demand the mean
value of at least three measurements were calculated to reduce the influence of measurement
errors. The results are shown in figure3.9. As expected, the charge energy generally increases
\\begin{array}{c}{{^{r s s}}}\ {{^{3.4,}}}\\end{array}
\\dot{v}\_{d}
\\dot{v}\_{d}
E\_{c h} m3
for higher air demands. The deviation for an air demand of 0.7 is a consequence of the
min
nonlinear dependence of the electrical power consumption on the air demand and the system
pressure (see section3.4.1).
0.7,{\\frac{\\mathsf{m}^{3}}{\\mathsf{m i n}}}
The experiments to determine the discharge energy Edchwere performed in the same way
as for the charge energy. When a full high-pressure storage is completely discharged, approximately the same amount of air can be retrieved from the storage, independent from the
actual air demand. But the reference power Prefused to calculate the discharge energy Edch,
which is the power the compressors would consume in normal operation mode to cover the air
demand, does depend on the air demand of the system. Therefore, the dependence of the
discharge energy Edchon the air demand is related to the specific power consumption of the
norm
compressors for p^sys= p^sys= 6 bargas shown in figure3.5. The discharge energy Edchof
theCAESfor different air demands during discharging is also illustrated in figure3.9.
E\_{d c h}
P\_{r e f}
E\_{d c h:}
E\_{d c h}
E\_{d c h}
\\hat{p} _{s y s}=\\hat{p}_{s y s}^{n o r m}=6,\\up{\\sf b a r}\_{9}
Figure 3.9: Charge and discharge energy for different air demands during charging and
discharging
Using the values for the charging energy Echand the discharging energy Edchof figure3.9,
the electrical round-trip efficiencyelof thecompressed air energy storagecan be calculated
with equation3.4. As shown in figure3.10, the round-trip efficiency has its maximum value
of 86.76 % for an air demand of V\_d= 0:2 during charging and discharging. The minimum
min
round-trip efficiency of 52.47 % occurs for an air demand of V\_d= 1:3 during charging and
min
V\_d= 2:4 during discharging.
min
E\_{c h}
\\eta\_{e I}
E\_{d c h}
\\begin{array}{r}{\\dot{V} _{d}=0.2\\frac{m_{n}^{3}}{m\_{n}}}\\end{array}
\\dot{V} _{d}=1.3,\\frac{\\mathsf{m}_{mathsf n}^{3}}{\\mathsf{m i n}}
\\dot{V} _{d}=2.4,\\frac{\\mathsf{m}_{n}^{3}}{\\mathsf{m i n}}
* * *
3.5. Economic evaluation of the compressed air energy storage system
100
70 3 n ) 60m i n Round-trip efficiency (%) g (m
0.0 i n
50 0.3 a r g
0.0 0.6 c
0.5
1.0 0.9 n
1.5
2.0 1.2 m
a A i r d e 2.5 1.5 e m a n d r d d i s c h a A i r g i n g (m 3 n m i n)
Figure 3.10: Round-trip efficiency of theCAESfor different air demands during charging and
discharging
# 3.5 Economic evaluation of the compressed air energy storage system
For an economic evaluation of theCAESsystem, the specific energy costs c _sto_ are calculated and compared with battery storages. The specific energy costs c _sto_ represent the costs for the energy that is retrieved from the storage. They can be calculated by dividing the investment costs C _inv_ by the product of the discharge energy E _dch_ that can be retrieved from the storage for one full discharge cycle and the number of full charge and discharge cycles Z within a certain observation period. If the number of full cycles Z within the observation period exceeds the number of maximum full cycles Z _max_, a new storage has to be used. This is considered by using the round up operator dxe in equation3.7. Additionally, costs for charging the storage have to be considered. To take the losses during charging and discharging into account, the energy costs c _en_(in kWh e ) are divided by the round-trip efficiency of the storage.
_CinvZ cen_ _csto_ = \+ (3.7) _Z EdchZmax_ For theCAESsystem three different cases are considered for the specific energy cost calcula- tions. For the best and worst case the parameters with the resulting best and worst round-trip efficiencies are used (see section3.4.3). For the mean case, the air demand during charging and discharging is considered to be the mean value of measured air demand data used for the experiments in this thesis (see chapter5.1.1, table5.2). The round-trip efficiency is linearly interpolated using the data shown in figure3.9. For the investment costs of theCAESonly the components needed in addition to a typical compressed air energy storage system are considered (see appendixA.2).
* * *
For the economic evaluation of thecompressed air energy storagesystem, the costs are compared with battery storage systems with a similar energy capacity. The cost and technical data
needed for the specific energy cost calculation of theCAESsystem and the battery storages
are summarized in table3.5. In addition to the parameters needed for the cost calculation, the
duration of one full charge and discharge cycle tZis given.
\\Delta t\_{Z}
Table 3.5: Costs and technical data of the storages for the specific energy cost calculations
| Storage | Cinv(€) | Edch(kWh) | Zmax(1) | η(%) | ΔtZ(h) | Source |
| CAES mean | 55,200 | 15.7 | ∞ | 64.3 | 5.7 CAES best | 55,200 | 20.1 | ∞ | 86.7 | 10.8 CAES worst | 55,200 | 13.9 | ∞ | 52.5 | 3.1 Sonnenbatterie eco | 21,224 | 14.0 | 10,000 | 94.1 | 8.5 | \[94\] |
| Tesla Powerwall1 | 4,200 | 5.6 | 10,000 | 88.8 | 4 | \[97\] |
C\_{i n v}
E\_{d c h}
Z\_{m a x}
\\eta
\\Delta t\_{Z}
Figure3.11shows the specific energy cost of theCAESsystem cases and the battery storage
depending on the number of full cycles per day. Here the observation period is defined to be
10 years and the electricity costs during charging are set to 0.10. The different maximum
kWh
cycles per day of the curves are a result of the individual duration of one full charge and
discharge cycle tZ. Each storage can only be charged and discharged with a certain number
of full cycles within the 24 hours of a day. The step in the specific costs of the battery storagesh
are caused by exceeding the maximum number of 10,000 cycles (2.74 cycles per day for
10 years). The results show, that the specific energy costs of theCAESsystem for all three
considered cases are higher than the costs of the battery storages. ts
0.10,\\frac{\\epsilon}{k W h}
\\Delta t\_{Z}
Figure 3.11: Specific storage costs depending on the number of full cycles per day for an
observation period of 10 years and electricity costs during charging of 0.10
kWh
0.10,\\frac{\\in}{N N h}
The costs and the round-trip efficiency are given including an inverter with investment costs of 2.000 e and an
efficiency of 96 %.
* * *
## Chapter 4
# Optimization Models
In this chapter, a linear, a mixed-integer linear, and a nonlinear mathematical model used for the different optimization methods are described and validated. While the sections of this chapter present the general structure of the models and the most important equations, a detailed mathematical description of each model is given in appendixB.
### 4.1 Objective function, sets, parameters, and variables
The objective of all optimization models described in this chapter is to minimize the total costs _ctot_ over the optimization horizon. The optimization horizon is described by the set of timesteps T = ft1\*;:::;tN\*g, where _T is the duration of the optimization horizon, t is the duration of_ each timestep, and N is the number of timesteps t 2T (see table4.1).
Table 4.1: Time set and parameters
**Name Unit Description** T Set of all timesteps T = ft1\*;:::;tN\*g _T_ h Duration of the optimization horizon _t_ s Timebase of the optimization (duration of one time period) _N_ 1 Number of timesteps N = _t=3600_ _T_
The total costs c _tot_ are calculated by the product of the electricity price C _tel_ and the total electrical energy consumption E _ttot_ at each timestep t, summed up for all timesteps. The total electrical energy consumption E _ttot_ of theCAESsystem at each timestep is defined by the total electrical power consumption P _ttot_ and the timestep duration _t._
0 1 0 1 X X _t_ min c _tot_ = min @ _C_ _tel_ _E_ _ttot_ A = min @ _C_ _tel_ _P_ _ttot_ s A (4.1) _t2T t2T_ 3600 h
To describe a mathematical optimization problem, the parameters used are distinguished into constant model parameters (usually referred to as parameters) and variable parameters (usually referred to as variables). The model parameters and variables are used to specify the optimization problem. The values of the parameters are constant, which means they do not
* * *
4. Optimization Models
change while the optimization problem is solved. In contrast, the values of the variables are unknown until the model has been solved. Solving an optimization model means finding the values for the variables, that lead to an optimal result of the objective function, satisfying all given constraints. The parameters and variables used to describe the optimization problems in this chapter are summarized in tables within the model description section for each model. The values of the parameters for each model can be found in appendixC.
# 4.2 Linear programming model
TheCAESsystem has three operation modes defining its behavior, normal, charge and discharge (see section3.3). Modeling these modes within an optimization problem requires integer variables and, thus, is not possible usinglinear programming. Also, the behavior of the booster, which has only an on/off mode, and the pressure dependency of the electric power consumption of the compressors and the booster (see figure3.4and3.7) can only be modeled using integer variables. Therefore, instead of modeling the booster and high-pressure storage tanks separately, they are summarized and treated as an electrical energy storage system using the parameters calculated in section3.4.3. Additionally, the three screw compressors are summarized as well and modeled as one single component covering the whole air demand. Figure4.1shows the structure of the LP model of theCAESsystem. The parameters and variables used to describe the LP model are summarized in table4.2and4.3.
Compressors Compressed air Electric power _Vcomp= Vd_ Zuschneiden: 31 _Pcomp_ 110 47 134 _PdchPch_ Booster and high pressure tank as electrical energy _Ptot_ storage Esto
Figure 4.1: Structure of the LP model of the CAES system
The objective of theLPmodel is to minimize the total costs over the optimization horizon. The costs depend on the electricity price C _tel_ and the total power consumption of the system P _ttot_ at each timestep (see eq.4.1). The total power consumption of the system P _ttot_ is comprised of the power consumption of the compressors P _tco_ and the charge power P _tch_ or discharge power P _tdch_ of the electrical energy storage.
_P_ _ttot_ = P _tco_ \+ P _tch_ _P_ _tdch_ (4.2)
* * *
Table 4.2: Parameters of the LP model
| Name | Unit | Description |
| $\\overline{E}\_{sto}$ | kWh | Maximum electrical energy capacity of the storage |
| $\\varsigma\_{1}$ | $\\frac{\\mathrm{kW}}{\\mathrm{m}\_{n}^{3}/\\mathrm{min}}$ | Slope of the linear function used to model the electrical power consumption of the compressors |
| $\\eta\_{ch}^{t}$ | 1 | Storage electrical charge efficiency at timestep t |
| $\\eta\_{dch}^{t}$ | 1 | Storage electrical discharge efficiency at timestep t |
| $\\dot{V}\_{d}^{t}$ | $\\frac{\\mathrm{m}\_{n}^{3}}{\\mathrm{min}}$ | Air demand at timestep t |
| $\\bar{P}\_{ch}^{t}$ | kW | Upper limit of the electrical charge power at timestep t dependent on $\\dot{V}\_{d}^{t}$ |
| $C\_{el}^{t}$ | $\\frac{\\mathrm{€}}{\\mathrm{kWh}}$ | Electricity price at timestep t |
| $\\Delta t$ | s | Timebase of the optimization (duration of one time period) |
\\overline{{E}}\_{s t o}
\\frac{k M}{m\_{n}^{3}m i n}
\\varsigma\_{1}
\\eta\_{c h}^{t}
\\eta\_{d c h}^{t}
\\underline{{\\mathfrak{m}}}\_{\\mathrm{n}}^{3}
\ {dot v\_\_{d}^{t}}
\\overline{{P}}\_{c h}^{t}
\ \\dot{v}\_{d}^{t}
C\_{e I}^{t}
\\frac{\\in}{\\mathbf{k}w h}
\\Delta t
Table 4.3: Variables of the LP model
| Name | ∈ | Unit | Description |
| $\\dot{V}\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | $\\frac{m\_{n}^{3}}{min}$ | Compressed air produced by the compressors at timestep t |
| $P\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |
| $P\_{tot}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |
| $P\_{ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical charge power of the storage at timestep t |
| $P\_{dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical discharge power of the storage at timestep t |
| $E\_{sto}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kWh | Electrical energy content of the storage at timestep t |
\\dot{v}\_{c o}^{t}
\\underline{{\\mathfrak{m}}}\_{\\mathsf{n}}^{3}
\\mathbb{R}\_{0}^{+}
P\_{c o}^{t}
\\mathbb{R}\_{0}^{+}
P\_{t o t}^{t}
\\mathbb{R}\_{0}^{+}
P\_{c h}^{t}
\\mathbb{R}\_{0}^{+}
P\_{d c h}^{t}
\\mathbb{R}\_{0}^{+}
E\_{s t o}^{t}
\\mathbb{R}\_{0}^{+}
Compressors
For the LP model, the system pressure is assumed to be constant.
consumption of the compressors P
as a linear function with the slope &
comparison with measured values. The LP formulation does not allow to use an offset in this
function, which leads to an inaccurate representation of the model, especially for low and high
air demands.
For the LP model, the system pressure is assumed to be constant. Therefore, the power
tco
consumption of the compressors P only depends on the air demand V\_dand is modeled
as a linear function with the slope &1. Figure4.2shows the modeled compressor power in
comparison with measured values. The LP formulation does not allow to use an offset in this
function, which leads to an inaccurate representation of the model, especially for low and high
P\_{c o}^{t}
P\_{d c h}^{t}
When theCAESsystem is in discharge mode, the compressors are switched off and the air
demand is covered by the air stored in the high-pressure storage tank. The power consumption
of the CAES system then becomes zero. In the LP model, this is represented by discharging
the electrical storage system. When the discharge power of the storage P
consumption of the compressors P
system is not able to generate electricity, so the discharge power of the storage is limited by
the power consumption of the compressors. The LP implementation does not allow one to use
tdch
a binary variable b
tdch
to define P to be either 0 or P
When theCAESsystem is in discharge mode, the compressors are switched off and the air
demand is covered by the air stored in the high-pressure storage tank. The power consumption
of the CAES system then becomes zero. In the LP model, this is represented by discharging
tdch
the electrical storage system. When the discharge power of the storage P equals the power
tco
consumption of the compressors P, the air demand is "covered" by the storage. The CAES
system is not able to generate electricity, so the discharge power of the storage is limited by
the power consumption of the compressors. The LP implementation does not allow one to use
representing the discharge mode of the system, thus, it is not possible
tco tdch tdch tco
to be either 0 or P dependent on the mode (e.g. P = b P), as can
P\_{c o}^{t}
(4.3)
Storage
P\_{c o}^{t}=\\varsigma\_{1}\\cdot\\dot{V}\_{d}^{t}
P\_{d c h}^{t}
P\_{c o}^{t}
P\_{d c h}^{t}=b\_{d c h}^{t}\\cdot P\_{c o}^{t})
* * *
4. Optimization Models
W 25 k Measured data ( LP model r e 20 w o p c 15 i tr c le 10 E
0.0 0.5 1.0 1.5 2.0 2.5
m3n A i r f l o w ( m i n )
Figure 4.2: LP function of compressor electric power consumption
be done for the MILP and the nonlinear model. This allows the LP model to obtain states in which the air demand is partly covered by the compressors, while the rest is covered by the storage. Because these states are not possible for the realCAESsystem, this could lead to inaccurate optimization results.
_P_ _tdch_ _P_ _tco_ (4.4)
When theCAESsystem is in charge mode, the booster is switched on and the high-pressure storage tank is filled. The compressors have to cover the additional air demand of the booster. In the LP model, this is modeled by charging the electrical storage system. The charge energy and, therefore, the mean charge power P _tch_ of the electrical storage representation of the _t_ CAESsystem is dependent on the air demand V\_ _d_(see chapter3.4.3, figure3.9). Therefore, _t_ _tch_ for each timestep and its (predicted) air demand V\_ _d_, the mean charge power P is calculated as explained in appendixC.1.1and used as an upper limit of the charge power P _tch_ . As explained before for the discharge power, it is not possible to to define P _tch_ to be either 0 or P _tch_
dependent on the system mode using a LP model, which might lead to inaccurate modeling results.
_P_ _tch_ _P_ _tch_ (4.5)
The energy content E _tsto_ +1 of the electrical energy storage for the timestep t+1 is calculated based on the energy content E _tsto_ , the charge power P _tch_ , and the discharge power P _tdch_
at timestep t. The losses during charging and discharging are represented by the charge efficiency _tch_ and the discharge efficiency _tdch_ . The electrical round-trip efficiency of the CAESsystem is dependent on the air demand during charging and discharging (see chapter
* * *
3.4.3, figure3.10). The charge efficiency and the discharge efficiency for each timestep are
calculated depending on the corresponding air demand as explained in appendixC.1.2.
E\_{s t o}^{t+1}=E\_{s t o}^{t}+\\eta\_{c h}^{t}\\cdot P\_{c h}^{t}-\\frac{1}{\\eta\_{d c h}^{t}}\\cdot P\_{d c h}^{t}
(4.6)
tsto
The energy storage content E is limited by the maximum energy capacity of the storage
Esto. The value of Estois the maximum measured discharge energy of theCAESsystem as
described in chapter3.4.3(Esto= 20:12 kWh).
E\_{s t o}^{t}
\\overline{{E}}\_{s t o}
\\overline{{E}}\_{s t o}
(\\overline{{E}}\_{s t o}=20.12,\\mathsf{k W h})
E\_{s t0}^{t}\\subseteq\\overline{{E}}\_{s t0}
(4.7)
For visualization and comparison of the optimization and simulation results with measured data,
the energy content of the storage can be converted to pressure values by a linear interpolation
between the minimum (psto) and maximum (psto) values of the storage pressure.
(\\bar{p}\_{s t o})
(p\_{s t o})
p\_{s t o}^{t}=\\frac{E\_{s t o}^{t}}{\\overline{{E}} _{s t o}}\\cdot\\left(\\overline{{p}}_{s t o}-\\underline{{p}} _{s t o}\\right)+\\underline{{p}}_{s t o}
(4.8)
Figure4.3shows the storage pressure profile for a charge and three discharging processes
calculated with equations4.6and4.8in comparison to measured values. The significant differm3
ence for the discharge process with an air demand of 0.2 results from the underestimation
min
tco
of the electric power consumption P (which limits the discharge energy, see eq.4.4) in this
operation point, as shown in figure g 4.2.
0.2\\frac{\\mathsf{m}^{3}}{\\mathsf{m}^{3}}
P\_{c o}^{t}
T i m e
Figure 4.3: Calculated storage pressure for exemplary charging and discharging processes
using the LP model compared to measured data
V\_{d}!=0.2,\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i}}
V\_{d}\ !2=\ .4\\frac{m\_{n}^{3}}{m n}
* * *
4.3 Mixed-integer linear programming model
In themixed-integer linear programming (MILP)formulation of the optimization problem, binary
variables representing the operation mode of theCAESsystem can be used.
CAESsystem can be modeled in more detail than with the LP model described in chapter4.2.
Figure4.4shows the structure of theMILPmodel. Here the booster and the high-pressure
tank are modeled separately. The three screw compressors are summarized and modeled as
one single component. The demand that has to be covered by the compressors depends on
the air demand and the operation mode of the system. The parameters and variables of the
MILP model are summarized in table4.4and4.5.
In themixed-integer linear programming (MILP)formulation of the optimization problem, binary
variables representing the operation mode of theCAESsystem can be used. Thus, the
CAESsystem can be modeled in more detail than with the LP model described in chapter4.2.
Figure4.4shows the structure of theMILPmodel. Here the booster and the high-pressure
tank are modeled separately. The three screw compressors are summarized and modeled as
one single component. The demand that has to be covered by the compressors depends on
the air demand and the operation mode of the system. The parameters and variables of the
MILP model are summarized in table4.4and4.5.
Figure 4.4: Structure of the MILP model of the CAES system
\\hat{p}\_{s y s}^{n o r m}
| Name | Unit | Description |
| $\\hat{p}\_{sys}^{norm}$ | barg | Setpoint pressure in normal mode(normal system pressure) |
| $\\varsigma\_{i}$ | | Parameters used to model the electrical power consumption of the compressors |
| $\\beta\_{i}$ | | Parameters used to model the electrical power consumption of the booster |
| $\\delta\_{i}$ | | Parameters used to model the storage pressure state equation |
| $\\dot{V}\_{d}^{t}$ | $\\frac{m\_{n}^{3}}{min}$ | Air demand at timestep t |
| $C\_{el}^{t}$ | $\\frac{\\epsilon}{kWh}$ | Electricity price at timestep t |
| $\\Delta t$ | s | Timebase of the optimization(duration of one time period) |
{tt b a r}\_{\\tt g}
\\beta\_{i}
\\delta\_{i}
\ {dot v\_\_{d d}^{t}}
\\underline{{\\mathfrak{m}}}\_{n}^{3}
C\_{e I}^{t}
\\Delta t
* * *
Table 4.5: Variables of the MILP model
| Name | ∈ | Unit | Description |
| $p\_{sys}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | System pressure at timestep t |
| $p\_{sto}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Storage pressure at timestep t |
| $\\Delta p\_{sto,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when charging |
| $\\Delta p\_{sto,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when discharging |
| $P\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |
| $P\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the booster at timestep t |
| $P\_{tot}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |
\\in
p\_{s y s}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt{b a t}\_{\\mathtt{g}}
p\_{s t o}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt{b a t}\_{\\mathtt{g}}
\\Delta p\_{s t o,c h}^{t}
\\mathbb{R}\_{0}^{+}
b a l\_{9}
\\Delta p\_{s t o,d c h}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt{b a t}\_{\\mathtt{g}}
P\_{c o}^{t}
\\mathbb{R}\_{0}^{+}
P\_{b o}^{t}
\\mathbb{R}\_{0}^{+}
P\_{t o t}^{t}
\\mathbb{R}\_{0}^{+}
The objective of theMILPmodel is to minimize the total costs over the optimization horizon.
tel
The costs depend on the electricity price C and the total power consumption of the system
ttot
P at each timestep (see eq.4.1). In the MILP model, the total power consumption of the
ttot tco
system P is comprised of the power consumptions of the compressors P and of the
tbo
booster P.
C\_{e I}^{t}
P\_{t o t}^{t}
P\_{t o t}^{t}
P\_{c o}^{t}
P\_{t o t}^{t}=P\_{c o}^{t}+P\_{b o}^{t}
P\_{b o}^{t}
(4.9)
Compressors
In the MILP model, the power consumption of the compressors can be formulated depending
on the operation mode. When the system is in normal mode, the compressors have to cover
t norm
the complete air demand V\_d. The system pressure is defined to be constant (psys= p^sys)
and, thus, has no influence on the consumed power. In the operation mode charge, in addition
to the air demand of the system V\_d, the air demand of the booster V\_bohas to be covered.
Furthermore, the system pressure psysduring charging is not constant, which affects the
power consumption of the compressors. This is taken into account with a linear dependence
of the power consumption on the difference of the system pressure and the normal system
t norm
pressure (psysp^sys) and the product of the air demand (V\_d+ V\_bo) and the system pressure
t norm
increase (psysp^sys). In discharge mode, the air demand is covered by the air out of the
high-pressure storage and the compressors are switched off.
(p\_{s v s}^{t}=\\hat{p}\_{s y s}^{n o r m})
\\dot{boldsymbol v\_\_{}}^{t}
\ {dot v\_\_{d d}^{t}}
\\dot{V}\_{b o}
p\_{s y s}^{t}
During charging, the system pressure psysof the CAES system depends on the storage
pressure psto(see chapter3.3). The system pressure has to be increased during charging,
when the storage pressure is above a certain value (psysrbo1 bar = 23 bar), because of the
limited compression ratio rboof the booster. If the storage pressure is below this value, or the
in normal mode,
(4.10)
\\small\\begin aligned}{\\small{P\_{c o}^{t}=\\begin{cases}{\\varsigma\_{1}\\cdot(\\dot{V} _{d}^{t}+\\dot{V}_{b o})+\\varsigma\_{2}\\cdot(p\_{s y s}^{t}-\\hat{\\rho} _{s y s}^{n o r m})}\ {+\\varsigma_{3}\\cdot(\\dot{V} _{d}^{t}+\\dot{V}_{b o})\\cdot(p\_{s y s}^{t}-\\hat{\\rho} _{s y s}^{n o r m})+\\varsigma_{4}}\ {\\varsigma\_{1}\\cdot\\dot{V} _{d}^{t}+\\varsigma_{4}}\ {0}\\end{cases}}\ \\end{aligned}
\ ,(p\_{s v s}^{t}\\cdot r\_{b o}-1\ \ !{\\sf b a l}=23\ \ \ {\\sf b\ l a l})0
r\_{b o} t
system is in normal or discharge operation mode, the system pressure psyscorresponds to
norm
the normal system pressure p^sys. Figure4.5shows the modeled system pressure dependent
on the storage pressure in charge mode, as defined in equation4.11.
p\_{s y s}^{t}
\\hat{p}\_{s y s}^{n o r m}
p\_{s y s}^{t}=\\left{\\begin{array}{l l}{((p\_{s t o}^{t}+2,\ \\mathsf{b a r})/r\_{b o}}&{\\mathrm{i f}\\qquad p\_{s t o}^{t}>p\_{s y s}^{t}\\cdot r\_{b o}-1,\\mathsf{b a r}\\qquad\\mathrm{i n},\\mathsf{c h a r g e},\\mathsf{m o d e},}\ {\\tilde{p}\_{s y s}^{s o o m}}&{\\mathrm{e l s e..}}\\end{array}\\right.
(4.11)
Figure 4.5: System pressure as a function of the storage pressure in charge mode
Figure4.6shows the modeled compressor power using the MILP formulation in comparison
with measured values. The possibility to use an offset (&4) in the linear function results in
a more accurate representation of the power consumption in comparison to the LP model
(see figure4.2). In contrast to the LP model, the MILP model considers energy losses during
start-up and shut-down of the compressors, as described in appendixB.2.
Booster
The power consumption of the booster depends mainly on its output pressure, which corresponds to the pressure in the high-pressure storage. Therefore, the power consumption of the
booster is defined as a linear function of the storage pressure with an offset2. The booster
only consumes power in charge mode. Figure4.7shows the modeled power consumption of
the booster compared to measured values. For the booster as well, losses for start-up and
shut-down are considered, as described in appendixB.2.
\\beta\_{2}
P\_{b o}^{t}=\\begin{cases}{\\beta\_{1}\\cdot p\_{s t o}^{t}+\\beta\_{2}\\qquad}&{\\mathsf{i n},c h a r g e,\\mathsf{m o d e},}\ {0\\qquad}&{\\mathsf{e l s e}.}\\end{array}
(4.12)
* * *
Figure 4.6: MILP model for the electric power consumption of the compressors
Figure 4.7: MILP model for the electric power consumption of the booster
* * *
Storage
t+1
The pressure in the high-pressure storage tank at the beginning of the next timestep psto
depends on the storage pressure pstoat timestep t and the operation mode of the system. In
charge mode, the pressure difference p is added. In discharge mode, the pressure is
sto;ch
reduced by p.
sto;dch
p\_{s t o}^{t+1}
p\_{s t o}^{t}
\\Delta p\_{s t o,c h}^{t}
\\Delta p\_{s t o,d c h}^{t}.
p\_{s t o}^{t+1}=\\begin{cases}{p\_{s t o}^{t}+\\Delta p\_{s t o,c h}^{t}\\qquad}&{\\mathsf{i n};c h a r g e;\\mathsf{m o d e},}\ {p\_{s t o}^{t}\\qquad}&{\\mathsf{i n};n o o m m l/;\\mathsf{m o d e},}\ {p\_{s t o}^{t}-\\Delta p\_{s t o,d c h}^{t}\\qquad}&{\\mathsf{i n};d i s c h a r g e;\\mathsf{m o d e}.}\\end{cases}
(4.13)
The pressure increase during charging is formulated as a linear function dependent on the
previous storage pressure psto.
p\_{s t o}^{t}
\\Delta p\_{s t o,c h}^{t}=\\Delta t\\cdot\\left(\\delta\_{c h,1}\\cdot p\_{s t o}^{t}+\\delta\_{c h,2}\\right)
(4.14)
The pressure decrease during discharging is modeled as a linear function dependent on the
air demand of the system V\_dand the previous storage pressure psto.
\\dot{v}\_{d}
p\_{s t o}^{t}
\\Delta p\_{s t o,d c h}^{t}=\\Delta t\\cdot\\left(\\delta\_{d c h,1}\\cdot\\dot{V} _{d}+\\delta_{d c h,2}\\cdot p\_{s t o}^{t}+\\delta\_{d c h,3}\\right)
(4.15)
Figure4.8shows the storage pressure profile for a charge and three discharging processes
calculated with equations4.13-4.15in comparison with measured values. The calculated
values show only a slight deviation from the measured data for all four cases. Compared to LP
(see figure4.3), the MILP model shows a better representation of the pressure characteristics
) m3
g n
for charge and discharge, especially for discharge with a low air demand (V\_d= 0:2).
min
\\begin{array}{r}{(\\dot{V} _{d}=0.2,\\frac{\\mathfrak{m}_{}^{3}}{\\mathfrak{m n}})}\\end{array}
T i m e
Figure 4.8: Calculated storage pressure for exemplary charging and discharging processes
using the MILP model compared to measured data
* * *
4.4 Nonlinear model
The nonlinear (and non-convex) formulation of the optimization problem allows for very high
freedom of expression to describe the CAES system. Thus, the system can be modeled in
much more detail than with a LP or MILP formulation.
programming (DP) and genetic algorithm (GA) use the nonlinear description of the CAES
system implemented as a simulation model, as described detailed in appendixB.3. To use the
mixed-integer nonlinear programming (MINLP) method a simplified version of the nonlinear
model is formulated using equality and inequality functions, as describe in appendixB.4.
The structure of the nonlinear CAES system model is shown in figure4.9. As in the MILP
The nonlinear (and non-convex) formulation of the optimization problem allows for very high
freedom of expression to describe the CAES system. Thus, the system can be modeled in
much more detail than with a LP or MILP formulation. The optimization methods dynamic
programming (DP) and genetic algorithm (GA) use the nonlinear description of the CAES
system implemented as a simulation model, as described detailed in appendixB.3. To use the
mixed-integer nonlinear programming (MINLP) method a simplified version of the nonlinear
model is formulated using equality and inequality functions, as describe in appendixB.4.
The structure of the nonlinear CAES system model is shown in figure4.9. As in the MILP
The structure of the nonlinear CAES system model is shown in figure4.9. As in the MILP
formulation, the booster and the high-pressure tank are modeled separately. The three screw
compressors are summarized and modeled as one single component. Here, the air receiver
tank, which is used to reduce compressor cycling, is also taken into account. The parameters
and variables used to describe the nonlinear model are summarized in table4.6and4.7.
Table 4.6: Parameters of the nonlinear model
| Name | Unit | Description |
| $\\hat{p}\_{sys}^{norm}$ | barg | Setpoint pressure in normal mode(normal system pressure) |
| $p\_{n}$ | bara | Normal pressure |
| $V\_{rec}$ | m3 | Volume of air receiver tank |
| $\\varsigma\_{i}$ | | Parameters used to model the electrical power consumption of the compressors |
| $\\beta\_{i}$ | | Parameters used to model the electrical power and air consumption of the booster |
| $\\delta\_{i}$ | | Parameters used to model the storage pressure state equation |
| $r\_{bo}$ | 1 | Maximum compression ratio of the booster |
| $\\dot{V}\_{d}^{t}$ | $\\frac{m\_{n}^{3}}{min}$ | Air demand at timestep t |
| $C\_{el}^{t}$ | $\\frac{\\epsilon}{kWh}$ | Electricity price at timestep t |
| $\\Delta t$ | s | Timebase of the optimization(duration of one time period) |
\\hat{p}\_{s y s}^{n o r m}
\ a r\_{9}
\\mathtt{b a t}\_{\\mathtt{a}}
p\_{n}
V\_{r e c}
m^{3}
\\varsigma\_{i}
\\beta\_{i}
\\delta\_{i}
r\_{b o}
\ {dot v\_\_{d d}^{t}}
\\frac{\\mathsf{m}\_{n}^{3}}{\\operatorname\*{m i n}}
Table 4.7: Variables of the nonlinear model
| Name | ∈ | Unit | Description |
| $p\_{sys}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | System pressure at timestep t |
| $p\_{sto}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Storage pressure at timestep t |
| $\\Delta p\_{sto,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when charging |
| $\\Delta p\_{sto,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when discharging |
| $\\Delta p\_{th,de}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Pressure decrease caused by temperature decrease after charging |
| $\\Delta p\_{th,in}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Pressure increase caused by temperature increase after discharging |
| $\\dot{V}\_{rec}^{t}$ | R | $\\frac{m\_{n}^{3}}{min}$ | Compressed air into (positive) or out of (negative) the air receiver tank |
| $\\dot{V}\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | $\\frac{m\_{n}^{3}}{min}$ | Compressed air consumption of the booster at timestep t |
| $P\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |
| $P\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the booster at timestep t |
| $P\_{tot}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |
\\Delta t
\\mathbb{R}\_{0}^{\\top}
\ a{t}\_{\\mathfrak{g}}
\\Delta p\_{s t o,c h}^{t}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0^^{+}}
_a a r_{n}
^{\\mathfrak{o a r}\_{\\mathfrak{g}}}
b a l\_{\\mathfrak{g}}
\\mathbb{R}\_{0}^{+}
\ _{\ }p^_{{t h,d e}^{\\iota}}
\\Delta p\_{t h,i n}^{t}
\\dot{V}\_{r e c}^{t}
\\mathbb{R}\_{0}^{+}
\\underline{{\\mathfrak{m}}}\_{\\mathsf{n}}^{3}
P\_{c o}^{t}
\\mathbb{R}\_{0}^{+}
\\underline{{\\mathfrak{m}}}\_{\\mathrm{n}}^{3}
P\_{b o}^{t}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
* * *
4. Optimization Models
Compressors
_Vcomp Vd_ _psys_
_Vrec_ Zuschneiden: Air 31 _Pcomp_ receiver 83 tank 47 134 _Pboost_ Booster
_Ptot_
High _psto_ pressure Compressed air storage Electric power
Figure 4.9: Structure of the nonlinear model of the CAES system
The total power consumption of the system P _ttot_ , which is used to calculate the total costs (see eq.4.1), is comprised of the power consumptions of the compressors P _tco_ and of the booster _P_ _tbo_ .
_P_ _ttot_ = P _tco_ \+ P _tbo_ (4.16)
## Air receiver tank
The air receiver tank is used in compressed air systems to reduce compressor cycling by smoothing high-frequent variations of the air demand. The pressure in the air receiver tank is equal to the system pressure. When the CAES system is charged, the system pressure has to be increased for high storage pressures. To increase the pressure in the air receiver tank, additional air V\_ _rec_ is needed, that has to be covered by the compressors. Figure4.10 shows the increase of the system pressure during charging from time t1to t2. When the CAES system switches to normal or discharge mode after charging, and the system pressure p _sys_ _t_ 1 is higher than the normal system pressure p^ _sys_ _norm_ , the receiver tank releases air V\_ _rec_ to reduce its pressure. This air covers the air demand V\_ _d_ as long as the pressure in the tank is greater than the normal system pressure p^ _sys_ _norm_ . As shown in figure4.10, the power consumption of the system becomes zero during this period (between t2and t3). Using the ideal gas equation of state (see eq.3.1) the additional air to raise the pressure (positive V\_ _rec_) or the released air to decrease it (negative V\_ _rec_), can be calculated by the pressure difference from p _sys_ _t_ 1 to p _sys_ _t_ as follows1.
1 It is assumed, that the air temperature is constant. The parameters of this equation have to be converted to SI units. The absolute pressure value has to be used.
* * *
\\dot{V} _{r e c}=\\frac{60,\\frac{s}{\\mathfrak m!{}}}{\\Delta t}\\cdot\\left(p_{s y s}^{t}-p\_{s y s}^{t-1}\\right)\\cdot\\frac{V\_{r e c}}{p\_{n}}
(4.17)
Figure 4.10: Storage and system pressure and total power consumption of the CAES system
during a charging process
Compressors
In the nonlinear model, the dependence of the power consumption of the compressors on the
system pressure and the air demand can be modeled in more detail than in the MILP model,
using a polynomial function of degree 3.
{\\dot{v}}\_{d}^{t}
In the operation mode charge, in addition to the air demand of the system V\_d, the air demand
of the booster V\_boand the air needed to increase the pressure in the receiver tank V\_rechas to
be covered. Thereby the air demand of the booster V\_bois not constant during the charging
process and depends on the storage pressure psto. In contrast to the LP and MILP model, this
relation is taken into account in the nonlinear model (see eq.4.19). The increase of the system
t norm
pressure related to normal system pressure (psysp^sys) also affects the power consumption
of the compressors. The relation between the system pressure psysand the storage pressure
pstoduring charging is formulated in the same way as in the MILP model (see eq4.11and
figure4.6).
\\dot{V}\_{b o}
\\dot{V}\_{r e c}
(p\_{s y s}^{t}-\\hat{p}\_{s y s}^{n o r m})
p\_{s t o}^{t}
:\\boldsymbol{p}\_{s t}^{t}
p\_{s v s}^{t}
* * *
P\_{c o\\mathbf o}^{t}=\\begin{cases}{\\varsigma\_{1}\\cdot(\\dot{V} _{d}^{t}+\\dot{V}_{b o}+\\dot{V} _{r e c})+\\varsigma_{2}}\ {+(p\_{t\\mathbf{mathit s s s}}^{t}-\\dot{P}\_{p\\mathbf{\\mathit{s o s}}}^{o r s})}\ {\ (\\cdot\ \
(4.18)
\\dot{V} _{b o}^{t}={\\beta}_{7}\\cdot{p\_{s t o}^{t}}^{2}+{\\beta} _{8}\\cdot{p_{s t o}^{t}}+{\\beta}\_{9}
(4.19)
Figure4.11shows the modeled compressor power in comparison with measured values.
Especially the power consumption for an increased system pressure is represented in more
detail than with the MILP model (see figure4.6). As in the MILP model, energy losses
during start-up and shut-down of the compressors are considered in the nonlinear model (see
appendixB.3).
Figure 4.11: Nonlinear model for the electric power consumption of the compressors
* * *
Booster
In the nonlinear model, the dependency of the power consumption of the booster on the
storage pressure pstois defined as a polynomial function of degree 5. Figure4.12shows the
modeled power consumption of the booster compared to measured values. The nonlinear
formulation results in a better representation of the power consumption, in comparison with the
MILP model (see figure4.7). For the booster as well, losses for start-up and shut-down are
considered, as described in appendixB.3.
p\_{s t o}^{t}
\ _{b o}^{t}=\\begin{cases}{\\beta_{1}\\cdot(p\_{s t o}^{t})^{5}+\\beta\_{2}\\cdot(p\_{s t o}^{t})^{4}+\\beta\_{3}\\cdot(p\_{s t o}^{t})^{3}}\ {+\\beta\_{4}\\cdot(p\_{s t o}^{t})^{2}+\\beta\_{5}\\cdot(p\_{s t o}^{t})+\\beta\_{6}}\ {0}\\end{cases}
(4.20)
Figure 4.12: Nonlinear model for the electric power consumption of the booster
* * *
Storage
t+1
The pressure in the high-pressure storage tank at the beginning of the next timestep psto
depends on the storage pressure pstoat timestep t and the operation mode of the system.
t t
In addition to the pressure increase p and decrease p during charging and
sto;ch sto;dch
t t
discharging, pressure changes p or p because of variations of the air temperature,
th;in th;de
are taken into account in the nonlinear model.
p\_{s t o}^{t+1}
p\_{s t o}^{t}
\\Delta p\_{s t o,c h}^{t}
\\Delta p\_{s t o,d c h}^{t}
\\Delta p\_{t h,i n}^{t}
\\Delta p\_{t h,d e}^{t}
p\_{s t o}^{t+1}=\\begin{cases}{p\_{s t o}^{t}+\\Delta p\_{s t o,c h}^{t}\\qquad}&{\\mathrm{i n ~~}c h a r g e\\mathsf{m\ d e d e},}\ {p\_{s t o}^{t}+\\Delta p\_{t h,i n}^{t}-\\Delta p\_{t h,d e}^{t}\\qquad}&{\\mathrm{i n~~}n o r m a l\\mathsf{m\ d e d e},}\ {\\rho\_{s t o}^{t}-\\Delta\\rho\_{s t o,d c h}^{t}}&{\\mathrm{i n~}c i s c h a r g e\\mathsf{m o d e}.}\\end{cases}
(4.21)
The pressure increase during charging is described as a polynomial function of degree 3,
dependent on the previous storage pressure psto.
p\_{s t o}^{t}
\\Delta p\_{s t o,c h}^{t}=\\Delta t\\cdot\\left(\\delta\_{c h,1}\\cdot\\left(p\_{s t o}^{t}\\right)^{3}+\\delta\_{c h,2}\\cdot\\left(p\_{s t o}^{t}\\right)^{2}+\\delta\_{c h,3}\\cdot p\_{s t o}^{t}+\\delta\_{c h,4}\\right)
(4.22)
The pressure decrease during discharging depends on the air demand of the system V\_d(taking
into account the air provided by the air receiver tank V\_rec) and the previous storage pressure
pstoand is modeled as follows.
{dot v\_\_{d d}^{t}}
(4.23)
\\Delta p\_{s t o,d c h}^{t}=\\Delta t\\cdot\\left(\\frac{\\delta\_{d c h,1}\\cdot(\\dot{V} _{d}^{t}+\\dot{V}_{r e c}^{t})}{\\delta\_{d c h,2}+(\\dot{V} _{d}^{t}+\\dot{V}_{r e c}^{t})}+\\delta\_{d c h,3}\\cdot p\_{s t o}^{t}+\\delta\_{d c h,4}\\right)
p\_{s t o}^{t}
In normal mode, the pressure storage is neither charged nor discharged. Nevertheless,
changes in the storage pressure caused by temperature variation have to be taken into account.
During charging, the air in the storage is heated up. After switching from charge to normal
mode, the air in the storage slowly cools down, which leads to a pressure decrease p
th;de
(see figure4.13). Analogous to the up-heating during charging, the air in the storage cools
down when the CAES system is discharged. After switching from discharge to normal mode,
the air in the storage slowly heats up, which leads to a pressure increase p. The pressure
th;in
decrease and increase are modeled by an exponential function of the storage pressure of the
form p = p0 e. The mathematical formulation is described in appendixB.3.1, eq.B.47
andB.48.
\\Delta p\_{t h.d e\\epsilon}^{t}
\\Delta p=\\Delta p\_{0}\\cdot e^{-k t}
As for the LP and the MILP model, the equations of the nonlinear model are used to calculate
the storage pressure profile for a charge and three discharging processes, as shown in figure
the storage pressure profile for a charge and three discharging processes, as shown in figure
4.14. Compared to the other models (see figures4.3and4.8), the nonlinear model shows
the best representation of pressure characteristics for charge and discharge. Here, only when
discharging with V\_d=1.3, differences between the simulated and measured values can be
min
seen.
the storage pressure profile for a charge and three discharging processes, as shown in figure
4.14. Compared to the other models (see figures4.3and4.8), the nonlinear model shows
the best representation of pressure characteristics for charge and discharge. Here, only when
, differences between the simulated and measured values can be
\\dot{V} _{d}=1.3,\\frac{m mathfrak_{{n}}^{3}}{\\mathfrak m\_{{n}}^{3}}
* * *
T i m e
Figure 4.13: Pressure profile of an exemplary charge and discharge cycle of the CAES
system (a) with magnified pressure decrease after charging (b) and pressure increase after
discharging (c)
T i m e
* * *
4.5 Validation of the models
To validate the different models of the CAES system, simulation results for the storage pressure
and total electrical power are compared to measured values.
4.5.1 Validation data
To obtain the validation data, three different control sequences with a time horizon of 24 hours
are applied to the CAES system. In control sequence "normal", the system is in normal
operation mode the whole time, so that the compressors cover the complete air demand. In
control sequence "random", a randomly chosen sequence of the operation modes normal,
charge and discharge is used. The third sequence "2 cycles" is chosen to result in two full
charge and discharge cycles of the system. For each control sequence two measurements
with a different air demand profile are performed.
Figure4.15shows the measured storage pressure and total electrical power consumption of
Figure4.15shows the measured storage pressure and total electrical power consumption of
the CAES system for the three control sequences with the typical working day air demand
profile, as described in chapter5.1.1. The same data for the air demand profile typical nonworking day is shown in figure4.16. Because of the lower air demand in the non-working day
profile, the pressure decreases slower during discharging, which leads to different pressure
profiles. Also the power consumption of the system is lower because of the lower air demand.
Figure 4.15: Validation data for air demand working day
* * *
Figure 4.16: Validation data for air demand non-working day
4.5.2 Results
For each model, the equations described in this chapter are used to simulate the operation of
the CAES system. The operation mode for each timestep is given by the measured validation
data. Figure4.17shows the resulting pressure storage and power consumption of the CAES
system using the linear (LP), the mixed-integer (MILP) and the nonlinear (NL) model for the
"random" control sequence with air demand typical working day. The models are simulated
using a timestep size of 5 minutes. The results are compared to the measured data, which is
aggregated to 5 minute average values for better visualization. Looking at the pressure profiles,
it can be seen that the results of LP model show the largest deviation, while the NL model
shows the best result.
To compare the results of the models, the mean absolute error of the pressure and the power
consumption for each model and validation data set was calculated. The results are shown
in figure4.18. The LP model shows the poorest results for all cases regarding pressure and
electric power. For the "random" and "2 cycle" cases, the NL model outperforms the MILP
model in both, pressure and electric power simulation. In the "normal" cases, both models
show the same results for the electrical power consumption.
* * *
Figure 4.17: Simulated results using the equations of the linear (LP), the mixed-integer (MILP)
and the nonliner (NL) model for the "random" control sequence with air demand "typical working
day"
* * *
## Chapter 5
# Model Predictive Control of the compressed air energy storage
# system
In this chapter, the optimization models are used for the Model Predictive Control (MPC) of the compressed air energy storage (CAES) system, with the objective to cover a given air demand over 24 hours with minimal costs. In the first part of this chapter, the general implementation of MPC for the CAES system is described and the scenarios are defined. The experiments are performed with different air demand and electricity price scenarios. Additionally, the influences of the optimization timestep size and the quality of the air demand forecast are investigated. Then, preliminary investigations and the optimization parameters are described. In the third part of this chapter, the results of the comparison between the optimization methods are presented.
### 5.1 Implementation
Figure5.1shows an overview of the implementation of MPC for the CAES system. The CAES system always starts with an empty storage (p _sto_ = 7 bar) and in normal operation mode. For each experiment, a given air demand for one day (24 hours) has to be covered. A time-sensitive electricity price is applied as an incentive to make sure that the storage system is used. Forecasts for the air demand and the electricity price are used as inputs to the optimization. Depending on the chosen model and optimization method, the optimal future control sequence for the 24-hour time horizon is calculated, so that the electricity costs are minimized. The first control signal, which represents one of the possible operation modes, normal, charge or discharge, is then applied to the CAES system. The superior controller prevents the applied target operation mode from being invalid by setting the concrete operation mode to normal if necessary (see chapter3.3). After every multiple of the timestep size, the storage pressure, the system pressure and the concrete operation mode are measured and used to start a new optimization for the remaining time horizon. To make sure that the results of the different experiments can be compared, the end of the optimization horizon is not shifted towards the future, but stays at the end of the 24-hour time horizon of the experiment.
* * *
Figure 5.1: Implementation of MPC for the CAES system
To compare the results of the different optimization methods, various experiment scenarios
varying the air demand, the forecast quality and the electricity price are used. Additionally, two
different values for the timestep size of the optimization are used to investigate their influence
on the results. Table5.1provides an overview of all experiment scenarios used in this thesis to
compare the different optimization methods. A detailed description of the respective differences
is given in the following sections.
5.1.1 Air demand time-series and forecast scenarios
In order to apply realistic values of the air demand of an industrial compressed air system for the
experiments within this thesis, real measured air demand time-series data is used. Therefore,
the compressed air demand of the toolmaking department of an automotive manufacturer was
measured for one year with a time resolution of one minute. Since the compressed air system
of this department has a maximumfree air deliveryof about 20 and a maximum measured
min
air demand of 18, the values have to be scaled down to be used for the compressed air
min
system introduced in this chapter. The scaling factor is fixed to 8 based on the relation of
the maximumfree air deliveryof the two systems. All following values for the air demand are
already scaled by the factor of 8. Table5.2shows the minimum, mean and maximum values
for the measured and scaled air demand data.
18,\ \ \\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i n}}
20,\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i n}}
* * *
5.1. Implementation
Table 5.1: Scenarios used in this thesis to compare the different optimization methods
| Forecast | Air demand | Electricity price | Timestep size |
| Perfect | Working day | Typical | 5 minutes |
| 15 minutes |
| Untypical | 5 minutes
| 15 minutes |
| Non-working day | Typical | 5 minutes 15 minutes |
| Untypical | 5 minutes
| 15 minutes |
| Inaccurate | Working day | Typical | 5 minutes |
| 15 minutes |
| Non-working day | Typical | 5 minutes 15 minutes |
| Worst-case | Working day | Typical | 5 minutes |
| 15 minutes |
| Non-working day | Typical | 5 minutes 15 minutes |
Table 5.2: Scaled minimum, mean and maximum values of the measured air demand
| Days | Minimum | Mean | Maximum |
| All days | 0$\\frac{m\_{n}^{3}}{min}$ | 0.57$\\frac{m\_{n}^{3}}{min}$ | 2.25$\\frac{m\_{n}^{3}}{min}$ |
| Working days | 0$\\frac{m\_{n}^{3}}{min}$ | 0.69$\\frac{m\_{n}^{3}}{min}$ | 2.25$\\frac{m\_{n}^{3}}{min}$ |
| Non-working days | 0$\\frac{m\_{n}^{3}}{min}$ | 0.33$\\frac{m\_{n}^{3}}{min}$ | 2.25$\\frac{m\_{n}^{3}}{min}$ |
\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf m i n}
\\textstyle{0.57,\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m n}}}
2.25,\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i}}
\\frac{\\mathsf{m}\_{mathsf n^^{3}}}{\ mathsf{m i n}}
\\frac{\\mathsf{m}\_{n}^{3}}{\\operatorname\*{m i n}}
\ frac\ {{mathsfmathsf m m}\_{}^^3}{\\operatorname\*{m i n}}
0.33,\\textstyle{\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i n}}}
For the working and non-working days, the typical and the untypical day of air demand timeseries were respectively determined. Therefore, the absolute difference of every minute of
one day to the mean demand of the same minute of all considered days was calculated and
summed up for the whole day. The day with the smallest error was chosen as the typical
day and the day with the biggest error as the untypical day. These demand time-series are
used to simulate a perfect and a worst-case air demand forecast scenario for the experiments.
Thereby, the air demand forecast used for the optimization always corresponds to the typical
air demand. In the case of a perfect forecast, the same typical air demand is applied to the
CAES system, whereas for the worst-case forecast, the untypical air demand is applied.
For the working and non-working days, the typical and the untypical day of air demand timeseries were respectively determined. Therefore, the absolute difference of every minute of
one day to the mean demand of the same minute of all considered days was calculated and
The day with the smallest error was chosen as the typical
day and the day with the biggest error as the untypical day. These demand time-series are
used to simulate a perfect and a worst-case air demand forecast scenario for the experiments.
Thereby, the air demand forecast used for the optimization always corresponds to the typical
air demand. In the case of a perfect forecast, the same typical air demand is applied to the
CAES system, whereas for the worst-case forecast, the untypical air demand is applied.
2.25,\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf{m i}} day seven days after the typical one. Figure5.3shows the same graphs for the non-working
day. Table5.3summarizes the definitions for the different forecast scenarios.
Figure 5.2: Working day air demands (used for the respective forecast scenario)
Figure 5.3: Non-working day air demands (used for the respective forecast scenario)
The available air demand was measured in a one minute resolution and this data is directly
applied to the control valve of the CAES system. The timestep size of the optimization used in
this thesis is either 5 or 15 minutes, as described in section5.1.3. Therefore, the mean value of
* * *
5.1. Implementation
Table 5.3: Definition of forecast scenarios
| Forecast scenario | Air demand for the optimization | Air demand applied to CAES system |
| Perfect | Typical day | Typical day |
| Inaccurate | Typical day | 7 days after typical day |
| Worst-case | Typical day | Untypical day |
the air demand over one time period has to be aggregated and used for the optimization. This
averaging over the optimization timestep size leads to a difference between the air demand
used for the MPC and the air demand applied to the CAES system, even in the perfect forecast
scenarios.
5.1.2 Electricity price scenarios
The variation over time of the electricity price provides the incentive to use the compressed air
energy storage system. For the experiments to compare the optimization methods for MPC
in this thesis, two different electricity price time-series are used. Based on the EPEX SPOT
day-ahead auction prices for Germany (Phelix) in 2015, the days with the typical and untypical
price curve were identified. To use them for this thesis, an offset was added to both curves,
so that their mean values over the day result in 0.13, which is a typical electricity price for
kWh
industrial customers in Germany. Additionally, for both curves, the difference to the mean value
in each hour was scaled by a factor so that the difference between the maximum and minimum
price of the day results in h 0.15. This ensures a big enough incentive to use the storage
kWh
system and prevents that the cheapest operation to cover the demand is staying in normal
mode for the whole day.(
0.13,\\frac{\\in}{N N h}
0.15,\\frac{\\in}{N N h}
* * *
5.1.3 Optimization timestep size
The timestep size of the optimization is an important parameter for Model Predictive Control. A
large timestep size may result in poor accuracy of the model and the reduced possibilities to
change the control signal based on measured parameters can lead to higher total costs. On
the other hand, a small timestep size leads to a larger optimization problem that takes more
time to be solved. This can result in an inexact solution either because the algorithm has to
be aborted before finding the optimal solution or the parameters of the algorithm have to be
adapted.
According to Müller \[73\] and Mauser \[64\], for the optimization of device operation, the timestep
According to Müller \[73\] and Mauser \[64\], for the optimization of device operation, the timestep
size is usually between 15 and 60 minutes. In the German power sector, a 15 minutes time
period is currently the shortest temporal resolution of trading (EPEX SPOT intra day market) or
measuring (industrial customers). Therefore, in this thesis, a timestep size of 15 minutes is
used for optimization. To investigate the influence of a decrease in the timestep size, every
experiment is additionally performed with a 5 minute timestep size, as shown in table5.1.
According to Müller \[73\] and Mauser \[64\], for the optimization of device operation, the timestep
size is usually between 15 and 60 minutes. In the German power sector, a 15 minutes time
period is currently the shortest temporal resolution of trading (EPEX SPOT intra day market) or
measuring (industrial customers). Therefore, in this thesis, a timestep size of 15 minutes is
used for optimization. To investigate the influence of a decrease in the timestep size, every
experiment is additionally performed with a 5 minute timestep size, as shown in table5.1.
5.2 Preliminary investigations and optimization parameters
5.2.1 Reference values
The results of the experiments using MPC for the CAES system are evaluated based on
cost savings compared to the normal operation of the system in which the booster and highpressure storage tank are not used and the air demand is always covered by the compressors.
Therefore, reference measurements for each demand (see figures5.2and5.3) were performed.
Based on these measurements, the reference energy costs for each scenario defined in section
5.1were calculated. The energy consumption and total costs for each reference measurement
are summarized in table5.4.
5.2.2 Influence of measurement inaccuracy and operation
| Air demand | Electricity price | Energy consumption(kWh) | Costs(€) |
| Working day (typical) | Typical | 139.22 | 18.21 |
| Working day (typical) | Untypical | 139.22 | 17.08 |
| Working day(7 days after typical) | Typical | 109.73 | 14.17 |
| Working day(untypical) | Typical | 73.51 | 9.05 |
| Non-working day(typical) | Typical | 70.32 | 8.66 |
| Non-working day(typical) | Untypical | 70.32 | 8.56 |
| Non-working day(7 days after typical) | Typical | 86.49 | 10.84 |
| Non-working day(untypical) | Typical | 173.19 | 22.60 |
* * *
5.2. Preliminary investigations and optimization parameters
Table 5.5: Energy consumption, costs and cost savings of 4 experiments for the same scenario
**Measurement Energy consumption (kWh) Costs (e) Cost savings (e)** 1 155.05 16.82 1.39 2 154.70 16.75 1.46 3 154.04 16.65 1.56 4 155.11 16.85 1.36 Maximum difference 2.17 0.20 0.20 conditions like temperature and humidity of the air. On the other hand, all measurement devices, such as the pressure transmitters and the power meters, have a certain measurement inaccuracy. Additionally, the compressors are not controlled directly. The MPC only gives the current operation mode to the SAM (as described in section3.3), which decides which compressors are running based on internal calculations. Another influence that can affect the results is the initial storage pressure. Before every experiment, the storage is completely discharged to a pressure of 7 bar. As explained in section4.4, temperature variations can lead to a small pressure increase after discharging the storage. Because the level of the pressure increase depends on the discharge time and the ambient temperature, the initial storage pressure is not exactly the same for every experiment. To estimate the total possible deviation caused by the described influences, the same experi- ment is performed four times and compared regarding the cost savings. Therefore, MPC using LP as the optimization method1 is applied to the scenario with perfect forecast, air demand working day, the typical electricity price and a timestep size of 5 minutes. Table5.5shows the energy consumption, costs and cost savings of these 4 experiments as well as the maximum difference of each parameter. These values can be used to assess and interpret the results, when the different optimization methods are compared.
## 5.2.3 Optimization parameters
Each optimization method is defined by various parameters that influence the solution quality and solving time. Since it is crucial for MPC that the problem is solved within the time period of one timestep, the optimization parameters have to be adjusted to ensure this. All optimization problems are solved using an Intel Core i7-3930K CPU 3.20 GHz, 64 GB RAM. The linear programming (LP) and the mixed-integer linear programming (MILP) model are formulated with Pyomo \[83\] and solved using the state of the art solver CPLEX \[40\]. The solver allows one to set a time limit, that stops the solving process when the limit is exceeded and returns the best current solution. To ensure that the solution can be used for the MPC within one timestep period of 5 or 15 minutes, considering time for pre and post-processing, the time limit is set to 4 minutes and 30 seconds or 14 minutes and 30 seconds, respectively2. The maximum number of CPU threads to be used by the solver is set to 8. For the MILP problem,
1 LP is used as the optimization method, because it finds the global optimum within the given time limit, so that the measured deviations are not caused by imperfect solutions of the optimization problem 2 For all experiments performed within this thesis, the LP problem was always solved in under 1 minute so that the time limit was never exceeded. For the MILP problem with a 5 minute timestep size, in some cases the time limit was exceeded before the absolute or relative MIP gap was reached.
* * *
5. Model Predictive Control of the compressed air energy storage system
the relative MIP gap is set to 0.0001 and the absolute MIP gap is set to 0.001. For all other parameters, the default values are used. The mixed integer nonlinear problem is also formulated with Pyomo but solved using the state of the art solver BARON \[98\]. BARON also allows to set a time limit and the maximum number of CPU threads. For both parameters the same values as for the LP and MILP settings are used. CPLEX is set as the LP solver, which is used by BARON to solve linear sub-problems. For all other parameters the default values are used. For the implementation of the genetic algorithm (GA) the evolutionary computation framework DEAP \[23\] is used. DEAP does not allow to set a time limit to stop the solving process. Therefore, the number of individuals within one generation (population) and the number of generations which are evaluated define the solving time of this algorithm. Based on investigations of Jungwirth \[42\], the number of individuals of one generation is set to 10, the mutation probability to 1/N (where N is the number of timestep) and the crossover probability to 0.7. Given this parameters, the number of generations has to be chosen such that the time limit of 5 minutes or 15 minutes, respectively, is not exceeded. Based on empirical experiments, the number of generations is set to 7 or 90, respectively. For all other parameters the default values are used. To implement dynamic programming as an optimization method for MPC in this thesis, a new open-source toolbox prodyn was developed and published online \[24\]. prodyn is a generic implementation of the dynamic programming algorithm for optimal system control written in Python. The time for solving a DP problem using prodyn can not be limited to a maximum value. Therefore the number of discretization steps for the state variable, which is the storage pressure in this case, has to be adjusted to ensure that the problem is solved within the given time limits. Empirical experiments showed that, with 621 discretization steps, the time for solving the problem does not exceed the time limit for the 5 minute optimization timestep. For the storage pressure, which is limited by its minimum value of 7 bar and its maximum value of 38 bar, this results in a discretization step size of 0.05 bar. For the 15 minute optimization timestep size, the discretization steps can be increased to 3101, which results in a discretization step size of
0.01 bar for the storage pressure. The software and solvers with the parameters used for the different optimization methods are summarized in table5.6.
## 5.2.4 Comparison of the nonlinear optimization methods
Before the differences of the linear, mixed-integer and nonlinear models for MPC are inves- tigated, one of the nonlinear optimization methods is chosen. Therefore, all three nonlinear optimization methods, MINLP, DP and GA, are used for MPC of the CAES system for the scenario with the air demand working day, a perfect forecast and a typical electricity price. For each method, the experiment is performed using an optimization timestep size of 5 and 15 minutes. Figure5.5shows the resulting costs for the different methods. Additionally, the reference costs (Ref) for normal operation of the CAES system without using the storage are shown (see section5.2.1). For both scenarios, the DP method shows the best result, leading to the lowest costs. Since the resulting costs are almost the same for both scenarios, it seems that the error made because
* * *
5.2. Preliminary investigations and optimization parameters
Table 5.6: Parameter settings of the used software and solvers for the different optimization
methods
| Method | Software/solver | Optimization parameters |
| Linear programming(LP) | Pyomo/CPLEX | -Maximum threads=8-Time limit=870s(15 minute timestep size)-Time limit=270s(5 minute timestep size) |
| Mixed-integer linear programming(MILP) | Pyomo/CPLEX | -Maximum threads=8-Relative MIP gap=0.0001-Absolute MIP gap=0.001-Time limit=870s(15 minute timestep size)-Time limit=270s(5 minute timestep size) |
| Mixed integer nonlinear programming(MINLP) | Pyomo/BARON | -Maximum threads=8-LP solver=CPLEX-Time limit=870s(15 minute timestep size)-Time limit=270s(5 minute timestep size) |
| Dynamic programming(DP) | prodyn | -Discretization steps=3101(15 minute timestep size)-Discretization steps=621(5 minute timestep size) |
| Genetic algorithm(GA) | DEAP | -Population=10-Crossover probability=0.7-Mutation probability=1/N-Generations=90(15 minute timestep size)-Generations=7(5 minute timestep size) |
To analyze how much the limited solving time influences the optimization result of the different
methods, the respective limiting parameters3
of the MPC for the 15 minute scenario (from the first timestep until the end of the horizon)
is solved. The solution is then used as an input for the nonlinear simulation model (as used
for the validation of the nonlinear model in chapter4.5, the results are not applied to the real
To analyze how much the limited solving time influences the optimization result of the different
methods, the respective limiting parameters3 are increased and the first optimization problem
of the MPC for the 15 minute scenario (from the first timestep until the end of the horizon)
is solved. The solution is then used as an input for the nonlinear simulation model (as used
for the validation of the nonlinear model in chapter4.5, the results are not applied to the real
for the validation of the nonlinear model in chapter4.5, the results are not applied to the real
CAES system in this case). The resulting costs calculated by the simulation over the solving
time are shown in figure5.6. The results show, that using the DP method, the solution found
within the required 15 minutes already is very close to the optimal solution and an increase
time are shown in figure5.6. The results show, that using the DP method, the solution found
within the required 15 minutes already is very close to the optimal solution and an increase
of discretization steps does not bring a benefit. For the MINLP method the resulting costs
decrease with the increase of the allowed solving time. It seems that the best solution is still
decrease with the increase of the allowed solving time. It seems that the best solution is still
not found after 12 hours. This shows, that the MINLP method, which is able to solve a wide
range of general optimization problems, is not suited to solve the given problems in the time
decrease with the increase of the allowed solving time. It seems that the best solution is still
not found after 12 hours. This shows, that the MINLP method, which is able to solve a wide
range of general optimization problems, is not suited to solve the given problems in the time
range of general optimization problems, is not suited to solve the given problems in the time
required to implement MPC. The results of the GA show, that this method is not able to find a
required to implement MPC. The results of the GA show, that this method is not able to find a
The following values are used for the increase of the limiting parameters (see section5.2.3):
required to implement MPC. The results of the GA show, that this method is not able to find a
The following values are used for the increase of the limiting parameters (see section5.2.3):
Number of generations for GA: 90, 360, 720, 1440, 4320
* * *
Figure 5.5: Cost comparison of the nonlinear optimization methods for scenario perfect forecast,
air demand working day and typical el. price with 5 and 15 minutes timestep size
better solution than operating in normal mode for all calculated cases except the last one. The
principle of the genetic algorithms is to evaluate a number of candidate solutions and create
new candidates using different genetic operators. The number of possible solutions for this
96 −40
problem is 3, where only 10 % of these possibilities can be evaluated in the case with
4320 generations, which takes about 12 hours. This shows that the given problem is too big to
reliably find a good solution using GA within the required time limit.
3^{96}
10^{-40}%
* * *
The results show that DP is the most suitable method to solve the nonlinear optimization
problems in this thesis. Therefore, in the following DP is compared with the LP and MILP
method for MPC of the CAES system.
5.2.5 Differences of the models in completely charging/discharging the
storage
How the pressure increases and decreases just before the storage is completely full or empty
is implemented in the different models can have a distinct influence on the optimization results,
especially for the MILP model. To illustrate the differences between the models, figure5.7
shows the modeled time curves of the storage pressure used for the optimization methods LP,
MILP and DP. The pressure curves are shown for a timestep size of 15 and 5 minutes.
For the 15 minute step size example, the storage pressure is at 36.5 bar at the beginning of
timestep 1. When the CAES system is in operation mode charge during the first timestep,
the maximum storage pressure of 38 bar is reached after half of the period. In this case, the
superior mode controller changes the operation mode to normal (see chapter3.3).
The nonlinear model used for DP is able to divide a time period in which the pressure limit is
The nonlinear model used for DP is able to divide a time period in which the pressure limit is
exceeded in two parts for internal calculations. As for the real system, the storage is in charge
model until the pressure is full and switches to normal mode after. For the solution of the
optimization problem, in which one period can only have one operation mode, here the mode
is set to charge. As described before, the superior mode controller prevents the pressure from
being raised above its maximum value when the result is applied to the CAES system.
Using the LP method, dividing one time period into two parts is not possible. But because the
Using the LP method, dividing one time period into two parts is not possible. But because the
charging power, which represents the pressure increase, is only limited to an upper bound
when charging (specifying an exact value is not possible without integer variables), it can be
reduced so that the maximum pressure is reached exactly at the end of the period. This is
not possible for the real system, since the booster can either be on or off and leads to an
inaccurate calculation of the power consumption. But since any charging power greater than
zero is treated as mode charge for the solution of the optimization problem, for this example it
would lead to the same results as with the DP method.
In the MILP model, the pressure increase during one timestep is determined exactly. Also
dividing the period into two parts is not possible. This is a more realistic representation than
with the LP model, but it also means that the storage can not be completely charged in this
case. For the internal calculations, running the system in charge mode during the first timestep
would lead to a storage pressure that is greater than the maximum allowed value. Since this
does not satisfy the constraint psto38 bar, it is not a feasible solution of the MILP method.
Further charging of the system using MPC with the MILP method is therefore not possible and
it has to run in normal (or discharge) mode. The same problem can occur during discharging
so that the storage can not be discharged completely. This limitation in using the whole storage
capacity can lead to lower cost savings using the MILP method. As also shown in figure5.7, a
smaller timestep size of 5 minutes reduces this problem. The shorter periods allow the MILP
model to use more of the storage capacity by getting closer to the pressure limits.
p\_{s t o}\\leq38,\\mathsf{b{r}},,
* * *
Figure 5.7: Pressure increase at the end of the charging process
In figure5.8, the optimization results using MILP for the same scenario with slightly different
initial storage pressures of 7.0 bar and 7.1 bar are shown. The small difference in the starting
pressure results in very different solutions for the same optimization problem, which will lead to
different costs when used for MPC. As explained in section5.2.2, the initial storage pressure
for the experiments is not always exactly the same. Therefore, the effects of this deviation on
the results of the MILP model has to be taken into account when the results are discussed.
Figure 5.8: Comparison of the optimization results of the MILP model with different initial
storage pressures
* * *
5.3 Results
To compare the optimization methods LP, MILP and DP for Model Predictive Control of the
compressed air energy storage system, various experiments with different scenarios for the air
demand, the electricity price and the forecast quality are performed. Primarily, the experiments
are performed with a optimization timestep size of 15 minutes. The influence of the reduction
of the timestep size to 5 minutes is then discussed in section5.3.3. The results of the different
methods and scenarios are evaluated based on the achieved cost savings compared to the
respective reference costs (see chapter5.2.1, table5.4) over the 24 hour time horizon.
5.3.1 Perfect air demand forecast
At first, the optimization methods are compared using a perfect forecast of the air demand. As
shown in table5.1, two different air demand scenarios, working day and non-working day, each
with two different electricity price scenarios, typical and untypical, are used for the comparison.
Figure5.9shows the storage pressure and the electric power consumption over time for the
three optimization methods for the working day air demand using the typical electricity price.
For reasons of clarity, the electric power consumption is aggregated to 15 minute values, which
is the case for all of the following figures in this section. The charging and discharging times
of the MILP and the DP methods are different, but the general pattern is very similar, which
results in almost the same costs for both approaches (see figure5.14). With the LP method,
the storage is not completely discharged in the first cycle, because the model does not take into
account that the booster consumes more power when the storage pressure is higher during
charging. Additionally, the charge and discharge processes are sometimes interrupted for
some time. This happens, when the feedback of the MPC differs from the predicted system
behavior of the model and the control schedule has to be adapted. Therefore, the resulting
costs of the LP method are higher than for the other two methods.
Figure 5.9: Results for perfect forecast, air demand working day and typical el. price
* * *
For the scenario using the untypical electricity price and the air demand working day, the
charging and discharging times of all three methods have only little differences, as shown in
figure5.10. Using the DP method, the storage is charged completely and discharged without
interruption during the first cycle. Using the LP and the MILP method, the storage is not
fully charged, which leads to an interruption during discharging in a time with high electricity
prices around hour 12. In the second charging process, it can be seen that the LP model
overestimates the time for charging, as it starts charging a few minutes before the electricity
price decreases at hour 15 but is already full a few minutes before the electricity price increases
at hour 17. In contrast, the MILP model underestimates the charging time in such a way that
the end of the charging process, where the most power is consumed, takes place after the
price increase in hour 17. The DP model almost perfectly predicts the charging process, in
such a way that it ends almost at the time of the price increase. This results in the lowest costs
for the DP and the highest costs using the LP method, as shown in figure5.14.
Figure 5.10: Results for perfect forecast, air demand working day and untypical el. price
The results of the scenario using the untypical electricity price and the air demand non-working
day also show few differences between the optimization methods, as can be seen in figure
5.14. The resulting costs of the DP and the MILP method are almost the same, while the costs
of the LP model are slightly higher caused by the corrections in the second cycle.
Figure5.12shows the storage pressure and power consumption for the scenario with air
demand non-working day and the typical electricity price. Despite the repeated interruption
Figure5.12shows the storage pressure and power consumption for the scenario with air
demand non-working day and the typical electricity price. Despite the repeated interruption
during the first discharging process using the DP method and the correction using the LP
method during the second cycle, the resulting costs for both methods are almost the same (see
figure5.14). One reason for the higher costs using the MILP model is that not the whole storage
capacity can be used in the first cycle and that the storage is charged to a higher pressure
level and cannot completely be discharged in the second cycle, because of the limitations of
the MILP model described in section5.2.5. Additionally, with the MILP method the charging of
* * *
Figure 5.11: Results for perfect forecast, air demand non-working day and untypical el. price
the second cycle begins almost an hour before the charging with the LP and DP method. This
happens because of the differences in modeling the power consumption during a charging
process in combination with the electricity price, which has its minimum of the second half of
ct ct ct
the day in hour 15 (3.277), while the prices of hour 14 (3.404) and hour 16 (3.394)
kWh kWh kWh
are only slightly higher. Figure5.13shows an example of a measured power consumption
during charging and the simulated power consumptions using the LP, MILP and nonlinear DP
(NL) model. These are the first hours of the validation results for the scenario 2 cycles for air
demand non-working day, as described in chapter4.5. All methods try to consume the most
energy during hour 15. Since the charging power is constant for the LP model and the price
in hour 16 is lower than in hour 14, it begins charging at the beginning of hour 15. For the
DP model, the power consumption at the beginning of a charging process is higher than in
the middle part. Therefore, here, the charging process starts at the beginning of hour 15 as
well. As shown in figure5.13, the MILP model underestimates the power consumption at the
beginning and end of the charging process and overestimates it in the middle part. Therefore,
the charging is started in hour 14 so the middle part of the charging process with the most
energy consumption takes place during hour 15. This results in higher costs for the MILP
model, because the real power consumption of the CAES system is more similar to the DP
model.
Figure5.14shows the resulting cost savings of all scenarios with a perfect air demand forecast
(3.277\\frac{c t}{k M h})
16,(3.394,\\frac{\\mathsf{c t}}{\\mathsf{k W h}})
Figure5.14shows the resulting cost savings of all scenarios with a perfect air demand forecast
using an optimization timestep size of 15 minutes. Taking into account that the influence of
measurement inaccuracy and the operation of the system can result in a cost difference of up
to 0.20 e (see section5.2.2), there is no significant variation in the results for the non-working
day air demand. For the working day air demand, the resulting cost savings with the LP
method are significantly lower than with the other methods. Except in the scenario with an
untypical electricity price, the cost savings with the DP and the MILP method are very similar.
0.20\\in
* * *
Figure 5.12: Results for perfect forecast, air demand non-working day and typical el. price
Figure 5.13: Simulated power consumption of a charging process using the linear programming
(LP), the mixed-integer linear programming (MILP) and the nonlinear (NL) model compared to
measured data
* * *
Figure 5.14: Cost savings for perfect air demand forecast with 15 minute optimization timestep
size
5.3.2 Imperfect air demand forecast
To compare the influence of the quality of the air demand forecast on the performance of the
different optimization methods, experiments with an inaccurate and a worst-case air demand
forecast are performed, as described in section5.1.1. For each forecast scenario, two different
air demand scenarios, working day and non-working day, are used for the comparison.
Air demand working day
To investigate the influence of an imperfect air demand forecast, the air demand time series
used for the optimization is different than the demand applied to the CAES system. The
optimization always uses the typical air demand shown in figure5.2, which is also applied
for the perfect forecast scenarios (as described in section5.1.1). For the scenarios with an
inaccurate forecast, a demand time series that differs a little bit from the typical one is applied
to the CAES system. For the scenarios with a worst-case forecast, the applied air demand is
very different from the one used for the optimization.
Figure5.15shows the storage pressure and the electric power consumption over time for
Figure5.15shows the storage pressure and the electric power consumption over time for
the three optimization methods using the inaccurate air demand forecast and an optimization
timestep size of 15 minutes. With the LP method, the storage is not completely discharged in
the first cycle because the model does not take into account that the booster consumes more
power when the storage pressure is higher during charging. This results in higher costs than
with the other two methods, as shown in figure5.19. Because of the limitations of the MILP
model described in section5.2.5, in contrast to the DP method, the storage capacity is not
used completely in the first cycle. Additionally, the more detailed DP model leads to a longer
charging period in the second cycle. This results in higher costs savings using the DP method.
* * *
Figure 5.15: Results for inaccurate forecast, air demand working day and typical el. price
Figure 5.16: Results for worst-case forecast, air demand working day and typical el. price
* * *
5.3. Results For the worst-case forecast scenario with the working day air demand, the storage can be charged completely during the first cycle because of a slightly different starting pressure (as explained in section5.2.5). Therefore, the behavior of the MILP and the DP method are very similar in this scenario, which leads to almost the same resulting cost savings. Because the applied air demand is much lower than the air demand used in the optimization (see figure
5.2), all three methods underestimate the discharging time. Because of the lower air demand, particularly at the end of the day, also less energy and money can be saved during discharging in the high price periods. This leads to lower cost savings especially for the LP method, in which the storage is completely discharged during this time.
## Air demand non-working day
For the non-working day air demand also an inaccurate and a worst-case forecast scenario are investigated. The non-working day air demands used for the imperfect forecast scenarios are shown in Figure5.3. Figure5.17shows the storage pressure and power consumption for the inaccurate forecast scenario with air demand non-working day. The results for the worst-case forecast scenario with the same air demand are shown in figure5.18. The charging times of both scenarios are very similar, whereby in the worst-case forecast scenario, the storage is discharged faster because of the higher air demand. The earlier charging process of the MILP method is caused by the difference in modeling the power consumption during charging, as explained in section
5.3.1for the non-working day air demand with a typical electricity price and perfect forecast scenario (see figure5.12). In the inaccurate forecast scenario, the similar behavior of the LP and DP method lead to almost the same cost savings (see figure5.19). Because of the low air demand, the short discharging and charging period in the middle of the second cycle using the LP method has only little influence on the costs. The earlier charging sequence of the MILP method together with the fact that the storage can not be completely discharged in this case (as explained in section5.2.5) leads to lower savings. In the worst-case forecast scenario, the short discharging and charging of the LP method has a bigger influence on the costs, as the higher air demand leads to a higher additional energy consumption. In this case, the storage can be discharged completely using the MILP method. Additionally, the higher storage pressure in the second cycle leads to higher cost savings. Therefore, the costs of the MILP and the DP are almost the same in this scenario. Figure5.19shows the resulting cost savings of all scenarios with an imperfect air demand forecast using an optimization timestep size of 15 minutes. For both inaccurate forecast scenarios, the DP method leads to the highest cost savings, while the savings of the LP and the MILP model depend on the air demand. For the worst-case forecast scenarios, the results of the DP and the MILP model are very similar and significantly better than with the LP method.
* * *
Figure 5.17: Results for inaccurate forecast, air demand non-working day and typical el. price
Figure 5.18: Results for worst-case forecast, air demand non-working day and typical el. price
* * *
Figure 5.19: Cost savings for imperfect air demand forecast with 15 minute optimization
timestep size
5.3.3 Influence of the optimization timestep size
Perfect forecast
To investigate the influence of the optimization timestep size, all experiments were performed
with a timestep size of 5 and 15 minutes. A smaller timestep size allows a faster adjustment
of the system operation, if the measured system behavior differs considerably from the one
predicted by the model. Additionally, the system is modeled in more detail and it is possible to
apply more operating state changes within a certain time period. But more timestep during
the optimization horizon increases the complexity of the optimization problem. Instead of
96 operation state decisions with a 15 minute timestep size, 288 decisions with a 5 minute
step size have to be calculated for a 24-hour optimization horizon. Additionally, the maximum
solving time decreases with the timestep size, since the problem has to be solved within one
time period. For the LP method, the optimization problem is always solved within the time limit
for both variants. For the MILP model in some cases the solving process is stopped because
the time limited is exceeded, before the absolute or relative MIP gap (see section5.2.3) is
reached, when a timestep size of 5 minutes is used. This may lead to a suboptimal solution
and therefore higher costs. For the DP method, the discretization steps of the storage pressure
have to be reduced when using a 5 minute step size, to ensure the problem is solved within the
time limit (see section5.2.3). This results in a less accurate model and therefore can also lead
to worse optimization results than with a 15 minute step size.
* * *
less detailed LP model shows the highest deviations using the different timestep sizes, but as
for the MILP model both variants can lead to lower costs, dependent on the given scenario.)
Working day - untypical price
Non-working day - untypical price
Figure 5.20: Cost savings compared by optimization timestep size for perfect forecast
With the MILP method, in two cases the 5 minute and in two cases the 15 minute timestep size
lead to lower costs dependent on the air demand and electricity price. Figure5.21shows the
results for both timestep variations for the scenario with the air demand working day and an
results for both timestep variations for the scenario with the air demand working day and an
untypical electricity price. The different charging and discharging times and pressure levels
are mainly caused by the slightly different starting pressures, as explained in section5.2.5. In
this case, the costs for the 5 minute timestep size are lower. In contrast, for the scenario with
working day air demand and typical electricity price, the costs using a 5 minute timestep size
are higher. As shown in Figure5.22, the storage cannot be completely discharged in the 5
minute case.
The LP method shows the widest cost difference between the two timestep size scenarios.
results for both timestep variations for the scenario with the air demand working day and an
untypical electricity price. The different charging and discharging times and pressure levels
are mainly caused by the slightly different starting pressures, as explained in section5.2.5. In
this case, the costs for the 5 minute timestep size are lower. In contrast, for the scenario with
working day air demand and typical electricity price, the costs using a 5 minute timestep size
are higher. As shown in Figure5.22, the storage cannot be completely discharged in the 5
The LP method shows the widest cost difference between the two timestep size scenarios.
The LP method shows the widest cost difference between the two timestep size scenarios.
Here in 3 of 4 cases the 15 minute step size results in higher cost savings, whereas in the
scenario with the highest difference, the 5 minute step size results in higher savings. Figure
5.23shows the storage pressure and the power consumption for both timestep variations for
the scenario with the air demand working day and a typical electricity price. Here the short
discharge period in hour 8, which is only performed in the 5 minute scenario, leads to a lower
pressure level for the following hours and causes some interruptions during the discharging
period in hour 20. The additional power consumption in this period with a high electricity price
leads to higher costs than for the 15 minute step size. In the scenario with the air demand
working day and a untypical electricity price, which is shown in figure5.24, the discharging in
hour 20 can be stopped after 5 minutes in the case with the lower step size. As a consequence
the storage can be discharged longer in the following hours with higher electricity prices, which
results in lower costs.
* * *
Figure 5.21: Results for perfect forecast, air demand working day, untypical el. price with
optimization method MILP
Figure 5.22: Results for perfect forecast, air demand working day, typical el. price with
optimization method MILP
* * *
Figure 5.23: Results for perfect forecast, air demand working day, typical el. price with
optimization method LP
Figure 5.24: Results for perfect forecast, air demand working day, untypical el. price with
optimization method LP
* * *
5.3. Results
For the DP method, the cost savings using the 15 minute step size are slightly higher for
all scenarios. Figure5.25shows the storage pressure and the power consumption for both
timestep variations for the scenario with the air demand working day and an untypical electricity
price. Although the curves are not exactly the same, there is no obvious explanation for the
higher costs using the 5 minute step size. Therefore, the very small difference in the costs is
probably caused by inaccuracy of the measurement and operation, as described in section
5.2.2.
Figure 5.25: Results for perfect forecast, air demand working day, untypical el. price with
optimization method DP
Imperfect forecast
Figure5.26compares the cost saving between the two optimization timestep sizes for all
scenarios with an inaccurate and a worst-case forecast. In general, the differences in the
resulting costs using a 5 minute or a 15 minute timestep size are higher than for the perfect
forecast scenarios. For the LP method the 15 minute step size leads to better results, the 5
minute step size yields superior results for the MILP method. For the DP method both variants
can lead to lower or higher costs.
* * *
Inaccurate forecast - non-working day
Worst-case forecast - working day
Worst-case forecast - non-working day
Figure 5.26: Cost savings compared by optimization timestep size for imperfect air demand
forecast
The differences in cost savings between the 5 and 15 minute timestep size using the DP
method are generally very small. Dependent on the scenario, the deviation of the real from the
predicted system behavior because of the imperfect air demand forecast can lead to higher
cost savings using both timestep sizes. For the inaccurate forecast - working day scenario,
shown in figure5.29, the fact that the air demand is slightly lower than predicted, leads to
higher cost savings using the 15 minute timestep size. In contrast, for the worst-case forecast -
working day scenario (see figure5.30), where the air demand is much lower than the forecast
used for the optimization, higher savings are achieved using the 5 minute step size.
For the LP method, the 15 minute timestep size results in higher cost savings for every scenario.
For the LP method, the 15 minute timestep size results in higher cost savings for every scenario.
Figure5.31shows the storage pressure and electric power consumption for the scenario with
a worst-case forecast and non-working day air demand. The reason for the higher costs using
the 5 minute step size are the frequent changes of the operation mode, especially during the
second cycle. These changes are caused by the failure of the predicted system behavior of
the inaccurate LP model and lead to additional start-up and shut-down losses of the system,
which can not be modeled using linear programming.
* * *
Figure 5.27: Results for inaccurate forecast, air demand non-working day, typical el. price
with optimization method MILP
Figure 5.28: Results for inaccurate forecast, air demand working day, typical el. price with
optimization method MILP
* * *
Figure 5.29: Results for inaccurate forecast, air demand working day, typical el. price with
optimization method DP
Figure 5.30: Results for worst-case forecast, air demand working day, typical el. price with
optimization method DP
* * *
Figure 5.31: Results for worst-case forecast, air demand non-working day, typical el. price
with optimization method LP
5.3.4 Result summary
Figure5.32shows the average cost savings for the scenarios with perfect and imperfect air
demand forecast, as well as for all performed scenarios together (total), compared by the
optimization timestep size and method. The results show that, in average, the highest cost
savings can be achieved using the most detailed nonlinear model solved with the dynamic
programming optimization method. However, the cost savings obtained by using the MILP
method are only 0.9 % less for all scenarios taken together and even 0.8 % higher for the
imperfect forecast scenarios. Although the LP method guarantees a fast and reliable solution of
the optimization problem within the MPC, the limited accuracy of the model leads to obviously
lower cost savings than the other methods (in average 11.7 % lower than DP fo all scenarios).
For the DP method, the influence of the two applied optimization timestep sizes is with 0.9 %
difference for all scenarios very small. For the MILP method, a lower timestep size reduces
the problem that the storage can not be completely charged and discharged in some cases,
as explained in section5.2.5. Therefore, using a 5 minute timestep size leads to higher costs
saving for the MILP method. A lower step size causes an increased number of changes in
operation mode because of the inaccuracies in the LP model. The resulting start-up and
shut-down losses lead to increased costs at a lower step size and thus the higher cost savings
are obtained for the 15 minute step size for the LP model.
Table5.7summarizes the cost savings of the different optimization methods for all performed
* * *
Figure 5.32: Mean cost savings compared by optimization timestep size and method for perfect
and imperfect air demand forecast and all scenarios (total)
Table 5.7: Cost savings of the optimization methods for all scenarios
| Forecast | Air demand | Electricity price | Timestep size | LP(€) | MILP(€) | DP(€) |
| Perfect | Working day | Typical | 5 minutes | 1.56 | 1.93 | 1.94 |
| 15 minutes | 1.69 | 1.95 | 1.94 |
| Untypical | 5 minutes | 1.88 | 1.97 | 2.04
| 15 minutes | 1.64 | 1.85 | 2.10 |
| Non-working day | Typical | 5 minutes | 1.85 | 1.87 | 1.88 15 minutes | 1.89 | 1.83 | 1.91 |
| Untypical | 5 minutes | 1.52 | 1.75 | 1.70
| 15 minutes | 1.66 | 1.76 | 1.74 |
| Inaccurate | Working day | Typical | 5 minutes | 1.32 | 1.54 | 1.62 |
| 15 minutes | 1.51 | 1.52 | 1.71 |
| Non-working day | Typical | 5 minutes | 1.61 | 1.79 | 1.69 15 minutes | 1.76 | 1.49 | 1.76 |
| Worst-case | Working day | Typical | 5 minutes | 1.10 | 1.83 | 1.84 |
| 15 minutes | 1.17 | 1.71 | 1.66 |
| Non-working day | Typical | 5 minutes | 0.96 | 1.69 | 1.65 15 minutes | 1.48 | 1.67 | 1.67 |
* * *
Chapter 6
Conclusion
In this thesis different optimization methods for Model Predictive Control (MPC) of a compressed air energy storage system were used and compared. In the first part of the thesis,
the implemented optimization methods were introduced and theoretically analyzed by their
advantages and disadvantages.
The compressed air energy storage (CAES) system, which was used to compare the optimiza-
The compressed air energy storage (CAES) system, which was used to compare the optimization methods, was described in the second part of this thesis. The CAES system represents
a typical compressed air system in the industry that is used to cover a given air demand. An
additional booster is used to store compressed air in a high-pressure storage tank. The stored
air can then be retrieved to cover the air demand. In this way, the electricity consumption of the
system can be influenced and adapted to a given incentive.
A methodology, based on experimental measurements, to calculate the electrical round-trip
A methodology, based on experimental measurements, to calculate the electrical round-trip
efficiency of the storage system was introduced. It was shown that the round-trip efficiency of
the system highly depends on the air demand during charging and discharging. The system
has its best round-trip efficiency of 87 % when charging and discharging in times of low air
demand, which can decrease down to 52 % in the worst-case when the air demand during
charging and discharging is high. An economic evaluation showed that the specific costs of the
CAES system are significantly higher compared to battery storages. Based on the performed
measurements, a linear, a mixed-integer and a nonlinear model was developed and used for
the different Model Predictive Control optimization methods.
The nonlinear model was used to compare the nonlinear optimization methods dynamic
The nonlinear model was used to compare the nonlinear optimization methods dynamic
programming (DP), genetic algorithm (GA) and mixed-integer nonlinear programming (MINLP).
Here the DP method showed the best results for MPC of the CAES system and was used for
further investigations.
To compare the linear programming (LP), mixed-integer linear programming (MILP) and dy-
To compare the linear programming (LP), mixed-integer linear programming (MILP) and dynamic programming methods, several scenarios with different air demands, electricity prices,
optimization timestep sizes and forecast quality were defined. The CAES system was controlled
using MPC with each method for each scenario to cover the given 24-hour air demand with
minimal operational costs. The methods were evaluated based on the cost savings compared
to normal operation mode (covering the demand without using the storage).
The results showed, that over all performed experiments, using the DP method leads to the
The results showed, that over all performed experiments, using the DP method leads to the
highest cost savings. With the LP method, in average 11.7 % less savings could be achieved.
* * *
6. Conclusion
Although LP is able to solve the given optimization problems very fast and with guaranteed optimality, this cannot compensate the limitations in the model representation. The difference in cost savings between the MILP model and the DP model was only 0.9 %. The MILP model is not able to represent the CAES system as exact as the nonlinear model used for DP but more in detail than the LP model. Here the inaccuracy compared to nonlinear model does not affect the results significantly. The identification of the model parameters and implementation of the optimization problem is much more complex for the DP than for the MILP method. The MILP method can also be used for larger energy systems with multiple storages, while the DP method is limited in the system complexity due to the "curse of dimensionality". Additionally, for the imperfect forecast scenarios, which are more realistic than a perfect forecast of all future parameters, the MILP model showed slightly better results in this thesis. Taking this into account, in general, a MILP programming model might be a better choice to use for MPC of an energy system with storages. For small systems with a good forecast, the results of this thesis showed that a nonlinear model using DP leads to the best results. The general structure of the CAES system introduced in this thesis is very similar to other systems that can be used for load management in the electricity sector, such as CHP units or heat pumps in combination with a heat storage. While the main purpose of the system is to cover a given demand (air or heat), the storage is used to decouple electricity consumption or production and supply of air or heat. In this way, the storage systems provide flexibility to the electricity system. Battery storage in combination with a PV system, where the battery is also used to decouple demand and production, can be interpreted similarly. Therefore, the most important question that has to be explored in further investigations is the way in which the results of this thesis can be transferred to other applications. The changes in performance of the different optimization methods when applied to more complex systems with additional storages or power conversion processes should also be further investigated. Additionally, the influence of the forecast quality and the optimization time horizon on the results should be explored further.
* * *
Appendix A
Compressed air energy storage
system specifications
TableA.1summarizes the components of the compressed air energy storage systems.
Table A.1: Components of the compressed air energy storage system
| Component | Manufacturer | Model | Type Dryer | KAESER | Secotec TB 19 | Refrigeration dryer | \[50\] |
| Filter | KAESER | FE 18 D | Filter | \[49\] |
| High-pressure tank | Maschinen- und Behälterbau GmbH | 2000l, 50barg, vertical | Air receiver | \[44\] |
| Air receiver tank | OKS Otto Klein GmbH | 2000l, 16barg, vertical | air receiver | \[44\] |
| Valve | Gemü | 751 40D 137 51AU08KC0 | Ball valve | \[33\] |
| Control valve | Gemü | 554 20D 19 51 1RS013 | Control valve | \[32\] |
| Control valve | Gemü | 1434000Z1A141A001030 | Positioner | \[32\] |
| Pressure regulator | Aircom tecsis | R120 - 12 E01 | Pressure regulator | \[2\] |
| $T\_{1}, T\_{2}, T\_{3}$ | tecsis | TEP11x222006 | Resistance thermometer | \[96\] |
| p\_{1}, p\_{2}$ | HYDAC | HDA 4745-A-016-000 | Pressure transmitter | \[39\] |
| p\_{3}$ | HYDAC | HDA 4745-A-045-000 | Pressure transmitter | \[39\] |
| P\_{1}, P\_{2}$ | Müller + Ziegler | Pdr-MU 50 Hz 400/230V 20/1A 10kW | Electric power meter | \[74\] |
| P\_{3}, P\_{4}$ | Müller + Ziegler | Pdr-MU 50 Hz 400/230V 10/1A 6kW | Electric power meter | \[74\] |
50\ \ mathsf b b a{\\mathfrak{r}\_{\\mathtt{g}}},
T\_{1},T\_{2},T\_{3}
p\_{3}
p\_{1},p\_{2}
P\_{1},,P\_{2}
P\_{3},,P\_{4}
* * *
A.2 Costs
TableA.2shows the costs of the components for theCAESneeded in addition to a typical
compressed air system in the industry.
Table A.2: Component costs of the compressed air energy storage system
| Component | Costs |
| Outlet valve | 200€ |
| Pressure regulator | 1.300€ |
| High-pressure storage tanks | 45.000€ |
| Booster | 8.700€ |
| Total | 55.200€ |
* * *
Appendix B
Mathematical description of the
models
This chapter contains the detailed mathematical description of all optimization models used in
this thesis.
The linear programming (LP), the mixed-integer linear programming (MILP) and the mixed-
The linear programming (LP), the mixed-integer linear programming (MILP) and the mixedinteger nonlinear programming (MINLP) models are implemented using Pyomo, a Pythonbased algebraic modeling language \[83\]. In Pyomo, as in other algebraic modeling languages,
optimization problems are defined by sets, variables, parameters, an objective function and a
number of equality and inequality constraints. The mathematical description of the models in
this thesis is based on this formulation.
The simulation model used for the genetic algorithm (GA) and dynamic programming (DP) is
this thesis is based on this formulation.
The simulation model used for the genetic algorithm (GA) and dynamic programming (DP) is
implemented in Python.
B.1 Linear programming model
The LP model is described by a set of linear equality and inequality functions, shown in this
section. The parameters and variables used to describe the problem are summarized in table
B.2and tableB.1. The values of the constant parameters are shown in sectionC.1, tableC.2.
The optimization horizon is described by the set of timesteps T = ft1;:::;tNg,where t is the
duration of each timestep, and N is the number of timesteps t 2T.
The objective of theLPmodel is to minimize the total costs over the optimization horizon, that
\\mathcal{T}={t\_{1},...,t\_{N}}
C\_{e I}^{t}
The objective of theLPmodel is to minimize the total costs over the optimization horizon, that
tel ttot
depend on the electricity price C and the total power consumption of the system P at
ttot
each timestep. The total power consumption of the system P is comprised of the power
tco tch tdch
consumption of the compressors P and the charge power P or discharge power P of
the electrical energy storage.
(B.1)
P\_{t o t}^{t}
\\mathsf{m i n},c\_{t o t}=\\mathsf{m i n}\\left(\\sum\_{t\\in\\mathcal{T}}C\_{e l}^{t}\\cdot P\_{t o t}^{t}\\cdot\\frac{\\Delta t}{3600,\\frac{\\mathsf{s}}{\\mathsf{h}}}\\right)
t\\in\\mathcal
P\_{c o}^{t}
P\_{t o t}^{t}=P\_{c o}^{t}+P\_{c h}^{t}-P\_{d c h}^{t}\ \ \ \ \\forall t\\in\\mathcal{T}
P\_{d c h}^{t}
* * *
Table B.1: Variables of the LP model
| Name | ∈ | Unit | Description |
| $\\dot{V}\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | $\\frac{m\_{n}^{3}}{min}$ | Compressed air produced by the compressors at timestep t |
| $P\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |
| $P\_{tot}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |
| $P\_{ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical charge power of the storage at timestep t |
| $P\_{dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical discharge power of the storage at timestep t |
| $E\_{sto}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kWh | Electrical energy content of the storage at timestep t |
| $c\_{tot}$ | $\\mathbb{R}\_{0}^{+}$ | € | Total costs to be minimized |
\\in
\\dot{v}\_{c o}^{t}
\\underline{{\\mathfrak{m}}}\_{\\mathrm{n}}^{3}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
P\_{c o}^{t}
P\_{t o t}^{t}
P\_{c h}^{t}
\\mathbb{R}\_{0}^{+}
P\_{d c h}^{t}
\\mathbb{R}\_{0}^{+}
E\_{s t o}^{t}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
c\_{t o t}
\\in
Table B.2: Parameters of the LP model
| Name | Unit | Description |
| $\\overline{E}\_{sto}$ | kWh | Maximum electrical energy capacity of storage |
| $s\_{1}$ | $\\frac{kW}{m\_{n}^{3}/\\min}$ | Slope of the linear function used to model the electrical power consumption of the compressors |
| $\\eta\_{ch}^{t}$ | 1 | Storage electrical charge efficiency at timestep t |
| $\\eta\_{dch}^{t}$ | 1 | Storage electrical discharge efficiency at timestep t |
| $\\dot{V}\_{d}^{t}$ | $\\frac{m\_{n}^{3}}{min}$ | Air demand at timestep t |
| $\\bar{P}\_{ch}^{t}$ | kW | Upper limit of the electrical charge power at timestep t dependent on $\\dot{V}\_{d}^{t}$ |
| $C\_{el}^{t}$ | $\\frac{\\epsilon}{kWh}$ | Electricity price at timestep t |
| $\\Delta T$ | h | Duration of the optimization horizon |
| $\\Delta t$ | s | Timebase of the optimization (duration of one time period) |
| N | 1 | Number of timesteps $N=\\frac{\\Delta T}{\\Delta t/3600}$ |
\\overline{{E}}\_{s t o}
\\frac{k M}{m\_{n}^{3}/m\ n}
\\overline{{\\eta\_{c h}^{t}}}
\\eta\_{d c h}^{t}
\\frac{\\mathsf{m}\_{\\mathsf{n}}^{3}}{\\mathsf\*{m i n}}
\ {dot v\_\_{d d}^{t}}
\\overline{{P}}\_{c h}^{t}
\ {dot v\_\_{d d}^{t}}
C\_{e I}^{t}
\\overline{{\\Delta T}}
\\Delta t
\\begin{array}{r}{N=\\frac{\\Delta T}{\\Delta t/3600}}\\end{array}
tco
The power consumption of the compressors P is modeled as a linear function of the air
demand V\_dwith the slope &1.
\\varsigma\_{1}
(B.3)
\\boldsymbol{P} _{c o}^{t}=\\boldsymbol{\\varsigma}_{1}\\cdot\\dot{\\boldsymbol{V}}\_{d}^{t};;;;;;\\forall t\\in\\mathcal{T}
{\\dot{v}}\_{d}^{t}
tsto +1
The energy content E of the electrical energy storage for the timestep t + 1 is calculated
tsto tch tdch
based on the energy content E, the charge power P, and the discharge power P
at timestep t. The losses during charging and discharging are represented by the charge
tch tdch
efficiency and the discharge efficiency, that are dependent on the corresponding air
demand at each timestep.
E\_{s t o}^{t+1}
tsto
The energy storage content E is limited by the maximum energy capacity of the storage
Esto.
E\_{s t o}^{t+1}=E\_{s t o}^{t}+\\eta\_{c h}^{t}\\cdot P\_{c h}^{t}-\\frac{1}{\\eta\_{d c h}^{t}}\\cdot P\_{d c h}^{t}\ \ \ \ \ \\forall t\\in\\mathcal{T}
(B.5)
E\_{s t o}^{t}\\leq\\overline{{E}}\_{s t o};;;;;;\\forall t\\in\\mathcal{T}
\\bar{E}\_{s t o}
* * *
B.1. Linear programming model
tdch
The power consumption of the compressors is used as an upper limit of discharge power P
in every timestep.
P\_{d c h}^{t}
\ _{d c h}^{t}\\leq P_{c o}^{t}\ \ \ \ \\forall t\\in\\mathcal{T}
(B.6)
tch tch
The mean charge power P is used as an upper limit of the charge power P in every
timestep.
\\overline{{P}}\_{c h}^{t}
\ _{c h}^{t}\\leq\\overline{{P}}_{c h}^{t}\ \\\ \\\forall{t\ \ \ \ }\ forallforall{t\\in\\mathcal{T}}
P\_{c h}^{t}
(B.7)
The compressed air energy storage (CAES) system expects a target operation mode, normal,
charge, or discharge as an input. Therefore the results of the solved LP problem has to be
converted to an adequate operation mode. Therefore, in every timestep where the storage is
tch
charged (P > 0) the target operation mode is set to charge, and in every state where the
tdch
storage is discharged (P > 0) it is set to discharge. If both, charge and discharge power
are zero, the target operation mode is set to normal.
(P\_{c h}^{t}>0)
(\\bar{P}\_{d c h}^{t}>0)
* * *
B.2 Mixed-integer linear programming model
This section describes the set of linear equality and inequality functions used to model the
mixed-integer linear programming (MILP) optimization problem. The parameters and variables
used to describe the problem are summarized in tableB.3and tableB.4. The values of the
constant parameters are shown in sectionC.2, tableC.3. The optimization horizon is described
by the set of timesteps T = ft1;:::;tNg,where t is the duration of each timestep, and N is
the number of timesteps t 2T.
\\mathcal{T}={t\_{1},...,t\_{N}}
\\Delta t
t\\in\\mathcal{T}.
Table B.3: Parameters of the MILP model
| Name | Unit | Description |
| $\\hat{p}\_{sys}^{norm}$ | barg | Setpoint pressure in normal mode (normal system pressure) |
| $\\bar{p}\_{sto}$ | barg | Maximum storage pressure |
| $p\_{sto}$ | barg | Minimum storage pressure |
| $\\dot{\\vec{V}}\_{co}$ | $\\frac{m\_{n}^{3}}{min}$ | Maximum free air delivery of the compressors |
| $E\_{co,su}$ | kWh | Start-up losses of the compressors |
| $E\_{co,sd}$ | kWh | Shut-down losses of the compressors |
| $E\_{bo,su}$ | kWh | Start-up losses of the booster |
| $E\_{bo,sd}$ | kWh | Shut-down losses of the booster |
| $\\varsigma\_{i}$ | | Parameters used to model the electrical power consumption of the compressors |
| $\\beta\_{i}$ | | Parameters used to model the electrical power consumption of the booster |
| $\\delta\_{ch,i},\\delta\_{dch,i}$ | | Parameters used to model the storage pressure state equation |
| $r\_{bo}$ | 1 | Maximum compression ratio of the booster |
| $\\dot{V}\_{d}^{t}$ | $\\frac{m\_{n}^{3}}{min}$ | Air demand at timestep t |
| $C\_{el}^{t}$ | $\\frac{€}{kWh}$ | Electricity price at timestep t |
| $\\Delta T$ | h | Duration of the optimization horizon |
| $\\Delta t$ | s | Timebase of the optimization (duration of one time period) |
| N | 1 | Number of timesteps N=$\\frac{\\Delta T}{\\Delta t/3600}$ |
\\hat{p}\_{s y s}^{n o r m}
b a r\_{9}
b a r\_{9}
\\overline{{p}}\_{s t o}
\\underline{{p\_{s t o}}}
\ a{mathfrak r}\_{\\mathfrak{g}}
\\underline{{\\mathfrak{m}}}\_{\\mathrm{n}}^{3}
\\dot{\\bar{V}}\_{c o}
E\_{c o,s u}
E\_{c o,s d}
E\_{b o,s u}
E\_{b o,s d}
\\varsigma\_{i}
\\beta\_{i}
\\delta\_{c h,i},\\delta\_{d c h,i}
\ {dot v\_\_{d d}^{t}}
\\underline{{\\mathfrak{m}}}\_{\\mathrm{n}}^{3}
C\_{e I}^{t}
\\frac{\\epsilon}{k W n}
\\overline{{\\Delta T}}
(B.8)
In theMILPformulation of the optimization problem binary variables representing the operation
mode of theCAESsystem can be used. Here the three modes normal, charge and discharge
tch tdch
are represented by two binary variables b and b that can be either 0 or 1. At timestep t,
tch tdch
theCAESsystem is in charge mode, when b = 1, and in discharge mode, when b = 1 .
When both variables are zero, the system is in normal operation mode. The constraint in eq.
B.8avoids that both variables become 1 at the same timestep.
\\Delta t
\\begin{array}{r}{N=\\frac{\\Delta T}{\\Delta t/3600}}\\end{array}
b\_{c h}^{t}
P\_{c o}^{t}
* * *
Table B.4: Variables of the MILP model
| Name | ∈ | Unit | Description |
| $p\_{sys}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | System pressure at timestep t |
| $\\tilde{p}\_{sys,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Auxiliary variable representing the product of the system pressure and the binary variable $b\_{ch}^{t}$ |
| $\\tilde{p}\_{sys,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Auxiliary variable representing the product of the system pressure and the binary variable $b\_{dch}^{t}$ |
| $p\_{sto}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Storage pressure at timestep t |
| $\\Delta p\_{sto,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when charging |
| $\\Delta \\tilde{p}\_{sto,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Auxiliary variable for calculating $\\Delta p\_{sto,ch}^{t}$ |
| $\\Delta p\_{sto,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when discharging |
| $\\Delta \\tilde{p}\_{sto,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Auxiliary variable for calculating $\\Delta p\_{sto,dch}^{t}$ |
| $p\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure for calculating the power consumption of the booster |
| $\\dot{V}\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | $\\frac{m\_{h}^{3}}{min}$ | Compressed air produced by the compressors at timestep t |
| $P\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |
| $P\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the booster at timestep t |
| $P\_{tot}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |
| $b\_{ch}^{t}$ | \[0,1\] | 1 | Binary variable related to the operation mode charge at timestep t |
| $b\_{dch}^{t}$ | \[0,1\] | 1 | Binary variable related to the operation mode discharge at timestep t |
| $b\_{co,su}^{t}$ | \[0,1\] | 1 | Binary variable related to the compressors startup at timestep t |
| $b\_{co,sd}^{t}$ | \[0,1\] | 1 | Binary variable related to the compressors shut-down at timestep t |
| $b\_{bo,su}^{t}$ | \[0,1\] | 1 | Binary variable related to the booster startup at timestep t |
| $b\_{bo,sd}^{t}$ | \[0,1\] | 1 | Binary variable related to the booster shut-down at timestep t |
| $c\_{tot}$ | $\\mathbb{R}\_{0}^{+}$ | € | Total costs to be minimized |
\\in
p\_{s y s}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt{b a t}\_{\\mathfrak{g}}
\\tilde{p}\_{s y s,c h}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt r a{\_mathfrak g}
\\mathbb{R}\_{0}^{+}
b\_{c h}^{t}
\\tilde{p}\_{s y s,d c h}^{t}
\\mathtt{b a r}\_{\\mathtt{g}}
p\_{s t o}^{t}
b\_{d c h}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt{b a r}\_{\\mathtt{g}}
\\Delta p\_{s t o,c h}^{t}
\\mathbb{R}\_{0}^{+}
\ a r\_{\\mathfrak{g}}
\\Delta\\tilde{p}\_{s t o,c h}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt r a{\_mathfrak g}
\\Delta p\_{s t o,c h}^{t}
\\Delta p\_{s t o,d c h}^{t}
b a l\_{\\mathfrak{g}}
\\mathbb{R}\_{0}^{+}
\\Delta\\tilde{p}\_{s t o,d c h}^{t}
\\mathbb{R}\_{0}^{+}
\\mathtt{b a r}\_{\\mathtt{g}}
\\Delta p\_{s t o,d c h}^{t}
p\_{b o}^{t}
\\mathbb{R}\_{0}^{+}
\ a{mathfrak r}\_{\\mathfrak{g}}
\\dot{v}\_{c o}^{t}
\\mathbb{R}\_{0}^{+}
\\frac{\\mathsf{m}\_{\\mathsf{n}}^{3}}{\\operatorname\*{m i n}}
P\_{c o}^{t}
\\mathbb{R}\_{0}^{+}
P\_{b o}^{t}
\\mathbb{R}\_{0}^{+}
P\_{t o t}^{t}
\\mathbb{R}\_{0}^{+}
b\_{c h}^{t}
b\_{d c h}^{t}
b\_{c o,s u}^{t}
b\_{c o,s d}^{t}
b\_{b o,s u}^{t}
b\_{b o,s d}^{t}
\\mathsf{m i n},c\_{t o t}=\\mathsf{m i n}\\left(\\sum\_{t\\in\\mathcal{T}}C\_{e l}^{t}\\cdot P\_{t o t}^{t}\\cdot\\frac{\\Delta t}{3600,\\frac{\\mathsf{s}}{\\mathsf{h}}}\\right)
(B.9)
C\_{t o t}
\\mathbb{R}\_{0}^{+}
\\in
E\_{b o,s u}
(b\_{c h}^{t}{=}1)
(b\_{b o,s u}^{t}=1
(b\_{b o,s d}^{t}=1
p\_{b o}^{t}
Booster
\ _{t o t}^{t}=P_{c o}^{t}+P\_{b o}^{t}\ \\\ forall t t\\in\\mathcal{T}
P\_{b o}^{t}
tbo
The power consumption of the booster P is modeled as a linear function dependent on the
t tch
pressure p at its output. The offset2is added if the system is in charge mode (b =1).
tbo;su
Additionally, energy losses Ebo;suduring startup (b = 1, when the system changes from
tbo;sd
charge or normal to discharge mode) and energy losses Ebo;sdduring shut-down (b = 1,
when the system switches from discharge to another mode) are considered.
(B.11)
\\begin{array}{l l l}}{{{P} _{b o}^{t}=\ {\\boldsymbol{\\beta}}_{1}\\cdot{\\boldsymbol{p}} _{b o}^{t}+{\\boldsymbol{\\beta}}_{2}\\cdot{\\boldsymbol{b}} _{c h}^{t}}\ {\\quad+quad{\\boldsymbol{b}}_{b o,s u}^{t}\\cdot{\\boldsymbol{E}} _{b o,s u}\\cdot\\frac{3600\ {\\mathrm{\\tiny ~~s~~}}}{\\Delta t}}\ {\\quad+{\\boldsymbol{b}}_{b o,s d}^{t}\\cdot{\\boldsymbol{E}} _{b o,s d}\\cdot\\frac{3600\ {\\frac{\ {boldsymbol s s}}{\\hbar}}}{\\Delta t}\\quad}&{\\forall t\\in\ {mathcal T}}\\endendarray}}\ b_{b o,s u}^{t}\\geq b\_{c h}^{t}-b\_{c h}^{t-1}~~~~~\\forall t\\in\\mathcal{T}
(B.12)
b\_{b o,s d}^{t}\\geq b\_{c h}^{t-1}-b\_{c h}^{t};;;;;;\\forall t\\in\\mathcal{T}
(B.13)
tdch t
When the booster is running (b =1), its output pressure p corresponds to the pressure in
the high pressure storage psto. To make sure, that the power consumption of the booster is
zero when it is not running, p has to be zero in this case.
(b\_{d c h}^{t}{=}1)
p\_{b o}^{t}
p\_{s t o}^{t}
p\_{b o}^{t}
p\_{b o}^{t}-p\_{s t o}^{t}\\geq-\\bar{p} _{s t o}\\cdot\\left(1-b_{d c h}^{t}\\right)\ ~~~~\\forall t\\in\\mathcal{T}
(B.14)
Compressors
The power consumption of the compressors is modeled as a linear function dependent on the
air covered by the compressors V\_co, the difference of the system pressure and the normal
t norm
system pressure (psys-p^sys) and the product of both. To implement the multiplication V\_co
t norm t t
(psysp^sys) as a linear expression, the auxiliary variables p~ and p~, representing
sys;ch sys;dch
t norm tch tdch
the multiplication of (psys-p^sys) with the binary variables b and b (as definde in eqs.B.22
-B.27), and the definition of the air covered by the compressors V\_coin eq.B.18are used. The
tdch
offset &4is added if the system is in charge or normal mode (b = 0). Additionally, energy
tco;su
losses Eco;suduring startup (b = 1, when the system changes from discharge to another
tco;sd
mode) and energy losses Eco;sdduring shut-down (b = 1, when the system switches from
normal or charge to discharge mode) are considered.
\\dot{V}\_{c o}^{t}
\\dot{V}\_{c o}^{t}
(p\_{s y s}^{t}\ \\hat{p}\_{s y s}^{n o r m})
\\tilde{p}\_{s y s,c h}^{t}
(p\_{s y s}^{t}-\\hat{p}\_{s y s}^{n o r m})
\\tilde{p}\_{s y s,d c h}^{t}
(p\_{s y s}^{t}\ \\hat{p}\_{s y s}^{n o r m})
b\_{c h}^{t}
b\_{d c h}^{t}
\\dot{v}\_{c o}^{t}
\\varsigma\_{4}
(b\_{d c h}^{t}=0)
E\_{c o,s u}
(b\_{c o,s u}^{t}=1
(b\_{c o,s d}^{t}=1
E\_{c o,s d}
\\begin{array}{r l}{P\_{c o}^{t}=}&{\\varsigma!{ _1}\\cdot\\dot{V}_{c o}^{t}+!\\varsigmavarsigma{ _2}\\cdot\\left(p_{s y s}^{t}-\\hat{\\rho} _{s y s}^{n o r m}\\right)}\ &{!+!{varsigma_{3}}\\cdot\\left(\\dot{{}V} _{d}^{t}\\cdot\\left(p_{s y s}^{t}-\\hat{\\rho} _{s y s}^{n o r m}\\right)-\\dot{V}_{d}^{t}\\cdot\\hat{\\rho} _{s y s,d c h}^{t}+\\dot{V}_{b o}\\cdot\\hat{p}} _{s y s,c h}^{t}\\right)}\ &{!+!!{varsigma{44}}\\cdot\\left(1-b{c h h}^{t}\\right)}\ &{!!+b!{_{c o s,}^{t}\ \\cdot!{! _c c c,s u}}\\cdot!!\\frac{3600\ \\frac{\\mathfrak{s}}{8}}{\\Delta t}}\ &{!!+!!{b_{c o s,d h}^{t}\\cdot!{E\_{c o o,s s}}}\\cdot!\\frac{360\ \ \\frac{\\mathfrak{s}}{8}}{\\Delta t}
(B.15)
b\_{c o,s u}^{t}\\geq b\_{d c h}^{t-1}-b\_{d c h}^{t}\\qquad\\forall t\\in\\mathcal{T}
(B.16)
tch tdch
When the system is in normal mode (b = b = 0), the compressors have to cover the
tch
complete air demand V\_d. In the operation mode charge (b = 1), additionally the air demand
of the booster V\_bohas to be covered. In discharge mode, the air demand is covered by the
high-pressure storage and the air delivered by the compressors is zero. The air that can be
delivered by the compressors is limited to V\_co.
{dot v\_\_{d d}^{t}}
\\dot{\\v V\_\_{c o}}
(b\_{c h}^{t}=1)
\\dot{V}\_{b o}
\|\\mathsf{e},(b\_{c h}^{t}=b\_{d c h}^{t}=0),
(B.18)
\\dot{V} _{c o}^{t}=(1-b_{d c h}^{t})\\cdot\\dot{V} _{d}^{t}+b_{c h}^{t}\\cdot\\dot{V}\_{b o}\ \ \ \ \ \\forall t\\in\\mathcal{T}
* * *
\\dot{V} _{c o}^{t}\\leq\\overline{{\\dot{V}}}_{c o}\\qquad\\forall t\\in\\mathcal{T}
(B.19)
As described in chapter4.3(see eq.4.11and figure4.5), the system pressure psysduring
charging depends on the storage pressure psto. In normal or discharge operation mode, the
t norm
system pressure psyscorresponds to the normal system pressure p^sys. Using the output
pressure of the booster p, which is equal to the storage pressure in charge mode and zero
else (see eq.B.14), this can be formulated as follows.
p\_{s y c}^{t}
p\_{s t o}^{t}
p\_{s y s}^{t}
\\hat{p}\_{s y s}^{n o r m}
p\_{b o}^{t}
p\_{s y s}^{t}\\geq\\hat{p}\_{s y s}^{n o r m}\ quad\\forallforall\ t\\in\\mathcal{T}
(B.20)
p\_{s y s}^{t}\\geq\\frac{p\_{b o}^{t}+2}{r\_{b o}}\\qquad\\forall t\\in\\mathcal{T}
(B.21)
The definition of the power consumption of the compressors (eq.B.15) includes the product
of the the air covered by the compressors and difference of the system pressure and the
t norm
normal system pressure V\_co(psysp^sys). Using the expression of the air covered by the
compressors V\_coin eq.B.18this can be stated as:
t t
t norm t t norm t t norm
V\_ (p p^) V\_ b (p p^) + V\_ b (p p^).
\\dot{V} _{c o}^{t}\\cdot(p_{s y s}^{t}-\\hat{p}\_{s y s}^{n o r m})
\\dot{v}\_{c o}^{t}
\\begin{array}{r}{\\dot{\\boldsymbol{V}} _{d}^{t}\\cdot\\big(boldsymbol p{\ \ s\ }^{t}-\\hat{\\boldsymbol{rho}}s boldsymbol\\gamma s{}}^{n o r m}\\big)-\\dot{\\boldsymbol{V}}{d}^{t}\\cdot\\boldsymbol{b}_{d c h}^{t}\\cdot\\big(\\boldsymbol{p} _{s!\ !{}}_{s!\ \
t t
t norm t t norm t t norm
V\_d(psysp^sys) V\_db (psysp^sys) + V\_bob (psysp^sys).
dch ch
tch t
Since multiplication of the two variables b and psyswould lead to a discontinuous problem,
tch t norm t
the expression b (psysp^sys) is substituted with the auxiliary variable p~, which is
sys;ch
defined as follows:
b\_{c h}^{t}
p\_{s y s}^{t}
b\_{c h}^{t}\\cdot\\big p\_{s v s}^{t}-\\hat{p}\_{s v s}^{n o r m}\\big)
\\tilde{p}\_{s y s,c h}^{t}
(B.22)
\\tilde{p} _{s y s,c h}^{t}-\\big(p_{s y s}^{t}-\\hat{p} _{s y s}^{n o r m}\\big)\\leq\\bar{p}_{s t o}\\cdot\\big(1-b\_{c h}^{t}\\big)~~~~~\\forall t\\in\\mathcal{T}
(B.23)
\\tilde{p} _{s y s,c h}^{t}-\\left(p_{s y s}^{t}-\\hat{p} _{s y s}^{n o r m}\\right)\\geq-\\bar{p}_{s t o}\\cdot\\left(1-b\_{c h}^{t}\\right)\ \ \ \ \\forall t\\in\\mathcal{T}
tdch t norm
The same applies to the expression b (psysp^sys), which is substituted with the auxiliary
variable p~.
sys;dch
\\tilde{p} _{s y s,d c h}^{t}-\\left(p_{s y s}^{t}-\\hat{p} _{s y s}^{n o r m}\\right)\\leq\\bar{p}_{s t o}\\cdot\\left(1-b\_{d c h}^{t}\\right)\\qquad\\forall t\\in\\mathcal{T}
(B.25)
Storage
\\tilde{p}\_{s y s,d c h}^{t}.
b\_{d c h}^{t}!\\cdot!(p\_{s y s}^{t}-!\\hat{p}\_{s y s}^{n o r m}),
p\_{s t o}^{t+1}
(B.27)
\\tilde{p} _{s y s,d c h}^{\\mathrm{t}}-\\left(p_{s y s}^{\\mathrm{t}}-\\hat{p} _{s y s}^{n o r m}\\right)\\geq-\\bar{p}_{s t o}\\cdot\\left(1-b\_{d c h}^{\\mathrm{t}}\\right)\ \ \ \ \\forall t\\in\\mathcal{T}
t+1
The pressure in the high pressure storage tank at the beginning of the next timestep psto
depends on the storage pressure pstoat timestep t and the operation mode of the system. In
charge mode, the pressure difference p is added. In discharge mode the pressure is
sto;ch
\\Delta p\_{s t o,c h}^{t} t
reduced by p. The storage pressure is limited by the lower bound pstoand the upper
sto;dch
bound psto.
\\Delta p\_{s t o,d c h}^{t}
\\underline{{p\_{s t o}}}
\\overline{{p}}\_{s t o}
p\_{s t o}^{t+1}=p\_{s t o}^{t}+\\Delta p\_{s t o,c h}^{t}-\\Delta p\_{s t o,d c h}^{t}~~~~~t\\in\\mathcal{T}
(B.28)
\ {underline{{p}}} _{s t o}\\leq{\\underline{{{p}}}}_{s t o}^{t}\\leq{\\bar{}}\_{s t o}\ ~~~~\\forall t\\in\\mathcal{T}
(B.29)
The pressure increase during charging is modeled as a linear function dependent on the
previous storage pressure psto.
p\_{s t o}^{t}
\\Delta\\tilde{p} _{s t o,c h}^{t}=\\Delta t\\cdot\\left(\\delta_{c h,1}\\cdot p\_{s t o}^{t}+\\delta\_{c h,2}\\right)\\qquad\\forall t\\in\\mathcal{T}
(B.30)
t t
The pressure difference p corresponds to the pressure increase ~p only during
sto;ch sto;ch
tch
charging (b =1), and has to be zero else. This can be stated using the following equations:
\\Delta p\_{s t o,c h}^{t}
\\Delta\\tilde{p}\_{s t o,c h}^{t}
(b\_{c h}^{t}{=}1)
\\Delta p\_{s t o,c h}^{t}\\leq b\_{c h}^{t}\\cdot\\bar{p}\_{s t o}~~~~~\\forall t\\in\\mathcal{T}
(B.31)
(B.32)
\\Delta p\_{s t o,c h}^{t}-\\Delta\\tilde{p} _{s t o,c h}^{t}\\leq\\bar{p}_{s t o}\\cdot\\left(1-b\_{c h}^{t}\\right)\ ~~~~\\forall t\\in\\mathcal{T}
\\Delta p\_{s t o,c h}^{t}-\\Delta\\tilde{p} _{s t o,c h}^{t}\\geq-\\bar{p}_{s t o}\\cdot(1-b\_{c h}^{t})\ \ \ \ \ \\forall t\\in\\mathcal{T}
(B.33)
The pressure decrease during discharging is modeled as a linear function dependent on the
air demand of the system V\_dand the previous storage pressure psto. The additional pressure
tco;sd
decrease at the beginning of a discharge period (b =1) is modeled with the parameter
dch;4.
{\\dot{v}}\_{d}^{t}
p\_{s t o}^{t}
(b\_{c o,s d}^{t}{=}1)
\\delta\_{d c h,4}
(B.34)
\\Delta\\tilde{p} _{s t o,d c h}^{t}=\\Delta t\\cdot\\left(\\delta_{d c h,1}\\cdot\\dot{V} _{d}^{t}+\\delta_{d c h,2}\\cdot p\_{s t o}^{t}+\\delta\_{d c h,3}\\right)+\\delta\_{d c h,4}\\cdot b\_{c o,s d}^{t}\\qquad\\forall t\\in\\mathcal{T},
As for charging, the pressure difference p corresponds to the pressure increase
sto;dch
t tdch
~p only during discharging (b =1), and has to be zero else. This can be stated using
sto;dch
the following equations:
(B.35)
(b\_{d c h}^{t}{=}1)
\\Delta\\tilde{p}\_{s t o,d c h}^{t}
(B.36)
\\Delta p\_{s t o,d c h}^{t}-\\Delta\\tilde{p} _{s t o,d c h}^{t}\\leq\\bar{p}_{s t o}\\cdot\\left(1-b\_{d c h}^{t}\\right)\ quad\\forallforall\ t\\in\\mathcal{T}
\\Delta p\_{s t o,d c h}^{t}-\\Delta\\tilde{p} _{s t o,d c h}^{t}\\geq-\\bar{p}_{s t o}\\cdot(1-b\_{d c h}^{t})~~~~~\\forall t\\in\\mathcal{T}
* * *
B.3 Nonlinear simulation model for dynamic programming and
the genetic algorithm
This section describes the simulation model, which is used for dynamic programming (DP) and
the genetic algorithm (GA) optimization methods. For the GA algorithm the model is simulated
for every individual that is evaluated, returning costs for the whole optimization horizon. For the
DP algorithm the model is used to calculate the cost and follow up state (storage pressure) for
every timestep and state independently. The parameters and variables to describe the model
are summarized in tableB.5and tableB.6. The parameter values are shown in appendixC.2,
table4.4. The simulation model is split into three parts, one part for each operation mode
(normal, charge, discharge).
This section describes the simulation model, which is used for dynamic programming (DP) and
the genetic algorithm (GA) optimization methods. For the GA algorithm the model is simulated
for every individual that is evaluated, returning costs for the whole optimization horizon. For the
DP algorithm the model is used to calculate the cost and follow up state (storage pressure) for
every timestep and state independently. The parameters and variables to describe the model
are summarized in tableB.5and tableB.6. The parameter values are shown in appendixC.2,
table4.4. The simulation model is split into three parts, one part for each operation mode
(normal, charge, discharge).
| Name | Unit | Description |
| $\\hat{p}\_{sys}^{norm}$ | barg | Setpoint pressure in normal mode (normal system pressure) |
| $\\bar{p}\_{sto}$ | barg | Maximum storage pressure |
| $p\_{sto}$ | barg | Minimum storage pressure |
| $p\_n$ | bara | Normal pressure |
| $\\dot{V}\_{co}$ | $\\frac{m^3}{min}$ | Maximum free air delivery of the compressors |
| $V\_{rec}$ | $m^3$ | Volume of air receiver tank |
| $E\_{co,su}$ | kWh | Start-up losses of the compressors |
| $E\_{co,sd}$ | kWh | Shut-down losses of the compressors |
| $E\_{bo,su}$ | kWh | Start-up losses of the booster |
| $E\_{bo,sd}$ | kWh | Shut-down losses of the booster |
| $\\varsigma\_i$ | | Parameters used to model the electrical power consumption of the compressors |
| $\\beta\_i$ | | Parameters used to model the electrical power and air consumption of the booster |
| $\\delta\_i$ | | Parameters used to model the storage pressure state equation |
| $r\_{bo}$ | 1 | Maximum compression ratio of the booster |
| $C\_{pen}$ | € | Penalty charge t |
| $\\dot{V}\_d^t$ | $\\frac{m^3}{min}$ | Air demand at timestep t |
| $C\_{el}^t$ | €/kWh | Electricity price at timestep t |
| $\\Delta T$ | h | Duration of the optimization horizon |
| $\\Delta t$ | s | Timebase of the optimization (duration of one time period) |
| N | 1 | Number of timesteps N=$\\frac{\\Delta T}{\\Delta t/3600}$ |
\\hat{p} _{s y s}^{n o r_
\\overset{{\\mathrm{{\\sf o b a r}} _{}}{{\\mathrm{b a r}}_{mathfrak g}}}
\\overline{{p}}\_{s t o}
\\mathtt{b a r}\_{\\mathtt{a}}
\ a a r\_\\text
\\underline{{p\_{s t o}}}
p\_{n}
\\dot{V}\_{c o}
E\_{c o,s u}
\\overset{\ \ ,,,,,,,,}{V\_{r e c}}
\\beta\_{i}
C\_{p e n}
\\varsigma\_{i}
\ {dot v\_\_{d d}^{t}}
\\underline{{\\underline{{\\mathfrak{m}}}{}\_{n}^{3}}}
^begin{}{{^{prime m i}\_\_{\\in}}}\ {^{\\prime\\in}}\ {}\ {}
C\_{e I}^{t}
\\Delta T
\\frac{\\in\\atop k W h}
\\Delta t
\\begin{array}{r}{N=\\frac{\\Delta T}{\\Delta t/3600}}\\end{array}
* * *
Table B.6: Variables of the nonlinear model
| Name | $\\in$ | Unit | Description |
| $p\_{sys}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | System pressure at timestep t |
| $p\_{sys}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Theoretical system pressure (auxiliary variable) |
| $p\_{sto}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Storage pressure at timestep t |
| $\\Delta P\_{sto,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when charging |
| $\\Delta P\_{sto,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Auxiliary variable for calculating $\\Delta P\_{sto,ch}^{t}$ |
| $\\Delta P\_{sto,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when discharging |
| $\\Delta P\_{sto,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | barg | Auxiliary variable for calculating $\\Delta P\_{sto,dch}^{t}$ |
| $\\Delta P\_{ch,last}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Pressure growth of last charge process |
| $\\Delta P\_{dch,last}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Pressure reduction of last discharge process |
| $\\Delta P\_{th,de}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Pressure decrease caused by temperature decrease after charging |
| $\\Delta P\_{th,in}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Pressure increase caused by temperature increase after discharging |
| $\\Delta P\_{dch,first}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | bar | Additional pressure decrease when starting discharge process |
| $t\_{ch,last}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | 1 | Timestep of last charge process |
| $t\_{dch,last}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | 1 | Timestep of last discharge process |
| $\\tau\_{ch}$ | $\\mathbb{R}\_{0}^{+}$ | 1 | Relative charging time during one timestep |
| $\\tau\_{dch}$ | $\\mathbb{R}\_{0}^{+}$ | 1 | Relative discharging time during one timestep |
| $\\dot{V}\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | $\\frac{\\mathrm{m}^{2}}{\\mathrm{min}}$ | Compressed air produced by the compressors at timestep t |
| $\\dot{V}\_{rec}^{t}$ | R | $\\frac{\\mathrm{m}^{2}}{\\mathrm{min}}$ | Compressed air into (positive) or out of (negative) the air receiver tank |
| $\\dot{V}\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | $\\frac{\\mathrm{m}^{2}}{\\mathrm{min}}$ | Compressed air consumption of the booster at timestep t |
| $P\_{co}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |
| $P\_{so,su}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed when compressors start up at timestep t |
| $P\_{co,sd}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed when compressors shut down at timestep t |
| $P\_{bo}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the booster at timestep t |
| $P\_{so,su}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed when booster starts up at timestep t |
| $P\_{so,sd}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed when booster shuts down at timestep t |
| $P\_{tot,ch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system in charge mode during timestep t |
| $P\_{tot,dch}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system in discharge mode during timestep t |
| $P\_{tot,n}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system in normal operation during timestep t |
| $P\_{tot}$ | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |
| $\\Theta^{t}$ | \[-1,0,1\] | 1 | Operation mode of the CAES system at timestep t (-1=discharge,0=normal,1=charge) |
| $b\_{co,run}^{t}$ | \[0,1\] | 1 | Binary variable related to the compressors running status at timestep t |
| $b\_{so,run}^{t}$ | \[0,1\] | 1 | Binary variable related to the booster running status at timestep t |
| $s\_{sto}^{t}$ | \[-1,0,1\] | 1 | State of the storage at timestep t (-1=empty,1=full) |
| $c\_{en}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | € | Energy costs at timestep t |
| $c\_{pen}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | € | Penalty costs at timestep t |
| $c\_{tot}^{t}$ | $\\mathbb{R}\_{0}^{+}$ | € | Total costs at timestep t |
| $c\_{tot}$ | $\\mathbb{R}\_{0}^{+}$ | € | Total costs to be minimized |
\\in
p\_{s y s}^{t}
\\mathbb{R}\_{0}^{+}
\ a r\_{9}
\\tilde{p}\_{s y s}^{t}
\\mathbb{R}\_{0}^{+}
b a r\_{9}
p\_{s t o}^{t}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
\\Delta p\_{s t o,c h}^{t}
\\Delta\\tilde{p}\_{s t o,c h}^{t}
b a r\_{mathfrak g
\\mathbb{R}\_{0}^{+}
\\Delta p\_{s t o,c h}^{t}
b a l\_{9}
\\Delta\\tilde{p}\_{s t o,d c h}^{t}
\\mathbb{R}\_{0}^{+}
b a r\_{9}
\\Delta p\_{c h,l a s t}^{t}
\\Delta p\_{s t o,d c h}^{t}
\\mathbb{R}\_{0}^{+}
\\Delta p\_{d c h,l a s t}^{t}
\\Delta p\_{t h,d e}^{t}
\\Delta p\_{t h,i n}^{t}
\\Delta p\_{d c h,f i r s t}^{t}\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
\\tau\_{c h}
\\mathbb{R}\_{0}^{+}
\\tau\_{d c h}
\\mathbb{R}\_{0}^{+}
\\dot{v}\_{c o}^{t}
\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf\*{m i n}}
\\frac{\\mathfrak{m} _{n}^{3}}{\\mathfrak_{n}\ {\\mathrm{i r}}}{\\mathfrak\_{n}^{3}}
\\dot{V}\_{r e c}^{t}
\\dot{V}\_{b o}^{t}
\\mathbb{R}\_{0}^{+}
P\_{c o}^{t}
P\_{c o,s u}^{t}
\\mathbb{R}\_{0}^{+}
P\_{c o,s d}^{t}
\\mathbb{R}\_{0}^{+}
P\_{b o}^{t}
\\mathbb{R}\_{0}^{+}
\\mathbb{R}\_{0}^{+}
P\_{b o,s d}^{t}
\\mathbb{R}\_{0}^{+}
P\_{t o t,d c h}^{\\tau}
P\_{t o t,n}^{t}
\\mathbb{R}\_{0}^{+}
P\_{t o t}^{t}
\\mathbb{R}\_{0}^{+}\ k M
s\_{s t o}^{t}
\\mathbb{R}\_{0}^{+}
\\Theta^{t}
\[left\[-1,0,1\\right\],1\
c\_{e n}^{t}\
t\\left(-1=e m p t y,1={t u l l}\\right)\
b\_{b o,r u n}^{t}\
\\mathbb{R}\_{0}^{+}\
\\mathbb{R}\_{0}^{+}\
C\_{p e n}^{t}\
c\_{t o t}\
\\mathbb{R}\_{0}^{+}\
* * *\
B.3.1 Normal mode\
In normal mode the compressors have to cover the air demand. If the system pressure is\
greater than the normal system pressure (because the storage was charge previously), a part\
or all of the air demand is covered by the air from the air receiver tank. At first the theoretical\
system pressure p~sysif the complete air demand would be covered by the air receiver tank is\
calculated using the ideal gas equation of state1 (eq.3.1).\
\\tilde{p}\_{s y s}^{t}\
\\tilde{p} _{s y s}^{t}=p_{s y s}^{t-1}-\\dot{V} _{d}^{t}\\cdot\\frac{\\Delta t}{60,\\frac{\\mathsf s}{\\mathsf m\ n mathsf}}\\cdot\\frac{p_{n}}{V\_{r e c}}\
(B.38)\
t norm\
The concrete system pressure psyshas to be al least p^sys.\
p\_{s y s}^{t}\
\\hat{p}\_{s y s}^{n o r m}\
(B.39)\
p\_{s y s}^{t}=\\begin{cases}{\\tilde{p} _{s y s}^{t}\\quad\\quad\\mathsf{i f}\\quad\\quad\\tilde{p}_{s y s}^{t}>\\hat{p} _{s y s}^{n o r m}}\ {\\hat{p}_{s y s}^{n o r m}\\quad\\mathsf{e l s e}.}\\end{cases}\
The air, that is covered by the air receiver tank, then can be calculated dependent on the\
system pressure change, using again the ideal gas equation of state1 (eq.3.1).\
\\dot{V} _{r e c}^{t}=\\frac{60,\\frac{s}{\\mathfrak{m}i n}}{\\Delta t}\\cdot\\left(p_{s y s}^{t}-p\_{s y s}^{t-1}\\right)\\cdot\\frac{V\_{r e c}}{p\_{n}}\
(B.40)\
The air, that has to be covered by the compressors, is composed of the air demand and the air\
from the receiver tank V\_rec.\
\\dot{V}\_{r e c}^{t}\
\\dot{\\boldsymbol{V}} _{c o}^{t}=\\dot{\\boldsymbol{V}}_{d}^{t}+\\dot{\\boldsymbol{V}}\_{r e c}^{t}\
(B.41)\
If the compressor have to deliver air, they need to run. In this case the power consumption of\
the compressors is calculated\
b\_{c o,r u n}^{t}=\\begin{cases}{1\\quad\\mathsf{i f}\\qquad\\dot{\\boldsymbol{V}}\_{c o}^{t}>0}\ {0\\quad\\mathsf{e l s e}.}\\end{cases}\
(B.42)\
The power consumption of the compressors is modeled dependent on the air covered by the\
compressors V\_co. It is zero, when all the air is covered by the receiver tank and.\
\\begin{array}{r}{P\_{c o}^{t}=\\begin{cases}{\\varsigma\_{1}\\cdot\\dot{\\boldsymbol{V}} _{c o}^{t}+\\varsigma_{2}}&{\\mathsf{i f}\\qquad\\dot{\\boldsymbol{V}}\_{c o}^{t}>}\ {0}&{\\mathsf{e l s e}.\ \\}end{{}\
(B.44)\
(B.43)\
E\_{c o,s u}\
It is assumed, that the air temperature is constant. The parameters of this equation have to be converted to SI\
units. The absolute pressure value has to be used.\
2 t\
V\_ is negative for air out of the storage\
{}^{2}\\dot{V}\_{r e c}^{t}\
2 t\
V\_r ecis negative for air out of the storage\
* * *\
The booster is not running in normal mode. But shut-down losses have to be considered if the\
booster was running in the previous timestep.\
P\_{b o,s d}^{t}=\\left{\\begin{array}{l l}{E\_{b o,s d}\\cdot\\frac{3600\\mathrm\ \\text8AA h{}}}{{{\\Delta t}}}&{\\mathrm{i f}\\qquad b\_{b o,r u n}^{t-1}=1,}\ {0}&{\\mathrm{e l s e}.}\\end{array}\\right.\
(B.45)\
The total power consumption of the system is comprised of the power consumption of the\
compressors with their start-up losses and the shut-down losses of the booster.\
P\_{t o t}^{t}=P\_{c o}^{t}+P\_{c o,s u}^{t}+P\_{b o,s d}^{t}\
(B.46)\
In normal mode the pressure storage is neither charged nor discharged. Nevertheless, changes\
of the storage pressure caused by temperature variation have to be taken into account. During\
charging, the air in the storage is heated up. After switching from charge to normal mode,\
the air in the storage slowly cools down, which leads to a pressure decrease p. This\
th;de\
kt\
is modeled by an exponential decrease of the storage pressure of the form p = p0 e.\
The pressure decrease between two timesteps can be stated as follows.\
\\Delta p\_{t h,d e}^{t}\
\\Delta p=\\Delta p\_{0}\\cdot e^{-k t}\
(B.47)\
\\begin{array}{r}{\\Delta p\_{t h,d e}^{t}=\\begin{cases}{(left\\delta\_c h h,\ cdot DeltaDelta\\rho\_{c h,l a s t}^{t-1}+\\delta\_{c h,\\delta}\\cdot p\_{t t o}^{t}+\\delta\_{c h,\ }\\right)}\ {\\cdot\\left(\\mathbf{e}^{-\\delta\_{c h,\\delta}\\cdot\\Delta t\\left(t-1-t\_{c h,b a t}^^t t\\right)}-e^{-\\delta\_{c h,\\delta}\\cdot\\Delta t\\cdot\ t-cdot\ t\_{c h,l a s t}^{t-1}}\\right)}&{\\mathrm{i f}}\ {0}&{\\mathrm{e f}\\Delta.}\\end{array}\\Delta p\_{c h,l a s t}^{t}>0,}\\end{array}\
Analog to the up-heating during charging, the air in the storage cools down when the CAES\
system is discharged. After switching from discharge to normal mode, the air in the storage\
slowly heats up, which leads to a pressure increase p. This is modeled in the same way\
th;in\
as the pressure decrease after charging. This effect does not occur if the pressure decrease of\
the last discharging process p is small. Therefore, it is only taken into account after\
ch;last\
pressure decreases greater than 5 bar.\
\\Delta p\_{t h,i n}^{t}.\
\\begin{array}{r}{\\Delta p\_{t h,i n}^{t}=\\begin{cases}{\\left(\\delta\_{d c h,\\theta{\\cdot}}\\Delta\\rho{{ _d c c,l a s t}^{t-1}}+\\delta_{d c h,\ {\\cdot}}\\rho\_{d t o}^{t}+\\delta\_{d t h,{theta\\cdot}}\\right)}\ {\\cdot\\left(\\mathbf{e}^{-\\delta\_{d c h,\\theta{\\cdot}}\\Delta t\\left({t-11-t\_{e c c,l u s t}^{t-1}}\\right)}-e^{-\\delta\_{d c h,\\theta{\\cdot}}\\Delta t\\left({t-t\_{e c c,h u t t}^{t-1}}\\right)}\\right)}&{\\mathrm{i f}}\ {0}&{\\mathrm{e l s e.}\ \\Delta\ rho{\_\_d d h,l a s t}^{t}>5,}\\end{array}}\ \\end{array}\
\\Delta p\_{c h,I a s t}^{t}\
(B.48)\
p\_{s t o}^{t+1}=p\_{s t o}^{t}+\\Delta p\_{t h,i n}^{t}-\\Delta p\_{t h,d\ ^{\\prime}}^{t}\
p\_{s t o}^{t+1}\
The total costs of the CAES system at timestep t can be calculated using the electricity price\
tel ttot\
C and the total power consumption P.\
C\_{e I}^{t} c\_{t o t}^{t}=C\_{e I}^{t}\\cdot P\_{t o t}^{t}\\cdot\\frac{\\Delta t}{3600,\\frac{\\mathsf{s}}{\\mathsf{h}}}\
(B.50)\
At the end some variables needed for the following timesteps have to be specified. The booster\
is never running in normal mode. The pressure growth of the last charging process p\
ch;last\
tch;last\
and the corresponding timestep t as well as the pressure reduction of the last discharging\
t tdch;last\
process p and its last timestep t are unchanged. Also the state of the storage\
dch;last\
does not change in normal mode.\
\\Delta p\_{c h,I a s t}^{t}\
t\_{c h,I a s t}^{t}\
t\_{d c h,I a s t}^{t}\
b\_{b o,r u n}^{t}=0\
\\Delta p\_{d c h,I a s t}^{t}\
(B.51)\
\\Delta p\_{c h,I a s t}^{t}=\\Delta p\_{c h,I a s t}^{t-1}\
(B.52)\
t\_{c h,I a s t}^{t}=t\_{c h,I a s t}^{t-1}\
(B.53)\
\\Delta p\_{d c h,l a s t}^{t}=\\Delta p\_{d c h,l a s t}^{t-1}\
(B.54)\
t\_{d c h,I a s t}^{t}=t\_{d c h,I a s t}^{t-1}\
(B.55)\
s\_{s t o}^{t}=s\_{s t o}^{t-1}\
(B.56)\
B.3.2 Charge mode\
As described in section3.3(eq.3.3), the system pressure psysduring charging depends on\
t norm\
the storage pressure psto. Its minimum value is given by the normal system pressure p^sys.\
p\_{s y s}^{t}=\\begin{cases}{\\big(p\_{s t o}^{t}+2,\\mathsf{b a r}\\big)/r\_{b o}}&{\\mathrm{i f}\\qquad p\_{s t o}^{t}>\\hat{p} _{s y s}\\cdot r_{b o}-1,\\mathsf{b a}}\ {\\hat{\\rho}\_{s y s}^{s o r m}}&{\\mathrm{e l s e}.}\\end{array}\
(B.57)\
In charge mode, the compressors have to cover the air demand V\_d, the air consumed by the\
t t\
booster V\_boand the air needed to raise the pressure in the air receiver tank V\_rec. The air\
consumed by the booster V\_bodepends on the storgae pressure and is modeled as a quadratic\
function.\
\\dot{V} _{r e c}^{t}=\\frac{60,\\frac{s}{\\mathfrak{m}}}{\\Delta t}\\cdot\\left(p_{s y s}^{t}-p\_{s y s}^{t-1}\\right)\\cdot\\frac{V\_{r e c}}{p\_{n}}\
\\dot{v}\_{b o}^{t}\
\\dot{v}\_{b o}^{t}\
It is assumed, that the air temperature is constant. The parameters of this equation have to be converted to SI\
units. The absolute pressure value has to be used.\
\\overline{{3+t}}^\_\\text{t}\
* * *\
\\dot{V} _{b o}^{t}=\\beta_{7}\\cdot{p\_{s t o}^{t}}^{2}+\\beta\_{8}\\cdot p\_{s t o}^{t}+\\beta\_{9}\
\\dot{\\boldsymbol{V}} _{c o}^{t}=\\dot{\\boldsymbol{V}}_{d}^{t}+\\dot{\\boldsymbol{V}} _{b o}^{t}+\\dot{\\boldsymbol{V}}_{r e c}^{t}\
(B.60)\
The power consumption of the compressors is modeled as a polynomial function of degree 3\
dependent on the air covered by the compressors V\_coand the difference of the system\
t norm\
pressure psysand the normal system pressure p^sys.\
\\dot{V}\_{c o}^{t}\
p\_{s y s}^{t}\
\\hat{p}\_{s y s}^{n o r m}\
\\begin{aligned}{P\_{c o}^{t}}\\end{array}\\quad\\varsigma{ _1}\\cdot\\dot{\ V}_{c o}^{t}+\\varsigma\_{2}\ \ {+quad}\ (\\wp{ _{s y s}^{t}}-\\dot{\\wp}{_{s y s}^{n o r m}})\\cdot\\left\ \\big(\\varsigma\_33\\cdot(\\dot{V} _{c o}^{t})^{3}+\\varsigma_{4}\\cdot(\\dot{V} _{c o}^{t})^{2}+\\varsigma_{5}\\cdot\\dot{V} _{c o}^{t}+\\varsigma_{6}\\right)\
(B.61)\
Additionally, energy losses Eco;suduring startup are considered, if the compressors were not\
tco;run 1\
running in the previous timestep (b = 0).\
E\_{c o,s u}\
(b\_{c o,r u n}^{t-1}=0)\
P\_{c o,s u}^{t}=\\left{\\begin{array}{l l}{E\_{c o,s u}\\cdot\\frac{3600\\mathrm\ \\text\\AA{h}}{\\Delta t}}&{\\mathsf{i f}\\qquad b\_{c o,r u n}^{t-1}=0,}\ {0}&{\\mathsf{e l s e}.}\\end{array}\\right.\
(B.62)\
tbo\
The power consumption of the booster P is modeled as a polynomial function of degree 5\
dependent on the storage pressure pstoat its output.\
P\_{b o}^{t}\
p\_{s t o}^{t}\
\\begin{array}{r}{P\_{b o}^{t}=\ \ \\beta\_{1}\\cdot(p\_{s t o}^{t})^{5}+\\beta\_{2}\\cdot(p\_{s t o}^{t})^{4}+\\beta\_{3}\\cdot(p\_{s t o}^{t})^{3}}\ {+\\beta\_{4}\\cdot(p\_{s t o}^{t})^{2}+\\beta\_{5}\\cdot(p\_{s t o}^{t})+\\beta\_{6}}\\end{array}\
(B.63)\
Additionally, energy losses Ebo;suduring startup are considered, if the booster was not running\
tbo;run 1\
in the previous timestep (b = 0).\
E\_{b o,s u}\
(B.64)\
(b\_{b o,r u n}^{t-1}=0)\
P\_{b o,s u}^{t}=\\left{\\begin{array}{l l}{\\displaystyle E\_{b o,s u}\\cdot\\frac{3600mathrm\\font{}^{\\mathrm{s}}}{\\Delta t}}&{\\sf i f\\qquad b\_{b o,r u n}^{t-1}=0,}\ {0}&{\\sf e l s e.}\\end{array}\\right.\
The total power consumption of the system is comprised of the power consumption of the\
compressors and the booster with their respective start-up losses.\
(B.65)\
\\Delta\\tilde{p}\_{s t o,c h}^{t}\
To avoid that the storage pressure exceeds its maximum psto, the concrete pressure increase\
p is calculated.\
sto;ch\
P\_{t o t,c h}^{t}=P\_{c o}^{t}+P\_{c o,s u}^{t}+P\_{b o}^{t}+P\_{b o,s u}^{t}\
\\overline{{p}}\_{s t o}\
\\Delta p\_{s t o,c h}^{t}\
* * *\
\\Delta p\_{s t o,c h}^{t}=\\begin{cases}{\\bar{p} _{s t o}-p_{s t o}^{t}}&{\\mathrm{i f}\\qquad p\_{s t o}^{t}+\\Delta\\tilde{p} _{s t o,c h}^{t}>\\bar{p}_{s t o},}\ {\\Delta\\tilde{p}\_{s t o,c h}^{t}}&{\\mathrm{e l s e}.}\\end{cases}\
(B.67)\
t+1\
To calculate the storage pressure pstoat the beginning of the next timestep t+1, the concrete\
pressure increase p is added to the storage pressure the beginning of timestep t.\
sto;ch\
p\_{s t o}^{t+1}\
\\Delta p\_{s t o,c h}^{t}\
p\_{s t o}^{t+1}=p\_{s t o}^{t}+\\Delta p\_{s t o,c h}^{t}\
(B.68)\
t t\
If the concrete pressure increase p is lower than the theoretical ~p, this means\
sto;ch sto;ch\
that the the CAES system is not in charge mode during the whole time t in this timestep. As\
soon as the maximum storage pressure is reached, the system switches to normal mode (see\
3.3). The relative time where the system is in charge mode can be calculated as follows:\
\\Delta p\_{s t o,c h}^{t}\
\\Delta\\tilde{p}\_{s t o,c h}^{t}\
\\Delta t\
\\tau\_{c h}=\\frac{\\Delta p\_{s t o,c h}^{t}}{\\Delta\\tilde{p}\_{s t o,c h}^{t}}\
(B.69)\
Ifchis equal to 1, the system is charged the whole time t. Ifchis e.g. 0.7, the system is\
70 % of the time t in charge mode and 30 % in normal mode. To determine the total power\
ttot;n\
of the CAES system for this case, the power consumption in normal mode P has to be\
calculated. In normal mode, the booster is not running and the compressors only have the\
cover the air demand V\_d.\
\\Delta t\
\\tau\_{c h}\
\\tau\_{c h}\
\\Delta t\
P\_{t o t,n}^{t}\
\\dot{v}\_{d}^{t}\
P\_{t o t,n}^{t}=\\varsigma{ _1}\\cdot\\dot{\\boldsymbol{V}}_{d}^{t}+\\varsigma\_{2}\
(B.70)\
tbo;sd\
Changing from charge to normal mode, the shut-down losses of the booster P have to be\
considered as well.\
P\_{b o,s d}^{t}\
P\_{b o,s d}^{t}=E\_{b o,s d}\\cdot\\frac{3600,\\frac{\\mathsf{s}}{\\mathsf{h}}}{\\Delta t}\
ttot\
The total power consumption P of the CAES system during timestep t can then be calculated\
as follows:\
P\_{t o t}^{t}\
\\begin{array}{r}{P\_{t o t}^{t}=\\begin{cases}{P\_{t o t,c h}^{t}}&{\\mathrm{i f}\\quad\\quad\\tau\_{c h}=1,}\ {\\tau\_{c h}\\cdot P\_{t o t,c h}^{t}+\\left(1-\\tau\_{c h}\\right)\\cdot P\_{t o t,n}^{t}+P\_{b o,s d}^{t}}&{\\mathrm{e l s e}.}\\end{array}}\\end{array}\
(B.72)\
c\_{e n}^{t}=C\_{e I}^{t}\\cdot P\_{t o t}^{t}\\cdot\\frac{\\Delta t}{3600,\\frac{\\mathrm{s}}{\\mathrm{h}}}\
C\_{e I}^{t}\
In some cases charging the CAES system is not possible. To avoid that the optimization\
algorithm chooses charge mode as cost optimal in these cases, penalty costs are applied.\
t m3\
For charging penalty costs are used if the air demand V\_dis greater 1.26 (maximum air\
min\
demand where the system can be charged), the storage pressure pstoor the air delivered by\
t tsto1\
the compressors V\_coexceed their maximum or the state of the storage is already full (s =1).\
\\dot{V}\_{c o}^{t}\
(s\_{s t o}^{t-1}{=}1)\
* * *\
c\_{p e n}^{t}=\\left{\\begin{array}{l l l l}{C\_{p e n}}&{\\mathrm{i f}}&{\\dot{V} _{d}^{t}>1.26,\\frac{m_{\ }^{3}}{m overline{n}}}{\\mathrm{ ~~\ \~~\\\ ~~}\\vee}&{p\_{s t o}^{t}\\geq\\overline{{{p}}}\_{s t o}}&{\\mathrm{~~\ \ \ \ \ }dot{V} _{c o}^{t}>\\overline{{{V}}}_{c o}}&{\\mathrm{~\ \ \ \ \ ~}\\vee}&{s\_{s t o}^{t-1}=1,}\ {0}&{\\mathrm{e t e s}.}\\end{array}\\right.\
(B.74)\
ten tpen\
The total cost in timestep t are composed of the energy costs c and the penalty costs c.\
c\_{e n}^{t}\
c\_{p e n}^{t}.\
c\_{t o t}^{t}=c\_{e n}^{t}+c\_{p e n}^{t}\
(B.75)\
At the end some variables needed for the following timestep have to be specified. In charge\
mode the compressors are always running. The booster is only running at the end of timestep\
t if the system is in charge mode during the whole timestep (ch= 1). The pressure growth of\
this charging process p is either initialized with (if the system was not in charge mode\
ch;last\
in the previous timestep) or raised by the pressure increase of this timestep. The timestep\
tch;last\
representing the end of the last charging process t is set to t. The pressure reduction of\
the last discharging process p is reseted to zero. The state of the storage is set to full\
dch;last\
tsto\
(s =1) if the storage pressure equals its maximum psto.\
(\\tau\_{c h}=1)\
\\Delta p\_{c h,I a s t}^{t}\
t\_{c h,I a s t}^{t}\
\\Delta p\_{d c h,I a s t}^{t}\
\\overline{{p}}\_{s t o}\
(s\_{s t o}^{t}{=}1)\
(B.76)\
b\_{c o,r u n}^{t}\ {!{=}}\\
(B.77)\
b\_{b o,r u n}^{t}=\\begin{cases}{1\\quad\\mathsf{i f}\\qquad\\tau\_{c h}=1,}\ {0\\quad\\mathsf{e l s e}.}\\end{array}\
\\Delta p\_{c h,l a s t}^{t}=\\begin{cases}{\\Delta p\_{c h,l a s t}^{t-1}+\\Delta p\_{s t o,c h}^{t}}&{\\mathrm{i f~}\\qquad\\Theta^{t-1}=1,}\ {\\Delta p\_{s t o,c h}^{t}}&{\\mathrm{e l s e.}}\\end{cases}\
(B.79)\
(B.80)\
\\Delta p\_{d c h,I a s t}^{t}=0\
B.3.3 Discharge mode\
In discharge mode the compressors and the booster are shut down and the air demand is\
covered by the storage tank. If the system pressure is greater than the normal system pressure\
(because the storage was charged previously), a part or all of the air demand is covered by the\
air from the air receiver tank. At first the theoretical system pressure p~sysif the complete air\
demand would be covered by the air of the air receiver tank is calculated using the ideal gas\
equation of state4 (eq.3.1).\
s\_{s t o}^{t}=\\begin{cases}{1\ &{\\mathsf{i f}\\qquad p\_{s t o}^{t+1}=\\bar{p}\_{s t o},}\ {0}&{\\mathsf{e l s e}.}\\end{array}\
It is assumed, that the air temperature is constant. The parameters of this equation have to be converted to SI\
units. The absolute pressure value has to be used.\
* * *\
\\tilde{p} _{s y s}^{t}=p_{s y s}^{t-1}-\\dot{V} _{d}^{t}\\cdot\\frac{\\Delta t}{60,\\frac{\\mathsf{s}}{\\mathsf{m i n}}}\\cdot\\frac{p_{n}}{V\_{r e c}}\
(B.82)\
norm\
The concrete system pressure has to be al least p^sys\
\\hat{p}\_{s y s}^{n o r m}\
p\_{s y s}^{t}=\\begin{cases}{\\tilde{p} _{s y s}^{t}\\quad\\quad\\mathrm{i f}\\quad\\quad\\tilde{p}_{s y s}^{t}>\\hat{p} _{s y s}^{n o r m}}\ {\\hat{p}_{s y s}^{n o r m}\\quad\\mathsf{e l s e}.}\\end{cases}\
(B.83)\
The air, that is covered by the air receiver tank, then can be calculated dependent on the\
system pressure change, using again the ideal gas equation of state1 (eq.3.1).\
\\dot{V} _{r e c}^{t}=\\frac{60,\\frac{s}{\\mathfrak{m}n}}{\\Delta t}\\cdot\\left(p_{s y s}^{t}-p\_{s y s}^{t-1}\\right)\\cdot\\frac{V\_{r e c}}{p\_{n}}\
(B.84)\
In discharge mode, the compressors and the booster are not running and therefore not\
consuming electrical power. Only shut-down losses of both systems are considered, if they\
were running in the previous timestep.\
P\_{c o,s d}^{t}=\\left{\\begin{aligned}{}&{{}E\_{c o,s d}\\cdot\\frac{3600,\\frac{\\mathrm{s}}{\\hbar{}}}{\\Delta t}}&{}}{{{\\sf i f}\\qquad b\_{c o,r u n}^{t-1}=1,}\ {}&{{}0}&{{}{\\sf e l s e}.}\\end{aligned}\\right.\
(B.85)\
P\_{b o,s d}^{t}=\\left{\\begin{aligned}{}&{{}E\_{b o,s d}\\cdot\\frac{3600,\\mathrm{\\tiny\ s~}}{\\Delta t}}&{{}\\mathrm{i f}\\qquad b\_{b o,r u n}^{t-1}=1,}\ {}&{{}0}&{{}\\mathrm{e l s e}.}\\end{aligned}\\right.\
(B.86)\
P\_{t o t,d c h}^{t}=P\_{c o,s d}^{t}+P\_{b o,s d}^{t}\
(B.87)\
The theoretical pressure decrease ~p of the storage tank during discharging is calcusto;dch\
lated based on the air demand V\_d, taking into account the air covered by the receiver tank\
V\_rec, and the storage pressure pstoat the beginning of timestep t.\
\\Delta\\ddot{p} _{s t o,d c h}^{t}=\\Delta t\\cdot\\left(\\frac{\\delta_{d c h,1}\\cdot(\\dot{V} _{d}^{t}+\\dot{V}_{r e c}^{t})}{\\delta\_{d c h,2}+(\\dot{V} _{d}^{t}+\\dot{V}_{r e c}^{t})}+\\delta\_{d c h,3}\\cdot p\_{s t o}^{t}+\\delta\_{d c h,4}\\right)\
(B.88)\
p\_{s t o}^{t}\
\\Delta p\_{s t o,d c h}^{t}=\\begin{cases}{p\_{s t o}^{t}-\\underline{{p}} _{s t o}}&{\\mathsf{i f}\\qquad\ p_{s t o}^{t}-\\Delta\\tilde{p} _{s t o,d c h}^{t}>\\underline{{p}}_{s t o},}\ {\\Delta\\tilde{\\rho}\_{s t o,d c h}^{t}}&{\\mathsf{e l s}\\Xi.}\\end{cases}\
t+1\
To calculate the storage pressure pstoat the beginning of the next timestep t+1, the cont\
crete pressure decrease p is subtracted from the storage pressure the beginning of\
sto;dch\
timestep t.\
\\Delta p\_{s t o,d c h}^{t}\
\\underline{{p\_{s t o}}}\
* * *\
B. Mathematical description of the models\
If the concrete pressure increase _p_ _sto;dch_ _t_ is higher than the theoretical ~ _p_ _sto;dch_ _t_ , this means that the the CAES system is not in discharge mode during the whole time _t in this timestep._ As soon as the minimum storage pressure is reached, the system switches to normal mode (as described in chapter3.3). The relative time, during which the system is in discharge mode can be calculated as follows:\
_p_ _sto;dch_ _t_ _dch_ = _t_(B.91) ~ _p_ _sto;dch_\
If _dch_ is equal to 1, the system is discharged the whole time _t. Ifdch_ is e.g. 0.7, the system is 70 % of the time _t in discharge mode and 30 % in normal mode. To determine the total_ power of the CAES system for this case, the power consumption in normal mode P _ttot;n_ has to be calculated. In normal mode, compressors are running and have the cover the air demand _V\_d_. _t_\
_ttot;n t_ _P_ = &1 _V\_d_ \+ &2(B.92)\
Changing from discharge to normal mode, the start-up losses of the compressors P _tco;su_ have to be considered as well.\
_tco;su_ 3600 h s _P_ = E _co;su_(B.93) _t_\
The total power consumption P _ttot_ of the CAES system during timestep t can then be calculated. While the power consumption in normal mode P _ttot;n_ is only taken into account partly (with the relative time 1- _dch_ the system is in normal mode in this timestep), the start-up and shut-down losses always are fully considered.\
8 <P t if = 1; _ttot tot;dch dch_ _P_ = (B.94) : _dchP_ _t_ \+ (1 _dch_) _P_ _t_ \+ P _t_ else: _tot;dch tot;n co;su_\
The energy costs of the CAES system at timestep t can be calculated using the electricity price C _tel_ and the total power consumption P _ttot_ .\
_ten tel ttott_ _c_ = C _P_ s (B.95) 3600 h\
In some cases discharging the CAES system is not possible. To avoid that the optimization algorithm chooses discharge mode as cost optimal in these cases, penalty costs are applied. For discharging penalty costs are used the state of the storage has already been empty (s _tsto1_ = 1).\
8 <C if _s_ _t_ 1 = 1; _tpen pen sto_ _c_ = (B.96) :0 else.\
The total cost in timestep t are composed of the energy costs c _ten_ and the penalty costs c _tpen_ .\
* * *\
c\_{t o t}^{t}=c\_{e n}^{t}+c\_{p e n}^{t}\
(B.97)\
At the beginning of each discharge process, an additional pressure reductions was observed,\
which is modeled using the constant parameterdch;4.\
\\delta\_{d c h,4}\
\\Delta p\_{d c h,f i r s t}^{t}=\\begin{cases}{\\delta\_{d c h,5}}&{\\mathrm{i f}\\qquad\\Theta^{t-1}>-1,}\ {0}&{\\mathrm{e l s e}.}\\end{array}\
(B.98)\
Additionally, changes of the storage pressure caused by temperature variation have to be taken\
into account. During charging, the air in the storage is heated up. After switching from charge\
to discharge mode, the air cools down, which leads to a pressure decrease p. This is\
th;de\
kt\
modeled by an exponential decrease of the storage pressure of the form p = p0 e\
(see eq.B.47).\
\\Delta p=\\Delta p\_{0}\\cdot e^{-k t}\
\\Delta p\_{t h,d e}^{t}\
(B.99)\
To calculate the pressure at the beginning of the next timestep, these pressure reductions have\
to be taken into account.\
p\_{s t o}^{t+1}=p\_{s t o}^{t+1}-\\Delta p\_{d c h,f i r s t}^{t}-\\Delta p\_{t h,d e}^{t}\
(B.100)\
At the end some variables needed for the following timesteps have to be specified. In discharge\
mode the compressors are running at the end of timestep t if the system is not in discharge\
mode during the whole timestep (dch< 1). The booster is never running. The pressure\
reduction of this discharging process p is either initialized with (if the system was\
dch;last\
not in discharge mode in the previous timestep) or declined by the pressure decrease of this\
t tdch;last\
timestep p. The timestep of the end of the last discharging process t is set to t.\
sto;dch\
The pressure growth of the last charging process p is reseted to zero. The state of the\
ch;last\
tsto\
storage is set to empty (s = 1) if the storage pressure equals its minimum psto.\
(\\tau\_{d c h}<1)\
\\Delta p\_{d c h,I a s t}^{t}\
t\_{d c h,I a s t}^{t}\
\\Delta p\_{s t o,d c h}^{t}\
b\_{c o,r u n}^{t}=\\begin{cases}{1\\quad\\mathsf{i f}\\qquad\\tau\_{d c h}<1,}\ {0\\quad\\mathsf{e l s e}.}\ \\end{cases}\
(s\_{s t o}^{t}=-1)\
\\underline{{p\_{s t o}}}\
(B.101)\
(B.102)\
\\Delta p\_{d c h,l a s t}^{t}=\\begin{cases}{\\Delta p\_{d c h,l s s t}^{t-1}+\\Delta p\_{s t o,d c h}^{t}}&{\\uplus\\qquad\\Theta^{t-1}=-1,}\ {\\Delta p\_{s t o,d c h}^{t}}&{\\mathsf{e l s e}.}\\end{cases}\
* * *\
B. Mathematical description of the models\
_t_ _tdch;last_ = t (B.105)\
8 < 1 if _p_ _t+1_ = p\*;\* _tsto sto sto_ _s_ = (B.106) :0 else:\
* * *\
B.4 Mixed-integer nonlinear programming model\
The mixed-integer nonlinear programming (MINLP) model is formulated as a set of equality\
and inequality functions, that are described in this chapter. The variables used for the definition\
of the optimization problem are summarized in tableB.7. The parameters are the same\
as for the nonlinear simulation model described in sectionB.3, tableB.5, with the values\
shown in sectionC.3, tableC.4. The optimization horizon is described by the set of timesteps\
T = ft1;:::;tNg,where t is the duration of each timestep, and N is the number of timesteps\
t 2T.\
\\mathcal{T}={t\_{1},...,t\_{N}}\
\\Delta t\
t\\in\\mathcal\
Table B.7: Variables of the MINLP model\
The CAES system is represented in the same way as for the simulation model, except the\
pressure decrease and increase after charging and discharging as well as the air receiver tank\
are not considered in the MINLP model to reduce the solving time.\
| Name | $\\in$ | Unit | Description |\
| | $\\mathbb{R}\_{0}^{+}$ | barg | System pressure at timestep t |\
| | $\\mathbb{R}\_{0}^{+}$ | barg | Storage pressure at timestep t |\
| to,ch | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when charging |\
| to,dch | $\\mathbb{R}\_{0}^{+}$ | barg | Pressure difference at timestep t when discharging |\
| | $\\mathbb{R}\_{0}^{+}$ | $\\frac{m\_{n}^{3}}{min}$ | Compressed air produced by the compressors at timestep t |\
| | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the compressors at timestep t |\
| | $\\mathbb{R}\_{0}^{+}$ | kW | Electrical power consumed by the booster at timestep t |\
| | $\\mathbb{R}\_{0}^{+}$ | kW | Total electrical power consumed by the CAES system at timestep t |\
| | \[0,1\] | 1 | Binary variable related to the operation mode charge at timestep t |\
| | \[0,1\] | 1 | Binary variable related to the operation mode discharge at timestep |\
| su | \[0,1\] | 1 | Binary variable related to the compressors startup at timestep t |\
| sd | \[0,1\] | 1 | Binary variable related to the compressors shut-down at timestep t |\
| su | \[0,1\] | 1 | Binary variable related to the booster startup at timestep t |\
| sd | \[0,1\] | 1 | Binary variable related to the booster shut-down at timestep t |\
| rise | \[0,1\] | 1 | Binary variable related to the necessity of raising the system pressure during charging at timestep t |\
| | $\\mathbb{R}\_{0}^{+}$ | € | Total costs to be minimized |\
\\in\
\\mathtt r a{\_mathfrak g}\
\\mathbb{R}\_{0}^{+}\
p\_{s y s}^{t}\
\\mathtt{b a r}\_{\\mathtt{g}}\
p\_{s t o}^{t}\
\\mathbb{R}\_{0}^{+}\
\\Delta p\_{s t o,c h}^{t}\
\\mathbb{R}\_{0}^{+}\
{a\\mathfrak{l}}\_{\\mathfrak{g}}\
\\Delta p\_{s t o,d c h}^{t}\
\\mathbb{R}\_{0}^{+}\
b a l\_{9}\
\\dot{v}\_{c o}^{t}\
\\mathbb{R}\_{0}^{+}\
\\frac{\\mathsf{m}\_{n}^{3}}{\\mathsf\*{m i n}}\
P\_{c o}^{t}\
\\mathbb{R}\_{0}^{+}\
P\_{b o}^{t}\
\\mathbb{R}\_{0}^{+}\
P\_{t o t}^{t}\
\\mathbb{R}\_{0}^{+}\
b\_{c h}^{t}\
b\_{d c h}^{t}\
b\_{c o,s u}^{t}\
b\_{c o,s d}^{t}\
b\_{b o,s u}^{t}\
b\_{b o,s d}^{t}\
b\_{p,r a i s e}^{t}\
b\_{c h}^{t}+b\_{d c h}^{t}\\leq1\
c\_{t o t}\
\\mathbb{R}\_{0}^{+}\
b\_{c h}^{t}\
b\_{d c h}^{t}=1\
b\_{c h}^{t}=\
As for the MILP model, in the MINLP formulation of the optimization problem binary variables\
representing the operation mode of theCAESsystem can be used. The three modes normal,\
tch tdch\
charge and discharge are represented by two binary variables b and b that can be either\
tch\
0 or 1. At timestep t, theCAESsystem is in charge mode, when b = 1, and in discharge\
tdch\
mode, when b = 1. When both variables are zero, the system is in normal operation mode.\
The constraint in eq.B.107avoids that both variables become 1 at the same timestep.\
b\_{d c h}^{t}\
(B.107)\
C\_{e I}^{t} ttot\
at each timestep. The total power consumption of the system P is comprised of the power\
tco tbo\
consumptions of the compressors P and of the booster P.\
P\_{t o t}^{t}\
P\_{c o}^{t}\
P\_{b o}^{t}\
\ {\\mathsf{m i n}},c c\_{t o t}={\\mathsf{m i n}}\\left(\\sum\_{t\\in\\mathcal{T}}C\_{e l}^{t}\\cdot P\_{t o t}^{t}\\cdot\\frac{\\Delta t}{3600,\\frac{\\mathfrak{s}}{\\mathfrak{h}}}\\right)\
(B.108)\
\ _{t o t}^{t}=P_{c o}^{t}+P\_{b o}^{t}\ \ \ \ \\forall tforall\\mathcal{T}\
(B.109)\
Booster\
tbo\
The power consumption of the booster P is modeled as a polynomial function of degree 5\
dependent on the pressure p at its output. The booster is only running when the system is in\
bo\
tch tbo;su\
charge mode (b = 1). Additionally, energy losses Ebo;suduring startup (b = 1, when\
the system changes from charge or normal to discharge mode) and energy losses Ebo;sd\
tbo;sd\
during shut-down (b = 1, when the system switches from discharge to another mode) are\
considered.\
P\_{b o}^{t}\
p\_{b o}^{t}\
(b\_{b o,s u}^{t}=1\
E\_{b o,s d}\
(b\_{c h}^{t}=1)\
E\_{b o,s\\iota}\
(b\_{b o,s d}^{t}=1\
\\begin{array}{r l r}P{ _{b o}^{t}=}&{{boldsymbol b}_{c h}^{t}\\cdot\\big({\\boldsymbol{beta}} _{1}\\cdot(\\{boldsymbol p p}_{s t o}^{t})^{5}+{\\boldsymbol{\\beta}} _{2}\\cdot({\\boldsymbol p}_{s t o}^{t})^{4}+{\\boldsymbol{\\beta}} _{3}\\cdot({\\boldsymbol p}_{s t o}^{t})^{3}}\ &{\\qquad\\qquad+{\\boldsymbol{\\beta}} _{4}\\cdot({{\\boldsymbol p rho}}_{s t o}^{t})^{2}+{\\boldsymbol{\\beta}} _{5}\\cdot({{\\boldsymbol p}}_{t t o}^{t})+{\\boldsymbol{\\beta}} _{6}\\big)}\ &{+b_{b o,s u}^{t}\\cdot{\\boldsymbol E} _{b o,s u}\\cdot\\frac{3600\ \\frac{\\mathbf{t}}{\\mathbf{t}}}{\\Delta{\\boldsymbol{}}}}\ &{+b_{b o,s d}^{t}\\cdot{\\boldsymbol E}\_{b o,s d}\\cdot\ \ &{\ \ \ \ \ \ \ \ \\
(B.110)\
b\_{b o,s u}^{t}\\geq b\_{c h}^{t}-b\_{c h}^{t-1}\ \ \ \ \\forall t\\in\\mathcal{T}\
(B.111)\
b\_{b o,s d}^{t}\\geq b\_{c h}^{t-1}-b\_{c h}^{t}\\qquad\\forall t\\in\\mathcal{T}\
(B.112)\
Compressors\
The power consumption of the compressors is modeled as a polynomial function of degree 3\
depending on the air covered by the compressors V\_co, the difference of the system pressure\
t norm\
and the normal system pressure (psysp^sys) and the product of both. The offset &2is added\
tdch\
if the system is in charge or normal mode (b = 0). Additionally, energy losses Eco;suduring\
tco;su\
startup (b = 1, when the system changes from discharge to another mode) and energy\
tco;sd\
losses Eco;sdduring shut-down (b = 1, when the system switches from normal or charge\
to discharge mode) are considered.\
\\dot{V}\_{c o}^{t},\
(p\_{s v s}^{t}-\\hat{p}\_{s v s}^{n o r m})\
\\begin{array}{r l}{\\small{P} _{c o}^{t}=}&{\ varsigma\ {1}\\cdot\\dot{\\boldsymbol{V}}{c o}^{t}+\\varsigma_{2}\\cdot(1-\\boldsymbol{b} _{c o}}\\\&{{+}(\\boldsymbol{p}_{s s}}\\{{} _{c o s}^{t}-\\dot{\\boldsymbol{rho}}_{s o s}^{n o r m})\\cdot\\Big(\\varsigma\_{3}\\cdot(\\dot{\\boldsymbol{V}} _{c o}^{t})^{3}+\\varsigma{4}\\cdot(\\dot{\\boldsymbol{V}}{c o}^{t})^{2}+\\varsigma_{5}\\cdot\\dot{\\boldsymbol{V}} _{c o}^{t}+\\varsigma_{6}\\Big)}\ &{{++}boldsymbol{b} _{c o,s s}^{t}\\cdot\\boldsymbol{E}_{c o,s u}\\cdot\\frac{360\\dot{\\boldsymbol{h}}}{\\Delta t}}\ &{{+}\\boldsymbol{b} _{c o,s o}^{t}\\cdot\\boldsymbol{E}_{c o,s o}\\cdot\\frac{360\ dot\ {\\mathsf{h}}}{\\Delta t}}\ &{{+}\\boldsymbol{b} _{c o,s d}^{t}\\cdot\\boldsymbol{E}_{c o,s o}\\cdot\\frac{360\ \ frac\ {\\mathsf{h}}}{\\Delta t}}&{\ \\\forall\ t t\\in\\mathcal{T}}\\end{array}\
E\_{c o,s u}\
\\dot{(b\_{d c h}^{t}=0)}\
(b\_{c o,s u}^{t}=1\
(b\_{c o,s d}^{t}=1\
E\_{c o,s d} b\_{c o,s u}^{t}\\geq b\_{d c h}^{t-1}-b\_{d c h}^{t}\ \ \ \ \ \\forall t\\in\\mathcal{T}\
(B.114)\
b\_{c o,s d}^{t}\\geq b\_{d c h}^{t}-b\_{d c h}^{t-1};;;;;;\\forall t\\in\\mathcal{T}\
(B.115)\
tch tdch\
When the system is in normal mode (b = b = 0), the compressors have to cover the\
tch\
complete air demand V\_d. In the operation mode charge (b = 1), additionally the air demand\
of the booster V\_bohas to be covered. In discharge model, the air demand is covered by the\
high pressure storage and the air delivered by the compressors is zero. The air that can be\
delivered by the compressors is limited to V\_co.\
(b\_{c h}^{t}=b\_{d c h}^{t}=0)\
{\\dot{v}}\_{d}^{t}\
(b\_{c h}^{t}=1)\
\\dot{V}\_{b o}\
\\dot{v\_{c o}}\
\\dot{V} _{c o}^{t}=(1-b_{d c h}^{t})\\cdot\\dot{V} _{d}^{t}+b_{c h}^{t}\\cdot\\dot{V}\_{b o}\\qquad\\forall t\\in\\mathcal{T}\
(B.116)\
\\dot{\\boldsymbol{V}} _{c o}^{t}\\leq\\bar{\\dot{V\\boldsymbol{\ V}}}_{c o}\\qquad\\forall t\\in\\mathcal{T}\
(B.117)\
As described in chapter4.3(see eq.4.11and figure4.5), the system pressure psysduring\
charging depends on the storage pressure psto. In normal or discharge operation mode, the\
t norm\
system pressure psyscorresponds to the normal system pressure p^sys. In charge mode the\
norm\
system pressure has to be raised, if the storage pressure is higher than p^sysrbo1. In\
tp;raise\
the MINLP model therefore the binary variable b is introduced, which is 1 if the system\
pressure has to be raised (the system is in charge mode and the storage pressure is greater\
norm\
than p^sysrbo1) and 0, else.\
p\_{s y s}^{t}\
p\_{s t o}^{t}\
p\_{s y s}^{t}\
\\hat{p}\_{s V s}^{n o r m}\
\\hat{p} _{s y s}^{n o r m}\\cdot r_{b o}-1\
b\_{p,r a i s e}^{t}\
\\hat{p} _{s y s}^{n o r m}\\cdot r_{b o}-1,\
(B.118)\
p\_{s t o}^{t}\\cdot\\left(1-b\_{p,r a i s e}^{t}\\right)\\cdot b\_{c h}^{t}\\leq\\hat{p} _{s y s}^{n o r m}\\cdot r_{b o}-1\ \ \ \ \\forall t\\in\\mathcal{T}\
p\_{s t o}^{t}\\cdot\\cdot b\_{c h}^{t}\\geq\\left(\\hat{\\rho} _{s y s}^{n o r m}\\cdot r_{b o}-1\\right)\\cdot b\_{p,r a i s e}^{t}\ \ \ \ \ t\\in\\mathcal{T}\
(B.119)\
(B.120)\
b\_{p,r a i s e}^{t}\\leq b\_{c h}^{t}\\qquad\\forall t\\in\\mathcal{T}\
(B.122)\
Storage\
(B.121)\
t+1\
The pressure in the high pressure storage tank at the beginning of the next timestep psto\
depends on the storage pressure pstoat timestep t and the operation mode of the system. In\
charge mode, the pressure difference p is added. In discharge mode the pressure is\
sto;ch\
reduced by p. The storage pressure is limited by the lower bound pstoand the upper\
sto;dch\
bound psto.\
p\_{s t o}^{t}\
p\_{s t o}^{t+1}\
\\Delta p\_{s t o,c h}^{t}\
\\Delta p\_{s t o,d c h}^{t}\
\\overline{{p}}\_{s t o}\
p\_{s y s}^{t}\\geq\\hat{p} _{s y s}^{n o r m}\\cdot(1-b_{p,r a i s e}^{t})+b\_{p,r a i s e}^{t}\\cdot\\frac{p\_{s t o}^{t}+2}{r\_{b o}};;;;;;\\forall t\\in\\mathcal{T}\
* * *\
B. Mathematical description of the models\
The pressure increase during charging (b _tch_ = 1) is modeled as a polynomial function of degree 3 depending on the previous storage pressure p _sto_ _t_ .\
_psto;ch_ _t_ = b _tch_ _tch;1_(p _sto_ _t_ ) 3 + _ch;2_(p _sto_ _t_ ) 2 + _ch;3psto_ _t_ + _ch;4_ 8t 2T (B.124)\
The pressure decrease during discharging (b _tdch_ = 1) is modeled as a function depending _t_ _t_ on the air demand of the system V\_ _d_ and the previous storage pressure p _sto_. The additional pressure decrease at the beginning of a discharge period (b _tco;sd_ =1) is modeled with the parameter _dch;5_.\
_t t_! _t tdch dch;1_(V\_ _dt_ \+ V\_ _rec_) _t_ _psto;dch_ = _b t_ _t_ + _dch;3psto_ + _dch;4_ _dch;2_ \+ (V\_ _d_ \+ V\_ _rec_) (B.125)\
+ _dch;5b_ _tco;sd_ 8t 2T\
* * *\
Appendix C\
Values of the constant model\
parameters\
In this chapter, the values of the constant parameters used to describe the different models of\
the CAES system are summarized. If not specified otherwise, the parameters are calculated\
using linear regression to find the optimal values for the given functions so that they match the\
measured data. In this thesis the "curve\_fit" method within the python package SciPy \[91\] is\
used for calculating the values. TableC.1shows the values for parameters that are used for\
more than one optimization model. The model specific values are summarized in the following\
sections.\
\ i f i!{{big\
Table C.1: General parameters of theCAESsystem\
| Symbol | Value | Unit | Description |\
| $\\hat{p}\_{sys}^{norm}$ | 6 | bar$\_{g}$ | Normal setpoint pressure |\
| $\\bar{p}\_{sto}$ | 38 | bar$\_{g}$ | Maximum storage pressure |\
| $p\_{sto}$ | 7 | bar$\_{g}$ | Minimum storage pressure |\
| $\\dot{\\overline{{V}}}\_{co}$ | 2.5 | $\\frac{m^{3}}{min}$ | Maximum free air delivery of the compressors |\
| $r\_{bo}$ | 4 | 1 | Maximum compression ratio of the booster |\
| $E\_{co,su}$ | 0.01 | kWh | Start-up losses of the compressors |\
| $E\_{co,sd}$ | 0.02 | kWh | Shut-down losses of the compressors |\
| $E\_{bo,su}$ | 0.24 | kWh | Start-up losses of the booster |\
| $E\_{bo,sd}$ | 0.06 | kWh | Shut-down losses of the booster |\
\\hat{p}\_{s y s}^{n o r m}\
\ a r\_{9}\
\\overline{{p}}\_{s t o}\
\ a r\_{9}\
p\_{s t o}\
\\mathsf r a\_{g}\
\\dot{\\bar{v}}\_{c o}\
\\underline{{\\mathfrak{m}}}\_{\\mathrm{n}}^{3}\
r\_{b o}\
E\_{c o,s u}\
E\_{c o,s d}\
E\_{b o,s u}\
E\_{b o,s d}\
* * *\
C. Values of the constant model parameters\
# C.1 Linear programming model\
TableC.2summarizes the values used to describe the linear programming (LP) model. The following subsections describe how the time-dependent parameters _tch_ , _tdch_ and P _tch_ are calculated.\
Table C.2: Parameter values of the LP model\
**Name Value Unit Description**\
_Esto_ 20.12 kWh Maximum electrical energy capacity of storage _&_\
17.684m3\
kW _=min_ Slope of the linear function used to model the electrical power consump- n tion of the compressors _P_ _tch_ kW Upper limit of the electrical charge power at timestep t depending on _V\__ (see sectionC.1.1) _td_\
_t_ % Storage electrical charge/discharge efficiency at timestep t (see section _ch_ _t_\
C.1.2)\
_dch_\
## C.1.1 Charge power\
As explained in chapter3.4.3, the electrical charge energy of theCAESsystem is depending on the air demand during charging (see figure3.10). The charge energy E _ch_ can be calculated by integrating the difference of P _tot_ and P _ref_ over the charging time (t0chto t1ch) (see eq.3.5). Thus, the mean charge power P _ch_ for each measured charge energy of figure3.9can be calculated as follows.\
_Ech_ _Pch_ = _ch ch_ (C.1) _t1 t0_\
_tch_ _t_ To calculate the mean charge power P for a specific air demand V\_ _d_ at timestep t, a linear _t_ interpolation between the measured points is used. For each air demand V\_ _d_ the corresponding _P_ _tch_ is calculated and can be used as an upper limit for the LP optimization model. Because m3n theCAESsystem can not be charged for air demands greater than 1.26 min , in these cases _P_ _tch_ is set to zero. FigureC.2shows the mean charge power P _tch_ used in the LP model as a function of the air demand .\
* * *\
Figure C.1: Mean charge power as a function of the air demand\
C.1.2 Charge and discharge efficiencies\
As shown in chapter3.4.3(figure3.10), the electrical round-trip efficiency of theCAESsystem\
is depending on the air demand during charging and discharging. Therefore, also the charge\
efficiency and the discharge efficiency for each timestep are depending on the corresponding\
air demand. To calculate the charge and discharge efficiencies, first the best round-trip\
efficiencybestand its corresponding charge energy Ech;bestand discharge energy Edch;best\
are identified from the measured values of figure3.9.\
\\eta\_{b e s t}\
E\_{c h,b e s t}\
E\_{d c h}\
\\eta\_{b e s t}=\\frac{E\_{d c h,b e s t}}{E\_{c h,b e s t}}\
(C.2)\
tch tdch\
Then the charge energy E and the discharge energy E for the respective air demand V\_d\
is calculated by linearly interpolating the measured values shown in figure3.9.\
tdch tdch\
The discharge efficiency is defined to be = 1, when the discharge energy E\
E\_{c h}^{t}\
E\_{d c h}^{\\tau}\
\ \\dot{}{\ V\_\_{}}^{t}\
\\eta\_{d c h}^{t}=\\frac{E\_{d c h}^{t}}{E\_{d c h,b e s t}}\
The round-trip efficiency is defined as product of the charge and the discharge efficiency.\
tdch tdch\
The discharge efficiency is defined to bedch;best= 1, when the discharge energy E\
tdch\
equals the best discharge energy Edch;best. For lower values of E, the efficiency decreases.\
tch\
Withdch;best= 1, this means that the best charge efficiencych;best(when E = Ech;best)\
is defined as the best round-trip efficiencybest\
\\eta\_{d c h,b e s t}=1.\
\\eta\_{d c h,b e s t}=1\
E\_{d c h,b e s t}.\
E\_{d c h}^{t}\
\\eta\_{c h,b e s t}\
E\_{c h}^{t}=E\_{c h,b e s t})\
* * *\
\\eta\_{b e s t}=\\eta\_{c h,b e s t}\\cdot\\eta\_{d c h,b e s t}=\\eta\_{c h,b e s t}\\cdot\\mathbf{1}=\\eta\_{c h,b e s t}\
(C.5)\
tch\
The charge efficiency of a specific air demand V\_dand its corresponding charge energy\
tch\
E can therefore be calculated as follows.\
\\eta\_{c h}^{t}\
{dot v\_\_{d}}{^{t}}\
\\eta\_{c h}^{t}=\\frac{E\_{c h,b e s t}}{E\_{c h}^{t}}\\cdot\\eta\_{b e s t}\
(C.6)\
E\_{c h}^{t}\
m3\
Because theCAESsystem can not be charged for air demands greater than 1.26, in\
min\
these cases the charge efficiency is set to zero. FigureC.2shows the charge and discharge\
efficiencies used in the LP model as a function of the air demand. They have the same behavior\
as the charge and discharge energy shown in figure3.9.\
1.26,\\frac{\\mathsf{m} _{\\mathsf{n}}^{3}}{\\mathsf{m}_{\\mathsf{n}}}\
Figure C.2: Charge and discharge effciencies as a function of the air demand\
* * *\
C.2 Mixed-integer linear programming model\
TableC.3shows the values of the parameters for the mixed-integer linear programming (MILP)\
model.\
Table C.3: Parameter values of the MILP model\
| Name | Value | Unit | Description |\
| $\\varsigma\_{1}$ | 7.22501 | $\\frac{\\mathrm{kW}}{\\mathrm{m}\_{n}^{3}/\\mathrm{min}}$ | |\
| $\\varsigma\_{2}$ | -8.845$\\cdot$10-3 | $\\frac{\\mathrm{kW}}{\\mathrm{bar}\_{g}}$ | Parameters used to model the electrical power consumption of the compressors |\
| $\\varsigma\_{3}$ | 0.66225 | 1 | |\
| $\\varsigma\_{4}$ | 0.83588 | kW | |\
| $\\beta\_{1}$ | 0.07354 | $\\frac{\\mathrm{kW}}{\\mathrm{bar}\_{g}}$ | Parameters used to model the electrical power consumption of the booster |\
| $\\beta\_{2}$ | 1.18055 | kW | |\
| $\\delta\_{ch,1}$ | 2.877$\\cdot$10-6 | $\\frac{1}{s}$ | Parameters used to model the storage pressure state equation |\
| $\\delta\_{ch,2}$ | 3.737$\\cdot$10-3 | $\\frac{\\mathrm{bar}}{s}$ | |\
| $\\delta\_{dch,1}$ | 4.670$\\cdot$10-3 | $\\frac{\\mathrm{bar}}{\\mathrm{m}\_{n}^{3}/60}$ | |\
| $\\delta\_{dch,2}$ | 9.423$\\cdot$10-6 | $\\frac{1}{s}$ | |\
| $\\delta\_{dch,3}$ | 1.524$\\cdot$10-4 | $\\frac{\\mathrm{bar}}{s}$ | |\
| $\\delta\_{dch,4}$ | 0.73984 | kW | |\
\\varsigma\_{1}\
\\frac{k W}{m\_{n}^{3}/m i n}\
-8.845\\cdot10^{-3}\
\\varsigma\_{2}\
\\frac{\\mathsf{k}!\\mathsf{W}}{\\mathsf{b}\\mathsf{r}\_{\\mathfrak{g}}}\
\\leqslant3\
\\varsigma\_{4}\
\\beta\_{1}\
\\frac{\\mathsf{K W}}{\\mathsf{b a r\_{g}}}\
\\beta\_{2}\
\\delta\_{c h,1}\
2.877\\cdot10^{-6}\
\\delta\_{c h,2}\
10^{-3}\
\\frac{\\mathrm{ ~~s~~}}{\\mathrm{ ~~b~~ a~~~~~}~\
\\delta\_{d c h,1}\
10^{-3}\
\\frac{\\log{\ }}{\ {m\_{n}^{3}/60}}\
\\delta\_{d c h,2}\
10^{-6}\
\\delta\_{d c h,3}\
\\frac{1}{s}\
1.524.cdot10^{-4}\
\\delta\_{d c h,4}\
* * *\
C.3 Nonlinear model\
The parameters used for the nonlinear models are summarized in tableC.4.\
Table C.4: Parameter values of the nonlinear models\
| Name | Value | Unit | Description |\
| $\\varsigma\_{1}$ | 7.22501 | kW/m3/min | |\
| $\\varsigma\_{2}$ | 0.83588 | kW | |\
| $\\varsigma\_{3}$ | -0.17706 | $\\frac{1}{(m^{3}/\\min)^{2}}$ | Parameters used to model the electrical power consumption of the compressors |\
| $\\varsigma\_{4}$ | 0.80336 | $\\frac{1}{m^{3}/\\min}$ | |\
| $\\varsigma\_{5}$ | -0.35959 | 1 | |\
| $\\varsigma\_{6}$ | 0.28238 | kW/bar9 | |\
| $\\beta\_{1}$ | -1.916·10-7 | kW/(bar9)2 | |\
| $\\beta\_{2}$ | 1.504·10-6 | kW/(bar9)4 | Parameters used to model the electrical power consumption of the booster |\
| $\\beta\_{3}$ | 2.595·10-5 | kW/(bar9)3 | |\
| $\\beta\_{4}$ | 5.005·10-3 | kW/(bar9)2 | |\
| $\\beta\_{5}$ | 0.24019 | kW/bar9 | |\
| $\\beta\_{6}$ | 0.13850 | kW | |\
| $\\beta\_{7}$ | 0.24019 | m3/bar2 | Parameters used to model the air consumption of the booster |\
| $\\beta\_{8}$ | 0.24019 | m2/bar2 | |\
| $\\beta\_{9}$ | 0.13850 | m3/min | |\
| $\\delta\_{ch,1}$ | -6.292·10-8 | $\\frac{1}{(bar9)^{2}\\cdot s}$ | Parameters used to model pressure increase during charging |\
| $\\delta\_{ch,2}$ | 1.082·10-5 | $\\frac{1}{(bar9)^{2}\\cdot s}$ | |\
| $\\delta\_{ch,3}$ | 3.620·10-4 | 1/s | |\
| $\\delta\_{ch,4}$ | 6.623·10-3 | bar/s | |\
| $\\delta\_{ch,5}$ | 2.688·10-3 | 1 | Parameters used to model the pressure reduction due to temperature decrease after charging |\
| $\\delta\_{ch,6}$ | 5.153·10-3 | 1 | |\
| $\\delta\_{ch,7}$ | 0.15070 | bar | |\
| $\\delta\_{ch,8}$ | 3.741·10-3 | 1 | |\
| $\\delta\_{dch,1}$ | 0.10263 | bar/s | Parameters used to model pressure decrease during discharging |\
| $\\delta\_{dch,2}$ | 20.1408 | m3/min | |\
| $\\delta\_{dch,3}$ | 9.103·10-6 | 1/s | |\
| $\\delta\_{dch,4}$ | 2.725·10-4 | bar/s | |\
| $\\delta\_{dch,5}$ | 0.74582 | bar | Parameters used to model the pressure raise due to temperature increase after discharging |\
| $\\delta\_{dch,6}$ | 3.216·10-3 | 1 | |\
| $\\delta\_{dch,7}$ | 7.091·10-3 | 1 | |\
| $\\delta\_{dch,8}$ | 0.06636 | bar | |\
| $\\delta\_{dch,9}$ | 4.836·10-3 | 1 | |\
\\varsigma\_{1}\
\\varsigma\_{3}\
\\frac{k W}{m\_{n}^{3}/m i n}\
\\leqslant5{}\
\\frac{1}{mathsf m{{}^\_{{3}}/\ \\
\\varsigma6\
\\frac{\\mathtt{K M}}{\\mathtt{b a r\_{9}}}\
\\beta\_{1}\
-.116\\cdot10^{-7}\
\\frac{k W}{(b a!\_\_{{9}})^{5}}\
\\beta\_{2}\
1.504\\cdot10^{-6}\
\\frac{k W}{(b a r\_{9})^{4}}\
\\beta\_{3}\
2.595\\cdot10^{-5}\
\\frac{\\mathsf{k w}}{\\({\\mathsf{b a r}\_{9mathfrak{}}})^{3}}\
\\beta\_{4}\
5.005\\cdot10^{-3}\
\\beta\_{5}\
\\frac{\\mathsf{K}}{\\mathsf{b}a\\mathsf{r}\_{\\mathfrak{g}}}\
\\beta\_{6}\
\\frac{\\mathsf{m}\_{n}^{3}}{6a r^{2}}\
\\beta\_{7}\
\\beta\_{8}\
\\beta\_{9}\
\\frac{\\mathsf{m}\_{n}^{3}}{\\operatorname\*{m i n}}\
\\delta\_{c h,1}\
-6.292\\cdot10^{-8}\
\\frac{1}{(\\mathsf{b a r}\_{\\mathfrak{g}})^{2}\\cdot\\mathsf{s}}\
\\delta\_{c h,2}\
1.082\\cdot10^{-5}\
\\frac{1}{(\\mathsf{b a r}\_{9})^{1}\\cdot\\mathsf{s}}\
\\delta\_{c h,3}\
3.620\\cdot10^{-4}\
\\delta\_{c h,4}\
\\cdot10^{-3}\
\\delta\_{c h,5}\
\\delta\_{c h,6}\
\\overline{{2.688\\cdot10^{-3}}}\
5.153\\cdot10^{-3}\
\\delta\_{c h,7}\
0.150,70\
3.741\\cdot10^{-3}\
\\delta\_{d c h,3}\
\\delta\_{d c h,4}\
\\frac{\\mathsf{m}\_{\\mathsf{n}}^{3}}{\\mathsf{m}i n}\
\\frac{\\mathfrak{b a r}}{\\mathfrak{S}}\
9.103\\cdot10^{-6}\
7.091\\cdot10^{-3}\
4.836\\cdot10^{-3}\
* * *\
# List of Figures\
1.1 General structure ofMPC ... 2\
3.1 Schematic representation of the compressed air energy storage test system... 13\
3.2 Control of the compressed air energy storage test system ... 14\
3.3 Storage pressure, electric power consumption and operation modes of theCAES\
system for one full cycle ... 15\
3.4 Power consumption of the compressors for different air flows and system pressures17\
3.5 Specific power consumption of the compressors for different air flows and pressures 18\
3.6 Measured power consumption of the individual compressors for different exemplary\
air flows and system pressures ... 19\
3.7 Power consumption of the booster ... 20\
3.8 Charge and discharge energy for one full cycle of the storage with a constant air\
demand ... 21\
3.9 Charge and discharge energy for different air demands during charging and discharging ... 22\
3.10 Round-trip efficiency of theCAESfor different air demands during charging and\
discharging ... 23\
3.11 Specific storage costs depending on the number of full cycles per day for an observation period of 10 years and electricity costs during charging of 0.10\
kWh e\
.. 24\
4.1 Structure of the LP model of the CAES system ... 26\
4.2 LP function of compressor electric power consumption ... 28\
4.3 Calculated storage pressure for exemplary charging and discharging processes\
using the LP model compared to measured data ... 29\
4.4 Structure of the MILP model of the CAES system ... 30\
4.5 System pressure as a function of the storage pressure in charge mode ... 32\
4.6 MILP model for the electric power consumption of the compressors ... 33\
4.7 MILP model for the electric power consumption of the booster ... 33\
4.8 Calculated storage pressure for exemplary charging and discharging processes\
using the MILP model compared to measured data ... 34\
4.9 Structure of the nonlinear model of the CAES system ... 36\
4.10 Storage and system pressure and total power consumption of the CAES system\
during a charging process ... 37\
4.11 Nonlinear model for the electric power consumption of the compressors ... 38\
4.12 Nonlinear model for the electric power consumption of the booster ... 39\
* * *\
## List of Figures\
4.13 Pressure profile of an exemplary charge and discharge cycle of the CAES system\
(a) with magnified pressure decrease after charging (b) and pressure increase after\
discharging (c) ... 41\
4.14 Calculated storage pressure for exemplary charging and discharging processes\
using the nonlinear model compared to measured data ... 41\
4.15 Validation data for air demand working day ... 42\
4.16 Validation data for air demand non-working day ... 43\
4.17 Simulated results using the equations of the linear (LP), the mixed-integer (MILP) and the nonliner (NL) model for the "random" control sequence with air demand\
"typical working day" ... 44\
4.18 Mean absolute error of pressure and electric power of the linear model (LP), the\
mixed-integer linear model (MILP) and the nonlinear model (NL) ... 44\
5.1 Implementation of MPC for the CAES system ... 46\
5.2 Working day air demands (used for the respective forecast scenario) ... 48\
5.3 Non-working day air demands (used for the respective forecast scenario) ... 48\
5.4 Electricity prices ... 49\
5.5 Cost comparison of the nonlinear optimization methods for scenario perfect forecast, air demand working day and typical el. price with 5 and 15 minutes timestep size. 54\
5.6 Simulated daily costs over solving time of the nonlinear optimization methods (air\
demand working day, typical el. price, 15 minutes timestep size) ... 54\
5.7 Pressure increase at the end of the charging process ... 56\
5.8 Comparison of the optimization results of the MILP model with different initial\
storage pressures ... 56\
5.9 Results for perfect forecast, air demand working day and typical el. price ... 57\
5.10 Results for perfect forecast, air demand working day and untypical el. price... 58\
5.11 Results for perfect forecast, air demand non-working day and untypical el. price. 59\
5.12 Results for perfect forecast, air demand non-working day and typical el. price.. 60\
5.13 Simulated power consumption of a charging process using the linear programming (LP), the mixed-integer linear programming (MILP) and the nonlinear (NL) model\
compared to measured data ... 60\
5.14 Cost savings for perfect air demand forecast with 15 minute optimization timestep\
size ... 61\
5.15 Results for inaccurate forecast, air demand working day and typical el. price... 62\
5.16 Results for worst-case forecast, air demand working day and typical el. price.. 62\
5.17 Results for inaccurate forecast, air demand non-working day and typical el. price. 64\
5.18 Results for worst-case forecast, air demand non-working day and typical el. price. 64\
5.19 Cost savings for imperfect air demand forecast with 15 minute optimization timestep\
size ... 65\
5.20 Cost savings compared by optimization timestep size for perfect forecast ... 66\
5.21 Results for perfectforecast, air demand working day, untypical el.price with\
optimization method MILP ... 67\
5.22 Results for perfect forecast, air demand working day, typical el.price with optimization method MILP ... 67\
* * *\
## List of Figures\
5.23 Results for perfect forecast, air demand working day, typical el.price with optimization method LP ... 68\
5.24 Results for perfectforecast, air demand working day, untypical el.price with\
optimization method LP ... 68\
5.25 Results for perfectforecast, air demand working day, untypical el.price with\
optimization method DP ... 69\
5.26 Cost savings compared by optimization timestep size for imperfect air demand\
forecast ... 70\
5.27 Results for inaccurate forecast, air demand non-working day, typical el. price with\
optimization method MILP ... 71\
5.28 Results for inaccurate forecast, air demand working day, typical el.price with\
optimization method MILP ... 71\
5.29 Results for inaccurate forecast, air demand working day, typical el.price with\
optimization method DP ... 72\
5.30 Results for worst-case forecast, air demand working day, typical el.price with\
optimization method DP ... 72\
5.31 Results for worst-case forecast, air demand non-working day, typical el. price with\
optimization method LP ... 73\
5.32 Mean cost savings compared by optimization timestep size and method for perfect\
and imperfect air demand forecast and all scenarios (total) ... 74\
C.1 Mean charge power as a function of the air demand ... 105\
C.2 Charge and discharge effciencies as a function of the air demand ... 106\
* * *\
# List of Tables\
2.1 Optimization methods used in this thesis with their advantages and disadvantages\
(based on \[57,25,86\]) ... 9\
3.1 Constants used for compressed air calculations ... 12\
3.2 Measured and calculated values of theCAESsystem ... 13\
3.3 Technical specifications of the compressors from manufacturer KAESER ... 13\
3.4 Control parameters of theCAESsystem used in this thesis ... 16\
3.5 Costs and technical data of the storages for the specific energy cost calculations. 24\
4.1 Time set and parameters ... 25\
4.2 Parameters of the LP model ... 27\
4.3 Variables of the LP model ... 27\
4.4 Parameters of the MILP model ... 30\
4.5 Variables of the MILP model ... 31\
4.6 Parameters of the nonlinear model ... 35\
4.7 Variables of the nonlinear model ... 35\
5.1 Scenarios used in this thesis to compare the different optimization methods ... 47\
5.2 Scaled minimum, mean and maximum values of the measured air demand ... 47\
5.3 Definition of forecast scenarios ... 49\
5.4 Energy consumption and costs of the reference measurements ... 50\
5.5 Energy consumption, costs and cost savings of 4 experiments for the same scenario 51\
5.6 Parameter settings of the used software and solvers for the different optimization\
methods ... 53\
5.7 Cost savings of the optimization methods for all scenarios ... 74\
A.1 Components of the compressed air energy storage system ... 77\
A.2 Component costs of the compressed air energy storage system ... 78\
B.1 Variables of the LP model ... 80\
B.2 Parameters of the LP model ... 80\
B.3 Parameters of the MILP model ... 82\
B.4 Variables of the MILP model ... 83\
B.5 Parameters of the nonlinear model ... 87\
B.6 Variables of the nonlinear model ... 88\
B.7 Variables of the MINLP model ... 99\
* * *\
## List of Tables\
C.1 General parameters of theCAESsystem ...\
C.2 Parameter values of the LP model ... 104\
C.3 Parameter values of the MILP model ... 107\
C.4 Parameter values of the nonlinear models ... 108\
* * *\
* * *\
# Acronyms\
**CAES** compressed air energy storage **CHP** combined heat and power **DP** dynamic programming **FAD** free air delivery **GA** genetic algorithm **HVAC** heating, ventilation, and air conditioning **LP** linear programming **MILP** mixed-integer linear programming **MINLP** mixed-integer nonlinear programming **MPC** Model Predictive Control **SAM** Sigma Air Manager **SMC** superior mode controller\
* * *\
* * *\
# Bibliography\
\[1\] A. Afram and F. Janabi-Sharifi. Theory and applications of hvac control systems – a review of model predictive control (mpc). Building and Environment, 72:343–355, 2014. doi:10.1016/j.buildenv.2013.11.016.3\
\[2\] Aircom. Brass pressure regulator up to 50 bar-r120. URL: https://www.aircom.net/ en/high-pressure/r120,157.html.77\
\[3\] F. Allerding, I. Mauser, and H. Schmeck. Customizable energy management in smart buildings using evolutionary algorithms. In A. I. Esparcia-Alcázar and A. M. Mora, editors, Applications of Evolutionary Computation, volume 8602 of Lecture Notes in Computer Science, pages 153–164. Springer Berlin Heidelberg, Berlin, Heidelberg,\
2014. doi:10.1007/978-3-662-45523-4{\\textunderscore}13.7\
\[4\] R. Baños, F. Manzano-Agugliaro, F. G. Montoya, C. Gil, A. Alcayde, and J. Gómez. Optimization methods applied to renewable and sustainable energy: A review. Renew- able and Sustainable Energy Reviews, 15(4):1753–1766, 2011. doi:10.1016/j.rser.\
2010.12.008.3\
\[5\] R. C. Bansal. Optimization methods for electric power systems: An overview. Inter- national Journal of Emerging Electric Power Systems, 2(1), 2005. doi:10.2202/1553- 779X.1021.3\
\[6\]R. Bellman. Dynamic programming. Princeton University Press, New Jersey, 1957.8\
\[7\] D. P. Bertsekas. Dynamic programming and optimal control. Athena Scientific optimiza- tion and computation series. Athena Scientific, Belmont, Mass., 3rd ed. edition, 2005. 8\
\[8\] S. P. Boyd and L. Vandenberghe. Convex optimization. Cambridge University Press, Cambridge, UK and New York, 2004.5\
\[9\] W. Boyes. Instrumentation reference book. Butterworth-Heinemann/Elsevier, Amster- dam and Boston, 4th ed. edition, 2010.11\
\[10\] M. C. Bozchalui, S. A. Hashmi, H. Hassen, C. A. Canizares, and K. Bhattacharya. Optimal operation of residential energy hubs in smart grids. IEEE Transactions on Smart Grid, 3(4):1755–1766, 2012. doi:10.1109/TSG.2012.2212032.6\
* * *\
\[11\] S. Bracco, F. Delfino, F. Pampararo, M. Robba, and M. Rossi. A mathematical model\
for the optimal operation of the university of genoa smart polygeneration microgrid:\
Evaluation of technical, economic and environmental performance indicators. Energy,\
64:912–922, 2014. doi:10.1016/j.energy.2013.10.039.6\
\[12\] Bundesministerium für Justiz. Erneuerbare-energien-gesetz vom 21. juli 2014 (bgbl.\
i s. 1066), das durch artikel 2 des gesetzes vom 22. dezember 2016 (bgbl. i s. 3106)\
geändert worden ist.1\
\[13\] Bundesministerium für Justiz. Kraft-wärme-kopplungsgesetz vom 21. dezember 2015\
(bgbl. i s. 2498), das durch artikel 1 des gesetzes vom 22. dezember 2016 (bgbl. i s.\
3106) geändert worden ist.1\
\[14\] Bundesministerium für Umwelt, Naturschutz, Bau und Reaktorsicherheit. Klimaschutzplan 2050 - klimaschutzpolitische grundsätze und ziele der bundesregierung, 14. November 2016. URL: www.bmub.bund.de/N53483/.1\
\[15\] Bundesministerium für Wirtschaft und Energie. Gesamtausgabe der energiedaten-datensammlung des bmwi, 01.11.2016. URL: http://www.bmwi.\
de/Redaktion/DE/Downloads/Energiedaten/energie-daten-gesamt.xls?\_\_\
blob=publicationFile&v=13.1\
\[16\] Bundesministerium für Wirtschaft und Energie. Richtlinien zur förderung von maßnahmen zur nutzung erneuerbarer energien im wärmemarkt, 11. März 2015.1\
\[17\] Bundesministerium für Wirtschaft und Energie. Förderung von stationären und dezentralen batteriespeichersystemen zur nutzung in verbindung mit photovoltaikanlagen,\
Bekanntmachung vom 17. Februar 2016, BAnz AT 29.02.2016 B1.1\
\[18\] S. Burer and A. N. Letchford. Non-convex mixed-integer nonlinear programming: A\
survey. Surveys in Operations Research and Management Science, 17(2):97–106,\
2012\. doi:10.1016/j.sorms.2012.08.001.7\
\[19\] E. F. Camacho and C. Bordons. Model predictive control. Advanced textbooks in control\
and signal processing. Springer, London and New York, 2nd ed. edition, 2007.2,3\
\[20\] E. Cardona, P. Sannino, A. Piacentino, and F. Cardona. Energy saving in airports\
by trigeneration. part ii: Short and long term planning for the malpensa 2000 chcp\
plant. Applied Thermal Engineering, 26(14-15):1437–1447, 2006. doi:10.1016/j.\
applthermaleng.2006.01.020.5\
\[21\] Christoph Passenberg, Dominik Meyer, Johannes Feldmaier, Hao Shen. Optimal water\
heater control in smart home environments. In IEEE Energycon 2016, Leuven, Belgien,\
2016.8\
\[22\] M. Conforti, G. Cornuejols, and G. Zambelli. Integer programming, volume 271 of\
\[22\] M. Conforti, G. Cornuejols, and G. Zambelli. Integer programming, volume 271 of\
Graduate Texts in Mathematics. Springer International Publishing and Imprint and\
Springer, Cham, 2014.6 github.com/DEAP/deap.52\
\[24\] Dennis Atabay. prodyn: Generic implementation of the dynamic programming algorithm\
for optimal system control. URL: https://github.com/yabata/prodyn.52\
\[25\] J. Dorfner. Open Source Modelling and Optimisation of Energy Infrastructure at Urban\
Scale. Doctoral thesis, Technische Universität München, 2016.9\
\[26\] M. Ellis, H. Durand, and P. D. Christofides. A tutorial review of economic model predictive\
control methods. Journal of Process Control, 24(8):1156–1178, 2014. doi:10.1016/j.\
jprocont.2014.03.010.2\
\[27\] T. Erseghe, A. Zanella, and C. G. Codemo. Optimal and compact control policies for\
energy storage units with single and multiple batteries. IEEE Transactions on Smart\
Grid, 5(3):1308–1317, 2014. doi:10.1109/TSG.2014.2303824.8\
\[28\] M. Fiorentini, P. Cooper, Z. Ma, and D. A. Robinson. Hybrid model predictive control of a\
residential hvac system with pvt energy generation and pcm thermal storage. Energy\
Procedia, 83:21–30, 2015. doi:10.1016/j.egypro.2015.12.192.6\
\[29\] M. Fiorentini, J. Wall, Z. Ma, J. H. Braslavsky, and P. Cooper. Hybrid model predictive\
control of a residential hvac system with on-site thermal energy generation and storage.\
Applied Energy, 187:465–479, 2017. doi:10.1016/j.apenergy.2016.11.041.6\
\[30\] V. Francois-Lavet, R. Fonteneau, and D. Ernst. Using approximate dynamic programming for estimating the revenues of a hydrogen-based high-capacity storage device. In\
2014 IEEE Symposium on Adaptive Dynamic Programming and Reinforcement Learning (ADPRL), pages 1–8. doi:10.1109/ADPRL.2014.7010624.8\
\[31\] C. Gamarra and J. M. Guerrero. Computational optimization techniques applied to\
microgrids planning: A review. Renewable and Sustainable Energy Reviews, 48:413–\
424, 2015. doi:10.1016/j.rser.2015.04.025.3\
\[32\] Gemü. Angle seat globe control valve, metal, 554. URL: https://www.gemu-group.\
com/gemu-cdn/dokumente/2/db\_554regel\_gb.pdf.77\
\[33\] Gemü. Ball valve, ball valve, stainless steel multi-port, 711, 728, 751.\
URL: https://www.gemu-group.com/gemu-cdn/dokumente/2/db\_711\_728\_751\_3-\
piece\_3-2-way\_gb.pdf.77\
\[34\] P. S. Georgilakis and N. D. Hatziargyriou. A review of power distribution planning in\
the modern power systems era: Models, methods and future research. Electric Power\
Systems Research, 121:89–100, 2015. doi:10.1016/j.epsr.2014.12.010.3\
\[35\] Gregor P. Henze, Doreen E. Kalz, Simeng Liu, and Clemens Felsmann. Experimental\
\[23\] DEAP. Distributed evolutionary algorithms in python, version 1.0.2. URL: https://\
github.com/DEAP/deap.52\
\[35\] Gregor P. Henze, Doreen E. Kalz, Simeng Liu, and Clemens Felsmann. Experimental\
analysis of model-based predictive optimal control for active and passive building thermal\
storage inventory. HVAC&R Research, 11(2):189–213, 2005. doi:10.1080/10789669.\
2005.10391134.8\
* * *\
120 Bibliography\
\[36\] L. Grüne and J. Pannek. Nonlinear model predictive control: Theory and agorithms.\
Communications and control engineering. Springer, London \[u.a.\], 2011.2\
\[37\] W. Gu, Z. Wu, R. Bo, W. Liu, G. Zhou, W. Chen, and Z. Wu. Modeling, planning and\
optimal energy management of combined cooling, heating and power microgrid: A\
review. International Journal of Electrical Power & Energy Systems, 54:26–37, 2014.\
doi:10.1016/j.ijepes.2013.06.028.3\
\[38\] G. P. Henze, C. Felsmann, and G. Knabe. Evaluation of optimal control for active and\
passive building thermal storage. International Journal of Thermal Sciences, 43(2):173–\
183, 2004. doi:10.1016/j.ijthermalsci.2003.06.001.8\
\[39\] HYDAC. Electronic pressure transmitter hda 4400. URL: http://www.hydac.com/\
fileadmin/pdb/pdf/PRO0000000000000000000018305050011.pdf.77\
\[40\] IBM ILOG CPLEX Interactive Optimizer. version 12.6.3.0. URL: http://www-01.ibm.\
com/software/commerce/optimization/cplex-optimizer/index.html.51\
\[41\] M. Iqbal, M. Azam, M. Naeem, A. S. Khwaja, and A. Anpalagan. Optimization classification, algorithms and tools for renewable energy: A review. Renewable and Sustainable\
Energy Reviews, 39:640–654, 2014. doi:10.1016/j.rser.2014.07.120.3\
\[42\] Johannes Jungwirth. Lastmanagement in Gebäuden: Entwicklung einer modellprädiktiven Regelung mit einem adaptiven Gebäudemodell zur Flexibilisierung der Wärmeund Kälteversorgung von Gebäuden. Dissertation, Technische Universität München,\
2014.7,52\
\[43\] Josef Lipp. Flexible Stromerzeugung mit Mikro-KWK-Anlagen: Experimentelle Untersuchung der Möglichkeiten einer flexiblen Stromerzeugung von Mikro-KWK-Anlagen\
mit Hilfe einer Wärmebedarfsprognose und einem intelligenten Speichermanagementsystem. Dissertation, Technische Universität München, 2015.7\
\[44\] KAESER KOMPRESSOREN SE. Air receivers. URL: http://www.kaeser.com/\
Images/P-775-ED-tcm8-7411.pdf.77\
\[45\] KAESER KOMPRESSOREN SE. Betriebsanleitung schraubenkompressor sm sfc sigma\
control 2 (9\_\_5873 24 d).17\
\[46\] KAESER KOMPRESSOREN SE. Betriebsanleitung schraubenkompressor sm sigma\
control 2 (9\_\_5871 24 d).17\
\[47\] KAESER KOMPRESSOREN SE. Betriebsanleitung schraubenkompressor sx sigma\
control 2 (9\_6925 21 d).17\
\[48\] KAESER KOMPRESSOREN SE. Boosters - n series. URL: http://www.kaeser.com/\
Images/P-480-ED-tcm8-13912.pdf.13\
\[49\] KAESER KOMPRESSOREN SE. Filters & centrifugal separators. URL: http://www.\
kaeser.com/Images/P-725-ED-tcm8-6771.pdf.77\
* * *\
\[50\] KAESER KOMPRESSOREN SE. Refrigeration dryers secotec. URL: http://www.\
kaeser.com/Images/P-013-ED-tcm8-6741.pdf.77\
\[51\] KAESER KOMPRESSOREN SE. Rotary screw compressors - sm series. URL: http:\
// www.kaeser.com/Images/P-651-24-ED-tcm8-52847.pdf.13\
\[52\] KAESER KOMPRESSOREN SE. Rotary screw compressors - sx series. URL: http:\
// www.kaeser.com/Images/P-651-0-ED-tcm8-6759.pdf.13\
\[53\] KAESER KOMPRESSOREN SE. Technische daten sm12 sfc sigma 026 (t10085).18,\
19\
\[54\] S. Kochanneck, I. Mauser, B. Bohnet, S. Hubschneider, H. Schmeck, M. Braun, and\
T. Leibfried. Establishing a hardware-in-the-loop research environment with a hybrid\
energy storage system. In 2016 IEEE Innovative Smart Grid Technologies - Asia (ISGT-\
Asia), pages 497–503. doi:10.1109/ISGT-Asia.2016.7796435.7\
\[55\] B. Kouvaritakis and M. Cannon. Model predictive control: Classical, robust and stochastic. Advanced textbooks in control and signal processing. Springer, Cham and Heidelberg\
and New York and Dordrecht and London, 2015.2\
\[56\] P. O. Kriett and M. Salani. Optimal control of a residential microgrid. Energy, 42(1):321–\
330, 2012. doi:10.1016/j.energy.2012.03.049.6\
\[57\] P. Kuhn. Iteratives Modell zur Optimierung von Speicherausbau und -betrieb in einem\
Stromsystem mit zunehmend fluktuierender Erzeugung. Doctoral thesis, Technische\
Universität München, 2012. URL: https://mediatum.ub.tum.de/?id=1271192.9\
\[58\] K. S. Kwan and D. K. Maly. Optimal battery energy storage system (bess) charge\
scheduling with dynamic programming. IEE Proceedings - Science, Measurement and\
Technology, 142(6):453–458, 1995. doi:10.1049/ip-smt:19951929.8\
\[59\] Lei Zhang and Yaoyu Li. Optimal energy management of wind-battery hybrid power\
system with two-scale dynamic programming. IEEE Transactions on Sustainable Energy,\
4(3):765–773, 2013. doi:10.1109/TSTE.2013.2246875.8\
\[60\] M. A. Lozano, M. Carvalho, and L. M. Serra. Operational strategy and marginal costs\
in simple trigeneration systems. Energy, 34(11):2001–2008, 2009. doi:10.1016/j.\
energy.2009.08.015.5\
\[61\] J. Ma, J. Qin, T. Salsbury, and P. Xu. Demand reduction in building energy systems based\
on economic model predictive control. Chemical Engineering Science, 67(1):92–100,\
2012\. doi:10.1016/j.ces.2011.07.052.5\
\[62\] Y. Ma, F. Borrelli, B. Hencey, A. Packard, and S. Bortoff. Model predictive control of\
thermal energy storage in building cooling systems. In 2009 Joint 48th IEEE Conference\
on Decision and Control (CDC) and 28th Chinese Control Conference (CCC), pages\
392–397. doi:10.1109/CDC.2009.5400677.7\
* * *\
\[63\] L. Majic and Krzelj, I. Delimar, M. Optimal scheduling of a chp system with energy\
storage. In 36th International Convention on Information & Communication Technology,\
Electronics & Microelectronics (MIPRO), 2013, pages 1253–1257, Piscataway, NJ, 2013.\
IEEE.5\
\[64\] I. Mauser, J. Müller, F. Allerding, and H. Schmeck. Adaptive building energy management\
with multiple commodities and flexible evolutionary optimization. Renewable Energy,\
87:911–921, 2016. doi:10.1016/j.renene.2015.09.003.7,50\
\[65\] B. Mayer, M. Killian, and M. Kozek. Management of hybrid energy supply systems in\
buildings using mixed-integer model predictive control. Energy Conversion and Management, 98:470–483, 2015. doi:10.1016/j.enconman.2015.02.076.6\
\[66\] B. Mayer, M. Killian, and M. Kozek. A branch and bound approach for building cooling\
supply control with hybrid model predictive control. Energy and Buildings, 128:553–566,\
2016\. doi:10.1016/j.enbuild.2016.07.027.6\
\[67\] D. Q. Mayne. Model predictive control: Recent developments and future promise.\
Automatica, 50(12):2967–2986, 2014. doi:10.1016/j.automatica.2014.10.128.2\
\[68\] E. D. Mehleri, H. Sarimveis, L. G. Papageorgiou, and N. C. Markatos. Model predictive\
control of distributed energy resources. In 2012 20th Mediterranean Conference on\
Control & Automation (MED 2012), pages 672–678. doi:10.1109/MED.2012.6265715.\
\[69\] L. Meng, E. R. Sanseverino, A. Luna, T. Dragicevic, J. C. Vasquez, and J. M. Guerrero.\
Microgrid supervisory controllers and energy management systems: A literature review.\
Renewable and Sustainable Energy Reviews, 60:1263–1273, 2016. doi:10.1016/j.\
rser.2016.03.003.3\
\[70\] H. Morais, P. Kádár, P. Faria, Z. A. Vale, and H. M. Khodr. Optimal scheduling of a\
renewable micro-grid in an isolated load area using mixed-integer linear programming.\
Renewable Energy, 35(1):151–156, 2010. doi:10.1016/j.renene.2009.02.031.6\
\[71\] M. J. Moran. Fundamentals of engineering thermodynamics. Wiley, \[Hoboken, N.J.?\],\
7th ed. edition, 2011.12\
\[72\] M. Morari and J. H. Lee. Model predictive control: Past, present and future. Computers &\
Chemical Engineering, 23(4-5):667–682, 1999. doi:10.1016/S0098-1354(98)00301-\
9.2,3\
\[73\] J. Müller, M. März, I. Mauser, and H. Schmeck. Optimization of operation and control\
strategies for battery energy storage systems by evolutionary algorithms. In G. Squillero\
and P. Burelli, editors, Applications of Evolutionary Computation, volume 9597 of Lecture\
Notes in Computer Science, pages 507–522. Springer International Publishing, Cham,\
2016\. doi:10.1007/978-3-319-31204-0{\\textunderscore}33.7,50\
\[74\] MÜLLER + ZIEGLER GmbH & Co. KG. Messumformer für wirkleistung, wechselstrom\
und drehstrom. URL: http://www.mueller-ziegler.de/fileadmin/user\_upload/\
Messumformer\_Netzgroessen/MZ\_Messumformer\_Pw-MU.pdf.77\
* * *\
Bibliography 123\
\[75\] M. Nguyen, D. Nguyen, and Y. Yoon. A new battery energy storage charging/discharging\
scheme for wind power producers in real-time markets. Energies, 5(12):5439–5452,\
2012\. doi:10.3390/en5125439.8\
\[76\] S. Nojavan, K. Zare, and B. Mohammadi-Ivatloo. Optimal stochastic energy management\
of retailer based on selling price determination under smart grid environment in the\
presence of demand response program. Applied Energy, 187:449–464, 2017. doi:\
10.1016/j.apenergy.2016.11.024.7\
\[77\] S. M. Nosratabadi, R.-A. Hooshmand, and E. Gholipour. A comprehensive review on\
microgrid and virtual power plant concepts employed for distributed energy resources\
scheduling in power systems. Renewable and Sustainable Energy Reviews, 67:341–\
363, 2017. doi:10.1016/j.rser.2016.09.025.3\
\[78\] A. Núñez-Reyes, D. Marcos Rodríguez, C. Bordons Alba, and M. Á. Ridao Carlini.\
Optimal scheduling of grid-connected pv plants with energy storage for integration in the\
electricity market. Solar Energy, 144:502–516, 2017. doi:10.1016/j.solener.2016.\
12.034.5\
\[79\] R. Ooka and S. Ikeda. A review on optimization techniques for active thermal energy\
storage control. Energy and Buildings, 106:225–233, 2015. doi:10.1016/j.enbuild.\
2015.07.031.3\
\[80\] R. Palma-Behnke, C. Benavides, F. Lanas, B. Severino, L. Reyes, J. Llanos, and D. Saez.\
A microgrid energy management system based on the rolling horizon strategy. IEEE\
Transactions on Smart Grid, 4(2):996–1006, 2013. doi:10.1109/TSG.2012.2231440.\
\[81\] A. Parisio, E. Rikos, and L. Glielmo. A model predictive control approach to microgrid\
operation optimization. IEEE Transactions on Control Systems Technology, 22(5):1813–\
1827, 2014. doi:10.1109/TCST.2013.2295737.6\
\[82\] A. Parisio, E. Rikos, G. Tzamalis, and L. Glielmo. Use of model predictive control for\
experimental microgrid optimization. Applied Energy, 115:37–46, 2014. doi:10.1016/\
j.apenergy.2013.10.027.6\
\[83\]Pyomo. version 4.2.10487. URL: http://www.pyomo.org/.51,79\
\[84\] S. Qin and T. A. Badgwell. A survey of industrial model predictive control technology.\
Control Engineering Practice, 11(7):733–764, 2003. doi:10.1016/S0967-0661(02)\
00186-7.2\
\[85\] D. Quiggin, S. Cornell, M. Tierney, and R. Buswell. A simulation and optimisation\
study: Towards a decentralised microgrid, using real world fluctuation data. Energy,\
41(1):549–559, 2012. doi:10.1016/j.energy.2012.02.007.5\
\[86\] S. S. Rao. Engineering optimization: theory and praxis. Wiley, New York, N.Y, 4th ed.\
edition, 2009.5,9\
* * *\
Pub, Madison, Wis., 2009.2\
\[88\] Y. Riffonneau, S. Bacha, F. Barruel, and S. Ploix. Optimal power flow management for\
grid connected pv systems with batteries. IEEE Transactions on Sustainable Energy,\
2(3):309–320, 2011. doi:10.1109/TSTE.2011.2114901.8\
\[89\] J. A. Rossiter. Model-based predictive control: A practical approach. Control series.\
CRC Press, Boca Raton, 2003.2\
\[90\] J. Sachs, A. Gienger, and O. Sawodny. Combined probabilistic and set-based uncertainties for a stochastic model predictive control of island energy systems. In 2016 American\
Control Conference (ACC), pages 6767–6772. doi:10.1109/ACC.2016.7526737.7\
\[91\]SciPy. version 0.18.1. URL: https://www.scipy.org/.103\
\[92\] E. Shirazi and S. Jadid. Optimal residential appliance scheduling under dynamic pricing\
scheme via hemdas. Energy and Buildings, 93:40–49, 2015. doi:10.1016/j.enbuild.\
2015.01.061.7\
\[93\] S. N. Sivanandam and S. N. Deepa. Introduction to genetic algorithms. Springer, Berlin\
and New York, 2007.7\
\[94\]sonnen GmbH. Die sonnenbatterie. URL: https://www.sonnenbatterie.de/.24\
\[95\] P. Stadler, A. Ashouri, and F. Maréchal. Model-based optimization of distributed and\
renewable energy systems in buildings. Energy and Buildings, 120:103–113, 2016.\
doi:10.1016/j.enbuild.2016.03.051.6\
\[96\] tecsis. Pt compact, pt compact plus. URL: http://www.tecsis.com/fileadmin/\
Content/tecsis/2\_Files/3\_Temperature/B\_Electrical\_Temperature\_\
Measuring/de1127.pdf.77\
\[97\] Tesla Motors. Powerwall. URL: https://www.teslamotors.com/de\_DE/powerwall.\
24\
\[98\] The Optimization Firm. Baron version 16.11.18. URL: http://www.minlp.com/home.\
52\
\[99\] A. N. Ünal, S. Ercan, and G. Kayakutlu. Optimisation studies on tri-generation: A review.\
International Journal of Energy Research, 39(10):1311–1334, 2015. doi:10.1002/er.\
3342.3\
\[100\] Y. Wang, X. Lin, M. Pedram, S. Park, and N. Chang. Optimal control of a grid-connected\
hybrid electrical energy storage system for homes. In Design Automation and Test in\
Europe, pages 881–886. doi:10.7873/DATE.2013.186.8\
\[101\] D. Wolf, A. Kanngießer, M. Budt, and C. Doetsch. Adiabatic compressed air energy\
storage co-located with wind energy—multifunctional storage commitment optimization\
for the german market using gomes. Energy Systems, 3(2):181–208, 2012. doi:\
10.1007/s12667-011-0044-7.6\
\[87\] J. B. Rawlings and D. Q. Mayne. Model predictive control: Theory and design. Nob Hill\
Pub, Madison, Wis., 2009.2\
* * *\
Bibliography\
\[102\] X. Xia and A. M. Elaiw. Optimal dynamic economic dispatch of generation: A review. Electric Power Systems Research, 80(8):975–986, 2010. doi:10.1016/j.epsr.2009.\
12.012.3\
\[103\] L. Xie and M. D. Ilic. Model predictive dispatch in electric energy systems with intermittent resources. In 2008 IEEE International Conference on Systems, Man and Cybernetics (SMC), pages 42–47. doi:10.1109/ICSMC.2008.4811248.5\
\[104\] Y. Yoon and Y.-H. Kim. Effective scheduling of residential energy storage systems under dynamic pricing. Renewable Energy, 87:936–945, 2016. doi:10.1016/j.renene.\
2015.09.072.8\
\[105\] Yudong Ma, F. Borrelli, B. Hencey, B. Coffey, S. Bengea, and P. Haves. Model predictive control for the operation of building cooling systems. IEEE Transactions on Control Systems Technology, 20(3):796–803, 2012. doi:10.1109/TCST.2011.2124461.7\
\[106\]X. Zhang, G. Hug, J. Z. Kolter, and I. Harjunkoski. Model predictive control of industrial loads and energy storage for demand response. In 2016 IEEE Power and Energy Society General Meeting (PESGM), pages 1–5. doi:10.1109/PESGM.2016.7741228. 6\
\[107\] Y. Zong, D. Kullmann, A. Thavlov, O. Gehrke, and H. W. Bindner. Application of model predictive control for active load management in a distributed power system with high wind penetration. IEEE Transactions on Smart Grid, 3(2):1055–1062, 2012. doi:\
10.1109/TSG.2011.2177282.6