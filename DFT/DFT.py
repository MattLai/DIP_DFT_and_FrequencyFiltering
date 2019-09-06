# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import numpy as np

class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""

        height, width = matrix.shape
        resultMatrix = [[0 for k in range(height)] for l in range(width)]

        for rowIndex in range(height):
            for columnIndex in range(width):
                eachLocation = 0
                for row in range(height):
                    for column in range(width):
                        eachLocation += matrix[row, column] * np.exp(- 1j * 2 * np.pi * (rowIndex * row / height + columnIndex * column / width))
                resultMatrix[rowIndex][columnIndex] = eachLocation/height/width

        return np.array(resultMatrix)

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""

        height, width = matrix.shape
        resultMatrix = [[0 for k in range(height)] for l in range(width)]
        resultMatrix = np.array(resultMatrix)

        for rowIndex in range(height):
            for columnIndex in range(width):
                eachLocation = 0
                for row in range(height):
                    for column in range(width):
                        eachLocation += matrix[row][column] * np.exp(1j * 2 * np.pi * (rowIndex * row / height + columnIndex * column / width))
                resultMatrix[rowIndex, columnIndex] = (eachLocation.real + (1/2))

        return resultMatrix


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""

        height, width = matrix.shape
        resultMatrix = [[0 for k in range(height)] for l in range(width)]

        for rowIndex in range(height):
            for columnIndex in range(width):
                eachLocation = 0
                for row in range(height):
                    for column in range(width):
                        eachLocation += matrix[row, column] * (np.cos((2 * np.pi * (rowIndex * row / height + columnIndex * column / width))))
                resultMatrix[rowIndex][columnIndex] = eachLocation / height / width

        return np.array(resultMatrix)


    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""

        height, width = matrix.shape
        resultRealMatrix = [[0 for k in range(height)] for l in range(width)]
        resultImageMatrix = [[0 for k in range(height)] for l in range(width)]
        resultMatrix = [[0 for k in range(height)] for l in range(width)]

        for rowIndex in range(height):
            for columnIndex in range(width):
                eachLocationReal = 0
                eachLocationImage = 0
                for row in range(height):
                    for column in range(width):
                        #  sqrt times
                        eachLocationReal += matrix[row, column] * (
                            np.cos((2 * np.pi * (rowIndex * row / height + columnIndex * column / width))))
                        eachLocationImage += (-matrix[row, column] * (
                            np.sin((2 * np.pi * (rowIndex * row / height + columnIndex * column / width)))))
                resultRealMatrix[rowIndex][columnIndex] = eachLocationReal / height / width
                resultImageMatrix[rowIndex][columnIndex] = eachLocationImage /height / width
                resultMatrix[rowIndex][columnIndex] = np.sqrt(np.square(resultRealMatrix[rowIndex][columnIndex]) +
                                                              np.square(resultImageMatrix[rowIndex][columnIndex]))

        return np.array(resultMatrix)

        # return matrix