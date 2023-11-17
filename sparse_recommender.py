class Sparse:
    def __init__(self):
        self.data = {}

    def set(self, row, col, value):
        #Sets the value at (row, col) to value.
        if row not in self.data:
            self.data[row] = {}
        self.data[row][col] = value
        # set(row, col, value): Sets the value at (row, col) to value

    def get(self, row, col):
        #Returns the value at (row, col).
        return self.data.get(row, {}).get(col, 0)
        # get(row, col): Returns the value at (row, col).

    # recommend(vector): Multiplies the sparse matrix with a given vector to produce
    # recommendations, and return the result
    def recommend(self, vector):
        result = {}
        for row in self.data:
            result[row] = sum(self.get(row, col) * vector[col] for col in self.data[row])
        return result
    
    # add_movie(matrix): Adds another sparse matrix, simulating the addition of a new
    # movie to the service, and return the result.
    def add_movie(self, matrix):
        result = Sparse()

        all_rows = set(self.data.keys()) | set(matrix.data.keys())
        all_cols = set(col for row in all_rows for col in set(self.data.get(row, {})) | set(matrix.data.get(row, {})))

        for row in all_rows:
            result.data[row] = {}
            for col in all_cols:
                result.set(row, col, self.get(row, col) + matrix.get(row, col))

        return result

    # to_dense(): Converts the sparse matrix to a dense matrix and return it.
    def to_dense(self):
        rows = sorted(self.data)
        columns = sorted(set(col for row in self.data.values() for col in row))
        
        dense_matrix = []
        for row in rows:
            dense_row = [self.get(row, col) for col in columns]
            dense_matrix.append(dense_row)
        
        return dense_matrix


