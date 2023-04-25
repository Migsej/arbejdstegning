import cv2
import numpy as np


LAYERS = 58

def main():
     
    # Load an color image in grayscale
    img = cv2.imread('/home/vincent/arbejdstegning/billede.png',0)
    (thresh, blackwhite) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    
    width = len(blackwhite) // LAYERS

    result = []
    for i in range(LAYERS):
        newarray = blackwhite[width*i:width*i+width]
        white = np.count_nonzero(newarray==255)
        black = np.count_nonzero(newarray==0)
        result.append((black//width)/len(blackwhite[0]))
    
        
    print(result)
    # show image
    cv2.imshow('image',blackwhite)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
