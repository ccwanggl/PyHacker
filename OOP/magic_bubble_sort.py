def magic_bubble_sort(numbers:List[int]):
    """
    有魔力的冒泡排序算法，默认所有的偶数都比奇数大
    :param numbers: 需要排序的列表，函数直接修改原始列表
    :return: 返回最大的数
    """
    stop_position = len(numbers)-1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i+1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False

            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i+1] = numbers[i + 1], numbers
                stop_position -= 1
    return numbers