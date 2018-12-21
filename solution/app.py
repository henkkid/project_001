while True:
    try:
        number_of_students = int(input("how many first year students are there? "))
    except ValueError:
        print("I do not understand that, try again")
        continue
    else:
        break

list_of_students_age = []

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

count = 0
combined_age = 0

for age in list_of_students_age:
    if age < 18:
        count = count + 1

    combined_age = combined_age + age

average = combined_age / number_of_students


print(f"the number of students that is underage is {count}")
print(f"the average age is {average}")


for passnum in range(len(list_of_students_age)-1, 0, -1):
    for i in range(passnum):
        if list_of_students_age[i]>list_of_students_age[i+1]:
            temp = list_of_students_age[i]
            list_of_students_age[i] = list_of_students_age[i+1]
            list_of_students_age[i+1] = temp


print("if all the ages are sorted the result is: ")
for item in list_of_students_age:
    print(item)


