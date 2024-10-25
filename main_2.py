class Team:
    def __init__(self, country, results=None, finalresult=0, score=0):
        self.country = country
        self.results = 0
        self.score = score
        self.finalresult = finalresult
        self.gd = 0
        self.goal_scored = 0
        self.goal_faced = 0

#team class to represent each team of the worldcup


# Create a list of all 32 teams
teams = [Team("Qatar"), Team("Ecuador"), Team("Senegal"), Team("Netherlands\n"),
         Team("England"), Team("Iran"), Team("USA"), Team("Wales\n"),
         Team("Argentina"), Team("Saudi Arabia"), Team("Mexico"), Team("Poland\n"),
         Team("France"), Team("Australia"), Team("Denmark"), Team("Tunisia\n"),
         Team("Spain"), Team("Costa Rica"), Team("Germany"), Team("Japan\n"),
         Team("Belgium"), Team("Canada"), Team("Morocco"), Team("Croatia\n"),
         Team("Brazil"), Team("Serbia"), Team("Switzerland"), Team("Cameroon\n"),
         Team("Portugal"), Team("Ghana"), Team("Uruguay"), Team("South Korea")]

#array of team object to append them in the order

class Group:
    def __init__(self, name, teams=None):
        self.name = name
        self.teams = teams or []

    def print_teams(self):
        print("Teams in group " + self.name + ":")
        for team in self.teams:
            print(team.country)

    def appendgroups(self, array, a, b, c, d, e, f, g, h): #atributes to be passed(arrays to append)
        a.append(array[0:4])
        b.append(array[4:8])
        c.append(array[8:12])
        d.append(array[12:16])
        e.append(array[16:20])
        f.append(array[20:24])
        g.append(array[24:28])
        h.append(array[28:])

#method to append team objects from the list to a group,just line in the worldcup

    def play_groups(self, group1): #group one represents the array to be passed from the ones appended before
        team1, team2 = group1[0][0], group1[0][1]  #team1 and team 2 are equal to the index passed of the array chosen
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            team1.score = 3
            team1.results = goal1 - goal2
            team2.results = goal2 - goal1
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = 1
            team2.score = 1

        else:
            if goal2 > goal1:
                winner = team2
                team2.score = 3
                team2.results = goal2 - goal1
                team1.results = goal1 - goal2
                print(f"the winner is team  {team2.country}")

        team1.gd = goal1 - goal2
        team2.gd = goal2 - goal1
        team1.finalresult = team1.results
        team2.finalresult = team2.results

    def play_groups2(self, group1):
        team1: object
        team1, team2 = group1[0][2], group1[0][3]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            team1.results = goal1 - goal2
            team2.results = goal2 - goal1
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                team2.results = goal2 - goal1
                team1.results = goal1 - goal2
                print(f"the winner is team  {team2.country}")

        team1.gd += goal1 - goal2
        team2.gd += goal2 - goal1
        team1.finalresult = team1.finalresult + team1.results
        team2.finalresult = team2.finalresult + team2.finalresult

    def play_groups3(self, group1):
        team1, team2 = group1[0][3], group1[0][1]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            team1.results = goal1 - goal2
            team2.results = goal2 - goal1
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                team2.results = goal2 - goal1
                team1.results = goal1 - goal2
                print(f"the winner is team  {team2.country}")

        team1.gd += goal1 - goal2
        team2.gd += goal2 - goal1
        team1.finalresult = team1.finalresult + team1.results
        team2.finalresult = team2.finalresult + team2.finalresult

    def play_groups4(self, group1):
        team1, team2 = group1[0][0], group1[0][2]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            team1.results = goal1 - goal2
            team2.results = goal2 - goal1
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                team2.results = goal2 - goal1
                team1.results = goal1 - goal2
                print(f"the winner is team  {team2.country}")

        team1.gd += goal1 - goal2
        team2.gd += goal2 - goal1
        team1.finalresult = team1.finalresult + team1.results
        team2.finalresult = team2.finalresult + team2.finalresult

    def play_groups5(self, group1):
        team1, team2 = group1[0][1], group1[0][2]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            team1.results = goal1 - goal2
            team2.results = goal2 - goal1
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                team2.results = goal2 - goal1
                team1.results = goal1 - goal2
                print(f"the winner is team  {team2.country}")

        team1.gd += goal1 - goal2
        team2.gd += goal2 - goal1
        team1.finalresult = team1.finalresult + team1.results
        team2.finalresult = team2.finalresult + team2.finalresult

    def play_groups6(self, group1):
        team1, team2 = group1[0][0], group1[0][3]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            team1.results = goal1 - goal2
            team2.results = goal2 - goal1
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                team2.results = goal2 - goal1
                team1.results = goal1 - goal2
                print(f"the winner is team  {team2.country}")

        team1.gd += goal1 - goal2
        team2.gd += goal2 - goal1
        team1.finalresult = team1.finalresult + team1.results
        team2.finalresult = team2.finalresult + team2.finalresult

    def top_two(self, groups1, counter):
        array = [groups1[0][0], groups1[0][1], groups1[0][2], groups1[0][3]]
        for i in range(0, 4):
            array.sort(key=lambda x: x.score, reverse=True)

        round16_teams.append(array[0])
        round16_teams.append(array[1])


