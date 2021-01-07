"""Program to move files across from BAU to STATIC_ASSETS. Any BAU folder which has been generated since the last execution of this 
program will be searched for new files and these new files will be added to STATIC_ASSETS folder """

import logging
import os
from shutil import copytree, copyfile
from datetime import date, datetime

def main():
    
    try: 
        
        # date of cookie, substitute for start_date
        # start_date = date(2020, 8, 1)
        cookieDay = datetime.fromtimestamp(os.path.getctime('//mkfile2/Ecommerce/Creative Team/Cat 81 - Argos.ie/STATIC ASSETS/argosincludes/cookie.htm')).strftime('%Y, %m, %d')
        year, month, finalday = int(cookieDay[0:4]), int(cookieDay[6:8]), int(cookieDay[10:12])
        start_date = date(year, month, finalday)
        end_date = date.today()
    except:
       logging.error("Date error")

    print('Last moved file date:  ' + start_date.strftime('%m/%d/%Y')) 
    print('Most recent server file(s) upload date:  ' + end_date.strftime('%m/%d/%Y'))

    if start_date.strftime("%Y") == end_date.strftime("%Y"):
        yearArray = [start_date.strftime("%Y")]
    else:
        yearArray = [start_date.strftime("%Y"), end_date.strftime("%Y")]

    if start_date.strftime("%m") == end_date.strftime("%m"):
        monthArray = [end_date.strftime("%m") + '_' + end_date.strftime("%B")]
    else:
        monthArray = [start_date.strftime("%m") + '_' + start_date.strftime("%B"), end_date.strftime("%m") + '_' + end_date.strftime("%B")]

    print(monthArray)

    root_path = '//mkfile2/Ecommerce/Creative Team/Bau'
    destinationfolder = '//mkfile2/Ecommerce/Creative Team/Cat 81 - Argos.ie/STATIC ASSETS/argosincludes/' 

    for year in yearArray:
        for month in monthArray:
            if year == start_date.strftime("%Y") and month != (start_date.strftime("%m") + '_' + start_date.strftime("%B")):
                continue
            if year == end_date.strftime("%Y") and month != (end_date.strftime("%m") + '_' + end_date.strftime("%B")):
                continue
            singledayArray = []
            doubledayArray = []
            dayArray = []
            for dir in os.listdir(root_path + '/' + year + '/' + month):  
                if dir[:1].isnumeric() and not dir[:2].isnumeric():
                    if len(monthArray) > 1:
                        if monthArray[len(monthArray) - 1] == month:
                            if int(dir[:1]) <= int(end_date.strftime("%e")):
                                singledayArray.append(dir)
                        elif monthArray[0] == month:
                            if int(dir[:1]) >= int(start_date.strftime("%e")):
                                singledayArray.append(dir)
                        else:
                            singledayArray.append(dir)
                    else:
                        if int(dir[:1]) >= int(start_date.strftime("%e")) and int(dir[:1]) <= int(end_date.strftime("%e")):
                                singledayArray.append(dir)
                elif dir[:1] == 0 and dir[:2].isnumeric():
                    if len(monthArray) > 1:
                        if monthArray[len(monthArray) - 1] == month:
                            if int(dir[:2]) <= int(end_date.strftime("%e")):
                                singledayArray.append(dir)
                        elif monthArray[0] == month:
                            if int(dir[:2]) >= int(start_date.strftime("%e")):
                                singledayArray.append(dir)
                        else:
                            singledayArray.append(dir)
                    else:
                        if int(dir[:2]) >= int(start_date.strftime("%e")) and int(dir[:2]) <= int(end_date.strftime("%e")):
                                singledayArray.append(dir)
                elif dir[:2].isnumeric() and not dir[:1] == 0:
                    if len(monthArray) > 1:
                        if monthArray[len(monthArray) - 1] == month:
                            if int(dir[:2]) <= int(end_date.strftime("%e")):
                                doubledayArray.append(dir)
                        elif monthArray[0] == month:
                            if int(dir[:2]) >= int(start_date.strftime("%e")):
                                doubledayArray.append(dir)
                        else:
                            doubledayArray.append(dir)
                    else:
                        if int(dir[:2]) >= int(start_date.strftime("%e")) and int(dir[:2]) <= int(end_date.strftime("%e")):
                                doubledayArray.append(dir)

            singledayArray.sort()
            doubledayArray.sort()
            dayArray = singledayArray + doubledayArray
            for day in dayArray:
                if os.path.exists(root_path + '/' + year + '/' + month + '/' + day + '/argosie/argosincludes'):
                    for file in os.listdir(root_path + '/' + year + '/' + month + '/' + day + '/argosie/argosincludes'):
                        if os.path.isfile(root_path  + '/' + year + '/' + month + '/' + day + '/argosie/argosincludes' + '/' + file) and file[:1] != '.':
                            srcfile = root_path  + '/' + year + '/' + month + '/' + day + '/argosie/argosincludes' + '/' + file
                            destinationfile = destinationfolder + file
                            copyfile(srcfile, destinationfile)
                            print('Moving:  ' + srcfile)
                            print('    To:  ' + destinationfile)
    os.remove('//mkfile2/Ecommerce/Creative Team/Cat 81 - Argos.ie/STATIC ASSETS/argosincludes/cookie.htm')
    f = open('//mkfile2/Ecommerce/Creative Team/Cat 81 - Argos.ie/STATIC ASSETS/argosincludes/cookie.htm', 'w')
    f.write('You win!')
    f.close()

if __name__ == "__main__":
    main()