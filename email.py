### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email:
    has_been_read = False
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line= subject_line
        self.email_content = email_content 
    def mark_as_read(self):
        self.has_been_read = True
        
    

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox =[]    
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    email_1 = Email('example@gmail.com ','Sales ',' Sales report')
    inbox.append(email_1)
    email_2 = Email('freshOutOfBootcamp@aol.com','Noobie :P ','Junior Developers')
    inbox.append(email_2)
    email_3 = Email('RunningOutOfIdeas@hotmail.com','No Idea!! ',' Better to be dumb and handsome than smart and poor')
    inbox.append(email_3)
populate_inbox()    #calling the function at initialisation
    # Create 3 sample emails and add it to the Inbox list. 

def list_emails():
    for index, email in enumerate(inbox):
        print(f'{index} {email.subject_line}' )
 
#     # Create a function which prints the email’s subject_line, along with a corresponding number.


def read_email(index):
   if index<len(inbox):
       print(f'Email address - {inbox[index].email_address} \nSubject Line of - {inbox[index].subject_line} \nThe Email content is - {inbox[index].email_content}')
       inbox[index].mark_as_read()
   else:
       print('Unfortunately Index is out of bounds')    
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Delete email by index (starting at 0)
    4. List Emails Subject Line with Order Number
    5. Read all viewed emails
    6. Quit application
    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        index_option = int(input(f'Please choose the index of the email. It has to be less than {len(inbox)}: '))
        read_email(index_option)
        print('This email has now been marked as read')
    elif user_choice == 2:
        # add logic here to view unread emails
        for email in inbox:
            if email.has_been_read == False:
                print(f'Email address is - {email.email_address} \nThe Subject Line is -  {email.subject_line} \nThe Content of the email is -{email.email_content}\n')                
                email.mark_as_read()
                print('These emails are now marked as read')
            else:
                print('All emails have been read')  
                break #to go back to menu
    elif user_choice == 3:
        
        index_option = int(input(f'Please choose the index of the email to DELETE. It has to be less than {len(inbox)}: '))      
        inbox.pop(index_option)  
        print(f'Email at index {index_option} successfully deleted!')
        
    elif user_choice ==4:
        list_emails() #adding this functionality otherwise it is not used at all.    
    elif user_choice==5: #Adding an option to re-read read emails otherwise no way to access.
        for email in inbox:
            if email.has_been_read == True:
                print(f'Email address is - {email.email_address} \nThe Subject Line is -  {email.subject_line} \nThe Content of the email is -{email.email_content}\n')                
            else:
                print('Please choose to read unread emails option 2')     
                break   
    elif user_choice ==6:
        
        print('Goodbye!!!')
        exit()
    else:
        print("Oops - incorrect input.")

