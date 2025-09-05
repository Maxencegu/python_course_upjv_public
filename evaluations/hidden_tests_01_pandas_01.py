import pandas as pd

def hidden_test_exo1(df):
    errors = []
    if not isinstance(df, pd.DataFrame):
        errors.append("df must be a DataFrame.")
    expected_names = ["Arnold", "Willy", "Max"]
    expected_ages = [55, 60, 33]
    if list(df["Name"]) != expected_names:
        errors.append("Column 'Name' must contain ['Arnold', 'Willy', 'Max'].")
    if list(df["Age"]) != expected_ages:
        errors.append("Column 'Age' must contain [55, 60, 33].")
    return "✅ Exercise 1 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo2(df_csv):
    errors = []
    expected_names = ["Arnold", "Willy", "Max", "Alice", "Bob", "Charlie"]
    expected_scores = [55, 60, 33, 85, 90, 78]
    if not isinstance(df_csv, pd.DataFrame):
        errors.append("df_csv must be a DataFrame.")
    if list(df_csv["Name"]) != expected_names:
        errors.append("Column 'Name' must contain ['Arnold', 'Willy', 'Max', 'Alice', 'Bob', 'Charlie'].")
    if list(df_csv["Score"]) != expected_scores:
        errors.append("Column 'Score' must contain [55, 60, 33, 85, 90, 78].")
    return "✅ Exercise 2 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo3(names, row_1, filtered):
    errors = []
    if list(names) != ["Arnold", "Willy", "Max", "Alice", "Bob", "Charlie"]:
        errors.append("names must be ['Arnold', 'Willy', 'Max', 'Alice', 'Bob', 'Charlie'].")
    if list(row_1) != ["Willy", 60]:
        errors.append("row_1 must correspond to Willy, 60.")
    filtered_ages = list(filtered["Score"])
    if filtered_ages != [60, 85, 90, 78]:
        errors.append("filtered must contain scores greater than 58: [60, 85, 90, 78].")
    return "✅ Exercise 3 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo4(summary, mean_score):
    errors = []
    expected_scores = [55, 60, 33, 85, 90, 78]
    expected_mean = sum(expected_scores)/len(expected_scores)
    if not abs(mean_score - expected_mean) < 1e-9:
        errors.append(f"mean_score must be {expected_mean}.")
    if summary["min"] != 33 or summary["max"] != 90:
        errors.append("Summary min/max values incorrect.")
    return "✅ Exercise 4 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)




