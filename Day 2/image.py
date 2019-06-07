import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='This is...')
parser.add_argument('image')
parser.add_argument('image_out')



im = plt.imread('GFPneuron.png')
plt.imshow(im)
im
above_mean = im[:, :, 1] > im.mean()
plt.imshow(above_mean.astype(float), cmap='gray')
plt.imsave('modifiedcell.jpg')
