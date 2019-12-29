#coding=utf-8

import cv2
import numpy as np
import glob
import os

signs = ["20km/h_korlatozo", "30km/h_korlatozo", "50km/h_korlatozo",
"60km/h_korlatozo", "70km/h_korlatozo", "80km/h_korlatozo", "80km/h_korlatozo_vege",
"100km/h_korlatozo", "120km/h_korlatozo", "elozni_tilos", "teherautoval_elozni_tilos",
"felsobbrendu_utkeresztezodes", "foutvonal", "elsobbsegadas_kotlezo",
"allj_elsobbsegadas_kotelezo", "mindket_iranybol_behajtani_tilos", "teherautoval_behajtani_tilos",
"behajtani_tilos", "veszely_jelzo", "veszelyes_utkanyarulat_balra",
"veszelyes_utakanyrulat_jobbra", "egymas_utani_veszelyes_utakanyarulatok", "egyenletlen_utburkolat",
"csuszos_utburkolat", "utszukulet", "utepites", "lampas_vasuti_atjaro",
"gyalogos_forgalom", "iskola", "biciklis_forgalom", "havas_utburkolat",
"vadveszely", "korlatozo_tabla_vege", "kotelezo_haladasi_irany_jobbra",
"kotelezo_haladasi_irany_balra", "kotelezo_haladasi_irany_egyenesen",
"kotelezio_haladasi_irany_jobbra_vagy_elore", "kotelezio_haladasi_irany_balra_vagy_elore",
"kotelezo_kikerulesi_irany_jobbra", "kotelezo_kikerulesi_irany_balra",
"korforgalom", "elozni_tilos_vege", "teherautoval_elozni_tilos_vege"]

pathVariables = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 
"10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", 
"23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", 
"36", "37", "38", "39", "40", "41", "42"]
print("Kerem masolja ide a mintakep eleresi utvonalat az alabbi formaban: 'utvonal/nev' ! ")
#read images
smpImg = cv2.imread(input())
smpImg = cv2.resize(smpImg, (300,300))
cv2.imshow("Sample", smpImg)


filec=100
percentage = 1
i=0

while (percentage/(filec/10) < 10):

	filec = 0
	goodCounter = 0
	a = 0
	percentage = 0
	


	#Iterating in the reference folder
	pattern = "reference/" + pathVariables[i]+ "/*"
	
	for fname in glob.glob(pattern):
		print('feldolgozas...')
		
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

		
		a = len(good)
		percentage = a + percentage 
		
			
		#count the passed images
		filec+=1
		
		#ends after 40 images
		if (filec == 40):
			break
			

	
	if (i == 19):
		break	
	i += 1
	
#match
print("Felismert tabla ", signs[i-1])

cv2.waitKey(0)
cv2.destroyAllWindows()
