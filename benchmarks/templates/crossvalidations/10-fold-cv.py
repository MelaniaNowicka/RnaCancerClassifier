

import random
import interfaces


def generator(Matrix):
    assert(len(Matrix)>=10)

    matrix = list(Matrix)
    random.shuffle(matrix)

    chunk_size, remainder = divmod(len(Matrix),10)
    
    chunks = [matrix[i*chunk_size:(i+1)*chunk_size] for i in range(10-remainder)]
    chunks+= [matrix[i*chunk_size:(i+1)*chunk_size+1] for i in range(10-remainder,10)]

    for i in range(10):
        learningset = [y for x in chunks if not chunks.index(x)==i for y in x]
        testdata = chunks[i]


        yield learningset, testdata
                   

def get_error(FunctionAnnotation, FunctionSolution, TestData):

    error = 0
    for row in TestData:
        row = interfaces.files.row2dict(row)
        
        if FunctionAnnotation(row)==FunctionSolution(row):
            error+=1

    return error


def get_generalization_error(TotalError, Matrix):

    return 1.*TotalError / len(Matrix)