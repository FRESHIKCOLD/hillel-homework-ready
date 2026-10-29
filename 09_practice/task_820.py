import sys


class Buffer:
    def __init__(self):
        self._part = []

    def add(self, *a):
        for number in a:
            self._part.append(number)
            if len(self._part) == 5:
                print(sum(self._part))
                self._part.clear()

    def get_current_part(self):
        return self._part.copy()


if __name__ == "__main__":
    buffer = Buffer()
    # Кожен рядок — наступна порція чисел. Порожній рядок завершує ввід.
    for line in sys.stdin:
        if not line.strip():
            break
        buffer.add(*map(int, line.split()))
        print(buffer.get_current_part())
