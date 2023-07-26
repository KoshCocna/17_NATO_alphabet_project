with open("file1.txt") as data1, open("file2.txt") as data2:
    numbers1 = data1.read().split('\n')
    numbers2 = data2.read().split('\n')

    numbers_list1 = [int(_) for _ in numbers1 if _ != '']
    print(numbers_list1)
    numbers_list2 = [int(_) for _ in numbers2 if _ != '']
    print(numbers_list2)

    result = [res for res in numbers_list1 if res in numbers_list2]
    result = list(dict.fromkeys(result))

    print(result)
