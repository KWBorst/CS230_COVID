from PIL import Image
import numpy as np

july_matrices = []
dec_matrices = []
may_matrices = []
march_matrices = []

for i in range(50):
        im1 = Image.open("/Users/kevinborst/CS230/CS230_COVID/images/" + str(i+1) + " 7:9:20.png")
        july_matrix = np.array(im1)
        july_matrices.append(july_matrix)
        im2 = Image.open("/Users/kevinborst/CS230/CS230_COVID/images/" + str(i+1) + " 12:17:20.png")
        dec_matrix = np.array(im2)
        dec_matrices.append(dec_matrix)
        im3 = Image.open("/Users/kevinborst/CS230/CS230_COVID/images/" + str(i+1) + " 5:22:21.png")
        may_matrix = np.array(im3)
        may_matrices.append(may_matrix)
        im4 = Image.open("/Users/kevinborst/CS230/CS230_COVID/images/" + str(i+1) + " 3:8:22.png")
        march_matrix = np.array(im4)
        march_matrices.append(march_matrix)

for i in range(50):
	np.save("/Users/kevinborst/CS230/CS230_COVID/matrices/" + str(i+1) + " 7:9:20", july_matrices[i])
	np.save("/Users/kevinborst/CS230/CS230_COVID/matrices/" + str(i+1) + " 12:17:20", dec_matrices[i])
	np.save("/Users/kevinborst/CS230/CS230_COVID/matrices/" + str(i+1) + " 5:22:21", may_matrices[i])
	np.save("/Users/kevinborst/CS230/CS230_COVID/matrices/" + str(i+1) + " 3:8:22", march_matrices[i])
