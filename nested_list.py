def count_leaves(input_list):
    if len(input_list) == 0:
        return
    else:
        counter = 0
        for element in input_list:
            if type(element) == list:
                counter = counter + count_leaves(element)
            else:
                counter = counter + 1
        return counter

names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
print(names)
c = count_leaves(names)
print(c)