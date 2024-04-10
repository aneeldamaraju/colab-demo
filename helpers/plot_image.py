from matplotlib import pyplot as plt

def plot_image_with_title(image,title):
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)