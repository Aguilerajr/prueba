# Class for representing a team
class Team:
    def __init__(self, name):
        self.name = name
# Class for representing a group of teams
class Group:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
# Class for representing a round of 16 match
class Round16:
    def __init__(self, team1, team2, result):
        self.team1 = team1
        self.team2 = team2
        self.result = result
# Class for representing a quarter final match
class QuarterFinal:
    def __init__(self, team1, team2, result):
        self.team1 = team1
        self.team2 = team2
        self.result = result
# Class for representing a semi-final match
class SemiFinal:
    def __init__(self, team1, team2, result):
        self.team1 = team1
        self.team2 = team2
        self.result = result
# Class for representing the final match
class Final:
    def __init__(self, team1, team2, result):
        self.team1 = team1
        self.team2 = team2
        self.result = result
# Function for organizing the competition
def organize_competition():
# Create 32 team objects
    teams = []
    for i in range(32):
        team = Team(f'Team {i+1}')
        teams.append(team)
# Assign teams to 8 group objects
    groups = []
    for i in range(8):
        group_teams = teams[i*4:(i+1)*4]
        group = Group(f'Group {i+1}', group_teams)
        groups.append(group)
# Round of 16 matches
    round16_matches = []
    for i in range(8):
        team1 = input(f'Enter the winner of match {i*2+1} in the round of 16: ')
        team2 = input(f'Enter the winner of match {i*2+2} in the round of 16: ')
        match = Round16(team1, team2, None)
        round16_matches.append(match)
# Quarter final matches
    quarterfinal_matches = []
    for i in range(4):
        team1 = input(f'Enter the winner of match {i*2+1} in the quarter finals: ')
        team2 = input(f'Enter the winner of match {i*2+2} in the quarter finals: ')
        match = QuarterFinal(team1, team2, None)
        quarterfinal_matches.append(match)
# Semi-final matches
    semifinal_matches = []
    for i in range(2):
        team1 = input(f'Enter the winner of match {i*2+1} in the semi-finals: ')
        team2 = input(f'Enter the winner of match {i*2+2} in the semi-finals: ')
        match = SemiFinal(team1, team2, None)
        semifinal_matches.append(match)
#Final match
    final_match = Final(input('Enter the winner of the first semi-final: '), input('Enter the winner of the second semi-final: '), None)
#Determine the winner of the final match
    winner = input('Enter the winner of the final: ')
#Print the results of each stage
    print('\nResults:')
    print('\nGroups:')
    for group in groups:
        print(f'{group.name}: {[team.name for team in group.teams]}')
        print('\nRound of 16:')
    for match in round16_matches:
        print(f'{match.team1.name} vs {match.team2.name}')
        print('\nQuarter Finals:')
    for match in quarterfinal_matches:
        print(f'{match.team1.name} vs {match.team2.name}')
        print('\nSemi-Finals:')
    for match in semifinal_matches:
        print(f'{match.team1.name} vs {match.team2.name}')
        print('\nFinal:')
        print(f'{final_match.team1.name} vs {final_match.team2.name}')
        print(f'\nWinner: {winner.name}')
organize_competition()