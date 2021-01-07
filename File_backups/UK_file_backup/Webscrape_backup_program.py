"""Program to download the most up to date version of both the mobile and desktop verstion of any static pages found in the ArgosIncludes folder 
and move them across to a folder on the shared network drive. Any pages that have been found to redirect will be added to a Redirects folder and 
pages that are no longer live will be added to a No Webpage folder. Any BAU folder which has been generated since the last execution of this 
program will be searched for new files and these new files will be added to the ArgosIncludes before the downloading of the webpages is carried 
out """

""" 
IMPORTANT: must run pip install pypiwin32 to work
"""

import logging
import os
import urllib.request
import math
import win32com.client as com
from shutil import copytree, rmtree, copyfile
from datetime import date, timedelta, datetime


def main():

    # get current directory
    dirpath = os.getcwd()

    # check for necessary directories and generate if not there, declare required variables
    if not os.path.isdir(dirpath + "/no_webpage"):
        os.mkdir(dirpath + "/no_webpage")
        os.mkdir(dirpath + "/no_webpage/m")
    if not os.path.isdir(dirpath + "/redirects"):
        os.mkdir(dirpath + "/redirects")
        os.mkdir(dirpath + "/redirects/m")
    if not os.path.isdir(dirpath + "/changed_files"):
        os.mkdir(dirpath + "/changed_files")
        os.mkdir(dirpath + "/changed_files/m")

    # finding date the program was last run by finding the date cookie was generated
    if os.path.exists('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes/cookie.html'):
        day = datetime.fromtimestamp(os.path.getctime('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes/cookie.html')).strftime('%Y, %m, %d')
        
        # changing date to date like object
        try: 
            year, month, finalday = int(day[0:4]), int(day[6:8]), int(day[10:12])
            start_date = date(year, month, finalday)
        except:
            try:
                year, month, finalday = int(day[0:4]), int(day[7:8]), int(day[10:12])
                start_date = date(year, month, finalday)
            except:
                logging.error("Date error")
    else:
        start_date = date(2017, 1, 1)
    

    # getting todays date and incrementing by one day  
    end_date = date.today()
    day = timedelta(days=1)

    # logging info to text file for current date
    log_name = end_date.strftime("%Y") + '-' + end_date.strftime("%m") + '-' + end_date.strftime("%d") + '.log'
    logging.basicConfig(filename=log_name,level=logging.DEBUG)
    logging.debug(start_date)

    # BAU route folder and dest folder to have BAU files copied to
    server_route = '//mkfile2/Ecommerce/Creative Team/BAU'
    dest_argosincludes = dirpath + "/argosincludes"

    # lambda function to find ordinal indicator for paths
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
    

    # checking different possible paths for the BAU folder name, iterating through each day from start date til end date
    while start_date <= end_date:

        path1 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%b") + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%B") + '/argos/argosincludes'
        path2 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%b") + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%b") + '/argos/argosincludes'
        path3 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%b") + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%B")[:4] + '/argos/argosincludes'
        path4 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%B") + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%B") + '/argos/argosincludes'
        path5 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%B") + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%B")[:4] + '/argos/argosincludes'
        path6 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%B") + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%b") + '/argos/argosincludes'
        path7 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%B")[:4] + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%B")[:4] + '/argos/argosincludes'
        path8 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%B")[:4] + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%B") + '/argos/argosincludes'
        path9 = server_route + '/' + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_' + start_date.strftime("%B")[:4] + '/' + ordinal(int(start_date.strftime("%d"))) + ' ' + start_date.strftime("%b") + '/argos/argosincludes'
        
         

        if os.path.exists(path1): 
            logging.debug(path1)
            findandmove(path1, dest_argosincludes)
        elif os.path.exists(path2): 
            logging.debug(path2)
            findandmove(path2, dest_argosincludes)
        elif os.path.exists(path3): 
            logging.debug(path3)
            findandmove(path3, dest_argosincludes)
        elif os.path.exists(path4): 
            logging.debug(path4)
            findandmove(path4, dest_argosincludes)
        elif os.path.exists(path5): 
            logging.debug(path5)
            findandmove(path5, dest_argosincludes)
        elif os.path.exists(path6): 
            logging.debug(path6)
            findandmove(path6, dest_argosincludes)
        elif os.path.exists(path7): 
            logging.debug(path7)
            findandmove(path7, dest_argosincludes)
        elif os.path.exists(path8): 
            logging.debug(path8)
            findandmove(path8, dest_argosincludes)
        elif os.path.exists(path9): 
            logging.debug(path9)
            findandmove(path9, dest_argosincludes)

        start_date += day

    skip = "no"

    # go through files in selected directory
    for file in os.listdir(dirpath + "/argosincludes"):

        # skipping unwanted files and m folder
        if file == "Thumbs.db" or file == "thumbs.db" or file == ".DS_Store" or file == "m":
            continue


        if file == "cookie.html":
            logging.debug("cookie moved")
            continue

        # checking for spaces in file name which will return broken urls but won't be flagged later for some reason, moving to no webpage if found
        for letter in file:
            if letter.isspace():
                skip = "yes"
                break
        if skip == "yes":
            if os.path.exists(dirpath + "/no_webpage/" + file):
                os.remove(dirpath + "/argosincludes/" + file)
            else:
                os.rename(dirpath + "/argosincludes/" + file, dirpath + "/no_webpage/" + file)
            if os.path.exists(dirpath + "/argosincludes/m/" + file):
                if os.path.exists(dirpath + "/no_webpage/m/" + file):
                    os.remove(dirpath + "/argosincludes/m/" + file)
                else:
                    os.rename(dirpath + "/argosincludes/m/" + file, dirpath + "/no_webpage/m/" + file)
            skip = "no"
            continue

        # add current file to web Argos static page address then plug into function
        desktop_url = "https://www.argos.co.uk/static/ArgosPromo3/includeName/" + file
        web_page_download(desktop_url, file, dirpath)
        

    # go through files found on web with no redirects for mobile file
    for file in os.listdir(dirpath + "/changed_files"):
        
        # ignoring m folder 
        if file == "m":
            continue

        # add current file to mobile address and set optional parameters, then plug into function
        mobile_url = "https://www.argos.co.uk/static/ArgosPromo3/mobile/true/includeName/" + file
        m, header_identifier, footer_identifier = 'm/', 'class="cmsBlock', 'id="footerNav'
        web_page_download(mobile_url, file, dirpath, m, header_identifier, footer_identifier)

    # removing changed files directory
    rmtree(dirpath + "/changed_files")

    # making sure program ran and folder isn't empty before deleteing currently existing folder
    src_argosincludes = (dirpath + "/argosincludes")
    fso = com.Dispatch("Scripting.FileSystemObject")
    folder = fso.GetFolder(src_argosincludes)
    logging.debug(str(folder.Size) + "B folder size")

    # moving files to shared server
    if folder.Size > 100000 :
        if os.path.exists('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes'):
            if os.path.exists('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes/m'):
                rmtree('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes/m')
            rmtree('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes')
            logging.debug("argosincludes successfully removed")
        dest_argosincludes = '//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/New_project/argosincludes'
        copytree(src_argosincludes, dest_argosincludes)
        logging.debug("argosincludes successfully copied")
        log_path = dirpath + '/' + log_name 
        log_dest = dest_argosincludes + log_name
        copyfile(log_path, log_dest)
    else:
        logging.debug("The downloaded files were empty, haven't been copied across")


        
