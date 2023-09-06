def group(ages):
    if(len(ages) == 0):
        return 0
    ages.sort()
    subgroups = []
    subgroup = []
    first = ages[0]
    for age in ages:
        if (age - first <= 2):
            subgroup.append(age)
        else:
            subgroups.append(subgroup)
            first = age
            subgroup = [first]
    subgroups.append(subgroup)
    print(subgroups)
        


#call the function with random unsequential values
ages = [123,11,41,21,2,22,12]
group(ages)




