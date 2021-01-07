import os
from shutil import copyfile

def main():
    # get current directory
    dirpath = os.getcwd()

    # check for necessary directories and generate if not there, declare required variables
    if not os.path.isdir(dirpath + "/service"):
        os.mkdir(dirpath + "/service")
        os.mkdir(dirpath + "/service/no_service")
        os.mkdir(dirpath + "/service/no_service/m")
        os.mkdir(dirpath + "/service/needtochange_service")
        os.mkdir(dirpath + "/service/needtochange_service/m")
        os.mkdir(dirpath + "/service/needtocompletelychange_service")
        os.mkdir(dirpath + "/service/needtocompletelychange_service/m")
        os.mkdir(dirpath + "/service/reallyold_service")
        os.mkdir(dirpath + "/service/reallyold_service/m")
    

    folder = "/argosincludes"
    service_check(dirpath, folder)
    service_check(dirpath, folder, m = "/m")

def service_check(pathroute, folder, m = ""):

    desired_folder = pathroute + folder + m
    for file in os.listdir(desired_folder):
        print(file)
        if file == 'm':
            continue
        if file == 'Thumbs.db':
            continue

        with open(desired_folder + "/" + file) as f:
            content = f.read()
            if '/wcsstore/argos/en_GB/siteAssets/service-messages/argos_service_messages-nolink.js' in content:
                continue
            elif '/wcsstore/argos/en_GB/siteAssets/service-messages/argos_service_messages-110219.js' in content:
                src_needtochange_service = (desired_folder + "/" + file)
                dest_needtochange_service = (pathroute + "/service/needtochange_service" + m + "/" + file)
                copyfile(src_needtochange_service, dest_needtochange_service)
            elif '="service-messag' in content:
                src_needtocompletelychange_service = (desired_folder + "/" + file)
                dest_needtocompletelychange_service = (pathroute + "/service/needtocompletelychange_service" + m + "/" + file)
                copyfile(src_needtocompletelychange_service, dest_needtocompletelychange_service)
            elif '/wcsstore/argos/en_GB/images/suppliershop/sitebuilder/ui/service_' in content or '/wcsstore/argos/en_GB/images/suppliershop/sitebuilder/ui/row_3/service_3col' in content or '/wcsstore/argos/en_GB/images/suppliershop/ui/row_3/service_3col_' in content:
                src_reallyold_service = (desired_folder + "/" + file)
                dest_reallyold_service = (pathroute + "/service/reallyold_service" + m + "/" + file)
                copyfile(src_reallyold_service, dest_reallyold_service)
            else:
                src_no_service = (desired_folder + "/" + file)
                dest_no_service = (pathroute + "/service/no_service" + m + "/" + file)
                copyfile(src_no_service, dest_no_service) 

        

if __name__ == "__main__":
    main()