def web_page_download(current_url, file, dirpath, m = '', header_identifier = 'id="staticcontent', footer_identifier = 'id="targetProducts'):
    """Downloads the html from the live site of the desired url and extracts the desired html for the static pages content section. Any pages that have been found to redirect will be added to a Redirects folder and pages that are no longer live will be added to a No Webpage folder. 
        current_url is the url for teh webpage to have it's html downloaded
        file is the name of the file that the extracted html is stored in
        m is an optional paramter that signifies if it's a mobile page or not; it's empty by default
        header_identifier is an optional parameter that is used to help identify when the static content to be extracted from the live page starts. The default parameter (id="staticcontent) is used to find desktop pages
        footer_identifier is an optional parameter that is used to help identify when the static content to be extracted from the live page ends. The default parameter (id="targetProducts) is used to find desktop pages"""

    logging.debug(current_url)
    # catching files that no longer have a webpage and storing the webpages that dont in no_wepage folder
    try:
        response = urllib.request.urlopen(current_url)
    except:
        try:
            if(m == ""):
                current_url = "https://www.argos.co.uk/static/StaticDisplay/includeName/" + file
                response = urllib.request.urlopen(current_url)
                logging.debug(current_url)
            else:
                current_url = "https://www.argos.co.uk/m/static/StaticDisplay/includeName/" + file
                response = urllib.request.urlopen(current_url)
                logging.debug(current_url)
        except:
            if os.path.exists(dirpath + "/no_webpage/" + file):
                os.remove(dirpath + "/argosincludes/" + file)
            else:
                os.rename(dirpath + "/argosincludes/" + file, dirpath + "/no_webpage/" + file)

        if os.path.exists(dirpath + "/argosincudes/m/" + file):
            if os.path.exists(dirpath + "/no_webpage/m/" + file):
                os.remove(dirpath + "/argosincludes/m/" + file)
            else:
                os.rename(dirpath + "/argosincludes/m/" + file, dirpath + "/no_webpage/m/" + file)
        return

    # checking for redirects and adding to redirect folder if ecomm and if mcomm using alternative path
    if(response.geturl() != current_url):
        if(m == ""):
            if os.path.exists(dirpath + "/redirects/" + file):
                os.remove(dirpath + "/argosincludes/" + file)
            else:
                os.rename(dirpath + "/argosincludes/" + file, dirpath + "/redirects/" + file)
            
            if os.path.exists(dirpath + "/argosincludes/m/" + file):
                if os.path.exists(dirpath + "/redirects/m/" + file):
                    os.remove(dirpath + "/argosincludes/m/" + file)
                else:
                    os.rename(dirpath + "/argosincludes/m/" + file, dirpath + "/redirects/m/" + file)
            return
        else:
            current_url = "https://www.argos.co.uk/m/static/ArgosPromo3/mobile/true/includeName/" + file
            response = urllib.request.urlopen(current_url)
            if(response.geturl() != current_url):
                if os.path.exists(dirpath + "/argosincludes/m/" + file):
                    os.rename(dirpath + "/argosincludes/" + m + file, dirpath + "/redirects/" + m + file)
                    return
                
    webcontent = response.read()

    # have to convert bytes to string as some reason reading in bytes
    actualwebcontent = webcontent.decode("windows-1252", "ignore")
    
    # check for index of start of page and end of page then add content between indexes to a variable

    try:
        pagestart = actualwebcontent.index(header_identifier)  + 30
        pageend = actualwebcontent.index(footer_identifier) - 150
        page_content = actualwebcontent[pagestart:pageend]
    except:
        try:
            pagestart = actualwebcontent.index('id="staticcontent')  + 35
            pageend = actualwebcontent.index('id="targetProducts') - 155
            page_content = actualwebcontent[pagestart:pageend]
        except:
            logging.debug("This should never show")
            return

    # open new file and write webcontent html to file
    with open(dirpath + "/changed_files/" + m + file, 'w') as f:
        try:
            f.write(page_content)
        except:
            logging.debug("Problem with charset")

    # checking to see if page is just redirect
    if ':redirectURL' in page_content:
        if os.path.exists(dirpath + "/redirects/" + "front_end_redirect_" + file):
            os.remove(dirpath + "/argosincludes/" + file)
        else:
            os.rename(dirpath + "/argosincludes/" + file, dirpath + "/redirects/" + "front_end_redirect_" + file)
        os.remove(dirpath + "/changed_files/" + file)

    # add sliced content to new file then close both files
    else:
        with open(dirpath + "/argosincludes/" + m + file, 'w') as final_file, open(dirpath + "/changed_files/" + m + file, 'r') as f:
            for line in f:
                if not line.isspace():
                    final_file.write(line)

def findandmove(path, dest):
    """Adds any new files found in current BAU folder to the ArgosIncludes folder. 
        path is the path to the BAU folder of interest.
        dest is the path to the local Argosincludes folder which should be in the same directory as the program"""

    # going through files in function path
    for file in os.listdir(path):

        true_path = path + '/' + file
        true_dest = dest + '/' + file

        # checking to see if file - ignoring folders
        if os.path.isfile(true_path):
            
            # ignore these two files
            if file == '.DS_Store' or file == 'Thumbs.db':
                continue

            # check to see if file already in argosinclude, if not copy new file to folder
            if not os.path.exists(true_dest):
                copyfile(true_path, true_dest)
                logging.debug(file + ' copied')

if __name__ == "__main__":
    main()