round16_teams = []
group = Group(teams)
groups_teams_a = []
group_teams_b = []
group_teams_c = []
group_teams_d = []
group_teams_e = []
group_teams_f = []
group_teams_g = []
group_teams_h = []
#arrays created to append for using them in the append methode and in the rest of the code

# Create 8 groups, each containing 4 teams
group_a = Group("A", teams[:4])
group_b = Group("B", teams[4:8])
group_c = Group("C", teams[8:12])
group_d = Group("D", teams[12:16])
group_e = Group("E", teams[16:20])
group_f = Group("F", teams[20:24])
group_g = Group("G", teams[24:28])
group_h = Group("H", teams[28:])

# Put all the groups in a list
groups = [group_a, group_b, group_c, group_d, group_e, group_f, group_g, group_h]
group.appendgroups(teams, groups_teams_a, group_teams_b, group_teams_c, group_teams_d, group_teams_e, group_teams_f,
                   group_teams_g, group_teams_h)

# code for the first round of matches between the groups
print("THIS IS THE FIRST ROUND OF MATCHES")
print("the game between qatar and ecuador")
group_a.play_groups(groups_teams_a)
print("the game between england and iran")
group_b.play_groups(group_teams_b)
print("the game between Argentina and Saudi Arabia")
group.play_groups(group_teams_c)
print("the game between France and Australia")
group_d.play_groups(group_teams_d)
print("the game between Spain and Costa Rica")
group_e.play_groups(group_teams_e)
print("the game between Belgium and Canada")
group_f.play_groups(group_teams_f)
print("the game between Brazil and Serbia")
group_g.play_groups(group_teams_g)
print("the game between Portugal and Ghana")
group_h.play_groups(group_teams_h)

# code for the second round of matches among the groups
print("THIS IS THE SECOND ROUND OF MATCHES FOR THE WORLD CUP")
print("The first match between Senegal and Netherlands")
group_a.play_groups2(groups_teams_a)
print("the game between the USA and Wales")
group_b.play_groups2(group_teams_b)
print("the game between the Mexico and Poland")
group_c.play_groups2(group_teams_c)
print("the game between denmark and tunisia")
group_d.play_groups2(group_teams_d)
print("the game between Germany and Japan")
group_e.play_groups2(group_teams_e)
print("the game between Morocco and Croatia")
group_f.play_groups2(group_teams_f)
print("the game between Switzerland and Cameroon")
group_g.play_groups2(group_teams_g)
print("the game between Uruguay and Korea Republic")
group_h.play_groups2(group_teams_h)

