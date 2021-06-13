def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]

        except TypeError:
            print("Wrong type")
            result = 0
        except ZeroDivisionError:
            print("Division by zero")
            result = 0
        except IndexError:
            print("Out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
