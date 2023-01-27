from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления'
                ' квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Вывод корней."""
    if your_number <= 0:
        return 'Нет вещественных корней'
    root = calculate_square_root(your_number)
    return (
        f'Мы вычислили квадратный корень из введённого вами числа.'
        f'Это будет: {root}'
    )


calc(25.5)
