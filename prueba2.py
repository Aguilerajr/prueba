class Teams():
    def __init__(self, country, score):
        self.country = country
        self.score = score

    def scores(self, team): #methode for the user to input and change the result or score for one team
        self.score = input(f"input the score for  {team.country} : ")

class TournamentGroups:
    def __init__(self, totalteams, totalgroups, winnersofgroup, pointstable):
        self.totalteams = totalteams
        self.totalgroups = totalgroups
        self.winnersofgroup = winnersofgroup
        self.pointstable = pointstable

    def printourna(self):
        print(self.totalteams, self.totalgroups, self.winnersofgroup, self.pointstable)

    # Function for organizing the competition
    def organize_competition(self):
        teams = []
        for i in range(32):
            team = team(f'Team {i + 1}')

        teams.append(team)

        # Assign teams to 8 group objects
        groups = []
        for i in range(8):
            TournamentGroups_Teams = Teams[i * 4:(i + 1) * 4]
            TournamentGroups = Group(f'Group {i + 1}', group_Teams)
            groups.append(TournamentGroups)

class round16(Teams):
    def __init__(self, max_teams1):
        self.max_teams1 = max_teams1
        self.match1 = []
        self.match2 = []

    def add_teams(self, teams):
        if len(self.match1) < self.max_teams1:
            self.match1.append(teams)

    def add_teams2(self, teams):
        if len(self.match2) < self.max_teams1:
            self.match2.append(teams)

    def winners(self, match):
        if match[0].score > match[1].score:
            print(f"the winner is  {match[0].country}")


        else:
            print(f"the winner is {match[1].country}")

    def winners1(self, match):
        if match[2].score > match[3].score:
            print(f"the winner is  {match[2].country}")



        else:
            print(f"the winner is {match[3].country}")

    def winners2(self, match):
        if match[4].score > match[5].score:
            print(f"the winner is  {match[4].country}")


        else:
            print(f"the winner is {match[5].country}")

    def winners3(self, match):
        if match[6].score > match[7].score:
            print(f"the winner is  {match[6].country}")


        else:
            print(f"the winner is {match[7].country}")

class qfinal(Teams):
    def __init__(self, max_teams1):
        self.max_teams1 = max_teams1
        self.match1 = []
        self.match2 = []
    def add_teams(self, teams):
        if len(self.match1) < self.max_teams1: #append the teams that play the first semi final into match1
            self.match1.append(teams)
    def add_teams2(self, teams):
        if len(self.match2) < self.max_teams1:  # apppend the teams that play the second semi final into match2
            self.match2.append(teams)
    def winners(self, match):
        if match[0].score > match[1].score:
            print(f"the winner is  {match[0].country}")
        else:
            print(f"the winner is {match[1].country}")

    def winners1(self, match):
        if match[2].score > match[3].score:
            print(f"the winner is  {match[2].country}")
        else:
            print(f"the winner is {match[3].country}")
    def winners2(self, match):
        if match[4].score > match[5].score:
            print(f"the winner is  {match[4].country}")
        else:
            print(f"the winner is {match[5].country}")
    def winners3(self, match):
        if match[6].score > match[7].score:
            print(f"the winner is  {match[6].country}")
        else:
            print(f"the winner is {match[7].country}")

class sfinal(Teams):
    def __init__(self, max_teams1):
        self.max_teams1 = max_teams1
        self.match1 = []
        self.match2 = []

    def add_teams(self, teams):
        if len(self.match1) < self.max_teams1: #append the teams that play the first semi final into match1
            self.match1.append(teams)

    def add_teams2(self, teams):
        if len(self.match2) < self.max_teams1:  # apppend the teams that play the second semi final into match2
            self.match2.append(teams)

    def winners(self, match): #methode to get the winners of each match,the attribute match takes an array(match1,match2)
        if match[0].score > match[1].score:
            print(f"the winner is  {match[0].country}")
            match = match.remove(match[1])
        else:
            print(f"the winner is {match[1].country}")
            match = match.remove(match[0])
            
class final():
    def __init__(self,winner):
        self.finalist = []
        self.winner = winner

    def addfinalist(self,leak1,leak2):
        self.finalist.append(leak1)
        self.finalist.append(leak2)

