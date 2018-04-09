#smallest number in the given list. program is as readable as posible
list = [42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21]
smallest = list[0]
for i in list:
    if i < smallest:
        smallest = i
        print("readable:",smallest)

#smallest number using in built function. program as efficient as possible
lst = [42,49, 86, 143, 234, 334, 401, 435, 2, 14, 21]
print("fastest smallest",min(lst))


#smallest number using functions. program is extendable and flexible
def smallest(my_list):
    start = my_list[0]
    for number in my_list:
        if number < start:
            start = number
    return start
my_list = [42,49, 86, 143, 234, 334, 401, 435, 2, 14, 21]
print("extendable and flexible:",smallest(my_list))

