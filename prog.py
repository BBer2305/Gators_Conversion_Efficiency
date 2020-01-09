# open-webpage.py

import urllib.request, urllib.error, urllib.parse

class team:
    def __init__(self,name,sp,rushE,rushR,passE,passR):
        self.name = name
        self.sp = sp
        self.rushE = rushE
        self.rushR = rushR
        self.passE = passE
        self.passR = passR

url = 'https://www.espn.com/college-football/story/_/id/28251219/sp+-rankings-conference-championship-games'

response = urllib.request.urlopen(url)
webContent = response.read()

file = open("sp_data.txt", "wb")
file.write(webContent)
#file.close()
file = open("sp_data.txt", "r")
for line in file: 
    if "<tr class=\"last\">" in str(line):
        found = line
        break
file.close()
my_string = found.split('<tr class="last"><td>')
i=0
write = False
teamNa = input("Which FBS team would you like to evaluate for? Please spell the name correctly. Please note that only the part of the name before the space is counted: ")
teamN = teamNa
teams = []
while len(teams) == 0:   
    teamN = teamN.split(' ')
    j = 0
    while j < len(teamN):
        for s in my_string:
            if "1. " in my_string[i]:
                write = True
            if write:
                if teamN[j] in my_string[i]:
                    teams.append(my_string[i])
                    print(my_string[i])
            i=i+1
        write = False
        i=0
        j=j+1
    if len(teams) == 0:
        teamN = input("You inputted an invalid team name. Please try again: ")
        write = False
        i = 0
i=1
teamNames = []
for t in teams:
    if teams[i-1].split('</td><td>')[0][2] == " ":
        temp = teams[i-1].split('</td><td>')[0][3:]
    elif teams[i-1].split('</td><td>')[0][3] == " ":
        temp = teams[i-1].split('</td><td>')[0][4:]
    else:
        temp = teams[i-1].split('</td><td>')[0][5:]
    temp = temp.split('(')
    #if len(temp) == 3:
        #print(str(i) + ". " + teams[i-1].split('</td><td>')[0].split('.')[1])
        #.split('.').split('(')[0]
    #else:
        #print(len(temp))
    teamNames.append(temp[0])
    if temp[0][:-1] == teamNa:
        break
    i=i+1

if temp[0][:-1] != teamNa:
    i=1
    for t in teamNames:
        print(str(i) + ". " + teamNames[i-1])
        i=i+1
    print(str(i) + ". None of the Above")
    teamNa = input("Type in the name of the team you would like to select exactly the same way it is listed on the screen: ")
    i = 0
    for t in teamNames:
        if teamNames[i][:-1] == teamNa:
            break
        i=i+1