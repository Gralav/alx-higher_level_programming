#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    numb1 = 0
    numb2 = 0
    for i in tuple_a:
        if i == tuple_a[0]:
             numb1 = numb1 + i
         elif i == tuple_a[1]:
             numb2 = numb2 + i
             for j in tuple_b:
                 if j == tuple_b[0]:
                     numb1 = numb1 + j
                 elif j == tuple_b[1]:
                     numb2 = numb2 + j
                     return (numb1, numb2)
             
