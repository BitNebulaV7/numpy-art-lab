# NumPy Art Lab 🎨

An educational project to learn NumPy fundamentals by creating and manipulating a mini RGB image.

## 🎯 Project Goals

This project helps you:

- Understand array shapes and multidimensional arrays
- Practice broadcasting
- Work with indexing and slicing
- Modify data using conditions
- Visualize results with `matplotlib`

---

## 🧩 Project Steps

1. Create a base image

   - Build a 3D array with shape `(50, 50, 3)` representing an RGB image.

2. Generate random colors

   - Fill each pixel with random values between 0 and 255.

3. Modify a specific region

   - Turn the top-left 10×10 pixel block completely blue.

4. Increase brightness

   - Add a constant value to the entire array using broadcasting.
   - Use `np.clip` to keep values between 0 and 255.

5. Display the image
   - Show the result using `matplotlib`.

---

## 📦 Installation & Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
