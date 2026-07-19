import type { ResearchSession } from '../types';

export const mockSessions: ResearchSession[] = [
  {
    id: '1',
    title: 'The Impact of CRISPR Gene Editing',
    date: '2023-10-24',
    status: 'completed',
    content: '# The Impact of CRISPR Gene Editing\n\nCRISPR-Cas9 has revolutionized genomic engineering, providing unprecedented precision in DNA modification...',
    stats: {
      sources: 34,
      wordCount: 4200,
      readingTime: 18,
      confidenceScore: 96,
      credibilityScore: 9.2,
    },
    progressStage: 12,
  },
  {
    id: '2',
    title: 'Quantum Computing in Cryptography',
    date: '2023-10-22',
    status: 'completed',
    content: `# Advances in Control Algorithms for Robotics: A Review of Model Predictive Control and Reinforcement Learning

## Introduction

Model Predictive Control (MPC) has emerged as a powerful control strategy in robotics, enabling the development of sophisticated and efficient control systems. MPC is an advanced control technique that uses a model of the system to predict its future behavior and optimize its performance. In robotics, MPC is particularly useful for controlling complex systems that involve multiple variables, constraints, and nonlinear dynamics. The use of MPC in robotics offers several key benefits, including improved control performance, handling of complex systems, adaptability to changing conditions, and robustness to uncertainty. This section provides an overview of MPC and its significance in robotics, highlighting its importance and applications in the field.


## Mathematical Foundations of Model Predictive Control

Model Predictive Control (MPC) is a modern control strategy that utilizes a model of the dynamic system to predict its future behavior and optimize its performance. The core idea of MPC is to use a model of the system to forecast its future evolution and optimize the control signal while accounting for possible violations of state trajectories and bounding the input to admissible sets of values. 

  The mathematical foundation of MPC involves solving an optimization problem at each control cycle to find a command that optimizes the future behavior of the robot. This approach enables the creation of versatile and reactive behaviors. A simple change in the cost function defining the goal of the controller leads to a different behavior without the need for a new algorithm. 

  In MPC, the controller solves an optimization problem of the form: 
  - abs(u[t]) <= u_max, t=0..T (maximum input box constraint)
  - norminf(u[t+1] - u[t]) <= S, t=0..T-1 (slew rate constraint)

  The optimization problem is solved at each control cycle to ensure optimal actions are taken at every instant of time while ensuring constraint satisfaction. However, the use of MPC on real, complex robots leads to important challenges, as the dynamics of complex robots are typically nonlinear.

  The available literature provides various examples of MPC applications in robotics, including aerial robotics. For instance, Linear MPC has been used for quadrotor control, as presented in the paper by K. Alexis, G. Nikolakopoulos, and A. Tzes, "Model Predictive Quadrotor Control: Attitude, Altitude and Position Experimental Studies."

  Despite its significance, the provided context does not offer a comprehensive mathematical derivation of MPC. A detailed mathematical treatment of MPC would involve discussing the underlying optimization techniques, such as quadratic programming or nonlinear programming, and the specific formulations used in different MPC variants.


## Model Predictive Control in Robotics: Fundamentals and Advantages

Model Predictive Control (MPC) has emerged as a powerful control strategy in robotics, enabling the development of sophisticated and efficient control systems. MPC uses a model of the system to predict its future behavior and optimize its performance. In robotics, MPC is particularly useful for controlling complex systems that involve multiple variables, constraints, and nonlinear dynamics. The core idea of MPC is to use a model of the dynamic system to predict the future evolution of the state trajectories in order to optimize the control signal and account for possible violation of the state trajectories while bounding the input to the admissible set of values. MPC circumvents the issue of computing a globally optimal control policy by instead re-computing at every control cycle an optimal control 'trajectory', i.e., a sequence of optimal actions to be taken from the current state of the system. This approach enables the creation of very versatile and reactive behaviors. A simple change in the cost function defining the goal of the controller leads to a different behavior without the need for a new algorithm. MPC offers several advantages, including the ability to handle complex multi-variable control problems, trajectory tracking, collision avoidance, and dynamic obstacle navigation in structured environments. However, the use of MPC on real, complex robots leads to important challenges, as the dynamics of complex robots is typically nonlinear and computing a globally optimal control policy is generally intractable.


## Reinforcement Learning in Robotics: Fundamentals and Applications

Reinforcement learning offers a framework and set of tools for designing sophisticated and hard-to-engineer behaviors in robotics. The challenges of robotic problems provide inspiration, impact, and validation for developments in reinforcement learning. The relationship between reinforcement learning and robotics has significant promise, similar to that between physics and mathematics. 

Reinforcement learning is not directly applicable to robotics yet, unlike supervised learning, which has made considerable progress in large-scale deployment. However, reinforcement learning can be employed for various physical systems and control tasks in robotics. The user must carefully select appropriate methods, as there are no single answers for the heterogeneous field of robotics. 

The choice between model-based and model-free methods, as well as between value function-based and policy search methods, is crucial. All methods require hand-tuning for choosing representations, reward functions, and prior knowledge. The correct use of models in robot reinforcement learning requires substantial future research. A key step in robotic reinforcement learning is the automated choice of these elements.

Open questions in robotic reinforcement learning include the automated selection of prior knowledge, representations, reward functions, and models. The field requires further research to address these challenges and make reinforcement learning more widely applicable in robotics.


## Industrial Applications of Control Algorithms in Robotics

The integration of advanced control algorithms in robotics has significantly transformed industrial automation. Historically, industrial robotics control systems have evolved from basic position control mechanisms to sophisticated frameworks, including PID controllers, adaptive control systems, and model predictive control (MPC) frameworks. This progression is driven by the increasing complexity of manufacturing processes and the need for robots to operate in dynamic environments while maintaining high performance standards. 

The current market demands intelligent automation solutions that can anticipate and respond to changing operational conditions. The fourth industrial revolution has intensified the requirements for predictive capabilities in robotic systems, particularly in sectors such as automotive manufacturing, electronics assembly, and precision machining, where microsecond-level accuracy and real-time adaptation are critical.

Model Predictive Control (MPC) has emerged as a powerful control strategy in robotics, enabling the development of sophisticated and efficient control systems. MPC uses a model of the system to predict its future behavior and optimize its performance, making it particularly useful for controlling complex systems that involve multiple variables, constraints, and nonlinear dynamics.

The application of MPC in robotics offers several key benefits, including improved control performance, handling of complex systems, adaptability to changing conditions, and robustness to uncertainty. These benefits position organizations to achieve competitive advantages through enhanced productivity, reduced operational costs, and improved product quality consistency in increasingly automated industrial environments.


## Future Research Directions

The future of robotic manipulation and control appears to be heavily influenced by advancements in Model Predictive Control (MPC) and reinforcement learning. Research in MPC for robotics has been gaining momentum, particularly in areas such as autonomous systems, robotic manipulation, and humanoid robotics. The integration of MPC with other control techniques, like reinforcement learning, is expected to play a crucial role in addressing complex control tasks. For instance, the application of MPC in multi-agent manipulation systems and its ability to handle uncertainty and disturbances make it a promising area of research. Moreover, the use of model-free deep policy networks for multi-objective force-position control in collaborative robotic systems presents opportunities for future exploration. However, the available literature does not provide enough information on the specific challenges and limitations that need to be addressed in the development and implementation of these control techniques. Future research should focus on investigating the potential of MPC and reinforcement learning in solving real-world robotic control problems, as well as addressing the challenges associated with their implementation in complex systems.


## Conclusion

The surveyed articles highlight the significance of manipulation in robotics, with a focus on control techniques such as reinforcement learning and model predictive control. Manipulation tasks require coordinated control of end-effector position and contact forces, which can be achieved through advanced control strategies. The integration of biological and robotic manipulation provides valuable insights into the development of sophisticated control systems. However, the available literature does not provide enough information on the specific applications and limitations of these control techniques in real-world scenarios. Future research should focus on addressing these gaps and exploring the potential of advanced control strategies in robotics.

`,
    stats: {
      sources: 18,
      wordCount: 2100,
      readingTime: 9,
      confidenceScore: 88,
      credibilityScore: 8.5,
    },
    progressStage: 12,
  },
  {
    id: '3',
    title: 'AGI Safety Protocols',
    date: '2023-10-20',
    status: 'completed',
    content: '# AGI Safety Protocols\n\nDeveloping aligned Artificial General Intelligence requires robust reward modeling...',
    stats: {
      sources: 42,
      wordCount: 5100,
      readingTime: 22,
      confidenceScore: 91,
      credibilityScore: 9.5,
    },
    progressStage: 12,
  }
];