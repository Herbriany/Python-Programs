"""Program to move most recent versions of all files across from BAU to STATIC_ASSETS.
"""
import os
from shutil import copytree, copyfile
from datetime import date

def main():
    root_path = '//mkfile2/Ecommerce/Creative Team/Bau/'
    # Add extra year if year has changed
    yearArray = ['2020']
    destinationfolder = '//mkfile2/Ecommerce/Creative Team/Cat 81 - Argos.co.uk/STATIC ASSETS/argosincludes/'

    for year in yearArray:
        monthArray = []
        for dir in os.listdir(root_path + '/' + year):
            if dir[:2].isnumeric():
                monthArray.append(dir)
        
        monthArray.sort()
        for month in monthArray:
            singledayArray = []
            doubledayArray = []
            dayArray = []
            for dir in os.listdir(root_path + '/' + year + '/' + month):  

                if (dir[:1].isnumeric() and not dir[:2].isnumeric()) or dir[:1] == 0:
                    singledayArray.append(dir)
                elif dir[:2].isnumeric():
                    doubledayArray.append(dir)

            singledayArray.sort()
            doubledayArray.sort()
            dayArray = singledayArray + doubledayArray
            for day in dayArray:
                if os.path.exists(root_path + '/' + year + '/' + month + '/' + day + '/argos/argosincludes'):
                    for file in os.listdir(root_path + '/' + year + '/' + month + '/' + day + '/argos/argosincludes'):
                        if os.path.isfile(root_path  + '/' + year + '/' + month + '/' + day + '/argos/argosincludes' + '/' + file) and file[:1] != '.':
                            srcfile = root_path  + '/' + year + '/' + month + '/' + day + '/argos/argosincludes' + '/' + file
                            destinationfile = destinationfolder + file
                            copyfile(srcfile, destinationfile)
                            if os.path.exists(root_path  + '/' + year + '/' + month + '/' + day + '/argos/argosincludes' + '/m/' + file):
                                srcfile = root_path  + '/' + year + '/' + month + '/' + day + '/argos/argosincludes' + '/m/' + file
                                destinationfile = destinationfolder + 'm/' + file
                                copyfile(srcfile, destinationfile)
                                print('Moving:  ' + srcfile)
                                print('    To:  ' + destinationfile)

if __name__ == "__main__":
        main()