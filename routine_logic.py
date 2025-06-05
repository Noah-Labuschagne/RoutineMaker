# routine_logic.py

import pandas as pd

csv_path = "Elements/MAG_Rings_Elements.csv"
elements_df = pd.read_csv(csv_path)




difficulty_scale = {
    "A": 0.1, "B": 0.2, "C": 0.3, "D": 0.4, "E": 0.5,
    "F": 0.6, "G": 0.7, "H": 0.8, "I": 0.9, "J": 1.0,
}

# Build ELEMENT_DB from CSV
ELEMENT_DB = {
    row["Element Name"]: {
        "difficulty": row["Difficulty"],
        "group": row["Element Group"]
    }
    for _, row in elements_df.iterrows()
}

def calculate_h5_score(routine):
    seen = set()
    unique_elements = []

    for element in routine:
        if element not in ELEMENT_DB:
            raise ValueError(f"Invalid element: {element}")
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)

    scored_elements = sorted(
        unique_elements,
        key=lambda el: difficulty_scale[ELEMENT_DB[el]["difficulty"]],
        reverse=True
    )[:5]

    total_difficulty = sum(
        difficulty_scale[ELEMENT_DB[el]["difficulty"]] for el in scored_elements
    )

    unique_groups = {ELEMENT_DB[el]["group"] for el in scored_elements}
    group_bonus = 0.5 * len(unique_groups)

    return {
        "counted_elements": scored_elements,
        "difficulty_score": round(total_difficulty, 2),
        "group_bonus": round(group_bonus, 2),
        "total_d_score": round(total_difficulty + group_bonus, 2)
    }
