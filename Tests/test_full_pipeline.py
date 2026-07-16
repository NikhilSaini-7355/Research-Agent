import asyncio
import sys
import pprint
from Graph.research_pipeline import app

async def main():
    inputs = {
        "topic": "Control alogrithms in robotics",
        "project_id": "71111111-1111-1111-1111-111111111112"
    }

    print("🚀 Starting Async Pipeline...")
    
    # You MUST await ainvoke
    final_result = await app.ainvoke(inputs)

    print("\n✅ Final Result:\n")
    for result in final_result.get("search_results", []):
        # indent=4 adds spaces for readability
        pprint.pprint(result, indent=4)
        print("-" * 50)
    
    print("\n research summary:\n")
    print(final_result.get("research_summary", "No research summary generated."))

    print("\n outline:\n")
    print(final_result.get("outline", "No outline generated."))
    
if __name__ == "__main__":
    # This prevents the "Event loop closed" error on Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(main())