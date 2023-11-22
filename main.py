# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:30:22 2023

@author: 32496
"""

#make sure current working directory is the one where this main code file is saved
#cd C:\Users\32496\OneDrive\Documenten\School\Internship\MainProject\GCATool

import os
import sys
from pprint import pprint
import pandas as pd

#walker function
#will walk through the directory tree and return the paths to the lowest level files
def walker(dirname=''):
    filelist = []
    for root, _, files in os.walk(dirname):
        for name in files:
            filepath = os.path.join(root, name)
            #if the name does not start with a period (hidden file), then add it to the list
            if not name.startswith('.'):
                filelist.append(filepath)
    return filelist

#readCSV function
#this will read in the CSV master file containing all participant info
#and filter for those participants with both an acute scan and a lesion mask
def readCSV(filepath=''):
    dataframe1 = pd.read_csv(filepath, delimiter= ';')
    dataframe2 = dataframe1[dataframe1.AcuteCTScan != "No"]
    dataframe2 = dataframe1[dataframe1.LesionMask != "No"] #using this will result in only those participants who have both an acute scan and a lesion mask!
    return dataframe2

#compilefilename function
#this function will compile mock filenames using acute CT scan dates and lesion mask dates 
#which we will later compare to the filenames actually present on the harddrive
#we are doing this because we only want to keep the acute scans and the correct lesion masks
def CompileFilename(dataframe):
    ID = dataframe["ID"].tolist()
    ScanDate = dataframe["AcuteCTScanDate"].tolist()
    LesionDate = dataframe["LesionMaskDate"].tolist()
    for i in range(len(ScanDate)):
        ScanDate[i] = ScanDate[i].replace("/", "") #get acute CT scan dates without slashes
    for i in range(len(LesionDate)):
        LesionDate[i] = LesionDate[i].replace("/", "") #get lesion mask dates without slashes
    mocklist = []
    p1 = ["p", "P"] #these variables are used in the j and k loops because the file- and folder names on the harddrive are inconsistent in terms of small vs capital letter p
    p2 = ["p", "P"]
    for i in range(len(dataframe)): 
        #this is basically hard code to simulate the filepaths of the harddrive - could probably be improved! perhaps using the dirname variable
        for j in range(len(p1)):
            for k in range(len(p2)):
                mocklist.append("D:/Ibe main project/OCS scans" + "\\" + p1[j] + str(ID[i]) + "\\Scans\\" + p2[k] + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT.nii")
                mocklist.append("D:/Ibe main project/OCS scans" + "\\" + p1[j] + str(ID[i]) + "\\Lesions\\" + p2[k] + str(ID[i]) + "_" + str(LesionDate[i]) + "_CT_Lesion.nii")
    return(mocklist)

#acutescans function
#we now want to compare the mock filenames to the actual filenames on the hard drive
#we get a list of all the acute CT scans and correct lesion masks on the hard drive
#these are the only ones we want to keep for further analysis
def AcuteScans(mocklist, filelist):
    acutefiles = []
    for i in range(len(mocklist)):
        if mocklist[i] in filelist:
            acutefiles.append(mocklist[i])
    return(acutefiles)



def main():
    #the first argument is the direcory we want to walk through
    dirname = sys.argv[1]
    filelist = walker(dirname)
    #the second argument is the filepath to the master file (csv)
    filepath = sys.argv[2]
    dataframe = readCSV(filepath)
    mocklist = CompileFilename(dataframe)
    acutefiles = AcuteScans(mocklist, filelist)
    #pprint(filelist)
    #pprint(dataframe)
    #pprint(mocklist)
    pprint(acutefiles)
    

if __name__ == "__main__":
    #run in command line
    #for me: %run main.py "D:/Ibe main project/OCS scans" "D:/Ibe main project/OCS scans/OCSMasterFile.csv"
    main()

