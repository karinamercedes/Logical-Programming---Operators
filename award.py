# ● Create a new Python file in this folder called award.py.
# ● Design a program that determines the award a person competing in a
#  triathlon will receive.
# ● Your program should read in the times (in minutes) for all three events of a
#  triathlon, namely swimming, cycling, and running, and then calculate and
#  display the total time taken to complete the triathlon.
# ● The award a participant receives is based on the total time taken to
#  complete the triathlon. The qualifying time for awards is 100 minutes.

# Display the award that the participant will receive based on the following criteria:
# Qualifying Criteria | Time Range | Award

# Within the qualifying time. | 0 - 100 minutes | Provincial Colours
# Within 5 minutes of the qualifying time. | 101 - 105 minutes | Provincial Half Colours
# Within 10 minutes of the qualifying time. | 106 - 110 minutes | Provincial Scroll
# More than 10 minutes off from the qualifying time. | 111+ | minutes No award

#Request inputs
swimming_time = int(input("Enter swimming time (in minutes): "))
cycling_time = int(input("Enter cycling time (in minutes): "))
running_time = int(input("Enter running time (in minutes): "))

# Calculate total time
total_time = swimming_time + cycling_time + running_time

# Print total time in a separate new line
print(f"\nTotal Time: {total_time} minutes")

# Conditions
if total_time <= 100:  
    print("Your award is : Provincial Colours")
elif total_time >= 101 and total_time < 106 :
    print("Your award is : Provincial Half Colours" )
elif total_time >= 106 and total_time < 111 :
    print("Your award is : Provincial Scroll" )
else:
    print("No award for you today.")