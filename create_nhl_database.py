# create_nhl_database.py - FIXED VERSION
import json
import random
from datetime import datetime

def create_nhl_players_database():
    """Create NHL players database"""
    
    nhl_teams = [
        ("Anaheim Ducks", "ANA", "Western", "Pacific"),
        ("Arizona Coyotes", "ARI", "Western", "Central"),
        ("Boston Bruins", "BOS", "Eastern", "Atlantic"),
        ("Buffalo Sabres", "BUF", "Eastern", "Atlantic"),
        ("Calgary Flames", "CGY", "Western", "Pacific"),
        ("Carolina Hurricanes", "CAR", "Eastern", "Metropolitan"),
        ("Chicago Blackhawks", "CHI", "Western", "Central"),
        ("Colorado Avalanche", "COL", "Western", "Central"),
        ("Columbus Blue Jackets", "CBJ", "Eastern", "Metropolitan"),
        ("Dallas Stars", "DAL", "Western", "Central"),
        ("Detroit Red Wings", "DET", "Eastern", "Atlantic"),
        ("Edmonton Oilers", "EDM", "Western", "Pacific"),
        ("Florida Panthers", "FLA", "Eastern", "Atlantic"),
        ("Los Angeles Kings", "LAK", "Western", "Pacific"),
        ("Minnesota Wild", "MIN", "Western", "Central"),
        ("Montreal Canadiens", "MTL", "Eastern", "Atlantic"),
        ("Nashville Predators", "NSH", "Western", "Central"),
        ("New Jersey Devils", "NJD", "Eastern", "Metropolitan"),
        ("New York Islanders", "NYI", "Eastern", "Metropolitan"),
        ("New York Rangers", "NYR", "Eastern", "Metropolitan"),
        ("Ottawa Senators", "OTT", "Eastern", "Atlantic"),
        ("Philadelphia Flyers", "PHI", "Eastern", "Metropolitan"),
        ("Pittsburgh Penguins", "PIT", "Eastern", "Metropolitan"),
        ("San Jose Sharks", "SJS", "Western", "Pacific"),
        ("Seattle Kraken", "SEA", "Western", "Pacific"),
        ("St. Louis Blues", "STL", "Western", "Central"),
        ("Tampa Bay Lightning", "TBL", "Eastern", "Atlantic"),
        ("Toronto Maple Leafs", "TOR", "Eastern", "Atlantic"),
        ("Vancouver Canucks", "VAN", "Western", "Pacific"),
        ("Vegas Golden Knights", "VGK", "Western", "Pacific"),
        ("Washington Capitals", "WSH", "Eastern", "Metropolitan"),
        ("Winnipeg Jets", "WPG", "Western", "Central")
    ]
    
    positions = ["C", "LW", "RW", "D", "G"]
    
    top_nhl_players = [
        ("Connor McDavid", "C", "EDM"),
        ("Nathan MacKinnon", "C", "COL"),
        ("Leon Draisaitl", "C", "EDM"),
        ("Auston Matthews", "C", "TOR"),
        ("David Pastrnak", "RW", "BOS"),
        ("Cale Makar", "D", "COL"),
        ("Nikita Kucherov", "RW", "TBL"),
        ("Mikko Rantanen", "RW", "COL"),
        ("Jack Hughes", "C", "NJD"),
        ("Jason Robertson", "LW", "DAL"),
        ("Matthew Tkachuk", "LW", "FLA"),
        ("Mitch Marner", "RW", "TOR"),
        ("Sidney Crosby", "C", "PIT"),
        ("Alex Ovechkin", "LW", "WSH"),
        ("Igor Shesterkin", "G", "NYR"),
        ("Andrei Vasilevskiy", "G", "TBL"),
        ("Connor Hellebuyck", "G", "WPG"),
        ("Juuse Saros", "G", "NSH"),
        ("Ilya Sorokin", "G", "NYI"),
        ("Thatcher Demko", "G", "VAN")
    ]
    
    players = []
    player_id = 3000
    
    # Add top players
    for name, position, team_abbr in top_nhl_players:
        team_full = next(t[0] for t in nhl_teams if t[1] == team_abbr)
        is_goalie = position == "G"
        
        goals = random.randint(20, 65) if not is_goalie else 0
        assists = random.randint(30, 90) if not is_goalie else 0
        
        player = {
            'id': f"nhl-{player_id}",
            'name': name,
            'playerName': name,
            'team': team_full,
            'teamAbbrev': team_abbr,
            'position': position,
            'pos': position,
            'sport': 'nhl',
            
            # Skater stats
            'goals': goals,
            'assists': assists,
            'points': goals + assists if not is_goalie else 0,
            'plusMinus': random.randint(-20, 40),
            'PIM': random.randint(10, 100),  # Penalty minutes
            'shots': random.randint(150, 350) if not is_goalie else 0,
            'shotPercentage': round(random.uniform(8, 20), 1) if not is_goalie else 0.0,
            'hits': random.randint(50, 250) if not is_goalie else 0,
            'blocks': random.randint(30, 200) if not is_goalie else 0,
            
            # Goalie stats
            'wins': random.randint(20, 45) if is_goalie else 0,
            'GAA': round(random.uniform(2.00, 3.50), 2) if is_goalie else 0.00,
            'savePercentage': round(random.uniform(.905, .935), 3) if is_goalie else .000,
            'shutouts': random.randint(0, 8) if is_goalie else 0,
            
            # Fantasy scoring
            'fantasyScore': random.uniform(100, 400),
            'fp': random.uniform(100, 400),
            'projectedFantasyScore': random.uniform(110, 420),
            'projFP': random.uniform(110, 420),
            
            # Financials
            'salary': random.randint(500000, 15000000),
            'contractValue': random.randint(1000000, 100000000),
            'capHit': random.randint(1000000, 13000000),
            
            # Performance metrics
            'avgPointsPerGame': round(random.uniform(0.5, 1.5), 2) if not is_goalie else 0,
            'consistencyRating': random.randint(65, 95),
            'injuryRisk': random.randint(10, 40),
            'yearsPro': random.randint(1, 15),
            'age': random.randint(22, 36),
            
            # Status
            'injuryStatus': random.choice(['healthy', 'healthy', 'healthy', 'day-to-day', 'IR']),
            
            # Game info
            'nextOpponent': random.choice([t[0] for t in nhl_teams if t[1] != team_abbr]),
            'opponentRank': random.randint(1, 32),
            'matchupDifficulty': random.choice(['easy', 'medium', 'medium', 'hard']),
            
            # Timestamps
            'lastUpdated': datetime.now().isoformat(),
            'timestamp': datetime.now().isoformat()
        }
        
        players.append(player)
        player_id += 1
    
    # Add 80 more generic players
    for i in range(80):
        team_full, team_abbr, conference, division = random.choice(nhl_teams)
        position = random.choice(positions)
        is_goalie = position == "G"
        
        first_names = ["Ryan", "Michael", "Chris", "Brad", "Eric", "Scott", "Steve", "Dan", "Matt", "Joe"]
        last_names = ["Smith", "Johnson", "Miller", "Brown", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson"]
        
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        goals = random.randint(5, 25) if not is_goalie else 0
        assists = random.randint(10, 35) if not is_goalie else 0
        
        player = {
            'id': f"nhl-{player_id}",
            'name': name,
            'playerName': name,
            'team': team_full,
            'teamAbbrev': team_abbr,
            'position': position,
            'pos': position,
            'sport': 'nhl',
            'conference': conference,
            'division': division,
            
            # Stats
            'goals': goals,
            'assists': assists,
            'points': goals + assists if not is_goalie else 0,
            'plusMinus': random.randint(-25, 15),
            'PIM': random.randint(5, 60),
            'shots': random.randint(80, 200) if not is_goalie else 0,
            
            # Goalie stats
            'wins': random.randint(10, 30) if is_goalie else 0,
            'GAA': round(random.uniform(2.50, 4.00), 2) if is_goalie else 0.00,
            'savePercentage': round(random.uniform(.890, .920), 3) if is_goalie else .000,
            
            'fantasyScore': random.uniform(50, 200),
            'fp': random.uniform(50, 200),
            'projectedFantasyScore': random.uniform(60, 210),
            'projFP': random.uniform(60, 210),
            
            'salary': random.randint(500000, 5000000),
            'avgPointsPerGame': round(random.uniform(0.3, 0.9), 2) if not is_goalie else 0,
            
            'injuryStatus': random.choice(['healthy', 'healthy', 'day-to-day']),
            'yearsPro': random.randint(1, 8),
            'age': random.randint(22, 34),
            
            'lastUpdated': datetime.now().isoformat()
        }
        
        players.append(player)
        player_id += 1
    
    return players

# Save NHL database
nhl_players = create_nhl_players_database()
with open('nhl_players_data.json', 'w') as f:
    json.dump(nhl_players, f, indent=2)

print(f"✅ Created NHL database with {len(nhl_players)} players")
