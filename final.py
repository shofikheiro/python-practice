# 1. Problen statement
# 2. Research what tools to use
# 3. Planning
#  Input will be list of events, will sort them by time
# Event will include macine name, username, and tell us if the event is a login or a log out
# We want our script to keep track of users as they log in and out of machines
# If it's login, add to list of users. If it's a log out, remove from list of users.


# This function below is the helper function that will be use to sort the list
def get_event_date(event):
    return event.date

# The function below is the processing function
def current_users(events):
    # Sort events by date using sort method and passing the get_event_date as key
    events.sort(key=get_event_date)
    # Create a dictionary to store the names and users of a machine
    machines = {}
    # Iterate through list of events
    for event in events:
        # Check if the machine affected by the event is in the dictionary. 
        # If it's not, add it with an empty set as the value.
        if event.machine not in machines:
            machines[event.machine] = set()
        # Add user to the list for login events
        # Remove user from the list for logout events
        if event.type == "login:":
            machines[event.machine].add(event.user)
        elif event.type == "logout:":
            machines[event.machine].remove(event.user)
    # This loop will make the dictionary will contain all machines we've seen as keys.
    return machines
    # Printing will be handled in a differennt function

# The dictionary is ready
# The function below is called generate_report which will print the result
def generate_report(machines):
    for machine, users in machine.items():
        if len (users) > 0:
            user_list = ",".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
    def __init__(self, event_date, event_type, machine_name, user) :
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)