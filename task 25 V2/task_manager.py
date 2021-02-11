#**************************************# Task 20: task_manager #**************************************#
from datetime import datetime   # Used for the current date used in the add task.

#****************************************************| Functions |****************************************************#

#**************************************# Register Function (admin only) #**************************************#
def reg_user():
    #if user_input == 'r' and username == 'admin':                           #If the user entered 'r' it will enter this block
    file = open("user.txt", "r")                                             #This opens the users text file


#***********************************| CHECKING USERNAME MATCH |***********************************#
    username_in_use = True                                          #We set the default value that a username is in use to true
    file = open("user.txt", "r+")                                   #We open the file and give it read and write permissions

    while username_in_use:                                          #Checks while the username is true
        username = input("Please enter your username: ")            #Requests the user to enter their desired username

        for line in file:                                           #Creates a for loop reading each line in the text document
            line = line.strip()                                     #We strip any white spaces in the file
            username_check = line.split(", ")                       #Splits our usernames and passwords into 2 different lists
            username_check = username_check[0]                      #We check the first list which is the username

            if username in username_check:                          #If the username matches the one in the text document we use this if statment
                print("Username in use")                            #We tell the user that name is in use
                username_in_use = True                              #And we keep the username_in_use to true so it does not fall through
                break                                               #We use this break so that as soon as it matches it does not continue and fall through the rest of the code
            else:
                username_in_use = False                             #If the username is not in the document we set this to false to continue the account creation

#***********************************| Creating password |***********************************#

        if not username_in_use:
            password_match = 0                                              #We will use this variable to test if passwords match

            while password_match == 0:                                      #While the password match is at 0 (which it is by default) it will run this while block
                password = input("Please enter a password: ")
                password_check = input("Please confirm your password: ")

                if password_check == password:                              #We check if the password_check is equal to the password
                    password_match += 1                                     #If it is equal we add one so that we break out the while loop

                else:
                    print("Your passwords did not match, please try again.")#If the passwords didn't match it will print this message and return to the original while loop

#***********************************| Creating user login details |***********************************#

            file.write(f"\n{username}, {password}")                #Once we break out the while loop we write the user details in the text document.

            print("Your account has been created. The program will now stop, launch again to use your account.")

        file.seek(0)                                                #Returns to the top of the text file should the username match a name in the file

    file.close()                                                    #Closes the file to save memory

#======================================================================================================================#


#**************************************# register  (None Admin)  #**************************************#

    #elif user_input == 'r' and username != 'admin':
        #print("You are not an admin. Only admin accounts can create new accounts.")

        #user_input = input("Please enter a value: ").lower()

# #**************************************# Add task #**************************************#
# def add_task():
#     if user_input == 'a':                                                     #If the user entered 'A' we enter the add a task block.
#         user_of_task = input("Please enter the user who will do this task: ")   #All of the below input statments are clearly marked what
#         task_title = input("Please enter the title of the task: ")              #information they'll be holding by their variable name.
#         task_desc = input("Please enter the description of the task: ")
#         due_date = input("Please enter a due date: ")
#         completed = "No"                                                        #Due to the idea of all the tasks being 'no' by default we make the output now
#         date_sub = datetime.date(datetime.now())                                #This gets the date the user submitted the task.
#
#         new_task = f" Assigned to \t\t| \t {user_of_task} , Task \t\t\t\t| \t {task_title} , Date Subbited \t\t| \t {date_sub} , Due Date \t\t\t| \t {due_date} , Task Descirption \t| \t {task_desc}, Completed \t\t\t| \t {completed}\n"
#
#         with open("tasks.txt", "a") as reg_task:                                #We open the tasks text document
#             reg_task.write(new_task)                                            #We write the new task (the long line of code above) and add a \n at the end to make sure that the tasks don't all clunk up on one line
#
#         print("Task has been added.")
#         user_input = input("Please enter a value: ").lower()
#
# #**************************************# View all tasks #**************************************#
# def view_all():
#     if user_input == 'va':                            #If this value was entered we view all the tasks in the text file
#
#         file = open("tasks.txt", "r")
#         read_lines = file.readlines()                   # Reads all the lines
#
#         for user_task in read_lines:
#             user_task = user_task.replace(",", "\n")    # If it is it gets all of them and replaces the ',' with a new line for ease of reading
#             print(user_task)                            # Prints out the user task
#
#         file.close()                                    # Closes the file to save memory
#         user_input = input("Please enter a value: ").lower()
#
#**************************************# View your tasks #**************************************#
def view_mine(username = 'admin'):              #Checks the username to see their tasks [The username input will change as I create the finished product]
    task_num = 1
    file = open("tasks.txt", "r")
    data = file.readlines()  # Reads all the lines
    data_new = []
    for i,e in enumerate(data, 1):

        if e.startswith(username):  #This checks if the username is in the user tasks folder                       #This checks if the username is in the user tasks folder

                    assigned_to, task, ds, dd, td, comp = e.strip(" ").strip("\n").split(",")                                           #Splits the string up by "," so we can easily edit each value
                    task_split = e.split("\n")

                    print(task_num)
                    print(f"Assigned to\t\t\t|\t{assigned_to}")
                    print(f"Task\t\t\t\t|\t{task}")
                    print(f"Date Submitted\t\t|\t{ds}")
                    print(f"Due Date\t\t\t|\t{dd}")
                    print(f"Task Description\t|\t{td}")
                    print(f"Completed\t\t\t|\t{comp}")
                    print("")
                    task_num += 1
    choice = int(input("enter the number of the task you want to display: "))  # Allows the user to select what task they want to change
    for i,e in enumerate(data, 1) :


        if choice == i:  # Checks if the user choice matchs any of the tasks
            print(e)


            print('#********************************************************#')
            print('1 - Mark task as completed')
            print('2 - Edit Task')
            print('-1 - Return to Main Menu')
            print('#********************************************************#')

            changes = int(input("Please enter an option: "))                    #Requests a user to enter a value of what they want to do
            e = e.strip()
            if changes == 1:                                                        #Checks if task is not completed

                if e.endswith("No"):   #TODO [I need to figure out a way that it checks that the 5th item in the list contains the word no]
                    e = e.strip(" ").strip("\n").split(",")
                    e[-1] = "Yes"
                    e = ", ".join(e)
                    data_new.append(e)
                    print("Task completed")

            elif changes == 2:
                if e.endswith("Yes"):
                    print("You can't edit a completed task.")

                else:
                    print('#********************************************************#')
                    print('1 - Edit Username')
                    print('2 - Edit Due Date')
                    print('#********************************************************#')
                    edit_data = int(input("Please enter a value type: "))

                    if edit_data == 1:
                        new_name = input("Please enter the new user to handle the task: ")
                        e = e.strip(" ").strip("\n").split(",")
                        e[0] = new_name
                        e = ", ".join(e)
                        data_new.append(e)
                        print("Task MOdifed successwhat aht")



                    elif edit_data == 2:

                        new_date = input("Please enter the new due date(1/january/2020: ")
                        e = e.strip(" ").strip("\n").split(",")
                        e[3] = new_date

                        e = ", ".join(e)
                        data_new.append(e)
                        print("Task data modified completed")


                    else:
                        print("you can't read sorry try again")
                        return view_mine()

            elif changes == -1:
                return

        else:
            e = e.strip()
            data_new.append(e)

    with open("tasks.txt", "w") as f:
        for i in data_new:
            f.write(i+"\n")






    #file.close()  # Closes the file to save memory
