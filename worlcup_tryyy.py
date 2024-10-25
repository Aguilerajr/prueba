class Team:
    def __init__(self, country, results=None,score = 0):
        self.country = country
        self.results = results or {}

# Create a list of all 32 teams
teams = [Team("Qatar",0), Team("Ecuador",0), Team("Senegal",0), Team("Netherlands\n",0),
         Team("England",0), Team("Iran",0), Team("USA",0), Team("Wales\n"),
         Team("Argentina",0), Team("Saudi Arabia",0), Team("Mexico"), Team("Poland\n",0),
         Team("France",0), Team("Australia",0), Team("Denmark",0), Team("Tunisia\n",0),
         Team("Spain",0), Team("Costa Rica",0), Team("Germany",0), Team("Japan\n",0),
         Team("Belgium",0), Team("Canada",0), Team("Morocco",0), Team("Croatia\n",0),
         Team("Brazil",0), Team("Serbia",0), Team("Switzerland",0), Team("Cameroon\n",0),
         Team("Portugal",0), Team("Ghana",0), Team("Uruguay",0), Team("South Korea",0)]


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
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            round16_teams.append(winner)
            print(f"the winner is team {team1.country}")
            return {team1:3,team2:0}
        elif goal1==goal2:
            print(f"the match between {team1.country} and {team2.country} was a draw")
            return {team1:1,team2:1}
        else:
            if goal2 > goal1:
                winner = team2
                round16_teams.append(winner)
                print(f"the winner is team  {team2.country}")
                return {team1:0,team2:3}

    def play_groups2(self,group1):
        team1 , team2 = group1[0][2] , group1[0][3]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            round16_teams.append(winner)
            print(f"the winner is team {team1.country}")
            return {team1:3,team2:0}
        elif goal1==goal2:
            print(f"the match between {team1.country} and {team2.country} was a draw")
            return {team1:1,team2:1}
        else:
            if goal2 > goal1:
                winner = team2
                round16_teams.append(winner)
                print(f"the winner is team  {team2.country}")
                return {team1:0,team2:3}

    def play_groups3(self,group1):
        team1 , team2 = group1[0][3] , group1[0][1]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            round16_teams.append(winner)
            print(f"the winner is team {team1.country}")
            return {team1:3,team2:0}
        elif goal1==goal2:
            print(f"the match between {team1.country} and {team2.country} was a draw")
            return {team1:1,team2:1}
        else:
            if goal2 > goal1:
                winner = team2
                round16_teams.append(winner)
                print(f"the winner is team  {team2.country}")
                return {team1:0,team2:3}

    def play_groups4(self,group1):
        team1 , team2 = group1[0][0] , group1[0][2]
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            round16_teams.append(winner)
            print(f"the winner is team {team1.country}")
            return {team1:3,team2:0}
        elif goal1==goal2:
            print(f"the match between {team1.country} and {team2.country} was a draw")
            return {team1:1,team2:1}
        else:
            if goal2 > goal1:
                winner = team2
                round16_teams.append(winner)
                print(f"the winner is team  {team2.country}")
                return {team1:0,team2:3}
    

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
print(group_teams_c)

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
















