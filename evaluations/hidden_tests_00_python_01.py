# hidden_tests_00_python_01.py
import re

def hidden_test_exo1(first_name, age, message):
    errors = []

    if not isinstance(first_name, str) or first_name.strip() == "":
        errors.append("first_name must be a non-empty string.")
    elif re.search(r'\d', first_name):
        errors.append("first_name must not contain digits.")

    if not isinstance(age, int) or not (16 <= age <= 25):
        errors.append("age must be an integer between 16 and 25.")

    expected_message = f"Hello, my name is {first_name} and I am {age} years old."
    if not isinstance(message, str) or message != expected_message:
        errors.append(f"message is incorrect. Expected: '{expected_message}'")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Congratulations, all tests passed!**"


def hidden_test_exo2(a, b, c, total, average):
    errors = []
    if (a, b, c) != (5, 10, 15):
        errors.append("Variables a, b, c must be 5, 10, 15 respectively.")
    if total != a + b + c:
        errors.append("Incorrect total value.")
    if average != total / 3:
        errors.append("Incorrect average value.")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 2!**"


def hidden_test_exo3(message, length):
    errors = []
    expected_message = "Python for Data Science"
    expected_length = len(expected_message)

    if message != expected_message:
        errors.append(f"text must be exactly: '{expected_message}'.")
    if length != expected_length:
        errors.append(f"length must be {expected_length} (the length of the text).")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great! All tests passed for exercise 3!**"


def hidden_test_exo4(number_1, number_2, sum_result, diff_result, prod_result, quot_result, rem_result):
    errors = []

    if number_1 != 7 or number_2 != 3:
        errors.append("Variables number_1 and number_2 must be 7 and 3 respectively.")

    if sum_result != number_1 + number_2:
        errors.append("Incorrect sum_result value.")
    if diff_result != number_1 - number_2:
        errors.append("Incorrect diff_result value.")
    if prod_result != number_1 * number_2:
        errors.append("Incorrect prod_result value.")
    if quot_result != number_1 / number_2:
        errors.append("Incorrect quot_result value (should be division).")
    if rem_result != number_1 % number_2:
        errors.append("Incorrect rem_result value (should be modulo).")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 4!**"


def hidden_test_exo5(colors):
    errors = []

    if not isinstance(colors, list):
        errors.append("`colors` must be a list.")
    else:
        expected = ["red", "black", "green", "grey"]
        if colors != expected:
            errors.append(f"`colors` list is incorrect. Expected: {expected}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great job! Exercise 5 passed successfully!**"


def hidden_test_exo6(numbers, even_numbers):
    errors = []

    if not isinstance(numbers, list):
        errors.append("`numbers` must be a list.")
    else:
        expected_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if numbers != expected_numbers:
            errors.append(f"`numbers` list is incorrect. Expected: {expected_numbers}")

    if not isinstance(even_numbers, list):
        errors.append("`even_numbers` must be a list.")
    else:
        expected_even = [2, 4, 6, 8, 10]
        if even_numbers != expected_even:
            errors.append(f"`even_numbers` list is incorrect. Expected: {expected_even}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great job! Exercise 6 passed successfully!**"


def hidden_test_exo7(numbers, sum_of_numbers):
    errors = []
    expected_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 15]

    if numbers != expected_list:
        errors.append(f"List 'numbers' is incorrect. Expected {expected_list}")

    if sum_of_numbers != sum(expected_list):
        errors.append(f"Sum 'sum_of_numbers' is incorrect. Expected {sum(expected_list)}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 7!**"


def hidden_test_exo8(values, squared, average):
    errors = []

    expected_values = [4, 8, 15, 16, 23, 42]
    expected_squared = [16, 64, 100]  # Squares under or equal 200 + appended 100
    expected_average = sum(expected_squared) / len(expected_squared)

    # Check values list unchanged
    if values != expected_values:
        errors.append(f"'values' list must be {expected_values}")

    # Check squared list content
    if sorted(squared) != sorted(expected_squared):
        errors.append(f"'squared' list is incorrect. Expected elements {expected_squared}")

    # Check average
    if not (abs(average - expected_average) < 1e-6):
        errors.append(f"'average' value is incorrect. Expected {expected_average}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Excellent! All tests passed for exercise 8!**"


def hidden_test_exo9(person):
    errors = []
    if not isinstance(person, dict):
        errors.append("person must be a dictionary.")
    else:
        if person.get("name") != "Alice":
            errors.append("person['name'] must be 'Alice'.")
        if person.get("age") != 20:
            errors.append("person['age'] must be 20.")
        if person.get("city") != "Paris":
            errors.append("person['city'] must be 'Paris'.")
    if errors:
        return "❌ **Tests failed:**\n- " + "\n- ".join(errors)
    return "✅ **Exercise 9 passed successfully!**"


def hidden_test_exo10(grades, average):
    errors = []
    if not isinstance(grades, dict):
        errors.append("grades must be a dictionary.")
    else:
        expected = {"math":85, "science":90, "history":78, "english":88}
        for k, v in expected.items():
            if grades.get(k) != v:
                errors.append(f"grades['{k}'] must be {v}.")
    expected_avg = sum(expected.values()) / len(expected)
    if average != expected_avg:
        errors.append(f"average must be {expected_avg}.")
    if errors:
        return "❌ **Tests failed:**\n- " + "\n- ".join(errors)
    return "✅ **Exercise 10 passed successfully!**"


def hidden_test_exo11(inventory, removed_quantity):
    errors = []
    if not isinstance(inventory, dict):
        errors.append("inventory must be a dictionary.")
    else:
        expected_inventory = {"apples": 15, "bananas": 8}
        for k, v in expected_inventory.items():
            if inventory.get(k) != v:
                errors.append(f"inventory['{k}'] must be {v}.")
    if removed_quantity != 3:
        errors.append("removed_quantity must be 3.")
    if errors:
        return "❌ **Tests failed:**\n- " + "\n- ".join(errors)
    return "✅ **Exercise 11 passed successfully!**"


def hidden_test_exo12(students, avg_math_grade):
    errors = []
    if not isinstance(students, dict):
        errors.append("students must be a dictionary.")
    else:
        expected_keys = {"John", "Emma", "Lucas", "Sophia"}
        if set(students.keys()) != expected_keys:
            errors.append(f"students keys must be {expected_keys}.")
        for student in expected_keys:
            if not isinstance(students[student], dict):
                errors.append(f"students['{student}'] must be a dictionary.")
        expected_grades = {
            "John": {"math":85, "science":92},
            "Emma": {"math":78, "science":88},
            "Lucas": {"math":90, "science":95},
            "Sophia": {"math":82, "science":91}
        }
        for student, grades in expected_grades.items():
            if students.get(student) != grades:
                errors.append(f"grades for '{student}' are incorrect.")
    expected_avg = (85 + 78 + 90 + 82) / 4
    if avg_math_grade != expected_avg:
        errors.append(f"avg_math_grade must be {expected_avg}.")
    if errors:
        return "❌ **Tests failed:**\n- " + "\n- ".join(errors)
    return "✅ **Exercise 12 passed successfully!**"
