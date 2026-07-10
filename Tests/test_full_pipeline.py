from Graph.research_pipeline import app

inputs = {
    "topic": "Benefits AI has given to the US Citizens",
    "project_id": "21111111-1111-1111-1111-111111111111"
}

final_result = app.ainvoke(inputs)

print("Final Result:\n")
print(final_result)