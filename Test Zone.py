class Teams():
    def __init__(self, country, score):
        self.country = country
        self.score = score

    def scores(self, team):  # methode for the user to input and change the result or score for one team
        self.score = input(f"input the score for  {team.country} : ")


class TournamentGroups():
    def __init__(self, name):
        self.name = name

    def printourna(self):
        pass

    # Function for organizing the competition
    def organize_competition(self):

        print(Teams)

    # def Groups_in_worldcup(self, Teams):

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


class qfinal:
    def __init__(self):
        Arr1 = []
        pass


class sfinal():
    def __init__(self, max_teams1):
        self.max_teams1 = max_teams1
        self.match1 = []
        self.match2 = []

    def add_teams(self, teams):
        if len(self.match1) < self.max_teams1:  # append the teams that play the first semi final into match1
            self.match1.append(teams)

    def add_teams2(self, teams):
        if len(self.match2) < self.max_teams1:  # apppend the teams that play the second semi final into match2
            self.match2.append(teams)

    def winners(self,
                match):  # methode to get the winners of each match,the attribute match takes an array(match1,match2)
        if match[0].score > match[1].score:
            print(f"the winner is  {match[0].country}")
            match = match.remove(match[1])
        else:
            print(f"the winner is {match[1].country}")
            match = match.remove(match[0])


class final():
    def __init__(self, winner):
        self.finalist = []
        self.winner = winner

    def addfinalist(self, leak1, leak2):
        self.finalist.append(leak1)
        self.finalist.append(leak2)


# teams = Teams("Netherlands")

# TournamentGroups = groups("one")
# organize_competition()
fp = TournamentGroups("1")
# fp.organize_competition()
# fp.Groups_in_worldcup()


groupa = [{"Qatar,", 0}, {"Ecuador", 0}, {"Senegal", 0}, {"Netherlands", 0}]
groupb = [{"England", 0}, {"Iran", 0}, {"USA", 0},
         {"Wales", 0}]
groupc= [{"Argentina,", 0}, {"Saudi Arabia", 0}, {"Mexico", 0}, {"Poland", 0}]
groupd= [{"France", 0}, {"Denmark", 0},
         {"Tunisia", 0}, {"Australia", 0}]
groupe= [{"Belgium,", 0}, {"Canada", 0}, {"Morocco", 0}, {"Croatia", 0}]
groupf= [{"Brazil", 0}, {"Serbia", 0},
         {"Switzerland", 0}, {"Spain", 0}, {"Costa Rica", 0}, {"Germany", 0}, {"Japan", 0},
         {"Cameroon", 0}]
groupg= [{"Portugal,", 0}, {"Ghana", 0}, {"Uruguay", 0}, {"Korea Republic", 0}]
grouph= [{"Portugal,", 0}, {"Ghana", 0}, {"Uruguay", 0}, {"Korea Republic", 0}]

Teams = groupa + groupb + groupc +groupd+groupe+groupf+groupg+grouph
# Teams.append()
print(Teams)
#print("Teams",Teams)


print("=====================================================================")

class ro16:
    def _init_(self):
        self.next_round=[]
        self.half1=[]
        self.half2=[]
    def add_team(self,Team):
        self.next_round.append(Team)
    def make_half(self):
        for i in range(len(self.next_round)):
            if i in [3,2,4,6,8,11,12,15,26,23,18,19,20,22,28,31]:
                self.half1.append(self.next_round[i])
            else:
                self.half2.append(self.next_round[i])


    


