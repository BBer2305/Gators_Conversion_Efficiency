# open-webpage.py

import urllib.request, urllib.error, urllib.parse

import requests
from bs4 import BeautifulSoup

import csv
import sys
import storage

origTeamNames = storage.origTeamNames #team names that come through in parsing that need to be changed
newTeamNames = storage.newTeamNames #new team names

class team:
    def __init__(self, name):
        self.name = name.replace('.', '')

    def addSPStats(self, sp, spR):
        self.sp = sp
        self.spR = spR

    def addEffeciencies(self, rushE, rushR, passE, passR):
        self.rushE = rushE
        self.rushR = rushR
        self.passE = passE
        self.passR = passR
    
    #print team details
    def getTeam(self):
        print("Team: " + self.name)
        print("Offense SP+: " + self.sp)
        print("Offense SP+ Rank: " + self.spR)
        print("Rushing YPA: " + self.rushE)
        print("Rushing YPA Rank: " + self.rushR)
        print("Passing YPT: " + self.passE)
        print("Passing YPT Rank: " + self.passR, end='\n'*2)

def passByValue(self):
    return self[0],self[1],self[2] #efficiency, name, rating

#function checks if the name of team should be changed so it aligns with other names
def checkIfNameShouldChange(stringToCheck):
    j=0 #indexing
    returnString = ""
    for txt in origTeamNames:
        if stringToCheck.find(txt) != -1: #if string found
            returnString = newTeamNames[j]
            break
        j+=1
    if len(returnString) == 0: #no changes needed
        returnString = stringToCheck
    return returnString

#specifically team name, SP+ rating, SP+ ranking
def generateTeams():
    URL = 'https://www.espn.com/college-football/story/_/id/28497018/final-sp+-rankings-2019-college-football-season'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    job_elems = soup.find_all('td', class_='')
    i=1

    teams = [] #initialize array of teams

    for job_elem in job_elems:
        if i % 5 == 1: #team name is in job_elem
            if job_elem.text.split(' ')[2][0] == '(': #team is a single word
                teams.append(team(checkIfNameShouldChange(job_elem.text.split(' ')[1])))
            elif job_elem.text.split(' ')[3][0] == '(': #team is two words
                teams.append(team(checkIfNameShouldChange(job_elem.text.split(' ')[1] + " " + job_elem.text.split(' ')[2])))
            else: #team is three words
                teams.append(team(checkIfNameShouldChange(job_elem.text.split(' ')[1] + " " + job_elem.text.split(' ')[2] + " " + job_elem.text.split(' ')[3])))
        elif i % 5 == 3: #the SP stats element is in job_elem
            teams[len(teams)-1].addSPStats(job_elem.text.split(' ')[0], job_elem.text.split(' ')[1].split('(')[1].split(')')[0])
        i=i+1

    teams.sort(key=lambda t: t.name) #sort names in alphabetical order
    return teams

def generateRushingStats():
    temp = []

    with open ('2019RushE.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0 #iteration purposes
        for row in csv_reader:
            if line_count > 1: #if not reading from header row
                temp.append((row[0], checkIfNameShouldChange(row[1]), row[11]))
            line_count += 1

    temp.sort(key=lambda t: t[1]) #sort names in alphabetical order
    return temp

def generatePassingStats():
    URL = 'https://www.teamrankings.com/college-football/stat/yards-per-pass-attempt?date=2020-01-20'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    job_elems = soup.find_all('td')
    i=1
    tempArray = [] #(item, item, item)
    temp = [] #((item, item, item), (item, item, item), (item, item, item)...)

    for elem in job_elems:
        if i % 8 < 4 and i % 8 > 0: #if a relevant column is highlighted
            tempString = ""
            isFalse = False
            try: #passes if elem is three words
                if i % 8 == 2:
                    tempString = checkIfNameShouldChange(elem.text.split(' ')[0] + " " + elem.text.split(' ')[1] + " " + elem.text.split(' ')[2])
                else:
                    tempString = elem.text.split(' ')[0] + " " + elem.text.split(' ')[1] + " " + elem.text.split(' ')[2]
                tempArray.append(tempString)
            except IndexError:
                isFalse = True
            if isFalse:
                try: #passes if elem is two words
                    if i % 8 == 2:
                        tempString = checkIfNameShouldChange(elem.text.split(' ')[0] + " " + elem.text.split(' ')[1])
                    else:
                        tempString = elem.text.split(' ')[0] + " " + elem.text.split(' ')[1]
                    tempArray.append(tempString)
                except IndexError: #if elem is only one word
                    if i % 8 == 2:
                        tempString = checkIfNameShouldChange(elem.text.split(' ')[0])
                    else:
                        tempString = elem.text.split(' ')[0]
                    tempArray.append(tempString)
        if i % 8 == 4: #append tuple to array
            temp.append(passByValue(tempArray))
            tempArray.clear() #empty temp array
        i += 1

    temp.sort(key=lambda t: t[1]) #sort
    return temp

def storeRushAndPassStats(teams,rushingStats,passingStats):
    i=0
    for team in teams:
        team.addEffeciencies(rushingStats[i][2], rushingStats[i][0], passingStats[i][2], passingStats[i][0])
        #team.getTeam()
        i+=1
    return teams

def generateTeamName():
    acceptedTeamNames = storage.acceptedTeamNames #options accepted by program
    teamIndex = -1
    currIndex = 0
    currTeam = acceptedTeamNames[0][0] #marks the official name of the team entered by the user
    while teamIndex == -1:
        chosenTeam = input('Which FBS team would you like to evaluate for? Please spell the name correctly. Do NOT include the term "University" in the spelling. Common acronyms are accepted: ')

        for team in acceptedTeamNames:
            if currIndex != team[1]: #updates the official team name
                currIndex = team[1]
                currTeam = team[0]
                if team[2] == True:
                    currTeam = currTeam + " State"
            if (team[0] == chosenTeam and team[2] == False) or ((team[0] + " St") == chosenTeam and team[2] == True) or ((team[0] + " St.") == chosenTeam and team[2] == True) or ((team[0] + " State") == chosenTeam and team[2] == True):
                teamIndex = team[1]
                break
        if (teamIndex == -1):
            print("Error: The entered team name is not valid. Please redo.", end='\n'*2)
        else:
            print(currTeam + " is your chosen team.", end='\n'*2)
            return currTeam, teamIndex

#load data of teams
teams = generateTeams() #team names and SP stats are derived
rushingStats = generateRushingStats() #team rushing stats are derived
passingStats = generatePassingStats() #team passing stats are derived
teams = storeRushAndPassStats(teams, rushingStats, passingStats) #rushing and passing stats are stored in list of teams

chosenTeam, teamIndex = generateTeamName() #user chooses a team