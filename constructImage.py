# Module for constructing new frame and storing it in a new directory

import PIL
import Image

# Written by Al Basyoni and rajat mehndiratta (github/knyte) at TartanHacks s2015

def addBars(imageFile):
    ## imageFile is a path
    ## the output is going to be an image, not a path
    im = Image.open(imageFile)
    mode = im.mode
    size = im.size
    (width, height) = size

    width1 = width/3
    width2 = 2*width/3
    length = 5
    
    box1 = (width1-length, 0, width1+length, height)
    box2 = (width2-length, 0, width2+length, height)

    newName = "p" + imageFile
    imCopy = im.copy()
    imCopy.paste("white", box1)
    imCopy.paste("white", box2)
    imCopy.save(newName)

    return newName
    

def addLayer(initialImage, imageFile, mask)
    
    im = Image.open(imageFile)
    (width, height) = im.size
    sequence = im.getdata()

    IM = Image.open(initialImage)
    SEQUENCE = IM.getdata()
    
    for i in xrange(width/3 -6, width/3 + 6):
        for j in xrange(height):
            if toPrint(i + j * width, mask):
                sequence[i + j * width] = SEQUENCE[i + j * width]
                
    for i in xrange(2*with/3 - 6, 2*width/3 + 6):
        for j in xrange(height):
            if toPrint(i + j * width, mask):
                sequence[i + j * width] = SEQUENCE[i + j * width]

    newName = "f" + imageFile
    result = im.copy()
    result.putdata(sequence)
    result.save(newName)
        
    return newName

def toPrint(position, mask):
    im = Image.open(mask).convert('RGB')
    sequence = im.getdata()
    M = sequence[position]
    R = M[0]
    G = M[1]
    B = M[2]
    threshold = 30
    if determinant(R, G, B) > threshold or R > 127 \
       and G > 127 and B > 127:
        return True
    return False

def determinant(R, G, B):
    return abs(R-G) + abs(G-B) + abs(R-B)





    
