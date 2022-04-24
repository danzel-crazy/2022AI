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
    # Begin your code (Part 4)
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
    
    file1 = []
    file2 = []
    
    with open(dataPath) as f:
        line = f.readline()
        line = line.strip()
        s = line.split(' ')
        path1 = (s[0])
        size1 = int(s[1])
        for i in range(size1):
            line = f.readline()
            line = line.strip()
            s = line.split(' ')
            for j in range(len(s)):
                file1.append(int(s[j]))
            
        line = f.readline()
        line = line.strip()
        s = line.split(' ')
        path2 = (s[0])
        size2 = int(s[1])
        for i in range(size2):
            line = f.readline()
            line = line.strip()
            s = line.split(' ')
            for j in range(len(s)):
                file2.append(int(s[j]))
        
    # print(path1)
    # print(path2)
    # print(size1)
    # print(size2)
    # print(file1)
    # print(file2)
    
    image1 = cv2.imread('data/detect/'+path1)
    image2 = cv2.imread('data/detect/'+path2)

    for i in range(size1):
        face1 = image1[file1[i*4+1]: file1[i*4+1]+file1[i*4+3], file1[i*4]: file1[i*4]+file1[i*4+2]]
        # plt.imshow(cv2.cvtColor(face1, cv2.COLOR_BGR2RGB))
        # plt.show()
        face1 = cv2.cvtColor(face1, cv2.COLOR_BGR2GRAY)
        face1 = cv2.resize(face1, (19, 19), interpolation=cv2.INTER_NEAREST)
        is_face = clf.classify(face1)
        if(is_face):
            green_color = (0, 255, 0) #BGR
            cv2.rectangle(image1, (file1[i*4], file1[i*4+1]), (file1[i*4]+file1[i*4+2], file1[i*4+1]+file1[i*4+3]), green_color, 3, cv2.LINE_AA)
        else:
            red_color = (0, 0, 255) #BGR
            cv2.rectangle(image1, (file1[i*4], file1[i*4+1]), (file1[i*4]+file1[i*4+2], file1[i*4+1]+file1[i*4+3]), red_color, 3, cv2.LINE_AA)
    
    for i in range(size2):
        face2 = image2[file2[i*4+1]: file2[i*4+1]+file2[i*4+3], file2[i*4]: file2[i*4]+file2[i*4+2]]
        # plt.imshow(cv2.cvtColor(face2, cv2.COLOR_BGR2RGB))
        # plt.show()
        face2 = cv2.cvtColor(face2, cv2.COLOR_BGR2GRAY)
        face2 = cv2.resize(face2, (19, 19), interpolation=cv2.INTER_NEAREST)
        is_face = clf.classify(face2)
        if(is_face):
            green_color = (0, 255, 0) #RGB
            cv2.rectangle(image2, (file2[i*4], file2[i*4+1]), (file2[i*4]+file2[i*4+2], file2[i*4+1]+file2[i*4+3]), green_color, 3, cv2.LINE_AA)
        else:
            red_color = (0, 0, 255) #RGB
            cv2.rectangle(image2, (file2[i*4], file2[i*4+1]), (file2[i*4]+file2[i*4+2], file2[i*4+1]+file2[i*4+3]), red_color, 3, cv2.LINE_AA)
    
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    plt.show()
    # End your code (Part 4)