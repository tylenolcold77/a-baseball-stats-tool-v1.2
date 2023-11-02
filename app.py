from constants import PLAYERS, TEAMS

def clean_data(players):
    cleaned_data = []
    for player in players:
        cleaned_player = player.copy()
        cleaned_player['height'] = int(cleaned_player['height'].split(' ')[0])
        cleaned_player['experience'] = cleaned_player['experience'] == 'YES'
        cleaned_player['guardians'] = cleaned_player['guardians'].split(' and ')
        cleaned_data.append(cleaned_player)
    return cleaned_data

def balance_teams(players, teams):
    players_per_team = len(players) // len(teams)
    balance_teams = {team: players[i:i+players_per_team] for i, team in enumerate(teams)}
    return balance_teams

def display_stats(team_name, team_players):
    num_players = len(team_players)
    num_experienced = sum(player['experience'] for player in team_players)
    num_inexperienced = num_players - num_experienced
    avg_height = sum(player['height'] for player in team_players) / num_players
    player_names = ', '.join(player['name'] for player in team_players)
    guardians = ', '.join(guardian for player in team_players for guardian in player['guardians'])
    
    print(f"Team: {team_name} Stats")
    print("------------------------")
    print(f"Total players: {num_players}")
    print(f"Total experienced: {num_experienced}")
    print(f"Total inexperienced: {num_inexperienced}")
    print(f"Average height: {avg_height}")
    print("\nPlayers on Team:")
    print(f"  {player_names}")
    print("\nGuardians:")
    print(f"  {guardians}")
    
def main():
    cleaned_players = clean_data(PLAYERS)
    balanced_teams = balance_teams(cleaned_players, TEAMS)
    
    while True:
        print("\n----MENU----\n")
        print("Here are your choices:")
        print("A) Display Team Stats:")
        print("B) Quit:")
        choice = input("Enter an option:")
        
        if choice.lower() == "b":
            break
        elif choice.lower() == 'a':
            for i, team in enumerate(TEAMS, 1):
                print(f"{i}) {team}")
            team_choice = input("Enter an option:")
            if team_choice > "0" and team_choice <= "3":
                team_choice = int(team_choice) - 1
                display_stats(TEAMS[team_choice], balanced_teams[TEAMS[team_choice]])
            else:
                print("That is not a valid option. Please try again.")
        else:
            print("Please select a valid option.")

if __name__ == '__main__':
    main()