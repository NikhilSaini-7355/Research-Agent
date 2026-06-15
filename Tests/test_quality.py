import os
import json
import shutil

from Agents.content_quality_evaluator import (
    ContentQualityEvaluator
)

SOURCE_DIR = "research_docs"

HIGH_DIR = os.path.join(
    SOURCE_DIR,
    "high_quality"
)

MEDIUM_DIR = os.path.join(
    SOURCE_DIR,
    "medium_quality"
)

LOW_DIR = os.path.join(
    SOURCE_DIR,
    "low_quality"
)

os.makedirs(HIGH_DIR, exist_ok=True)
os.makedirs(MEDIUM_DIR, exist_ok=True)
os.makedirs(LOW_DIR, exist_ok=True)

evaluator = ContentQualityEvaluator()

classification_log = []

total_files = 0
high_count = 0
medium_count = 0
low_count = 0

for filename in os.listdir(SOURCE_DIR):

    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(
        SOURCE_DIR,
        filename
    )

    print(f"\nEvaluating: {filename}")

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        result = evaluator.evaluate(
            content[:8000]
        )

        quality = result.quality.upper()

        if quality == "HIGH":

            destination = os.path.join(
                HIGH_DIR,
                filename
            )

            high_count += 1

        elif quality == "MEDIUM":

            destination = os.path.join(
                MEDIUM_DIR,
                filename
            )

            medium_count += 1

        else:

            destination = os.path.join(
                LOW_DIR,
                filename
            )

            low_count += 1

        shutil.move(
            filepath,
            destination
        )

        classification_log.append(
            {
                "file": filename,
                "quality": result.quality,
                "knowledge_density": result.knowledge_density,
                "reason": result.reason
            }
        )

        total_files += 1

        print(
            f"{filename} → {quality}"
        )

    except Exception as e:

        print(
            f"Failed processing {filename}"
        )

        print(e)

with open(
    os.path.join(
        SOURCE_DIR,
        "classification_results.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        classification_log,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\n" + "=" * 60)
print(f"Total Files : {total_files}")
print(f"HIGH        : {high_count}")
print(f"MEDIUM      : {medium_count}")
print(f"LOW         : {low_count}")
print("=" * 60)