import os
import cv2
import numpy as np

def loadImages(dataPath):
  """
  load all Images in the folder and transfer a list of tuples. The first 
  element is the numpy array of shape (m, n) representing the image. 
  The second element is its classification (1 or 0)
    Parameters:
      dataPath: The folder path.
    Returns:
      dataset: The list of tuples.
  """
  # Begin your code (Part 1)
  # raise NotImplementedError("To be implemented")
  """
  1.create a list to store the data of face and non-face
  2.use file1 and file 2 to get direct path of face and non-face
  3.use os.listdir to iterate file in the folder 
  4.use cv2.imread to read the image 
  5. if path is face, load 1, else 0 
  6.use list.appeend to load data 
  """
  dataset = [] 
  file1 = dataPath+"/face";
  file2 = dataPath+"/non-face";

  for i in os.listdir(file1):
      img = cv2.imread(file1+'/'+i, cv2.IMREAD_GRAYSCALE);
      dataset.append((img,1))

  for i in os.listdir(file2):
      img = cv2.imread(file2+'/'+i, cv2.IMREAD_GRAYSCALE);
      dataset.append((img,0))
  # End your code (Part 1)
  return dataset
