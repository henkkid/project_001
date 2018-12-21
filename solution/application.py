#ask user for number of students
while True:
    try:
        number_of_students = int(input("how many first year students are there? "))
    except ValueError:
        print("I do not understand that, try again")
        continue
    else:
        break

list_of_students_age = []

#fill list of ages of students by asking the user
for x in range(1,  number_of_students + 1):

    while True:
        try:
            age = int(input(f"what is the age of student {x}? "))
        except ValueError:
            print("I do not understand that, try again")
            continue
        else:
            break

    list_of_students_age.append(age)

#set variables to zero
count = 0
combined_age = 0

#count the number of underaged people and combine all the ages for caculating the avarage
for age in list_of_students_age:
    if age < 18:
        count = count + 1

    combined_age = combined_age + age

#calculate avarage
average = combined_age / number_of_students

#bubblesort the list_of_students_age
for passnum in range(len(list_of_students_age)-1, 0, -1):
    for i in range(passnum):
        if list_of_students_age[i]>list_of_students_age[i+1]:
            temp = list_of_students_age[i]
            list_of_students_age[i] = list_of_students_age[i+1]
            list_of_students_age[i+1] = temp


#print everything on the screen
print(f"the number of students that is underage is {count}")
print(f"the average age is {average}")
print("if all the ages are sorted the result is: ")
for item in list_of_students_age:
    print(item)
