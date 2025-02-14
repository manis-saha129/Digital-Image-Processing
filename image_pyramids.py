import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('room.jpg')
img = cv2.resize(img, (480, 576))


gp = [img]
for i in range(3):  
    img = cv2.pyrDown(img)
    gp.append(img)


lp = [gp[-1]]
for i in range(3, 0, -1):  
    gaussian_expanded = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_expanded)
    lp.append(laplacian)


gp_rgb = [cv2.cvtColor(g, cv2.COLOR_BGR2RGB) for g in gp]
lp_rgb = [cv2.cvtColor(l, cv2.COLOR_BGR2RGB) for l in lp]


def plot_pyramid(images, title):
    fig, axes = plt.subplots(1, 4, figsize=(12, 6))
    fig.suptitle(title, fontsize=16, fontweight='bold')
    
    for i, ax in enumerate(axes):
        ax.imshow(images[i], aspect='auto') 
        ax.set_xticks([])  
        ax.set_yticks([])  
        ax.set_title(f'Level {i}', fontsize=12)  

    plt.tight_layout()  
    plt.show()

plot_pyramid(gp_rgb, "Gaussian Pyramid")
plot_pyramid(lp_rgb, "Laplacian Pyramid")
