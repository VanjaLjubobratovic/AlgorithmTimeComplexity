import random
import time
import json
class MatrixMultiplication:
    def MatrixMulti(A, B):
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

    def generate_random_matrix(n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = random.randint(0, 100) 
        return matrix

    def generate_testcases(low, high, step):
        data = []
        while low < high:
            size_n = low
            mat = MatrixMultiplication.generate_random_matrix(size_n)
            data.append(mat)
            low += step
        return data
    
    #DEPRECATED FUNCTION, no longer reading test cases from json file
    def read_testcases():
        test_cases = []
        with open("MatrixTestCases.txt") as fp:
            data = json.load(fp)
        for i in data['Matrices']:
            test_cases.append(i['Matrix'])
        return test_cases

    def generate_results(test_cases):
        data = {}
        data["Results"] = []
        for i in test_cases:
            begin = time.perf_counter()
            mat = MatrixMultiplication.MatrixMulti(i,i)
            end = time.perf_counter()
            data["Results"].append({
                    "Size": len(i[0]),
                    "Time": (end - begin),
                })
        with open("MatrixResults.txt", "w") as outfile:
            json.dump(data, outfile)


def main():
    test_cases = MatrixMultiplication.generate_testcases(2,50,2)
    begin = time.perf_counter()
    MatrixMultiplication.generate_results(test_cases)
    end = time.perf_counter()
    print(f"Generation finished in: {end - begin:0.4f}s")

if __name__ == "__main__":
    main()

