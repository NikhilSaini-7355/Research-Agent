from typing import Dict


CONTROL_THEORY = [
    "pid",
    "state space",
    "lqr",
    "lqg",
    "mpc",
    "model predictive control",
    "kalman",
    "observer",
    "controllability",
    "observability",
    "adaptive control",
    "robust control",
    "pole placement",
    "root locus",
    "bode plot",
    "nyquist"
]

PROCESS_CONTROL = [
    "process control",
    "distillation",
    "chemical process",
    "feedforward",
    "cascade control",
    "ratio control",
    "boiler",
    "reactor",
    "heat exchanger",
    "process dynamics"
]

AUTOMATION = [
    "plc",
    "scada",
    "hmi",
    "modbus",
    "profibus",
    "profinet",
    "industrial ethernet",
    "industrial automation",
    "opc ua",
    "ladder logic"
]

INSTRUMENTATION = [
    "sensor",
    "transmitter",
    "flow meter",
    "pressure sensor",
    "temperature sensor",
    "instrumentation",
    "calibration",
    "measurement",
    "control valve",
    "actuator"
]

INDUSTRIAL_IOT = [
    "iot",
    "iiot",
    "digital twin",
    "edge computing",
    "predictive maintenance",
    "industry 4.0"
]


def classify_query(query: str) -> Dict[str, int]:
    query = query.lower()

    scores = {
        "control_theory": 0,
        "process_control": 0,
        "automation": 0,
        "instrumentation": 0,
        "industrial_iot": 0
    }

    for keyword in CONTROL_THEORY:
        if keyword in query:
            scores["control_theory"] += 1

    for keyword in PROCESS_CONTROL:
        if keyword in query:
            scores["process_control"] += 1

    for keyword in AUTOMATION:
        if keyword in query:
            scores["automation"] += 1

    for keyword in INSTRUMENTATION:
        if keyword in query:
            scores["instrumentation"] += 1

    for keyword in INDUSTRIAL_IOT:
        if keyword in query:
            scores["industrial_iot"] += 1

    best_domain = max(scores, key=scores.get)

    if scores[best_domain] == 0:
        best_domain = "general"

    return {
        "domain": best_domain,
        "scores": scores
    }


if(__name__ == "__main__"):

    queries = [
        "Explain Model Predictive Control",
        "How does a PLC work?",
        "What is SCADA?",
        "Explain Kalman Filter",
        "Pressure transmitter calibration procedure",
        "Industrial IoT architecture"
    ]
    
    for q in queries:
        print(q)
        print(classify_query(q))
        print("-" * 50)