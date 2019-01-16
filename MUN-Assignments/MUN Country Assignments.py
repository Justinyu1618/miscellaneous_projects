import random


def inputCountries():
    choices = open('Country Requests.txt', 'r+')
    result = {}
    name_col = choices.readline().split(",").index("Name")
    for line in choices:
        templist = line.split(",")
        formattedlist = []
        for x in templist[name_col: name_col+10]:
            formattedlist.append(x)
        result[formattedlist[0]] = formattedlist[1:]
    return result

def pickRandom(a):
    #print(a)
    return a[int(random.random()* len(a))]

def getLast(n):
    return n[len(n)-1]

def checkOverlap(n, key, week, dictionary):
    keys = list(dictionary.keys())
    for i in range(len(keys)):
        if(dictionary[keys[i]] != None and len(dictionary[keys[i]]) == week):
            if(dictionary[keys[i]][week-1] == n or n in dictionary[key]):
                return True
    return False

def countryAssignments(n):
    names = list(n.keys())
    result = {}
    week = 1
    
    #populate result dictionary
    for i in range(len(names)):
        result[names[i]] = []

    for j in range(1, 11):
        result[names[0]].append(pickRandom(n[names[0]]))
        for i in range(1,len(names)):
            templist = list(n[names[i]])
            for x in range(100): #change to forever loop
                random = pickRandom(templist)
                if(not checkOverlap(random, names[i], j, result) and random != ''):
                    #print("Adding" , i)
                    result[names[i]].append(random)
                    n[names[i]].remove(random)
                    break;
                else:
                    templist.remove(random)
                    if(len(templist) == 0):
                        clearListRow(j, result)
                        return result

    return result

def clearListRow(week, n):
    names = list(n.keys())

    for i in range(0,len(names)):
        if(len(n[names[i]]) == week):
            n[names[i]].remove(getLast(n[names[i]]))

    return True
    
def newAssignments():
    result = countryAssignments(inputCountries())
    assignments = open('Country Assignments.txt', 'w')
    for key in result:
        assignments.write(str(key) + ":" + str(result[key]) + "\n")
    return countryAssignments(inputCountries())
        
    



countries = inputCountries()

newAssignments()
