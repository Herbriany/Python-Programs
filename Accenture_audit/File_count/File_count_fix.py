import os
import math
from datetime import date, timedelta, datetime

def main():

    # getting start/end date and incrementing by one day, setting up counter variables
    start_date = date(2020, 10, 1) 
    end_date = date(2020, 10, 29)
    day = timedelta(days=1)
    counter = 0
    competition_counter = 0

    # path variables to make it easier to read
    server_route = '//mkfile2/Ecommerce/Creative Team/BAU/'

    # lambda function to find ordinal indicator for paths
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])    
    
    # checking different possible paths for the BAU folder name, iterating through each day from start date til end date
    while start_date <= end_date:

        path_route = server_route + start_date.strftime("%Y") + '/' + start_date.strftime("%m") + '_'
        full_month = start_date.strftime("%B")
        four_char_month = start_date.strftime("%B")[:4]
        three_char_month = start_date.strftime("%b")
        true_ordinal = '/' + ordinal(int(start_date.strftime("%d"))) + ' '
        
        path1 = path_route + three_char_month + true_ordinal + full_month 
        path2 = path_route + three_char_month + true_ordinal + three_char_month 
        path3 = path_route + three_char_month + true_ordinal + four_char_month
        path4 = path_route + full_month + true_ordinal + full_month 
        path5 = path_route + full_month + true_ordinal + four_char_month 
        path6 = path_route + full_month + true_ordinal + three_char_month 
        path7 = path_route + four_char_month + true_ordinal + four_char_month 
        path8 = path_route + four_char_month + true_ordinal + full_month 
        path9 = path_route + four_char_month + true_ordinal + three_char_month 
         

        if os.path.exists(path1):  
            counter, competition_counter = counter_func(path1, counter, competition_counter)            
        elif os.path.exists(path2): 
            counter, competition_counter = counter_func(path2, counter, competition_counter)  
        elif os.path.exists(path3): 
            counter, competition_counter = counter_func(path3, counter, competition_counter)   
        elif os.path.exists(path4): 
            counter, competition_counter = counter_func(path4, counter, competition_counter) 
        elif os.path.exists(path5): 
            counter, competition_counter = counter_func(path5, counter, competition_counter) 
        elif os.path.exists(path6): 
            counter, competition_counter = counter_func(path6, counter, competition_counter)  
        elif os.path.exists(path7): 
            counter, competition_counter = counter_func(path7, counter, competition_counter) 
        elif os.path.exists(path8): 
            counter, competition_counter = counter_func(path8, counter, competition_counter)
        elif os.path.exists(path9): 
            counter, competition_counter = counter_func(path9, counter, competition_counter)

        start_date += day
    
    print("Counter = " + str(counter))
    print("Competition counter = " + str(competition_counter))


def counter_func(path, counter1, counter2, m=''):

    if os.path.exists(path + '/argos/argosincludes' + m):
        for file in os.listdir(path + '/argos/argosincludes' + m):
            if os.path.isfile(path + '/argos/argosincludes' + m + '/' + file):

                # skipping unwanted files and m folder
                if file == "Thumbs.db" or file == "thumbs.db" or file == ".DS_Store":
                    continue

                elif file == "argoscompetitions.htm":
                    
                    counter2 += 1
                    if os.path.exists(path + '/argos/en_GB/images/competitions'):
                        for file in os.listdir(path + '/argos/en_GB/images/competitions'):
                            if file == "Thumbs.db" or file == "thumbs.db" or file == ".DS_Store":
                                continue
                            else:
                                counter2 += 1
                                counter1 -= 1
                else :
                    print('+ ' + path + '/argos/argosincludes' + m + '/' + file)
                    counter1 += 1  

    # checking for m folder then recursing 
    if os.path.exists(path + '/argos/argosincludes' + m + '/m'):
        counter1, counter2 = counter_func(path, counter1, counter2, (m +'/m'))

    # checking for emergency folder then recursing
    if os.path.exists(path + ' - Emergency'):
        pathEmergency = path + ' - Emergency'
        counter1, counter2 = counter_func(pathEmergency, counter1, counter2)

    return counter1, counter2

if __name__ == "__main__":
    main()