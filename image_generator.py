import numpy as np  
import matplotlib.pyplot as plt



image = np.zeros((50, 50, 3), dtype=np.uint8)


image[:, :, 0] = np.random.randint(0, 256, (50, 50))  # Red
image[:, :, 1] = np.random.randint(0, 256, (50, 50))  # Green
image[:, :, 2] = np.random.randint(0, 256, (50, 50))  # Blue

image[0:10, 0:10] = [0, 0, 255]

plt.imshow(image)
plt.axis("off")
plt.show()
