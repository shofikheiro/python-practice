''' If-elif-else rule:
If condition1 is True:
  Then perform action1 and exit if-elif-else block
If condition2 is True:
  Then perform action2 and exit if-elif-else block
If neither condition1 nor condition2 are True:
  Then perform action3 and exit if-elif-else block
'''

# Function to check if a Bangkit Cohort is required to submit an abstract
# Function name is abstract_submission_requirement
# Parameters are name and reason for not attending
def abstract_submission_requirement(name, reason_for_not_attending):
    
    # Condition 1 : missed session for an indispensable event ; Sick or Ill or Natural Disaster
    # Action 1 : print message : is not required to submit an abstract for the missed session.
    if reason_for_not_attending == "Sick" or "Ill" or "Natural Disaster":
        message = name + " " + "is not required to submit an abstract for the missed session."

    # Condition 2 : missed session for an indispensable event ; Thesis Related or Exam or Family Emergency or Personal Urgency or D-Day Technical Problem
    # Action 2 : print message : is required to submit an abstract for the missed session at a later date.
    elif reason_for_not_attending == "Thesis Related" or "Exam" or "Family Emergency" or "Personal Urgency" or "D-Day Technical Problem":
        message = name + " " + "is required to submit an abstract for the missed session at a later date."

    # Condition 3 : missed session for a dispensable event
    # Action 3 : print message : is required to submit an abstract for the missed session immidiately.
    else:
        message = name + " " + "is required to submit an abstract for the missed session immidiately."
    
    # End of if-elif-else block. The next line returns the output from the if-elif-else block.
    return message

# I'm expecting the result to be "name" + "message"
print(abstract_submission_requirement("Shofiyya", "Exam"))

# It failed threee times but I succeed in the end
# I think it's safe to say that I am ready to move on to the next module