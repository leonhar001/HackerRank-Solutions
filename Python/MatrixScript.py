#!/bin/python3
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = '' #output string

for i in range(m): #initial decoded script 
    for j in range(n):
        string += matrix[j][i] 

string = re.sub(r'(?<=[a-zA-z0-9])([^a-zA-z0-9]+)(?=[a-zA-z0-9])', r' ', string) #matches just special characters between alphanumeric and replace they to whitespace

print(string)
