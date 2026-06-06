from src.agents.question_generator import generate_questions

persona = {
    "role": "Indian Macroeconomist",
    "perspective": "India's GDP growth rate and large youth population give it an edge over China in the long term, but it needs to focus on economic reforms and infrastructure development."
}
questions = generate_questions(
    topic="AI in Healthcare",
    persona=persona
)

for q in questions:
    print("-", q)