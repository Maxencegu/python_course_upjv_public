# hidden_tests_00_python_02.py

def hidden_test_exo1(x, y, sum_result):
    errors = []
    if x != 4 or y != 6:
        errors.append("x should be 4 and y should be 6.")
    if sum_result != x + y:
        errors.append("sum_result is incorrect.")
    return "✅ All tests passed for exercise 1!" if not errors else "❌ " + "\n".join(errors)


def hidden_test_exo2(a, b, c, total, average):
    errors = []

    if a != 5:
        errors.append("Variable `a` must be equal to 5.")
    if b != 10:
        errors.append("Variable `b` must be equal to 10.")
    if c != 15:
        errors.append("Variable `c` must be equal to 15.")
    if total != a + b + c:
        errors.append("Variable `total` must be the sum of a, b, and c.")
    if average != total / 3:
        errors.append("Variable `average` must be the total divided by 3.")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 2!**"



def hidden_test_exo3(age_1, age_2, age_3, category_1, category_2, category_3):
    errors = []

    if age_1 != 15:
        errors.append("age_1 should be 15 (minor)")
    if age_2 != 30:
        errors.append("age_2 should be 30 (adult)")
    if age_3 != 70:
        errors.append("age_3 should be 70 (senior)")

    if category_1 != "Minor":
        errors.append("Expected 'Minor' for age_1 = 15")
    if category_2 != "Adult":
        errors.append("Expected 'Adult' for age_2 = 30")
    if category_3 != "Senior":
        errors.append("Expected 'Senior' for age_3 = 70")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great! All conditions are correctly tested and passed.**"



def hidden_test_exo4(number_1, number_2, number_3, result_1, result_2, result_3):
    errors = []

    if number_1 != 9:
        errors.append("number_1 should be 9 (divisible by 3 and odd)")
    if number_2 != 6:
        errors.append("number_2 should be 6 (divisible by 3 but even)")
    if number_3 != 10:
        errors.append("number_3 should be 10 (not divisible by 3)")

    if result_1 != "Divisible by 3 and odd":
        errors.append("Expected 'Divisible by 3 and odd' for number_1 = 9")
    if result_2 != "Does not meet the condition":
        errors.append("Expected 'Does not meet the condition' for number_2 = 6")
    if result_3 != "Does not meet the condition":
        errors.append("Expected 'Does not meet the condition' for number_3 = 10")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Perfect! You've correctly covered all logical conditions.**"

