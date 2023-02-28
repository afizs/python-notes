import matplotlib.image as img
import matplotlib.pyplot as plt
  
# reading the image
dog = img.imread('puppy.png')

def show_images(image_1, image_2, image_3):
    fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))
    ax0.imshow(image_1)
    ax0.set_title("RGB image")
    # ax0.axis('off')
    ax1.imshow(image_2)
    ax1.set_title("Hue channel")
    # ax1.axis('off')
    ax2.imshow(image_3)
    ax2.set_title("Value channel")
    # ax2.axis('off')

    fig.tight_layout()

