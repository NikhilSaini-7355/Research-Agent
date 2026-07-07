from Agents.outline_generator import OutlineGenerator

summary = """
Fundamentals:
Model Predictive Control predicts future outputs.

Applications:
Chemical plants and power systems.

Advantages:
Constraint handling and multivariable control.

Limitations:
High computational cost.

Research Gaps:
Real-time nonlinear MPC.
"""

generator = OutlineGenerator()

outline = generator.generate_outline(summary)

print(outline.model_dump())