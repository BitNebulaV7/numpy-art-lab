import numpy as np  
import matplotlib.pyplot as plt



image = np.zeros((50, 50, 3), dtype=np.uint8)


image[:, :, 0] = np.random.randint(0, 256, (50, 50))  # Red
image[:, :, 1] = np.random.randint(0, 256, (50, 50))  # Green
image[:, :, 2] = np.random.randint(0, 256, (50, 50))  # Blue

image[0:10, 0:10] = [0, 0, 255]
vector = image.reshape(-1)
print(vector)
print("Vector shape:", vector.shape) 

image_back = image.reshape(50,50,3)
print(image_back)
print("Image shape:", image_back.shape) 

transposed = np.transpose(image,(2,0,1))
print("Original shape:", image.shape)     
print("Transposed shape:", transposed.shape) 


rows = [0, 10, 20]
cols = [0, 10, 20]
pixels = image[rows,cols,:]
print("Selected pixels (RGB):")
for i,p in enumerate(pixels):
    print(f"pixel {i + 1} at rows ({rows[i]}, {cols[i]}: {p})")

patch = image[0:10,0:10, :]
print("\nPatch shape:", patch.shape)

mean_color = patch.mean(axis=(0,1))
print("Mean color of patch (RGB):", mean_color.astype(int))

mean_rows = patch.mean(axis=1)
print("Mean color per row (shape):", mean_rows.shape)

mean_cols = patch.mean(axis=0)
print("Mean color per column (shape):", mean_cols.shape)

gray_patch = patch.mean(axis=2)
print("Gray patch shape:", gray_patch.shape)



# pixel = image[10,20,0]
# print("Pixel value:", pixel)

# pixel_1 = image[12,8,0]
# print("pixel 1:",pixel_1)
# pixel_2 = image[0,0,1]
# print("2:",pixel_2)
# pixel_3 = image[49,49,2]
# print("3:", pixel_3)

# pixel_4 = image[49,49,0]
# print(pixel_4)
# pixel_5 = image[25,25,2]
# print(pixel_5)
# pixel_6 = image[1,1,2]
# print(pixel_6)
# patch = image[0:10, 0:10, :]
# print("Patch shape:", patch.shape)


plt.imshow(image)
plt.axis("off")
plt.show()
