from matplotlib import pyplot as plt

def plot_image(image,title):
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)