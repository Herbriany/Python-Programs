import os
import math
from datetime import date, timedelta, datetime

def main():

    # getting start/end date and incrementing by one day 
    start_date = date(2020, 10, 1) 
    end_date = date(2020, 10, 29)
    day = timedelta(days=1)

    # path variables to make it easier to read
    server_route = '//mkfile2/Ecommerce/Creative Team/BAU/'

    # lambda function to find ordinal indicator for paths
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

    # checking different possible paths for the BAU folder name, iterating through each day from start date til end date

    counter = 0
    
    while start_date <= end_date:

        path_route = server_route + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_'
        full_month = start_date.strftime("%B")
        four_char_month = start_date.strftime("%B")[:4]
        three_char_month = start_date.strftime("%b")
        true_ordinal = '/' + ordinal(int(start_date.strftime("%d"))) + ' '
        
        path1 = path_route + three_char_month + true_ordinal + full_month 
        path2 = path_route + three_char_month + true_ordinal + three_char_month 
        path3 = path_route + full_month + true_ordinal + full_month 
        path4 = path_route + full_month + true_ordinal + four_char_month 
        path5 = path_route + full_month + true_ordinal + three_char_month 
        path6 = path_route + four_char_month + true_ordinal + four_char_month 
        path7 = path_route + four_char_month + true_ordinal + full_month 
        path8 = path_route + four_char_month + true_ordinal + three_char_month 
        path9 = path_route + three_char_month + true_ordinal + four_char_month 

        if os.path.exists(path1):  
            counter = counter_func(path1, counter)            
        elif os.path.exists(path2): 
            counter = counter_func(path2, counter)  
        elif os.path.exists(path3): 
            counter = counter_func(path3, counter)   
        elif os.path.exists(path4): 
            counter = counter_func(path4, counter) 
        elif os.path.exists(path5): 
            counter = counter_func(path5, counter) 
        elif os.path.exists(path6): 
            counter = counter_func(path6, counter)  
        elif os.path.exists(path7): 
            counter = counter_func(path7, counter) 
        elif os.path.exists(path8): 
            counter = counter_func(path8, counter)
        elif os.path.exists(path9): 
            counter = counter_func(path9, counter)

        start_date += day

    print("Counter = " + str(counter))

def counter_func(path, counter1):

    if os.path.exists(path + '/argosie/argosincludes'):
        for file in os.listdir(path + '/argosie/argosincludes'):
            if os.path.isfile(path + '/argosie/argosincludes' + '/' + file):
                # skipping unwanted files and m folder
                if file == "Thumbs.db" or file == "thumbs.db" or file == ".DS_Store":
                    continue
                else :
                    print(path + '/argosie/argosincludes' + '/' + file)
                    counter1 += 1                  

    # checking for emergency folder then recursing
    if os.path.exists(path + ' - Emergency'):
        pathEmergency = path + ' - Emergency'
        counter1 = counter_func(pathEmergency, counter1)

    return counter1

if __name__ == "__main__":
    main()