import matplotlib.pyplot as plt

im = plt.imread('matplotlib.png')
plt.imshow(im)
im
above_mean = im > im.mean()
plt.imshow(above_mean.astype(float))