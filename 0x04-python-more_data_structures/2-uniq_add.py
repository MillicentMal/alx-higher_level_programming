#!/usr/bin/python3
def uniq_add(my_list=[]):                      
    unique_list = []                           
    i = len(my_list) - 1                       
                                               
    while i > 1:                               
        j = 0                                  
        while j < i:                           
        # If the value on the left is bigger sw
            if my_list[j] > my_list[j+1]:      
                                               
                temp = my_list[j]              
                my_list[j] = my_list[j+1]      
                my_list[j+1] = temp            
            else:                              
                 j += 1                        
        i -= 1                                 
    print(my_list)                             
                                               
    k = len(my_list) - 1                       
    while k >= 0:                              
        if my_list[k] != my_list[k-1]:         
            unique_list.append(my_list[k])     
        k -= 1                                 
                                               
    m = 0                                      
    result = 0                                 
    while m != len(unique_list):               
        result = result + unique_list[m]       
        m += 1                                 
    return result                              
