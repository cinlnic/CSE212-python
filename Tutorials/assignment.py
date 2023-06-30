"""
You are creating an assignment reminder app that will
notify the user when assignments are close to the due date.
To implement this you need to add the assingments to a stack
with the assignment due last at the bottom of the stack and
the soonest at the top. Loop through the list and pop the earliest
due date then print the list after each pop.

The solutions should look like the following:
['July 15', 'June 26', 'June 10', 'May 25', 'May 5', 'April 15']
['July 15', 'June 26', 'June 10', 'May 25', 'May 5']
['July 15', 'June 26', 'June 10', 'May 25']
['July 15', 'June 26', 'June 10']
['July 15', 'June 26']
['July 15']
[]

Assignment due dates:

- April 3
- April 15
- May 5
- June 26
- July 15
- June 10
- May 25
"""
# start by creating the empty stack using a list
due = []

# append the due dates with the last due date added first
due.append("July 15")
due.append("June 26")
due.append("June 10")
due.append("May 25")
due.append("May 5")
due.append("April 15")
due.append("April 3")

# loop through the stack and pop the first due date out each time
# then print the list - the last print will be an empty stack
for date in range(len(due)):
    due.pop()
    print(due)
