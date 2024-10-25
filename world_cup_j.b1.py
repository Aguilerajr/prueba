class Team:
    def __init__(self, country, results=None,score = 0):
        self.country = country
        self.results = results or {}

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
        goal1 = int(input(f"Input the goals for {team1.country} :"))
        goal2 = int(input(f"input the goals for  {team2.country} :"))
        if goal1 > goal2:
            winner = team1
            round16_teams.append(winner)
            print(f"the winner is team {team1.country}")
            team1=group1[0][0]
            print(f"The points for {team1.country} is:")
            team1=+3
            print(team1)
            team1=group1[0][1]
            print(f"The points for {team2.country} is:")
            team2=+0
            print(team2)
        elif goal1==goal2:
            print(f"the match between {team1.country} and {team2.country} was a draw")
            team1=group1[0][0]
            print(f"The points for {team1.country} is:")
            team1=+1
            print(team1)
            team1=group1[0][1]
            print(f"The points for {team2.country} is:")
            team2=+1
            print(team2)
        else:
            if goal2 > goal1:
                winner = team2
                round16_teams.append(winner)
                print(f"the winner is team {team2.country}")
                team1=group1[0][0]
                print(f"The points for {team1.country} is:")
                team1=+0
                print(team1)
                team1=group1[0][1]
                print(f"The points for {team2.country} is:")
                team2=+3
                print(team2)



        

           

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


















