def sort_list(my_list, direction=None):
    """Сортировка списка my_list методом пузырька.
    :param my_list: список значений
    :param direction: (опциональный) направление сортировки. Возможные значения: 1, -1
    """
    if direction:
        for i in range(len(my_list)):
            for j in range(i, len(my_list)):
                if (direction == -1 and my_list[i] > my_list[j]) or (direction == 1 and my_list[i] < my_list[j]):
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp

    return my_list


print(sort_list([1, 2, 3]))
