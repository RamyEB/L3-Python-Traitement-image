from PIL import Image

#--------------------------------
# EXERCICE 2
#--------------------------------

def ex2():
    im = Image.open('noir_et_blanc.png')
    im.show()
    
    valeur_pixel = im.getpixel((0,0))
    print(valeur_pixel)
    
    im.putpixel((10,10), 255)
    im.show()

#--------------------------------
# EXERCICE 3
#--------------------------------

def ex3():
    im = Image.open('noir_et_blanc.png')
    im.show()
    valeur_pixel = im.getpixel((25,50))
    print(valeur_pixel)

#--------------------------------
# EXERCICE 4
#--------------------------------

def inversion(image):
    x,y = image.size
    x-=1
    y-=1
    image_inverse = image.copy()
    for i in range(x):
        for j in range(y):
            image_inverse.putpixel((x-i,y-j), image.getpixel((i,j)))
    return image_inverse

def ex4():
    im = Image.open('noir_et_blanc.png')
    inversion(im).show()
    
#--------------------------------
# EXERCICE 5
#--------------------------------

def noir_et_blanc(image, s):
    x,y = image.size
    # x-=1
    # y-=1
    for i in range(x):
        for j in range(y):
            if (image.getpixel((i,j)) < s):
                image.putpixel((i,j), 0)
            else:
                image.putpixel((i,j), 255)
    return image

def ex5():
    im = Image.open('noir_et_blanc.png')
    noir_et_blanc(im, 100).show()

#--------------------------------
# EXERCICE 6
#--------------------------------

def ligne(image, y, c):
    x,y_unused = image.size
    for i in range(x):
        image.putpixel((i,y), c)
    return image
    

def ex6():
    im = Image.open('noir_et_blanc.png')
    ligne(im, 120, 255).show()

#--------------------------------
# EXERCICE 7
#--------------------------------

def assombrir(image):
    x,y = image.size
    for i in range(x):
        for j in range(y):
            image.putpixel((i,j), (int)(image.getpixel((i,j))/2))
    return image
            

def ex7():
    im = Image.open('noir_et_blanc.png')
    assombrir(im).show()
    
#--------------------------------
# EXERCICE 8
#--------------------------------

def eclaircir(image):
    x,y = image.size
    for i in range(x):
        for j in range(y):
            if(image.getpixel((i,j)) <= 127):
                image.putpixel((i,j), (int)(image.getpixel((i,j))*2))
            else:
                image.putpixel((i,j), 255)
    return image
            

def ex8():
    im = Image.open('noir_et_blanc.png')
    eclaircir(im).show()

#--------------------------------
# EXERCICE 10
#--------------------------------

def no_rouge(image):
    x,y = image.size
    for i in range(x):
        for j in range(y):
            rgb = (0, image.getpixel((i,j))[1], image.getpixel((i,j))[2])
            image.putpixel((i,j), rgb)
    return image

def ex10():
    im = Image.open('couleurs.png')
    no_rouge(im).show()
        
#--------------------------------
# EXERCICE 11
#--------------------------------

def valeur_derniers_bits(n):
    val = ((int2bin(n)[::-1])[0:3])[::-1]
    return int("".join(str(x) for x in val), 2)

def int2bin(decimal_number):
    tabdebin=[]
    while(decimal_number//2!=0):
        tabdebin.insert(0,decimal_number%2)
        decimal_number = decimal_number//2
    tabdebin.insert(0,decimal_number%2)
    return tabdebin

#--------------------------------
# EXERCICE 12
#--------------------------------

def decaler(m):
    return int("".join(str(x) for x in int2bin(m)+[1,0,0,0,0]), 2)

#--------------------------------
# EXERCICE 13
# Pas mal l'image de l'alpaga en astronaute 
#--------------------------------

def decoder(image):
    x,y = image.size
    for i in range(x):
        for j in range(y):
            rgb = (decaler(valeur_derniers_bits(image.getpixel((i,j))[0])), 
                   decaler(valeur_derniers_bits(image.getpixel((i,j))[1])), 
                   decaler(valeur_derniers_bits(image.getpixel((i,j))[2]))
                   )
            image.putpixel((i,j), rgb)
    return image

def ex13():
    im = Image.open('cache.png')
    decoder(im).show()
        
#--------------------------------
# EXERCICE 14
#--------------------------------

def int2binto8(decimal_number):
    tabdebin=[]
    while(decimal_number//2!=0):
        tabdebin.insert(0,decimal_number%2)
        decimal_number = decimal_number//2
    tabdebin.insert(0,decimal_number%2)
    
    while(len(tabdebin) < 8):
        tabdebin.insert(0,0)
    return tabdebin

def cinq_prem_bits(n):
    val = int2binto8(n)[0:5]
    return val

def trois_prem_bits(n):
    val = int2binto8(n)[0:3]
    return val

def combiner_deux_nb_bin(nb1, nb2):
    return int("".join(str(x) for x in cinq_prem_bits(nb1)+trois_prem_bits(nb2)), 2)

def cache(image_illusion, image_cacher):
    x,y = image_illusion.size
    image_a_retourner = image_cacher.copy()
    for i in range(x):
        for j in range(y):
            rgb = (combiner_deux_nb_bin( image_illusion.getpixel((i,j))[0] , image_cacher.getpixel((i,j))[0]), 
                   combiner_deux_nb_bin( image_illusion.getpixel((i,j))[1] , image_cacher.getpixel((i,j))[1]),
                   combiner_deux_nb_bin( image_illusion.getpixel((i,j))[2] , image_cacher.getpixel((i,j))[2])
                   )
            image_a_retourner.putpixel((i,j), rgb)
    return image_a_retourner
    
def ex14():
    image_illusion = Image.open('f.png')
    image_cacher = Image.open('b.png')
    cache(image_illusion, image_cacher).save("cache.png")
