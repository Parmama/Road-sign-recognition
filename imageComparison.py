#coding=utf-8

import cv2
import numpy as np
import glob
import os



'''def similarity_check (smpImg, refImg, asd, goodCounter, a):
		sift = cv2.xfeatures2d.SIFT_create()
		kp1, des1 = sift.detectAndCompute(smpImg, None)
		kp2, des2 = sift.detectAndCompute(refImg, None)
		
		
		if (not np.any(des2)):
			asd = False
			return(asd)

		index_params = dict(algorithm = 0, trees = 5)
		search_params = dict()

		flann = cv2.FlannBasedMatcher(index_params, search_params)

		matches = flann.knnMatch(des1, des2, k=2)

		good = []
		for m, n in matches:
			if m.distance < 0.6*n.distance:
				good.append(m)

		result = cv2.drawMatches(smpImg, kp1, refImg, kp2, good, None)
		cv2.imshow("Found Matches", result)
		a = len(good)
		print(len(good))
		print(a)
		return(a)'''
		

signs = ["20km/h_korlatozo", "30hm/h_korlatozo", "50hm/h_korlatozo",
"60hm/h_korlatozo", "70hm/h_korlatozo", "80hm/h_korlatozo", "80hm/h_korlatozo_vege",
"100hm/h_korlatozo", "120hm/h_korlatozo", "elozni_tilos", "teherautoval_elozni_tilos",
"felsobbrendu_utkeresztezodes", "foutvonal", "elsobbsegadas_kotlezzo",
"allj_elsobbsegadas_kotelezo", "behajtani_tilos", "teherautoval_behajtani_tilos",
"behajtas_a_tuloldalrol", "veszely_jelzo", "eles_utkanyarulat_balra",
"eles_utakanyrulat_jobbra", "tobb_eles_utakanyarulat", "bukkanok",
"csudzos_utburkolat", "utszukulet", "utepites", "lampas_vasuti_atjaro",
"gyalogos_forgalom", "iskola", "biciklis_forgalom", "havas_utburkolat",
"vadveszely", "krolatozo_tabla_vege", "kotelezo_haladasi_irany_jobbra",
"kotelezo_haladasi_irany_balra", "kotelezo_haladasi_irany_egyenesen",
"kotelezio_haladasi_irany_jobbra,elore", "kotelezio_haladasi_irany_balra,elore",
"kotelezo_kikerulesi_irany_jobbra", "kotelezo_kikerulesi_irany_balra",
"korforgalom", "elozni_tilos_vege", "teherautoval_elozni_tilos_vege"]

pathVariables = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 
"10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", 
"23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", 
"36", "37", "38", "39", "40", "41", "42"]

#read images
smpImg = cv2.imread('/home/parma/Documents/Gépi látás/reference/aasd/00002_00007.ppm')
smpImg = cv2.resize(smpImg, (300,300))
cv2.imshow("Sample", smpImg)
'''compImg = cv2.imread('/home/parma/Documents/Gépi látás/reference/00003/00036_00001.ppm')
#create gray immages
srcImg = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
compImg = cv2.cvtColor(compImg, cv2.COLOR_BGR2GRAY)'''


filec=100
percentage = 1
i=0

while (percentage/(filec/10) < 10):

	filec = 0
	goodCounter = 0
	a = 0
	percentage = 0
	


	#Iterating in the reference folder
	pattern = "/home/parma/Documents/Gépi látás/reference/" + pathVariables[i]+ "/*"
	
	for fname in glob.glob(pattern):
		print('file name :', fname)
		
		refImg = cv2.imread(fname)
		refImg = cv2.resize(refImg, (300,300))
		
		sift = cv2.xfeatures2d.SIFT_create()
				
		kp1, des1 = sift.detectAndCompute(smpImg, None)
		kp2, des2 = sift.detectAndCompute(refImg, None)
		

		index_params = dict(algorithm = 0, trees = 5)
		search_params = dict()

		flann = cv2.FlannBasedMatcher(index_params, search_params)

		matches = flann.knnMatch(des1, des2, k=2)

		good = []
		for m, n in matches:
			if m.distance < 0.6*n.distance:
				good.append(m)

		result = cv2.drawMatches(smpImg, kp1, refImg, kp2, good, None)
		cv2.imshow("Found Matches", result)
		
		a = len(good)
		percentage = a + percentage 
		print("sum of good matches :", percentage)
		
			
		#count the passed images
		filec+=1
		print("inspected image counter :", filec)
		
		#ends after 100 images
		if (filec == 40):
			break
			

	
	if (i == 42):
		break	
	i += 1
	
	#match ratio
	#match ratio
	print(percentage/(filec/10))
	print(signs[i-1])



	
	

	
'''#check for similarities
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(smpImg, None)
kp2, des2 = sift.detectAndCompute(refImg, None)

index_params = dict(algorithm = 0, trees = 5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
	if m.distance < 0.6*n.distance:
		good.append(m)

result = cv2.drawMatches(smpImg, kp1, refImg, kp2, good, None)
cv2.imshow("Found Matches", result)
print(len(good))'''


	

'''cv2.imshow("Source", srcImg)
cv2.imshow("Compared image", compImg)
cv2.imshow("Difference", difference)'''
cv2.waitKey(0)
cv2.destroyAllWindows()
