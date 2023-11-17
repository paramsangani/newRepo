from sparse_recommender import Sparse

def test_setMatrix():
    matrix = Sparse()
    matrix.set(0, 0, 4)
    matrix.set(0, 1, 3)
    matrix.set(1, 0, 6)
    matrix.set(1, 1, 2)
    assert matrix.get(1, 0) == 6
    assert matrix.get(0, 3) == 0

def test_getMatrix():
    matrix = Sparse()
    matrix.set(0, 0, 9)
    matrix.set(0, 1, 8)
    matrix.set(1, 0, 7)
    matrix.set(1, 1, 6)
    assert matrix.get(0, 0) == 9
    assert matrix.get(3, 1) == 0 #testing edge case that is not set

def test_recommendMatrix():
    matrix = Sparse()
    matrix.set(0, 0, 4)
    matrix.set(0, 1, 3)
    matrix.set(1, 0, 6)
    matrix.set(1, 1, 2)
    assert matrix.recommend([0,6]) == {0: 18, 1: 12}
    assert matrix.recommend([2,3]) == {0: 17, 1: 18}
    assert matrix.recommend([4,8,5]) == {0: 40, 1: 40}

def test_to_dense():
    matrix = Sparse()
    matrix.set(0, 0, 4)
    matrix.set(0, 1, 3)
    matrix.set(1, 0, 6)
    matrix.set(1, 1, 2)
    matrix.set(1, 5, 5) #testing edge case here
    assert matrix.to_dense() == [[4, 3, 0], [6, 2, 5]]    


def test_add_movie():
    matrix = Sparse()
    matrix.set(0, 0, 4)
    matrix.set(0, 1, 3)
    matrix.set(1, 0, 6)
    matrix.set(1, 1, 2)
    matrixNew = Sparse()
    matrixNew.set(0, 2, 4)
    matrixNew.set(0, 3, 9)
    result = matrix.add_movie(matrixNew)
    assert result.get(0, 1) == 3
    assert result.get(0, 2) == 4
    assert result.get(0, 3) == 9
    
    
def test_add_movie():
    matrix1 = Sparse()
    matrix1.set(1, 1, 3)
    matrix2 = Sparse()
    matrix2.set(1, 1, 2)
    result_matrix = matrix1.add_movie(matrix2)
    assert result_matrix.get(1, 1) == 5

