import csv
import json
from datetime import datetime


def process_exam_results(input_file: str, output_file: str) -> None:

    scores_dict: dict[str, dict] = {}
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row["best_score"] = int(row.pop("score"))

            r = scores_dict.get(row["email"], row)
            best_row = max(
                r,
                row,
                key=lambda item: (
                    item["best_score"],
                    datetime.fromisoformat(item["date_and_time"]),
                ),
            )

            scores_dict[row["email"]] = best_row

    with open(output_file, 'w', encoding='utf-8') as f_out:
        output_json = sorted(scores_dict.values(), key=lambda x: x['email'])
        json.dump(output_json, f_out, indent=3)


process_exam_results('exam_results.csv', 'best_scores.json')
