from PIL import Image

#--------------------------------
# EXERCICE 1
#--------------------------------

def ex1():
    im = Image.open("joconde.png")
    (l , h) = im.size
    im = Image.new("RGB", (l,h))
    im.show()

#--------------------------------
# EXERCICE 3
#--------------------------------

def photomaton(image):
    l , h = image.size
    l_photomaton = (int)(l/2)
    h_photomaton = (int)(h/2)
    returned_image = Image.new("RGB", (l,h))
    for i in range(0,l,2):
        for j in range(0,h,2):
            color1 = image.getpixel((i,j))
            color2 = image.getpixel((i+1,j))
            color3 = image.getpixel((i,j+1))
            color4 = image.getpixel((i+1,j+1))
            
            returned_image.putpixel(((int)(i/2),(int)(j/2)), color1)
            returned_image.putpixel(((int)(i/2+l_photomaton),(int)(j/2)), color2)
            returned_image.putpixel(((int)(i/2),(int)(j/2+h_photomaton)), color3)
            returned_image.putpixel(((int)(i/2+l_photomaton),(int)(j/2+h_photomaton)), color4)
    return returned_image
    
def ex3():
    im = Image.open("joconde.png")
    photomaton(im).show()

#--------------------------------
# EXERCICE 5
#--------------------------------

def etirement(image):
    l , h = image.size
    returned_image = Image.new("RGB", (l*2,(int)(h/2)))
    for i in range(0,l,2):
        for j in range(0,h,2):
            color1 = image.getpixel((i,j))
            color2 = image.getpixel((i+1,j))
            color3 = image.getpixel((i,j+1))
            color4 = image.getpixel((i+1,j+1))
            
            returned_image.putpixel(((int)(i*2),(int)(j/2)), color1)
            returned_image.putpixel(((int)(i*2+1),(int)(j/2)), color3)
            returned_image.putpixel(((int)(i*2+2),(int)(j/2)), color2)
            returned_image.putpixel(((int)(i*2+3),(int)(j/2)), color4)
    return returned_image
    

def ex5():
    im = Image.open("joconde.png")
    etirement(im).show()
    

#--------------------------------
# EXERCICE 7
#--------------------------------

def repliment(image):
    l , h = image.size
    returned_image = Image.new("RGB", ((int)(l/2),h*2))
    l_new , h_new = returned_image.size
    for i in range(l):
        for j in range(h):
            color = image.getpixel((i,j))
            if( i >= l_new):
                returned_image.putpixel((l-1-i,h_new-1-j), color)
            else:
                returned_image.putpixel((i,j), color)
    return returned_image
    
def ex7():
    im = Image.open("joconde.png")
    repliment(im).show()
    
#--------------------------------
# EXERCICE 8
#--------------------------------

def boulanger(image):
    return repliment(etirement(image))
    
def ex8():
    im = Image.open("joconde.png")
    boulanger(im).show()
    
#--------------------------------
# EXERCICE 8
#--------------------------------
    
def ex9():
    im = Image.open("joconde.png")
    for i in range(19):
        im = boulanger(im)
        im.show()
ex9()