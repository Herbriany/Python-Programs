import os
import urllib.request
import urllib.parse
from shutil import copytree, rmtree

def main():
    # get current directory
    dirpath = os.getcwd()

    # check for necessary directories and generate if not there, declare required variables
    if not os.path.isdir(dirpath + "/no_webpage"):
        os.mkdir(dirpath + "/no_webpage")
    if not os.path.isdir(dirpath + "/redirects"):
        os.mkdir(dirpath + "/redirects")
    if not os.path.isdir(dirpath + "/changed_files"):
        os.mkdir(dirpath + "/changed_files")
    if not os.path.isdir(dirpath + "/new_argos_includes"):
        os.mkdir(dirpath + "/new_argos_includes")

    skip = "no"

    # go through files in selected directory
    for file in os.listdir(dirpath + "/argosincludes"):

        # skipping thumbs.db and DS_Store
        if file == "Thumbs.db" or file == "thumbs.db" or file == ".DS_Store":
            continue
        
        # checking for spaces in file name which will return broken urls but won't be flagged later for some reason, moving to no webpage if found
        for letter in file:
            if letter.isspace():
                skip = "yes"
                break
        if skip == "yes":
            with open(dirpath + "/no_webpage/" + file, 'w') as f:
                skip = "no"
            continue

        # add current file to web Argos static page address then plug into function
        desktop_url = "https://www.argos.ie/static/ArgosPromo3/includeName/" + file
        web_page_download(desktop_url, file, dirpath)

    # removing changed files directory
    rmtree(dirpath + "/changed_files")

    # moving files to shared server
    if os.path.exists('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/Ireland_project/argosincludes'):
        rmtree('//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/Ireland_project/argosincludes')
        print("argosincludes successfully removed")
    dirpath = os.getcwd()
    src_argosincludes = (dirpath + "/argosincludes")
    dest_argosincludes = '//mkfile2/Ecommerce/Creative Team/-=Team folders=-/Brian/Ireland_project/argosincludes'
    copytree(src_argosincludes, dest_argosincludes)
    print("argosincludes successfully copied")


        
def web_page_download(current_url, file, dirpath):
        print(current_url)

        # catching files that no longer have a webpage and storing the webpages that dont in no_wepage folder
        try:
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            values = {'name': 'Brian Derrig',
                      'location': 'Milton Keynes',
                      'language': 'Python'}
            headers = {'User-Agent': user_agent}
            data = urllib.parse.urlencode(values)
            data = data.encode('ascii')
            req = urllib.request.Request(current_url, data, headers)
            response = urllib.request.urlopen(req)
        except:
            with open(dirpath + "/no_webpage/" + file, 'w') as f:
                return

        # checking for redirects and adding to redirect folder if ecomm and if mcomm using alternative path
        if(response.geturl() != current_url):
            with open(dirpath + "/redirects/" + file, 'w') as f:
                return

        # have to convert bytes to string as some reason reading in bytes
        webcontent = response.read()
        
        with open(dirpath + "/new_argos_includes/" + file, 'w') as final_file:
            try:
                actualwebcontent = webcontent.decode("cp1252", "ignore")
                pagestart = actualwebcontent.index('id="staticcontent')  + 20
                pageend = actualwebcontent.index('id="dropdownmenus') - 130
                page_content = actualwebcontent[pagestart:pageend]
                final_file.write(page_content)
            except:
                print("This should never show")
                return

        # add sliced content to new file then close both files
        with open(dirpath + "/argosincludes/" + file, 'w') as final_file, open(dirpath + "/new_argos_includes/" + file, 'r') as f:
            for line in f:
                if not line.isspace():
                    final_file.write(line)

            


if __name__ == "__main__":
    main()