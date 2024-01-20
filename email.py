### --- OOP Email Simulator --- ###

class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.address = email_address
        self.subject = subject_line
        self.content = email_content
 
    def mark_as_read(self):
        self.has_been_read = True

# Inbox variable stores all email objects received.
inbox = []

def populate_inbox(email_address, subject_line, email_content):
    '''Creates a new email object and add them to the inbox'''
    new_email = Email(email_address, subject_line, email_content)
    inbox.append(new_email)

# Create 3 sample emails and add it to the Inbox list. 
populate_inbox("default@outlook.com", "Welcome", "Welcome to your new email inbox.")
populate_inbox("john.smith@company.com", "Welcome to the company!", "We are looking forward to having you on the team. You should receive details shortly for the onboarding schedule.")
populate_inbox("hr@company.com", "Onboarding schedule", "Please meet at reception at 10am for a tour of the office.")

def list_emails(emails):
    '''Prints the subject line of each email in the input list of emails against a corresponding number.'''
    email_list = enumerate(emails, start=0)
    disp_str = "\nInbox:\n"
    for email in email_list:
        status = "Read" if email[1].has_been_read else "Unread"
        disp_str += f"{email[0]}\t{email[1].subject}\t\t[{status}]\n"
    print(disp_str)

def read_email(index):
    '''Displays email at the index shown in 'list_emails()' and marks email as read.'''
    email = inbox[index]
    disp_str = f"From:\t\t{email.address}\n"
    disp_str += f"Subject:\t{email.subject}\n"
    disp_str += f"Contents:\t{email.content}\n"
    print(disp_str)

    email.has_been_read = True

# --- Email Program --- #

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        while True:
            list_emails(inbox)
            email_index = input("Enter the number of the email you would like to read: ")
            if 0 <= int(email_index) <= len(inbox) - 1:
                read_email(int(email_index))
                break
            else:
                print("Invalid selection. Please try again.")
                continue
        
    elif user_choice == 2:
        unread_emails = []
        for email in inbox:
            if not email.has_been_read:
                unread_emails.append(email)
        
        list_emails(unread_emails)
            
    elif user_choice == 3:
        print("Email inbox is closing...")
        break

    else:
        print("Oops - incorrect input.")

