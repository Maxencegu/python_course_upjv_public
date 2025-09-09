# hidden_tests_00_python_03.py

def hidden_test_exo1(my_numbers, the_sum):
    errors = []
    if my_numbers != [1, 3, 4, 5, 6]:
        errors.append("`numbers` must be [1, 3, 4, 5, 6].")
    if the_sum != sum(my_numbers):
        errors.append("`total` must be the sum of all elements in numbers.")
    return "✅ Exercise 1 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo2(n, multiples):
    errors = []
    if n != 7:
        errors.append("`n` must be equal to 7.")
    expected = [n * i for i in range(1, 16)]
    if multiples != expected:
        errors.append("`multiples` must contain the multiplication table of 7 from 1 to 15.")
    return "✅ Exercise 2 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo3(the_values):
    errors = []
    expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    if the_values != expected:
        errors.append("`values` must contain the sequence [2, 4, ..., 20].")
    return "✅ Exercise 3 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo4(limit, num_primes):
    errors = []
    if limit != 20:
        errors.append("`limit` must be equal to 20.")
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    if num_primes != expected:
        errors.append("`primes` must contain the prime numbers up to 20.")
    return "✅ Exercise 4 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)
