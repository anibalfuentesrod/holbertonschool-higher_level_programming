#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            numerator = my_list_1[i]
            denominator = my_list_2[i]
            try:
                result.append(float(numerator) / float(denominator))
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except ValueError:
                print("wrong type")
                result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
