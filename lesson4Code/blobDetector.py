#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
import sys

# original code : http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html
# other version : https://github.com/TheLaueLab/blob-detection

from math import sqrt
from skimage import data
from skimage.transform import rescale
from skimage.feature import blob_dog, blob_log, blob_doh # Blob detection methods
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import os

def imcrop(img, bbox):
    x1, y1, x2, y2 = bbox
    if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
        img, x1, x2, y1, y2 = pad_img_to_fit_bbox(img, x1, x2, y1, y2)
    return img[y1:y2, x1:x2]

def pad_img_to_fit_bbox(img, x1, x2, y1, y2):
    img = cv2.copyMakeBorder(img, - min(0, y1), max(y2 - img.shape[0], 0),-min(0, x1), max(x2 - img.shape[1], 0),cv2.BORDER_REPLICATE)
    y2 += -min(0, y1)
    y1 += -min(0, y1)
    x2 += -min(0, x1)
    x1 += -min(0, x1)
    return img, x1, x2, y1, y2

def overlappingKeyPoints(p,kpList,th):
    returnList=[p]

    #put all superposed to p
    i=0
    while i<len(returnList):
        x=returnList[i]
        for q in kpList:
            if (cv2.KeyPoint_overlap(x,q)>th or cv2.KeyPoint_overlap(q,x)>th )  and not q in returnList:
                #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@apending with i "+str(i))
                returnList.append(q)
        i+=1
    return returnList

def refineKeypoints(kpList,th):
    returnList=[]
    checkedList=[]
    for kp in kpList:
        if not kp in checkedList:
            overlapping=overlappingKeyPoints(kp,kpList,th)
            if len(overlapping)>1:
                #print("found "+str(len(overlapping)))
                #merge overlapping overlappingKeyPoints
                maxX=overlapping[0].pt[0]
                minX=overlapping[0].pt[0]
                maxY=overlapping[0].pt[1]
                minY=overlapping[0].pt[1]
                for kp2 in overlapping:
                    checkedList.append(kp2)
                    #print ("point "+str(kp2.pt[0])+" , "+str(kp2.pt[1])+" size "+str(kp2.size))
                    if(kp2.pt[0]<minX):minX=kp2.pt[0]
                    if(kp2.pt[0]>maxX):maxX=kp2.pt[0]
                    if(kp2.pt[1]<minY):minY=kp2.pt[1]
                    if(kp2.pt[1]>maxY):maxY=kp2.pt[1]
                #now create new keypoints
                #newP=cv2.KeyPoint(minX+(maxX-minX)/2,minY+(maxY-minY)/2,max((maxX-minX),((maxY-minY))))
                #print(" creating point "+str(newP.pt[0])+" , "+str(newP.pt[1])+" size "+str(newP.size))
                returnList.append(cv2.KeyPoint( minX+(maxX-minX)/2,minY+(maxY-minY)/2,2*max((maxX-minX),((maxY-minY)))))
            else:
                checkedList.append(kp)
                returnList.append(kp)
            #print("returnList lenght  " +str(len(returnList))+" checked list lenght "+str(len(checkedList)))

    return returnList



def SimpleBlobDetector(argv,im):

    # Read image
    #im = cv2.imread(argv[1], cv2.IMREAD_GRAYSCALE)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 200
    params.maxArea = 1500

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.2

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.25
    params.maxConvexity = 0.75

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    if len(argv)>4: params.minArea=int(argv[4])


    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else :
        detector = cv2.SimpleBlobDetector_create(params)


    # Detect blobs.
    keypoints = detector.detect(im)

    #now refine keypoints so overlapping blobs are merged
    overlapThreshold=0.001
    #print ("number of keypoints "+str(len(keypoints)))

    refinedKeypoints=refineKeypoints(keypoints,overlapThreshold)
    #print ("number of keypoints "+str(len(refinedKeypoints)))

    #return keypoints
    return refinedKeypoints

