from math import isfinite

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)


def read_input():
    return input().split()


def validate_input(parts):
    if len(parts) != 12:
        raise ValueError("Потрібно рівно 12 чисел через пробіл")
    try:
        values = [float(part) for part in parts]
    except ValueError as error:
        raise ValueError("Усі значення мають бути числами; десятковий роздільник — крапка") from error
    if any(not isfinite(value) or value < 0 for value in values):
        raise ValueError("Опади мають бути скінченними невід'ємними числами")
    return values


def calculate(values):
    total = sum(values)
    maximum = max(values)
    minimum = min(values)
    return (total, total / 12,
            (maximum, MONTHS[values.index(maximum)]),
            (minimum, MONTHS[values.index(minimum)]))


def show_result(result):
    print(result)


def main():
    try:
        values = validate_input(read_input())
        show_result(calculate(values))
    except ValueError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()
