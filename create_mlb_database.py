# create_mlb_database.py - ENHANCED VERSION
import json
import random
from datetime import datetime

def create_mlb_players_database():
    """Create MLB players database"""
    
    mlb_teams = [
        ("Arizona Diamondbacks", "ARI", "NL", "West"),
        ("Atlanta Braves", "ATL", "NL", "East"),
        ("Baltimore Orioles", "BAL", "AL", "East"),
        ("Boston Red Sox", "BOS", "AL", "East"),
        ("Chicago Cubs", "CHC", "NL", "Central"),
        ("Chicago White Sox", "CWS", "AL", "Central"),
        ("Cincinnati Reds", "CIN", "NL", "Central"),
        ("Cleveland Guardians", "CLE", "AL", "Central"),
        ("Colorado Rockies", "COL", "NL", "West"),
        ("Detroit Tigers", "DET", "AL", "Central"),
        ("Houston Astros", "HOU", "AL", "West"),
        ("Kansas City Royals", "KC", "AL", "Central"),
        ("Los Angeles Angels", "LAA", "AL", "West"),
        ("Los Angeles Dodgers", "LAD", "NL", "West"),
        ("Miami Marlins", "MIA", "NL", "East"),
        ("Milwaukee Brewers", "MIL", "NL", "Central"),
        ("Minnesota Twins", "MIN", "AL", "Central"),
        ("New York Mets", "NYM", "NL", "East"),
        ("New York Yankees", "NYY", "AL", "East"),
        ("Oakland Athletics", "OAK", "AL", "West"),
        ("Philadelphia Phillies", "PHI", "NL", "East"),
        ("Pittsburgh Pirates", "PIT", "NL", "Central"),
        ("San Diego Padres", "SD", "NL", "West"),
        ("San Francisco Giants", "SF", "NL", "West"),
        ("Seattle Mariners", "SEA", "AL", "West"),
        ("St. Louis Cardinals", "STL", "NL", "Central"),
        ("Tampa Bay Rays", "TB", "AL", "East"),
        ("Texas Rangers", "TEX", "AL", "West"),
        ("Toronto Blue Jays", "TOR", "AL", "East"),
        ("Washington Nationals", "WSH", "NL", "East")
    ]
    
    positions = ["P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH"]
    
    top_mlb_players = [
        ("Shohei Ohtani", "DH/P", "LAD"),
        ("Aaron Judge", "RF", "NYY"),
        ("Ronald Acuña Jr.", "RF", "ATL"),
        ("Mookie Betts", "RF", "LAD"),
        ("Freddie Freeman", "1B", "LAD"),
        ("Corey Seager", "SS", "TEX"),
        ("Juan Soto", "RF", "NYY"),
        ("Bryce Harper", "RF", "PHI"),
        ("Matt Olson", "1B", "ATL"),
        ("Kyle Tucker", "RF", "HOU"),
        ("Yordan Alvarez", "LF", "HOU"),
        ("Corbin Carroll", "CF", "ARI"),
        ("Francisco Lindor", "SS", "NYM"),
        ("Jose Ramirez", "3B", "CLE"),
        ("Marcus Semien", "2B", "TEX"),
        ("Gerrit Cole", "P", "NYY"),
        ("Spencer Strider", "P", "ATL"),
        ("Zac Gallen", "P", "ARI"),
        ("Kevin Gausman", "P", "TOR"),
        ("Corbin Burnes", "P", "BAL")
    ]
    
    players = []
    player_id = 2000
    
    # Add top players
    for name, position, team_abbr in top_mlb_players:
        team_full = next(t[0] for t in mlb_teams if t[1] == team_abbr)
        is_pitcher = "P" in position
        
        # Generate realistic stats
        batting_avg = round(random.uniform(.240, .330), 3) if not is_pitcher else .000
        home_runs = random.randint(10, 50) if not is_pitcher else 0
        rbis = random.randint(30, 130) if not is_pitcher else 0
        era = round(random.uniform(2.50, 4.50), 2) if is_pitcher else 0.00
        wins = random.randint(5, 20) if is_pitcher else 0
        strikeouts = random.randint(50, 250) if is_pitcher else 0
        
        player = {
            "id": f"mlb-{player_id}",
            "name": name,
            "playerName": name,
            "team": team_full,
            "teamAbbrev": team_abbr,
            "position": position,
            "pos": position,
            "sport": "mlb",
            
            # Hitting stats (for non-pitchers)
            "battingAvg": batting_avg,
            "homeRuns": home_runs,
            "RBIs": rbis,
            "runs": random.randint(40, 120) if not is_pitcher else 0,
            "stolenBases": random.randint(5, 50) if not is_pitcher else 0,
            "OBP": round(random.uniform(.310, .420), 3) if not is_pitcher else .000,
            "SLG": round(random.uniform(.400, .600), 3) if not is_pitcher else .000,
            "OPS": round(batting_avg + random.uniform(.200, .300), 3) if not is_pitcher else .000,
            
            # Pitching stats
            "ERA": era,
            "wins": wins,
            "strikeouts": strikeouts,
            "WHIP": round(random.uniform(1.00, 1.30), 2) if is_pitcher else 0.00,
            "inningsPitched": random.randint(50, 200) if is_pitcher else 0,
            "saves": random.randint(0, 40) if is_pitcher and position == "RP" else 0,
            
            # Fantasy scoring
            "fantasyScore": random.uniform(100, 600),
            "fp": random.uniform(100, 600),
            "projectedFantasyScore": random.uniform(110, 620),
            "projFP": random.uniform(110, 620),
            
            # Financials
            "salary": random.randint(500000, 40000000),
            "contractValue": random.randint(1000000, 300000000),
            
            # Performance metrics
            "avgPointsPerGame": random.uniform(5, 25),
            "consistencyRating": random.randint(60, 95),
            "injuryRisk": random.randint(10, 50),
            "yearsPro": random.randint(1, 15),
            "age": random.randint(23, 38),
            
            # Status
            "injuryStatus": random.choice(["healthy", "healthy", "healthy", "day-to-day", "10-day IL"]),
            
            # Game info
            "nextOpponent": random.choice([t[0] for t in mlb_teams if t[1] != team_abbr]),
            "opponentRank": random.randint(1, 30),
            "matchupDifficulty": random.choice(["easy", "medium", "medium", "hard"]),
            "ballparkFactor": random.choice(["hitter-friendly", "pitcher-friendly", "neutral"]),
            
            # Timestamps
            "lastUpdated": datetime.now().isoformat(),
            "timestamp": datetime.now().isoformat()
        }
        
        players.append(player)
        player_id += 1
    
    # Add 70 more generic players
    for i in range(70):
        team_full, team_abbr, league, division = random.choice(mlb_teams)
        position = random.choice(positions)
        is_pitcher = position == "P"
        
        first_names = ["Mike", "Chris", "David", "John", "Mark", "Paul", "Steven", "Kevin", "Brian", "Jason"]
        last_names = ["Anderson", "Wilson", "Taylor", "Moore", "Martin", "Lee", "Walker", "Clark", "Lewis", "Young"]
        
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        player = {
            "id": f"mlb-{player_id}",
            "name": name,
            "playerName": name,
            "team": team_full,
            "teamAbbrev": team_abbr,
            "position": position,
            "pos": position,
            "sport": "mlb",
            "league": league,
            "division": division,
            
            # Stats
            "battingAvg": round(random.uniform(.220, .290), 3) if not is_pitcher else .000,
            "homeRuns": random.randint(5, 25) if not is_pitcher else 0,
            "RBIs": random.randint(20, 80) if not is_pitcher else 0,
            "ERA": round(random.uniform(3.50, 5.50), 2) if is_pitcher else 0.00,
            "wins": random.randint(3, 12) if is_pitcher else 0,
            "strikeouts": random.randint(30, 150) if is_pitcher else 0,
            
            "fantasyScore": random.uniform(50, 300),
            "fp": random.uniform(50, 300),
            "projectedFantasyScore": random.uniform(60, 310),
            "projFP": random.uniform(60, 310),
            
            "salary": random.randint(500000, 10000000),
            "avgPointsPerGame": random.uniform(3, 15),
            
            "injuryStatus": random.choice(["healthy", "healthy", "day-to-day"]),
            "yearsPro": random.randint(1, 10),
            "age": random.randint(23, 35),
            
            "lastUpdated": datetime.now().isoformat()
        }
        
        players.append(player)
        player_id += 1
    
    return players

# Save MLB database
mlb_players = create_mlb_players_database()
with open('mlb_players_data.json', 'w') as f:
    json.dump(mlb_players, f, indent=2)

print(f"✅ Created MLB database with {len(mlb_players)} players")
