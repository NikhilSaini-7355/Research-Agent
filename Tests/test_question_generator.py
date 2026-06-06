from src.agents.question_generator import generate_questions

questions = generate_questions(
    topic="AI in Healthcare",
    persona="Doctor"
)

for q in questions:
    print("-", q)