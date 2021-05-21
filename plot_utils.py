import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision

width = 16 #output[0][0].shape[0]
height = 16 #output[0][0].shape[1]
def save_frame(output, filename):
    global width
    global height
    if filename=="compressed.png":
        width = 8
        height = 8
    elif filename=="testepoch.png":
        width = 16
        height = 16
    x1 = output[0][0].view(1, width, height)
    x1 = x1.permute(1, 2, 0)
    x1 = x1.cpu()
    x1 = x1.detach().numpy()
    plt.figure(1)
    plt.axis("off")
    plt.clf()
    plt.title('output')
    plt.imshow(x1, cmap="gray")
    #plt.pause(1)
    #plt.draw()
    plt.savefig(filename)
    plt.close()
    width = 16
    height = 16

def save_sequences(data, video, output, filename):
    
    figure = plt.figure(figsize=(7, 7))
    figure.add_subplot(2, 4, 1)
    frame0 = data[0][[video]].view(1, width, height)
    frame0 = frame0.permute(1, 2, 0)
    frame0 = frame0.cpu()
    frame0 = frame0.detach().numpy()
    plt.axis("off")
    plt.imshow(frame0, cmap="gray")
    figure.add_subplot(2, 4, 2)
    frame1 = data[5][video].view(1,width,height)
    frame1 = frame1.permute(1, 2, 0)
    frame1 = frame1.cpu()
    frame1 = frame1.detach().numpy()
    plt.axis("off")
    plt.imshow(frame1, cmap="gray")
    figure.add_subplot(2, 4, 3)
    frame2 = data[10][video].view(1,width,height)
    frame2 = frame2.permute(1, 2, 0)
    frame2 = frame2.cpu()
    frame2 = frame2.detach().numpy()
    plt.axis("off")
    plt.imshow(frame2, cmap="gray")
    figure.add_subplot(2, 4, 4)
    frame3 = data[19][video].view(1,width,height)
    frame3 = frame3.permute(1, 2, 0)
    frame3 = frame3.cpu()
    frame3 = frame3.detach().numpy()
    plt.axis("off")
    plt.imshow(frame3, cmap="gray")
    #first row with original samples done, now output
    figure.add_subplot(2, 4, 5)
    frame4 = output[0][video].view(1, width, height)
    frame4 = frame4.permute(1, 2, 0)
    frame4 = frame4.cpu()
    frame4 = frame4.detach().numpy()
    plt.axis("off")
    plt.imshow(frame4, cmap="gray")
    figure.add_subplot(2, 4, 6)
    frame5 = output[5][video].view(1, width, height)
    frame5 = frame5.permute(1, 2, 0)
    frame5 = frame5.cpu()
    frame5 = frame5.detach().numpy()
    plt.axis("off")
    plt.imshow(frame5, cmap="gray")
    figure.add_subplot(2, 4, 7)
    frame6 = output[10][video].view(1, width, height)
    frame6 = frame6.permute(1, 2, 0)
    frame6 = frame6.cpu()
    frame6 = frame6.detach().numpy()
    plt.axis("off")
    plt.imshow(frame6, cmap="gray")
    figure.add_subplot(2, 4, 8)
    frame7 = output[19][video].view(1, width, height)
    frame7 = frame7.permute(1, 2, 0)
    frame7 = frame7.cpu()
    frame7 = frame7.detach().numpy()
    plt.axis("off")
    plt.imshow(frame7, cmap="gray")

    plt.savefig(filename)
    plt.close()