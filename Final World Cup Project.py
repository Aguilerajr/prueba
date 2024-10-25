class Team:
    def _init_(self, country, results=None):
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
    def _init_(self, name, teams=None):
        self.name = name
        self.teams = teams or []

    def print_teams(self):
        print("Teams in group " + self.name + ":")
        for team in self.teams:
            print(team.country)

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

for group in groups:
    group.print_teams()


class Round16:
    def _init_(self, teams, results = None):
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
    def _init_(self, teams, results=None):
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
    def _init_(self, teams, results=None):
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
    def _init_(self, teams, result=None):
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