# code for the third round of games
print("THIS IS THE THIRD ROUND OF GAMES")
print("the first match between Ecuador and Netherlands")
group_a.play_groups3(groups_teams_a)
print("the game between Iran and wales")
group_b.play_groups3(group_teams_b)
print("the game between Saudi arabia and Poland")
group_c.play_groups3(group_teams_c)
print("the game between Austria and tunisia")
group_d.play_groups3(group_teams_d)
print("the game between Costa Rica and Japan")
group_e.play_groups3(group_teams_e)
print("the game between Canada and Croatia")
group_f.play_groups3(group_teams_f)
print("the game between Serbia and Cameroon")
group_g.play_groups3(group_teams_g)
print("the game between Ghana and Korea Republic")
group_h.play_groups3(group_teams_h)

# code for the fourth roud of matches in the group phase
print("THIS IS THE FOURTH ROUND OF GAMES IN THE GROUP PHASE")
print("the first match between Qatar and Senegal")
group_a.play_groups4(groups_teams_a)
print("the game between England and USA")
group_b.play_groups4(group_teams_b)
print("the game between Argentina and Mexico")
group_c.play_groups4(group_teams_c)
print("the game between France and Denmark")
group_d.play_groups4(group_teams_d)
print("the game between Spain and Germany")
group_e.play_groups4(group_teams_e)
print("the game between Belgium and Morocco")
group_f.play_groups4(group_teams_f)
print("the game between Brazil and Switzerland")
group_g.play_groups4(group_teams_g)
print("the game between Portugal and Uruguay")
group_h.play_groups4(group_teams_h)

# code for the fifth round of matches in the group phase
print("THIS IS THE FIFTH ROUND OF GAMES IN THE GROUP PHASE")
print("the first match between Ecuador and Senegal")
group_a.play_groups5(groups_teams_a)
print("the game between Iran and USA")
group_b.play_groups5(group_teams_b)
print("the game between Saudi arabia and Mexico")
group_c.play_groups5(group_teams_c)
print("the game between Australia and Denmark")
group_d.play_groups5(group_teams_d)
print("the game between Costa Rica and Germany")
group_e.play_groups5(group_teams_e)
print("the game between Canada and Morocco")
group_f.play_groups5(group_teams_f)
print("the game between Serbia and Switzerland")
group_g.play_groups5(group_teams_g)
print("the game between Ghana and Uruguay")
group_h.play_groups5(group_teams_h)

# code for the six round of matches in the group phase
print("THIS IS THE SIX ROUND OF GAMES IN THE GROUP PHASE")
print("the first match between Qatar and Netherlands")
group_a.play_groups6(groups_teams_a)
print("the game between England and Wales")
group_b.play_groups6(group_teams_b)
print("the game between Argentina and Poland")
group_c.play_groups6(group_teams_c)
print("the game between France and Tunisia")
group_d.play_groups6(group_teams_d)
print("the game between  Spain and Japan")
group_e.play_groups6(group_teams_e)
print("the game between Belgium and Croatia")
group_f.play_groups6(group_teams_f)
print("the game between Brazil and Cameroon")
group_g.play_groups6(group_teams_g)
print("the game between Portugal and Korea Republic")
group_h.play_groups6(group_teams_h)
group.top_two(groups_teams_a, 0)
group.top_two(group_teams_b, 0)
group.top_two(group_teams_c, 0)
group.top_two(group_teams_d, 0)
group.top_two(group_teams_e, 0)
group.top_two(group_teams_f, 0)
group.top_two(group_teams_g, 0)
group.top_two(group_teams_h, 0)


