class Team:
    def __init__(self, country, results=None, score=0):
        self.country = country
        self.results = results or {}
        self.score = score

# Create a list of all 32 teams
teams = [Team("Qatar"), Team("Ecuador"), Team("Senegal"), Team("Netherlands\n"),
         Team("England"), Team("Iran"), Team("USA"), Team("Wales\n"),
         Team("Argentina"), Team("Saudi Arabia"), Team("Mexico"), Team("Poland\n"),
         Team("France"), Team("Australia"), Team("Denmark"), Team("Tunisia\n"),
         Team("Spain"), Team("Costa Rica"), Team("Germany"), Team("Japan\n"),
         Team("Belgium"), Team("Canada"), Team("Morocco"), Team("Croatia\n"),
         Team("Brazil"), Team("Serbia"), Team("Switzerland"), Team("Cameroon\n"),
         Team("Portugal"), Team("Ghana"), Team("Uruguay"), Team("South Korea")]


class Group:
    def __init__(self, name, teams=None):
        self.name = name
        self.teams = teams or []

    def print_teams(self):
        print("Teams in group " + self.name + ":")
        for team in self.teams:
            print(team.country)

    def appendgroups(self,array,a,b,c,d,e,f,g,h):
        a.append(array[0:4])
        b.append(array[4:8])
        c.append(array[8:12])
        d.append(array[12:16])
        e.append(array[16:20])
        f.append(array[20:24])
        g.append(array[24:28])
        h.append(array[28:])


    def play_groups(self,group1):
        team1 , team2 = group1[0][0] , group1[0][1]
        goal1 = input(f"Input the goals for {team1.country} :")
        goal2 = input(f"input the goals for  {team2.country} :")
        if goal1 > goal2:
            winner = team1
            team1.score = 3
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = 1
            team2.score = 1

        else:
            if goal2 > goal1:
                winner = team2
                team2.score = 3
                print(f"the winner is team  {team2.country}")

    def play_groups2(self,group1):
        team1 , team2 = group1[0][2] , group1[0][3]
        goal1 = input(f"Input the goals for {team1.country} :")
        goal2 = input(f"input the goals for {team2.country} :")
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                print(f"the winner is team  {team2.country}")

    def play_groups3(self,group1):
        team1 , team2 = group1[0][3] , group1[0][1]
        goal1 = input(f"Input the goals for {team1.country} :")
        goal2 = input(f"input the goals for {team2.country} :")
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                print(f"the winner is team  {team2.country}")

    def play_groups4(self,group1):
        team1 , team2 = group1[0][0] , group1[0][2]
        goal1 = input(f"Input the goals for {team1.country} :")
        goal2 = input(f"input the goals for  {team2.country} :")
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                print(f"the winner is team  {team2.country}")

    def play_groups5(self,group1):
        team1 , team2 = group1[0][1] , group1[0][2]
        goal1 = input(f"Input the goals for {team1.country} :")
        goal2 = input(f"input the goals for  {team2.country} :")
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                print(f"the winner is team  {team2.country}")


    def play_groups6(self,group1):
        team1 , team2 = group1[0][0] , group1[0][3]
        goal1 = input(f"Input the goals for {team1.country} :")
        goal2 = input(f"input the goals for  {team2.country} :")
        if goal1 > goal2:
            winner = team1
            team1.score = team1.score + 3
            print(f"the winner is team {team1.country}")

        elif goal1 == goal2:
            team1.score = team1.score + 1
            team2.score = team2.score + 1
        else:
            if goal2 > goal1:
                winner = team2
                team2.score = team2.score + 3
                print(f"the winner is team  {team2.country}")
    def top_two(self):
        for group in groups:
            top_two = sorted(group.teams,key=lambda x: x.results.get(group.name,0),reverse =True)[:2]
            round16_teams.extend(top_two)


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
group.appendgroups(teams,groups_teams_a,group_teams_b,group_teams_c,group_teams_d,group_teams_e,group_teams_f,group_teams_g,group_teams_h)


