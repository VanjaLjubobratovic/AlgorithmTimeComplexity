import random
import time
import numpy
import json
def MatrixMultiplication(A, B):
    if(len(A[0]) != len(B)):
        return "Invalid matrix dimensions"
    result = [[0 for i in range(len(A[0]))] for j in range(len(B[0]))]

    # iterating by row of A
    for i in range(len(A)):

	    # iterating by column by B
        for j in range(len(B[0])):

		    # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]                        
    return result

def Generate_random_matrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(0, 100) 
    return matrix

def generate_testcases(low, high, step):
        data = {}
        data["Matrices"] = []

        while low < high:
            size_n = low
            g = Generate_random_matrix(size_n)
            data["Matrices"].append({
                "Size": size_n,
                "Matrix": g,
            })
            low += step

        with open("MatrixTestCases.txt", "w") as outfile:
            json.dump(data, outfile)

def Read_testcases():
    test_cases = []
    with open("MatrixTestCases.txt") as fp:
        data = json.load(fp)
    for i in data['Matrices']:
        test_cases.append(i['Matrix'])
    return test_cases



#generate_testcases(2,50,1)
test_cases = Read_testcases()
for i in test_cases:
    begin = time.perf_counter()
    mat = MatrixMultiplication(i,i)
    end = time.perf_counter()
    print(f"Time to execute: {end - begin:0.7f} s")

