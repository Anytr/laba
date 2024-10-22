numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
miss_ind = numbers.index(None)
numbers_none = [num for num in numbers if num is not None]
average = round(sum(numbers_none) / len(numbers_none), 2)
average = round((average + 0.82), 2)
numbers[miss_ind] = average # TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)