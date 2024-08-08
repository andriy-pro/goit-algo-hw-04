import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    # Купа для зберігання перших елементів кожного списку
    min_heap = []
    # Список для зберігання результату злиття
    result = []

    # Додаємо перший елемент кожного списку в купу разом з індексами списку та елемента
    for i, lst in enumerate(lists):  # Проходимо по кожному списку
        if lst:  # Перевіряємо, чи список не порожній

            # Значення, індекс списку, індекс елемента
            heapq.heappush(min_heap, (lst[0], i, 0))
            # print(f"\033[1;30mСписки: {lists}\033[0m")
            # print(
            #     f"\033[1;34mДодано до купи: значення {lst[0]} з списку {i}, індекс елемента {0}\033[0m"
            # )
            # print(f"\033[0;32mКупа: {min_heap}\033[0m")

    # Поки в купі є елементи, витягуємо мінімальний елемент і додаємо його до злитого списку
    while min_heap:
        # Отримуємо найменший елемент з купи
        value, list_index, element_index = heapq.heappop(min_heap)
        # Додаємо його до списку-результату
        result.append(value)
        # print(f"\033[1;30mСписки: {lists}\033[0m")
        # print(
        #     f"\033[0;33mВийнято з купи: значення {value} з списку {list_index}, індекс елемента {element_index}\033[0m"
        # )
        # print(f"\033[0;32mКупа: {min_heap}\033[0m")
        # print(f"Проміжний результат: {result}")

        # Додаємо до купи наступний елемент з того ж списку, з якого був вибраний поточний елемент.
        # Перевіряємо, чи ми не вишли за межі поточного списку
        if element_index + 1 < len(lists[list_index]):
            # Отримуємо наступний елемент
            next_value = lists[list_index][element_index + 1]
            # Додаємо його до купи
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
            # print(f"\033[1;30mСписки: {lists}\033[0m")
            # print(
            #     f"\033[1;34mДодано до купи: значення {next_value} з списку {list_index}, індекс елемента {element_index + 1}\033[0m"
            # )
            # print(f"\033[0;32mКупа: {min_heap}\033[0m")

    return result


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
result = merge_k_lists(lists)
print("\033[1;37mВідсортований список:\033[0m", result)
# Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
