import csv
with open('Previous_Elections_1997-2013.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    parties = []
    for row in csv_reader:
        parties.append(row["Party"])
keyList=[]
for i in parties:
    if i not in keyList:
        keyList.append(i)
Candidate=[]
dis={}
for row in keyList:
    Candidate = []
    with open('Previous_Elections_1997-2013.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            if row == i["Party"]:
                Candidate.append(i["Candidate"])
        dis.update({row:Candidate})
TurncoatList = []
TurncoatData = {}
party = []
count = 0
print("Turncoats are\n")
for i in keyList:
    memberOfParty = dis.get(i)
    party = []
    me = ""
    check = True
    for z in memberOfParty:
        for j in dis:
            if i == j or j == 'IND' or i == 'IND':
                q = 0
            else:
                allmember = dis.get(j)
                for a in allmember:
                    if (z == a):
                        me = a
                        party.append(j)
                        if a not in TurncoatList:
                            TurncoatList.append(a)
                            count = count + 1
                            check = False
                        break
        if check == False:
            party.append(i)
            print(me, " ", party)
            check = True
        party = []
print("Total Turncoats are :: ", count)