def main(argv):
    # Blod detector tester function
    #parameters:
    #argv[1] contains input file name
    #argv[2] contains output file name
    #argv[3] contains type of blob detector: 0 for simple detector, 1 for Laplacian Of Gaussians (LoG), 2 for Difference of Gaussian (DoG), 3 for Hessian of Gaussian (HoG)
    # other parameters are included after、argv[4] and later, check each method

    image_gray=cv2.imread(argv[1], cv2.IMREAD_GRAYSCALE)
    image=image_gray
    image_black=(255-image_gray)

    #switch between the different types of blob detector
    if int(argv[3])==0:
        keypoints=SimpleBlobDetector(argv,image)
        #print ("number of keypoints outside "+str(len(keypoints)))

    elif int(argv[3])==1:
        #parameters: http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.blob_log
        min_s=30
        over=.1
        #example!, other parameters exist
        if len(argv)>4: min_s=int(argv[4])
        if len(argv)>5: over=float(argv[5])
        #print("starting laplacion of gaussians detector with parameters "+str(min_s)+" "+str(over))
        blob_List = blob_log(image_black, min_sigma=min_s,  overlap=over)
        # Compute radii in the 3rd column.
        blob_List[:, 2] = blob_List[:, 2] * sqrt(2)
    elif int(argv[3])==2:
        #parameters: http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.blob_dog
        blob_List = blob_dog(image_black,min_sigma=40,  threshold=1)
        blob_List[:, 2] = blob_List[:, 2] * sqrt(2)
    elif int(argv[3])==3:
        #parameters: http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.blob_doh
        min_s=30

        if len(argv)>4: min_s=int(argv[4])

        blob_List = blob_doh(image_gray,min_sigma=min_s, max_sigma=100, threshold=.01,overlap=0.4)
    else:
        print("Blob detector type not supported: "+argv[3])
        sys.exit(-1)

    #Now write the results to file
    if int(argv[3])==1 or int(argv[3])==2 or int(argv[3])==3:
        for blob in blob_List:
            y, x, r = blob
            cv2.rectangle(image,(int(x-r), int(y-r)), (int(x+r), int(y+r)), (0, 0, 255), 1)
            #cv2.circle(image,(int(x),int(y)),int(r),(0,0,255))
        cv2.imwrite(argv[2],image)
    else:
        # must be 0 as we already controled other cases
        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        #im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #cv2.imwrite("sambombita.jpg",im_with_keypoints)

        for kp in keypoints:
            x = kp.pt[0]
            y = kp.pt[1]
            r = kp.size
            cv2.rectangle(image,(int(x-r), int(y-r)), (int(x+r), int(y+r)), (0, 0, 255), 1)
            #cv2.circle(image,(int(x),int(y)),int(r),(0,0,255))
        cv2.imwrite(argv[2],image)

    #now crop each kanji image
    #sys.exit(0)
    #print("now Cropping")
    try:
        os.mkdir(argv[2]+"PATCHES")
    except:
        #print("An exception occurred Probably directory already existed")
        pass
    margin=5
    scale_percent = 5000 # percent of original size

    if int(argv[3])==1 or int(argv[3])==2 or int(argv[3])==3:
        i=0
        image=cv2.imread(argv[1], cv2.IMREAD_GRAYSCALE)
        #print("Number of Blobs "+str(len(blob_List)))
        print(str(len(blob_List)))
        for blob in blob_List:
            #print("Cropping blob "+str(i))
            y, x, r = blob
            currentKanjiImage=imcrop(image, (int(x-r-margin), int(y-r-margin), int(x+r+margin), int(y+r+margin) ) )
            newImageName=argv[2]+"PATCHES/kanji"+str(i)+".png"
            #cv2.imwrite(newImageName,currentKanjiImage)
            width = int(currentKanjiImage.shape[1] * scale_percent / 100)
            height = int(currentKanjiImage.shape[0] * scale_percent / 100)
            #width = int(800)
            #height = int(593)
            dim = (width, height)

            # resize image
            resized = cv2.resize(currentKanjiImage, dim, interpolation = cv2.INTER_NEAREST)

            #negative image
            negImage=(255-resized)

            cv2.imwrite(newImageName,negImage)

            i=i+1
    else:
        i=0
        image=cv2.imread(argv[1], cv2.IMREAD_GRAYSCALE)
        #print("Number of Blobs "+str(len(keypoints)))
        print(str(len(keypoints)))
        for kp in keypoints:
            #print("Cropping simple blob  "+str(i))
            x = kp.pt[0]
            y = kp.pt[1]
            r = kp.size

            currentKanjiImage=imcrop(image, (int(x-r-margin), int(y-r-margin), int(x+r+margin), int(y+r+margin) ) )
            newImageName=argv[2]+"PATCHES/kanji"+str(i)+".png"

            #cv2.imwrite(newImageName,currentKanjiImage)
            width = int(currentKanjiImage.shape[1] * scale_percent / 100)
            height = int(currentKanjiImage.shape[0] * scale_percent / 100)
            #width = int(800)
            #height = int(593)
            dim = (width, height)

            # resize image
            resized = cv2.resize(currentKanjiImage, dim, interpolation = cv2.INTER_NEAREST)

            #negative image
            negImage=(255-resized)

            cv2.imwrite(newImageName,negImage)

            i=i+1




if __name__ == '__main__':
    main(sys.argv)