class Round16:
    def __init__(self, teams, turns=None, results=None):
        self.teams = teams
        self.results = results or {}
        self.turns = [[0, 3], [1, 2], [4, 7], [5, 6], [8, 11], [9, 10], [12, 15], [13, 14]] #match order

    def winners16(self, group, counter):
        for i in self.turns:
            team1 = (group[self.turns[counter][0]]) #team 1 is equal to a counter who increase by one by each interation
            team2 = group[self.turns[counter][1]]
            counter = counter + 1
            goal1 = int(input(f"Input the goals for {team1.country} :"))
            goal2 = int(input(f"input the goals for  {team2.country} :"))
            if goal1 > goal2:
                winner = team1
                qfinal_teams.append(winner)
                print(f"the winner is team {team1.country}")
            else:
                winner = team2
                qfinal_teams.append(winner)
                print(f"the winner is team {team2.country}")


class QFinals:
    def __init__(self, teams,turns2 = None,results=None):
        self.teams = teams
        self.results = results or {}
        self.turns2 = [[0,2],[1,3],[4,6],[7,5]] #same logic as before for the turns

    def winnersqfinal(self, group, counter):
        for i in self.turns2:
            team1 = (group[self.turns2[counter][0]]) #is equal to the counter in index 0
            team2 = (group[self.turns2[counter][1]])
            counter = counter + 1
            print(f"the match between {team1.country} and {team2.country}")
            goal1 = int(input(f"Input the goals for {team1.country} :"))
            goal2 = int(input(f"input the goals for  {team2.country} :"))
            if goal1 > goal2:
                winner = team1
                sfinal_teams.append(winner)
                print(f"the winner is team {team1.country}")
            else:
                winner = team2
                sfinal_teams.append(winner)
                print(f"the winner is team {team2.country}")


class SFinals:
    def __init__(self, teams,turn3 =None,results=None):
        self.teams = teams
        self.results = results or {}
        self.turns3 = [[0,2],[1,3]]

    def winnerssfinal(self,group,counter):
        for i in self.turns3:
            team1 = (group[self.turns3[counter][0]])
            team2 = (group[self.turns3[counter][1]])
            counter = counter + 1
            print(f"the match between {team1.country} and {team2.country}")
            goal1 = int(input(f"Input the goals for {team1.country} :"))
            goal2 = int(input(f"input the goals for  {team2.country} :"))
            if goal1 > goal2:
                winner = team1
                final_teams.append(winner)
                print(f"the winner is team {team1.country}")
            else:
                winner = team2
                final_teams.append(winner)
                print(f"the winner is team {team2.country}")



class Final:
    def __init__(self, teams, result=None):
        self.teams = teams
        self.result = result or {}


    def winnerfinal(self):
        for i in range(0, len(final_teams), 2):
            team1, team2 = final_teams[i], final_teams[i + 1]
            result = print("\nEnter the result of the match between", (team1.country), "and", (team2.country))
            goals1 = int(input(f"Enter the goals for {team1.country}:"))
            goals2 = int(input(f"Enter the goals for {team2.country}:"))
            team1.score = goals1
            team2.score = goals2
            winner = team1 if goals1 > goals2 else team2
            print(f"The winner of the World Cup is {winner.country}!")


# Create empty lists for each round
qfinal_teams = []
sfinal_teams = []
final_teams = []

# Create an object for the round of 16
# round16 = Round16(round16_teams)
# Create an object for the round of 16
round16 = Round16(teams)
print("\nRound 16")
# Now we can simulate the rest of the tournament by looping through the list of teams in each round
# and finding the winners. For example:
round16.winners16(round16_teams, 0)

# Create an object for the quarter-finals
print(qfinal_teams)
qfinals = QFinals(qfinal_teams)
print("\nQuarter-Final")
# Repeat the process for the semi-finals and final
qfinals.winnersqfinal(qfinal_teams,0)

sfinals = SFinals(sfinal_teams)
print("\nSemi-Final")
sfinals.winnerssfinal(sfinal_teams,0)

final = Final(final_teams)
print("\nFinal")
final.winnerfinal()