round_16 = round16(16)
team1 = Teams("Netherland", 0)
team2 = Teams("USA", 0)
team3 = Teams("Argentina", 0)
team4 = Teams("Australia", 0)
team5 = Teams("France", 0)
team6 = Teams("Poland", 0)
team7 = Teams("England", 0)
team8 = Teams("Senegal", 0)
team9 = Teams("Japan", 0)
team10 = Teams("Croatia", 0)
team11 = Teams("Brazil", 0)
team12 = Teams("SouthKorea", 0)
team13 = Teams("Morocco", 0)
team14 = Teams("Spain", 0)
team15 = Teams("Portugal", 0)
team16 = Teams("Switzerland", 0)
round_16.add_teams(team1)
round_16.add_teams(team2)
round_16.add_teams(team3)
round_16.add_teams(team4)
round_16.add_teams(team5)
round_16.add_teams(team6)
round_16.add_teams(team7)
round_16.add_teams(team8)
round_16.add_teams2(team9)
round_16.add_teams2(team10)
round_16.add_teams2(team11)
round_16.add_teams2(team12)
round_16.add_teams2(team13)
round_16.add_teams2(team14)
round_16.add_teams2(team15)
round_16.add_teams2(team16)
print(f"Match 1 is {round_16.match1[0].country} and {round_16.match1[1].country} ")
team1.scores(team1)
team2.scores(team2)

print(f"Match 2 is {round_16.match1[2].country} and {round_16.match1[3].country} ")
team3.scores(team3)
team4.scores(team4)

print(f"Match 3 is {round_16.match1[4].country} and {round_16.match1[5].country} ")
team5.scores(team5)
team6.scores(team6)

print(f"Match 4 is {round_16.match1[6].country} and {round_16.match1[7].country} ")
team7.scores(team7)
team8.scores(team8)

print(f"Match 1 is {round_16.match2[0].country} and {round_16.match2[1].country} ")
team9.scores(team9)
team10.scores(team10)

print(f"Match 2 is {round_16.match2[2].country} and {round_16.match2[3].country} ")
team11.scores(team11)
team12.scores(team12)

print(f"Match 3 is {round_16.match2[4].country} and {round_16.match2[5].country} ")
team13.scores(team13)
team14.scores(team14)

print(f"Match 4 is {round_16.match2[6].country} and {round_16.match2[7].country} ")
team15.scores(team15)
team16.scores(team16)


round_16.winners(round_16.match1)
round_16.winners1(round_16.match1)
round_16.winners2(round_16.match1)
round_16.winners3(round_16.match1)
round_16.winners(round_16.match2)
round_16.winners1(round_16.match2)
round_16.winners2(round_16.match2)
round_16.winners3(round_16.match2)

qfinals=qfinal(8)
team1=Teams(round_16.winners(round_16.match1))
team2=Teams(round_16.winners1(round_16.match1))
team3=Teams(round_16.winners2(round_16.match1))
team4=Teams(round_16.winners3(round_16.match1))
team5=Teams(round_16.winners(round_16.match2))
team6=Teams(round_16.winners1(round_16.match2))
team7=Teams(round_16.winners2(round_16.match2))
team8=Teams(round_16.winners3(round_16.match2))

qfinals.add_teams(team1)
qfinals.add_teams(team2)
qfinals.add_teams(team3)
qfinals.add_teams(team4)
qfinals.add_teams2(team5)
qfinals.add_teams2(team6)
qfinals.add_teams2(team7)
qfinals.add_teams2(team8)

print(f"Match 1 is {qfinals.match1[0].country} and {qfinals.match1[1].country} ")
team1.scores(team1)
team2.scores(team2)

print(f"Match 2 is {round_16.match1[2].country} and {qfinals.match1[3].country} ")
team3.scores(team3)
team4.scores(team4)

print(f"Match 3 is {qfinals.match2[4].country} and {qfinals.match2[5].country} ")
team5.scores(team5)
team6.scores(team6)

print(f"Match 4 is {qfinals.match2[6].country} and {qfinals.match2[7].country} ")
team7.scores(team7)
team8.scores(team8)

qfinals.winners(qfinals.match1)
qfinals.winners1(qfinals.match1)
qfinals.winners2(qfinals.match2)
qfinals.winners3(qfinals.match2)

