from routine_logic import calculate_h5_score

# Example routine with valid element names from your CSV
test_routine = [
    "Iron Cross",
    "Maltese Cross",
    "Back Uprise to Handstand",
    "Jonasson",
    "Dismount – Double Layout",
    "Planche",  # Extra element to check top 5 selection
    "Iron Cross"  # Duplicate – should be ignored
]

result = calculate_h5_score(test_routine)

print("Scoring Breakdown:")
print(f"  Counted Elements: {result['counted_elements']}")
print(f"  Difficulty Score: {result['difficulty_score']}")
print(f"  Group Bonus: {result['group_bonus']}")
print(f"  Total D-Score: {result['total_d_score']}")