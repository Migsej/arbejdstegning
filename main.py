import cv2
import numpy as np
import math


paptykke = 3 #mm

HEIGHT = 250 #mm

LAYERS = HEIGHT//paptykke

def pretyprint(liste):
    for element in liste:
        element = round_down(element,1)
        print(str(element)+" mm")


def round_down(value, decimals):
    return math.floor(value * 100)/100.0


def main():
     
    # Load an color image in grayscale
    img = cv2.imread('billede.png',0)
    (_, blackwhite) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    dimensions = blackwhite.shape
    print(dimensions) 
    
    forhold = HEIGHT/dimensions[1]
    
    width = len(blackwhite) // LAYERS

    result = []
    for i in range(LAYERS):
        newarray = blackwhite[width*i:width*i+width]
        black = np.count_nonzero(newarray==0)
        element = (black//width)/len(blackwhite[0])
        result.append(element*dimensions[0]*forhold/2)
    
        
    pretyprint(result)
    # show image
    cv2.imshow('image',blackwhite)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

