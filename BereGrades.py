# admins dictionary has my login credentials ...pliz use them to access the programwhen you run it
admins = { 'Ras':'Bere',
           'Py':'6666',
           'Admin':'Dumbass'}
studentDict = {'Min':[3.54],
               'Omer':[3.66],
               'Marbin': [3.45]}

def enterNew():
    zita = input('Student Name: ').title()
    mark = input('Grade: ')

    studentDict[zita] = mark
    print(zita, 'Has been added ')
    view_grades()

def enterGrades():
    print("""
          ******************************************
          +     ENTER STUDENT GRADE                +
          +                                        +
          ****************************************** """)
    zita = input('Student Name: ').title()
    mark = input('Grade: ')
    mark = int(mark)
    if zita in studentDict:
        print('Adding Grades....')
        studentDict[zita].append(mark)
        view_grades()
    elif zita not in studentDict.keys():
        add_new = input('{} not is sytem, ADD ? Y/n?'.format(zita))
        add_new = add_new.lower()
        if add_new != 'n':
            zita = input('Student Name: ').title()
            mark = input('Grade: ')
            studentDict[zita] = mark
            print()
            print("###################################")
            print(zita, 'Has been added ')
            print("###################################")
            view_grades()
        else:
            print()
            print("You did not add {} to system! ".format(zita))
            
    else:
        print('Student does not exist')

def rmvStudent():
    print("""
          ******************************************
          +     REMOVE STUDENT GRADE                +
          +                                         +
          ****************************************** """)
    zita = input('Student Name: ').title()

    if zita in studentDict:
        print('Removing Student.... ', zita)
        del studentDict[zita]
        view_grades()
        print()
        print(zita, 'Has been removed!.... ')
    else:
        print('Student does not exist')

def view_grades():
    print()
    for k,v in studentDict.items():         #chex all students in dict
        print()
        print("{} has {} GPA ".format(k,v))


def main():
    
    print("""
             
      Welcome to BERE School Manangement Sytem(SMS)
    [1] - Enter New Student
    [2] - Update Grades
    [3] - Remove Student
    [4] - View Student Grades
    [5] - Exit
    """)
    act = input('What would you Like to Do?(enter a number): ')

    if act == '1':
        enterNew()
    elif act =='2':
        enterGrades()
    elif act =='3':
        rmvStudent()
    elif act =='4':
        view_grades()
    elif act == '5':                 #this line exits the program (by selecting option )
        a = input("Are you sure you want to exit? Y/n? ").lower()
        if a == 'y':
            exit()
        else:
            main()
        
    else:
        print('No Valid Choice Was Chosen!')
def login():
    print("""
          *************************************************
          +       WELCOME TO MY FIRST PROJECT             +
          + "IT STORES STUDENT GRADES using PYTHON 3"     +
          +                                               +
          + made  by: Elisha Bere                         +
          *************************************************
          """)
    print()
    login = input('Username: ').title()
    passwd = input('Password: ')

    if login in admins:                               #chex to see if login input == one in list admins
        if admins[login]== passwd:                   #chex if login name in admin == pwd entered
            print('Succesfully Logged in ,',login)
            while True:
                main()
        elif admins[login] != passwd:
               print('username and password is incorrect')
            
    elif login not in admins :
        print('username and password is incorrect')
    
login()
