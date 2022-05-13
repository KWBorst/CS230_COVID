from PIL import Image
import numpy as np

matrices2021 = []
matrices2022 = []
input_matrices = []

for i in range(20):
        im1 = Image.open("/Users/kevinborst/CS230/CS230_COVID/images/" + str(i+1) + " 2021.png")
        matrix2021 = np.array(im1)
        matrices2021.append(matrix2021)
        im2 = Image.open("/Users/kevinborst/CS230/CS230_COVID//images/" + str(i+1) + " 2022.png")
        matrix2022 = np.array(im2)
        matrices2022.append(matrix2022)
        input_matrix = np.absolute(matrix2022 - matrix2021)
        input_matrix = input_matrix * (input_matrix >= 200)
        input_matrices.append(input_matrix)

np.save("/Users/kevinborst/CS230/CS230_COVID/2021", matrices2021)
np.save("/Users/kevinborst/CS230/CS230_COVID/2022", matrices2022)
np.save("/Users/kevinborst/CS230/CS230_COVID/input", input_matrices)