#code for the first round of matches between the groups
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


#code for the second round of matches among the groups
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


#code for the third round of games
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

#code for the fourth roud of matches in the group phase
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

#code for the fifth round of matches in the group phase
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


#code for the six round of matches in the group phase
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
group_a.top_two()
print(round16_teams)


class Round16:
    def __init__(self, teams, results = None):
        self.teams = teams
        self.results = results or {}

    def winners16(self):
        for i in range(0, len(round16_teams), 2):
            team1, team2 = round16_teams[i], round16_teams[i + 1]
            # Prompt the user to enter the result of the match
            result = print("\nEnter the result of the match between", (team1.country), "and", (team2.country))
            # Split the result into the goals scored by each team2:
            goals1 = int(input(f"Enter the goals for {team1.country}:"))
            goals2 = int(input(f"Enter the goals for {team2.country}:"))
            # Update the results for each team
            team1.results["Round of 16"] = goals1
            team2.results["Round of 16"] = goals2
            # Determine the winner of the match
            winner = team1 if goals1 > goals2 else team2
            # Append the winner to the list for the quarter-finals
            qfinal_teams.append(winner)


class QFinals:
    def __init__(self, teams, results=None):
        self.teams = teams
        self.results = results or {}
    def winnersqfinal(self):
        for i in range(0, len(qfinal_teams), 2):
            team1, team2 = qfinal_teams[i], qfinal_teams[i + 1]
            result = print("\nEnter the result of the match between", (team1.country), "and", (team2.country))
            goals1 = int(input(f"Enter the goals for {team1.country}:"))
            goals2 = int(input(f"Enter the goals for {team2.country}:"))
            team1.results["Quarter-finals"] = goals1
            team2.results["Quarter-finals"] = goals2
            winner = team1 if goals1 > goals2 else team2
            sfinal_teams.append(winner)

class SFinals:
    def __init__(self, teams, results=None):
        self.teams = teams
        self.results = results or {}
    def winnerssfinal(self):
        for i in range(0, len(sfinal_teams), 2):
            team1, team2 = sfinal_teams[i], sfinal_teams[i + 1]
            result = print("\nEnter the result of the match between", (team1.country), "and", (team2.country))
            goals1 = int(input(f"Enter the goals for {team1.country}:"))
            goals2 = int(input(f"Enter the goals for {team2.country}:"))
            team1.results["Semi-finals"] = goals1
            team2.results["Semi-finals"] = goals2
            winner = team1 if goals1 > goals2 else team2
            final_teams.append(winner)

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
            team1.results["Final"] = goals1
            team2.results["Final"] = goals2
            winner = team1 if goals1 > goals2 else team2
            print(f"The winner of the World Cup is {winner.country}!")



# Create empty lists for each round
round16_teams = []
qfinal_teams = []
sfinal_teams = []
final_teams = []

# Iterate through the groups and find the winners
for group in groups:
    # Find the top two teams in the group
    top_two = sorted(group.teams, key=lambda x: x.results.get(group.name, 0), reverse=True)[:2]
    # Append the top two teams to the list for the round of 16
    round16_teams.extend(top_two)

# Create an object for the round of 16
# round16 = Round16(round16_teams)
# Create an object for the round of 16
round16 = Round16(round16_teams)
print("\nRound 16")
# Now we can simulate the rest of the tournament by looping through the list of teams in each round
# and finding the winners. For example:
round16.winners16()

# Create an object for the quarter-finals
qfinals = QFinals(qfinal_teams)
print("\nQuarter-Final")
# Repeat the process for the semi-finals and final
qfinals.winnersqfinal()

sfinals = SFinals(sfinal_teams)
print("\nSemi-Final")
sfinals.winnerssfinal()

final = Final(final_teams)
print("\nFinal")
final.winnerfinal()