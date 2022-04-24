import os
import cv2
import matplotlib.pyplot as plt

def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 5)
    # raise NotImplementedError("To be implemented")
    """
    1.read information in detectData.txt
    2.store image name, face_number, face_position in path, size, file
    3.then use for loop to classiy whether it is a face
    4.first store face image in face1,2
    5.second use cv2.cvtcolor() and cv2.resize() to chage image to grayscale and 19 x 19
    6.third check if image is clt.classify() as face 
    7.if is a face, use cv2.rectangle() to draw red rectangle, else draw red
    8.plot image while change BGR to RGB
    """
    # Begin your code (Part 5)
    """
    Part 5: Test classifier on your own images
    1.I use warrios.jpg to detect 
    2.the face position is stored in image.jpg
    """

    file3 = []
    
    with open(dataPath) as f:     
        line = f.readline()
        line = line.strip()
        s = line.split(' ')
        path3 = (s[0])
        size3 = int(s[1])
        for i in range(size3):
            line = f.readline()
            line = line.strip()
            s = line.split(' ')
            for j in range(len(s)):
                file3.append(int(s[j]))

    image3 = cv2.imread('data/detect/'+path3)
    for i in range(size3):
        face3 = image3[file3[i*4+1]: file3[i*4+1]+file3[i*4+3], file3[i*4]: file3[i*4]+file3[i*4+2]]
        # plt.imshow(cv2.cvtColor(face3, cv2.COLOR_BGR2RGB))
        # plt.show()
        face3 = cv2.cvtColor(face3, cv2.COLOR_BGR2GRAY)
        face3 = cv2.resize(face3, (19, 19), interpolation=cv2.INTER_NEAREST)
        is_face = clf.classify(face3)
        if(is_face):
            green_color = (0, 255, 0) #RGB
            cv2.rectangle(image3, (file3[i*4], file3[i*4+1]), (file3[i*4]+file3[i*4+2], file3[i*4+1]+file3[i*4+3]), green_color, 3, cv2.LINE_AA)
        else:
            red_color = (0, 0, 255) #RGB
            cv2.rectangle(image3, (file3[i*4], file3[i*4+1]), (file3[i*4]+file3[i*4+2], file3[i*4+1]+file3[i*4+3]), red_color, 3, cv2.LINE_AA)
    
    plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
    plt.show()
    # End your code (Part 5)