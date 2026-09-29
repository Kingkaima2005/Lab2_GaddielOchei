# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


# Fill in the body of each function below (look for the TODO comments).


def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return f"{hours}:{minutes:02d}:{seconds:02d}"


def admission_price(age):
    if age < 5:
        return 0.0
    elif age <= 12:
        return 8.0
    elif age <= 64:
        return 15.0
    else:
        return 10.0


def sum_multiples(limit):
    total = 0

    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number

    return total


def total_of_positives(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number

    return total


def main():
    # Optional testing
    # print(seconds_to_hms(3661))
    # print(admission_price(10))
    # print(sum_multiples(10))
    # print(total_of_positives([1, -2, 3]))
    pass


if __name__ == "__main__":
    main()