import time
import random


def init_list():
    list = []
    for i in range(1000):
        random_int = random.randint(0, 9)
        list.append(random_int)
    return list


def print_list(list):
    for i in list:
        print(i, end=" ")
    print("\n")


def alg_babelkowy(list):
    restart = True
    while restart:
        restart = False
        for i in range(len(list)-1):
            if list[i+1] < list[i]:
                list[i+1], list[i] = list[i], list[i+1]
                restart = True
                break
    return list


def selection_sort(list):
    for i in range(0, len(list)):
        smallest = 11
        index = 0
        for j in range(i, len(list)):
            if list[j] < smallest:
                smallest = list[j]
                index = j
        list[index] = list[i]
        list[i] = smallest
    return list


def quicksort(list):
    if not list:
        return list
    pivot = list[random.choice(range(0, len(list)))]
    front = quicksort([item for item in list if item < pivot])
    back = quicksort([item for item in list if item > pivot])
    quicksort_list = front + [item for item in list if item == pivot] + back
    return quicksort_list


start_list = init_list()
print("Lista podstawowa:")
print_list(start_list)

start = time.clock()
alg_babelkowy_list = alg_babelkowy(start_list)
end = time.clock()
print("Lista posortowana algorytmem bąbelkowym:")
print_list(alg_babelkowy_list)
print("Czas wykonywania algorytmu babelkowego: ", end-start, "s\n")

start = time.clock()
selection_sort_list = selection_sort(start_list)
end = time.clock()
print("Lista posortowana metodą 'selection sort':")
print_list(selection_sort_list)
print("Czas wykonywania metody 'selection sort':", end-start, "s\n")

start = time.clock()
quicksort_list = quicksort(start_list)
end = time.clock()
print("Lista posortowana metodą 'quicksort':")
print_list(quicksort_list)
print("Czas wykonywania metody 'quicksort':", end-start, "s\n")
