array_cord = list(map(int, input().split()))

for i in range(len(array_cord)):
    if array_cord[i] <= 0:
        print('Вы ввели отрицательное значение или 0')
        exit()

def square(a, b, c):
    permit = 0.5 * (a + b + c)
    return (permit * (permit - a) * (permit - b) * (permit - c)) ** 0.5


def treyg(a, b, c):
    return a + b > c and b + c > a and a + c > b

max_square = 0
cord = []

for a in range(len(array_cord)):
    for b in range(len(array_cord)):
        for c in range(len(array_cord)):
            if a != b and b != c and a != c:
                if treyg(array_cord[a], array_cord[b], array_cord[c]):
                    new_square = square(array_cord[a], array_cord[b], array_cord[c])
                    new_square = int(new_square * 100) / 100
                    if new_square > max_square:
                        max_square = new_square
                        cord = array_cord[a], array_cord[b], array_cord[c]

print(f"Результат: \nСтороны треугольника с наибольшей площадью = {cord} \nПлощадь = {max_square}")

