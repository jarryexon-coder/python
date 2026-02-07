# create_nfl_database.py
import json
import random
from datetime import datetime, timedelta

def create_nfl_players_database():
    """Create NFL players database"""
    
    # NFL team names and abbreviations
    nfl_teams = [
        ("Arizona Cardinals", "ARI", "NFC", "West"),
        ("Atlanta Falcons", "ATL", "NFC", "South"),
        ("Baltimore Ravens", "BAL", "AFC", "North"),
        ("Buffalo Bills", "BUF", "AFC", "East"),
        ("Carolina Panthers", "CAR", "NFC", "South"),
        ("Chicago Bears", "CHI", "NFC", "North"),
        ("Cincinnati Bengals", "CIN", "AFC", "North"),
        ("Cleveland Browns", "CLE", "AFC", "North"),
        ("Dallas Cowboys", "DAL", "NFC", "East"),
        ("Denver Broncos", "DEN", "AFC", "West"),
        ("Detroit Lions", "DET", "NFC", "North"),
        ("Green Bay Packers", "GB", "NFC", "North"),
        ("Houston Texans", "HOU", "AFC", "South"),
        ("Indianapolis Colts", "IND", "AFC", "South"),
        ("Jacksonville Jaguars", "JAX", "AFC", "South"),
        ("Kansas City Chiefs", "KC", "AFC", "West"),
        ("Las Vegas Raiders", "LV", "AFC", "West"),
        ("Los Angeles Chargers", "LAC", "AFC", "West"),
        ("Los Angeles Rams", "LAR", "NFC", "West"),
        ("Miami Dolphins", "MIA", "AFC", "East"),
        ("Minnesota Vikings", "MIN", "NFC", "North"),
        ("New England Patriots", "NE", "AFC", "East"),
        ("New Orleans Saints", "NO", "NFC", "South"),
        ("New York Giants", "NYG", "NFC", "East"),
        ("New York Jets", "NYJ", "AFC", "East"),
        ("Philadelphia Eagles", "PHI", "NFC", "East"),
        ("Pittsburgh Steelers", "PIT", "AFC", "North"),
        ("San Francisco 49ers", "SF", "NFC", "West"),
        ("Seattle Seahawks", "SEA", "NFC", "West"),
        ("Tampa Bay Buccaneers", "TB", "NFC", "South"),
        ("Tennessee Titans", "TEN", "AFC", "South"),
        ("Washington Commanders", "WAS", "NFC", "East")
    ]
    
    # NFL positions
    positions = ["QB", "RB", "WR", "TE", "OL", "DL", "LB", "CB", "S", "K", "P"]
    
    # Top NFL players with realistic stats
    top_nfl_players = [
        ("Patrick Mahomes", "QB", "KC"),
        ("Josh Allen", "QB", "BUF"),
        ("Justin Jefferson", "WR", "MIN"),
        ("Christian McCaffrey", "RB", "SF"),
        ("Tyreek Hill", "WR", "MIA"),
        ("Travis Kelce", "TE", "KC"),
        ("Jalen Hurts", "QB", "PHI"),
        ("Joe Burrow", "QB", "CIN"),
        ("Nick Bosa", "DL", "SF"),
        ("Aaron Donald", "DL", "LAR"),
        ("Micah Parsons", "LB", "DAL"),
        ("Myles Garrett", "DL", "CLE"),
        ("T.J. Watt", "LB", "PIT"),
        ("Derrick Henry", "RB", "TEN"),
        ("Davante Adams", "WR", "LV"),
        ("Stefon Diggs", "WR", "BUF"),
        ("Justin Herbert", "QB", "LAC"),
        ("Lamar Jackson", "QB", "BAL"),
        ("Ja'Marr Chase", "WR", "CIN"),
        ("CeeDee Lamb", "WR", "DAL")
    ]
    
    players = []
    player_id = 1000
    
    # Add top players
    for name, position, team_abbr in top_nfl_players:
        team_full = next(t[0] for t in nfl_teams if t[1] == team_abbr)
        
        player = {
            "id": f"nfl-{player_id}",
            "name": name,
            "playerName": name,
            "team": team_full,
            "teamAbbrev": team_abbr,
            "position": position,
            "pos": position,
            "sport": "nfl",
            
            # NFL-specific stats
            "passingYards": random.randint(2500, 5000) if position == "QB" else 0,
            "passingTDs": random.randint(15, 45) if position == "QB" else 0,
            "rushingYards": random.randint(100, 1200) if position in ["QB", "RB"] else random.randint(0, 200),
            "rushingTDs": random.randint(1, 15) if position in ["QB", "RB"] else 0,
            "receivingYards": random.randint(800, 1800) if position in ["WR", "TE"] else 0,
            "receivingTDs": random.randint(5, 15) if position in ["WR", "TE"] else 0,
            "receptions": random.randint(40, 120) if position in ["WR", "TE"] else 0,
            "tackles": random.randint(30, 150) if position in ["DL", "LB", "CB", "S"] else 0,
            "sacks": random.randint(5, 20) if position in ["DL", "LB"] else 0,
            "interceptions": random.randint(0, 8) if position in ["CB", "S"] else 0,
            
            # Fantasy scoring (PPR format)
            "fantasyScore": random.uniform(150, 400),
            "fp": random.uniform(150, 400),
            "projectedFantasyScore": random.uniform(160, 420),
            "projFP": random.uniform(160, 420),
            
            # Financials
            "salary": random.randint(500000, 50000000),
            "contractValue": random.randint(1000000, 200000000),
            
            # Performance metrics
            "avgPointsPerGame": random.uniform(10, 30),
            "consistencyRating": random.randint(60, 95),
            "injuryRisk": random.randint(5, 45),
            "yearsPro": random.randint(1, 12),
            "age": random.randint(22, 35),
            
            # Status
            "injuryStatus": random.choice(["healthy", "healthy", "healthy", "questionable", "doubtful"]),
            "practiceStatus": random.choice(["full", "limited", "full", "full", "DNP"]),
            "gameStatus": random.choice(["active", "active", "active", "active", "inactive"]),
            
            # Opponent info
            "nextOpponent": random.choice([t[0] for t in nfl_teams if t[1] != team_abbr]),
            "opponentRank": random.randint(1, 32),
            "matchupDifficulty": random.choice(["easy", "medium", "medium", "hard"]),
            
            # Timestamps
            "lastUpdated": datetime.now().isoformat(),
            "timestamp": datetime.now().isoformat()
        }
        
        players.append(player)
        player_id += 1
    
    # Add 80 more generic players
    for i in range(80):
        team_full, team_abbr, conference, division = random.choice(nfl_teams)
        position = random.choice(positions)
        first_names = ["James", "Michael", "Robert", "John", "David", "William", "Richard", "Joseph", "Thomas", "Christopher"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        player = {
            "id": f"nfl-{player_id}",
            "name": name,
            "playerName": name,
            "team": team_full,
            "teamAbbrev": team_abbr,
            "position": position,
            "pos": position,
            "sport": "nfl",
            "conference": conference,
            "division": division,
            
            # Stats based on position
            "passingYards": random.randint(1000, 4500) if position == "QB" else 0,
            "passingTDs": random.randint(5, 35) if position == "QB" else 0,
            "rushingYards": random.randint(50, 1000) if position in ["QB", "RB"] else random.randint(0, 100),
            "rushingTDs": random.randint(0, 10) if position in ["QB", "RB"] else 0,
            "receivingYards": random.randint(200, 1200) if position in ["WR", "TE"] else 0,
            "receivingTDs": random.randint(1, 8) if position in ["WR", "TE"] else 0,
            "receptions": random.randint(10, 80) if position in ["WR", "TE"] else 0,
            "tackles": random.randint(10, 100) if position in ["DL", "LB", "CB", "S"] else 0,
            "sacks": random.randint(0, 12) if position in ["DL", "LB"] else 0,
            "interceptions": random.randint(0, 5) if position in ["CB", "S"] else 0,
            
            "fantasyScore": random.uniform(50, 250),
            "fp": random.uniform(50, 250),
            "projectedFantasyScore": random.uniform(60, 260),
            "projFP": random.uniform(60, 260),
            
            "salary": random.randint(500000, 10000000),
            "avgPointsPerGame": random.uniform(5, 20),
            
            "injuryStatus": random.choice(["healthy", "healthy", "healthy", "questionable"]),
            "yearsPro": random.randint(1, 8),
            "age": random.randint(22, 32),
            
            "lastUpdated": datetime.now().isoformat()
        }
        
        players.append(player)
        player_id += 1
    
    return players

# Save NFL database
nfl_players = create_nfl_players_database()
with open('nfl_players_data.json', 'w') as f:
    json.dump(nfl_players, f, indent=2)

print(f"✅ Created NFL database with {len(nfl_players)} players")
