#!/usr/bin/python3
# Python code to convert string to list
def roman_to_int(roman_string):
    roman_number = []
    if roman_string == None and type(roman_string) != str:
        return 0

    for roman in roman_string:
        roman_number.append(roman)

    roman_to_int = 0
    for roman in roman_number:
        i = len(roman_string)
        while i => 0:
            i -= 1
            if roman_string[i -1] == 'I' & roman_string[i] != 'I':
                roman_to_int -= 1
            else:
                
                if roman == 'I':
                    roman_to_int += 1
                elif roman == 'V':
                    roman_to_int += 5
                elif roman == 'X':
                    roman_to_int += 10
                elif roman == 'L':
                    roman_to_int += 50
                elif roman == 'C':
                    roman_to_int += 100
                elif roman == 'D':
                    roman_to_int += 500
                elif roman == 'M':
                    roman_to_int += 1000
                
     
    return roman_to_int
