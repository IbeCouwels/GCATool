# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
from pprint import pprint
import pandas as pd


#walker function
#will walk through the directory tree and return the paths to the lowest level files
def walker(wd, dirname):
    #wd is working directory in which tree of interest is located
    #dirname is name of tree we want to walk through
    os.chdir(wd)
    filelist = []
    for root, _, files in os.walk(dirname):
        for name in files:
            filepath = os.path.join(root, name)
            if not name.startswith('.'):
                filelist.append(filepath)
    return filelist

filelist = walker("D:/Ibe main project", "OCS scans")
print(filelist)
#this returns a list of filepaths


#readCSV function
#this will read in the CSV file containing all participant info
def readCSV(wd, csvfilename):
    os.chdir(wd)
    dataframe1 = pd.read_csv(csvfilename, delimiter= ';')
    return dataframe1

dataframe1 = readCSV("D:/Ibe main project/OCS scans", "MasterFileTest.csv")
print(dataframe1)
#this returns a dataframe of the participant info


#filter function
#this will filter out the participants in the dataframe who do not have an acute CT scan and GCA scores
def filterdata(dataframe):
    dataframe2 = dataframe[dataframe.AcuteCTScan != "No"]
    return dataframe2

dataframe2 = filterdata(dataframe1)
print(dataframe2)
#this returns a dataframe of participant info of those participants with all scan data


#compilefilename function
#based on dataframe2 (the one without missing data), this function will compile mock filenames using acute CT scan dates, which we will compare to the filenames actually present on the harddrive (filelist)
#we are doing this because we only want to keep the acute scans
def CompileFilename(dataframe):
    ID = dataframe["ID"].tolist()
    ScanDate = dataframe["AcuteCTScanDate"].tolist()
    for i in range(len(ScanDate)):
        ScanDate[i] = ScanDate[i].replace("/", "") #get acute CT scan dates without slashes
    mocklist = []
    for i in range(len(dataframe2)):
        mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Scans\\p" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT.nii")
        mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Scans\\p" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT.nii")
        mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Scans\\P" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT.nii")
        mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Scans\\P" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT.nii")
        #mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Lesions\\p" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT_Lesion.nii")
        #mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Lesions\\p" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT_Lesion.nii")
        #mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Lesions\\P" + str(ID[i]) + "_" + str(ScanDate[i]) + "_CT_Lesion.nii")
        #mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Lesions\\P" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT_Lesion.nii")
        mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Scans\\p" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT.nii")
        mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Scans\\p" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT.nii")
        mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Scans\\P" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT.nii")
        mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Scans\\P" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT.nii")
        #mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Lesions\\p" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT_Lesion.nii")
        #mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Lesions\\p" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT_Lesion.nii")
        #mocklist.append("OCS scans" + "\\" + "p" + str(ID[i]) + "\\Lesions\\P" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT_Lesion.nii")
        #mocklist.append("OCS scans" + "\\" + "P" + str(ID[i]) + "\\Lesions\\P" + str(ID[i]) + "_0" + str(ScanDate[i]) + "_CT_Lesion.nii")
    return(mocklist)


mocklist = CompileFilename(dataframe2)
print(mocklist)
#this returns a mock filename


#acutescans function
#we now want to compare the mock filenames to the actual filenames on the hard drive
#this way, we get a list of all the acute CT scans on the hard drive - these are the only ones we want to keep for further analysis
def AcuteScans(mocklist, filelist):
    acutefiles = []
    for i in range(len(mocklist)):
        print(mocklist[i] in filelist)
        if mocklist[i] in filelist:
            acutefiles.append(mocklist[i])
    return(acutefiles)

acutefiles = AcuteScans(mocklist, filelist)
print(acutefiles)
#this returns a list of files on the hard drive that are in fact acute scans





    






    
       
        





            

    

    
        
    
    


    


        
    




    
    
    
    



    
    
    
    
        
    
    
        

        
        
    


      
      