view_mine()

"""
Current issues:

- The program not showing all the possible options that are in the text file (It'll show the first item and then the second after we edit the first line)
- Indentation when printing new data
- The entire file will be reset and only add the new task (I know this is to do with using 'w' and not 'a' when reading the file, however, I need to remove the original line.
"""
# #**************************************# Stats  (admin only)  #**************************************#
# def stats():
#     if username == 'admin' and user_input == 's':                 #This checks if the username is admin and they typed 's'
#         num_users = 0                                               #These are just place holder values
#         num_tasks = 0
#
#         file_user = open("user.txt", "r")                           #Opens the users text document
#         for line in file_user:                                      #Checks the lines in the user file document
#             if line != "\n":                                        #If the line does not have a \n add 1
#                 num_users += 1
#         file_user.close()
#
#         file_task = open("tasks.txt", "r")                          #Checks the tasks text document
#         for line in file_task:                                      #Cehcks each line in the document
#             if line != "\n":                                        #If it does not contain a \n add 1
#                 num_tasks += 1
#         file_task.close()
#
#
#         print(f"The total number of users are | \t {num_users}")    #Prints the num of users
#         print(f"The total number of tasks are | \t {num_tasks}")    #Prints the num of tasks
#
#         user_input = input("Please enter a value: ").lower()
#
# #**************************************# Stats  (None Admin)  #**************************************#
#     elif username != 'admin' and user_input == 's':                 #Checks if the username is not an admin
#         print("Only admins are able to view the statistics page.")  #Tells the user only admins can view this page
#
#         user_input = input("Please enter a value: ").lower()
#
# #==================================================================| END OF FUNCTIONS |==================================================================#
#
#
#
# #**************************************# login #**************************************#
# login = False                                           #This will be used to check if the user is logged in
# user_file = open("user.txt", "r+")                      #Opens the user file
#
# while login == False:                                   #While the logged in variable if false this whole statment will run
#
#     username = input("Please enter your username: ")
#     password = input("Please enter your password: ")
#
#     for line in user_file:                              #Checks the user_file continuously to check for all the details
#         line = line.rstrip()                            #We use this to remove the white space at the end of any user account
#         valid_user, valid_password = line.split(", ")   #Splits the username and password by replaceing the ", "
#
#         if username == valid_user:                      #Checks if the username matches the username in the text file
#             if password == valid_password:              #Checks if the password matches with that account
#                 login = True                            #Sets login to true
#                 print("Correct details!")
#
#     if login == False:                                  #Sets the login to false so that the while loop repeats
#         print("Your details are inncorect.")
#
#     user_file.seek(0)                                   #Goes back to the start of the text document should we need to read through it again.
#
# if username != 'admin' and login == True:               #If the username is not equal to admin, this message will be printed
#     print("#****************************************************************************#")
#     print("Welcome, Please select one of the following tasks you'd like to perform!")
#     print("")
#     print("a  |\t Add a task")
#     print("va |\t View all the tasks")
#     print("vm |\t View all your current tasks")
#     print("e  |\t Exit the program")
#     print("")
#     print("#****************************************************************************#")
#
# if username == 'admin' and login == True:               #Checks if the user is 'admin' and if it is this text block will be displayed
#     print("#****************************************************************************#")
#     print("Welcome, Please select one of the following tasks you'd like to perform!")
#     print("")
#     print("r  |\t Register a user")
#     print("a  |\t Add a task")
#     print("va |\t View all the tasks")
#     print("vm |\t View all your current tasks")
#     print("s  |\t Prints out the total number of users and tasks")
#     print("e  |\t Exit the program")
#     print("")
#     print("#****************************************************************************#")
#
# user_input = input().lower()                                        #This requests the user to input any of the following above lines
#
# while user_input != 'e':                                            #This checks if the user didn't enter 'e', if they did it will not run the loop and the program will exit