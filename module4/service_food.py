import json


def find_best_ass(file_name: str) -> None:

    food_service_name: dict[str, int] = {}
    food_service_area: dict[str, int] = {}

    with open(file_name, "r", encoding="utf-8") as f:
        jsoned_value = json.load(f)

        for row in jsoned_value:
            if row["OperatingCompany"]:
                company = row["OperatingCompany"]
                food_service_name[company] = food_service_name.get(company, 0) + 1

            area = row["District"]
            food_service_area[area] = food_service_area.get(area, 0) + 1

    best_food_name = max(food_service_name, key=lambda x: food_service_name[x])
    best_district = max(food_service_area, key=lambda x: food_service_area[x])

    print(
        f"{best_district}: {food_service_area[best_district]}",
        f"{best_food_name}: {food_service_name[best_food_name]}",
        sep="\n",
    )


find_best_ass("food_services.json")
