#M02 Lab - Case Study: if...else and while
"""
Reed Peglow
SDEV 220
GPA ranking script
A Python script that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll
Each itteration will update a list and print out results of all students entered at the end of the program
"""
# start function
def ranking():
    # create empty lists
    dean_list= []
    honor_roll = []
    non_honor = []
# flag for while loop
    last_name = input("What is student's last name? [type ZZZ to quit] :")
# enter ZZZ to escape loop
    while last_name != "ZZZ":
            
            # add first name and gpa from input        
            first_name = input("What is student's first name? :")
            try:
                gpa = float(input("What is student's GPA? :"))
            
                      #check for correct value entered
                if gpa > 4 or gpa < 0 :
                    print("GPA must be between 4.0 and 0.0. Please re-enter Student Information.")
                
#logic for sorting GPA, adding to each list once sorted
                elif gpa >= 3.5: 
                    print(first_name,last_name + " has made the Dean's List.")
                    student_info = first_name, last_name, gpa
                    dean_list.append(student_info)
                elif gpa <= 3.4 and gpa >= 3.25: 
                    print(first_name,last_name + " has made the Honor Roll.")
                    student_info = first_name, last_name, gpa
                    honor_roll.append(student_info)
                    
                else:
                    print(first_name,last_name + " must improve their GPA to be eligable.")
                    student_info = first_name, last_name, gpa
                    non_honor.append(student_info)
        #value error for float checking
            except ValueError:
                 print("GPA must be between 4.0 and 0.0. Please re-enter Student Information.")
            # flag reset for while loop
            last_name = input("What is student's last name? [type ZZZ to quit] :")

           
            #print for each list 
    print(f"Dean's List students are {dean_list}")
    print(f"Honor Roll students are {honor_roll}")
    print(f"Students who don't have high enough GPA are {non_honor}")



        
        #call function
ranking()
