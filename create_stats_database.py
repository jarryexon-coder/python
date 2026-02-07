# create_stats_database.py
import json
import random
from datetime import datetime, timedelta

def create_sports_stats_database():
    """Create comprehensive sports statistics database"""
    
    stats_db = {
        "nba": {
            "league_stats": {
                "avg_points_per_game": 114.2,
                "avg_pace": 99.1,
                "avg_offensive_rating": 115.8,
                "avg_defensive_rating": 115.0,
                "three_point_rate": 0.395,
                "true_shooting_percentage": 0.578,
                "avg_turnovers": 13.8,
                "avg_rebounds": 44.2,
                "avg_assists": 25.6
            },
            "team_stats": [],
            "player_trends": [],
            "historical_data": []
        },
        "nfl": {
            "league_stats": {
                "avg_points_per_game": 43.0,
                "avg_yards_per_game": 338.5,
                "avg_pass_yards": 225.8,
                "avg_rush_yards": 112.7,
                "avg_turnovers": 2.4,
                "third_down_percentage": 0.388,
                "red_zone_efficiency": 0.552,
                "avg_time_of_possession": 30.15
            },
            "team_stats": [],
            "player_trends": [],
            "historical_data": []
        },
        "mlb": {
            "league_stats": {
                "avg_runs_per_game": 8.7,
                "avg_era": 4.33,
                "avg_ba": 0.248,
                "avg_obp": 0.320,
                "avg_slg": 0.414,
                "avg_hr_per_game": 2.3,
                "avg_strikeouts_per_game": 16.8,
                "avg_walks_per_game": 6.5
            },
            "team_stats": [],
            "player_trends": [],
            "historical_data": []
        },
        "nhl": {
            "league_stats": {
                "avg_goals_per_game": 6.2,
                "avg_shots_per_game": 61.5,
                "avg_pp_percentage": 0.203,
                "avg_pk_percentage": 0.797,
                "avg_save_percentage": 0.905,
                "avg_penalty_minutes": 10.2,
                "avg_hits_per_game": 42.3,
                "avg_faceoff_percentage": 0.500
            },
            "team_stats": [],
            "player_trends": [],
            "historical_data": []
        },
        "trends": {
            "betting_trends": [],
            "injury_impacts": [],
            "weather_effects": [],
            "venue_advantages": []
        },
        "analytics": {
            "predictive_models": [],
            "machine_learning_insights": [],
            "ai_predictions": []
        },
        "metadata": {
            "last_updated": datetime.now().isoformat(),
            "data_sources": ["internal", "api_integrations", "web_scraping"],
            "version": "2.0.0",
            "total_records": 0
        }
    }
    
    # Generate team stats for each sport
    nba_teams = ["LAL", "GSW", "BOS", "MIL", "PHX", "DEN", "PHI", "MIA", "LAC", "DAL"]
    for team in nba_teams:
        stats_db["nba"]["team_stats"].append({
            "team": team,
            "wins": random.randint(25, 55),
            "losses": random.randint(15, 35),
            "win_percentage": round(random.uniform(0.450, 0.750), 3),
            "points_per_game": round(random.uniform(105, 125), 1),
            "points_allowed": round(random.uniform(105, 120), 1),
            "offensive_rating": round(random.uniform(110, 125), 1),
            "defensive_rating": round(random.uniform(110, 120), 1),
            "net_rating": round(random.uniform(-5, 15), 1),
            "pace": round(random.uniform(95, 105), 1),
            "effective_fg_percentage": round(random.uniform(0.500, 0.580), 3),
            "turnover_percentage": round(random.uniform(0.120, 0.160), 3),
            "offensive_rebound_percentage": round(random.uniform(0.200, 0.300), 3),
            "ft_rate": round(random.uniform(0.200, 0.300), 3),
            "three_point_percentage": round(random.uniform(0.340, 0.400), 3),
            "home_record": f"{random.randint(15, 25)}-{random.randint(5, 15)}",
            "road_record": f"{random.randint(10, 20)}-{random.randint(10, 20)}",
            "last_10": f"{random.randint(4, 8)}-{random.randint(2, 6)}",
            "streak": random.choice(["W1", "W2", "W3", "L1", "L2", "W4"]),
            "playoff_probability": round(random.uniform(0.10, 0.99), 2)
        })
    
    # Generate player trends
    for i in range(20):
        stats_db["nba"]["player_trends"].append({
            "player_id": f"player-{1000 + i}",
            "name": f"Player {i+1}",
            "trend": random.choice(["hot", "cold", "rising", "declining", "consistent"]),
            "metric": random.choice(["points", "rebounds", "assists", "three_pointers", "fantasy_points"]),
            "last_5_games": [random.randint(10, 40) for _ in range(5)],
            "avg_last_5": round(sum([random.randint(10, 40) for _ in range(5)]) / 5, 1),
            "season_avg": round(random.uniform(12, 28), 1),
            "change_percentage": round(random.uniform(-20, 40), 1),
            "analysis": random.choice([
                "Shooting efficiency has improved significantly",
                "Minutes restriction affecting production",
                "Benefiting from increased role",
                "Struggling with new offensive system",
                "Excellent matchup next game"
            ]),
            "confidence": random.randint(60, 95),
            "timestamp": datetime.now().isoformat()
        })
    
    # Generate betting trends
    for i in range(15):
        stats_db["trends"]["betting_trends"].append({
            "id": f"trend-{i}",
            "sport": random.choice(["nba", "nfl", "mlb", "nhl"]),
            "trend": random.choice([
                "Home underdogs covering 62% of spreads",
                "Over hitting in 70% of division games",
                "Primetime favorites struggling ATS",
                "Back-to-back games affecting totals",
                "Cold weather impacting scoring"
            ]),
            "accuracy": round(random.uniform(0.55, 0.75), 3),
            "sample_size": random.randint(50, 200),
            "timeframe": random.choice(["last 30 days", "this season", "last 2 seasons"]),
            "actionability": random.choice(["high", "medium", "low"]),
            "last_verified": (datetime.now() - timedelta(days=random.randint(1, 7))).isoformat()
        })
    
    # Generate injury impacts
    for i in range(10):
        stats_db["trends"]["injury_impacts"].append({
            "id": f"injury-{i}",
            "player": f"Star Player {i+1}",
            "team": random.choice(nba_teams),
            "injury": random.choice(["ankle sprain", "knee soreness", "hamstring strain", "back tightness"]),
            "status": random.choice(["out", "doubtful", "questionable", "probable"]),
            "games_missed": random.randint(1, 15),
            "team_performance_with": f"{random.randint(8, 12)}-{random.randint(3, 7)}",
            "team_performance_without": f"{random.randint(3, 7)}-{random.randint(8, 12)}",
            "point_differential_change": round(random.uniform(-8, 8), 1),
            "fantasy_impact": random.choice(["significant", "moderate", "minimal"]),
            "return_timeline": random.choice(["1-2 weeks", "day-to-day", "3-5 games", "indefinite"]),
            "updated": datetime.now().isoformat()
        })
    
    # Generate AI predictions
    for i in range(8):
        stats_db["analytics"]["ai_predictions"].append({
            "id": f"ai-pred-{i}",
            "game": f"{random.choice(['LAL', 'GSW', 'BOS'])} vs {random.choice(['MIA', 'DEN', 'PHX'])}",
            "prediction": random.choice([
                "Home team wins by 3-7 points",
                "Total points over 225.5",
                "Underdog covers spread",
                "Star player over on points",
                "High scoring first half"
            ]),
            "confidence": random.randint(65, 92),
            "model_used": random.choice(["neural_network", "random_forest", "gradient_boosting", "ensemble"]),
            "key_factors": [
                random.choice(["Home court advantage", "Rest advantage", "Matchup history"]),
                random.choice(["Injury reports", "Weather conditions", "Officiating crew"])
            ],
            "expected_value": round(random.uniform(0.05, 0.25), 2),
            "timestamp": datetime.now().isoformat(),
            "expires": (datetime.now() + timedelta(hours=24)).isoformat()
        })
    
    # Calculate total records
    total_records = 0
    for sport in ["nba", "nfl", "mlb", "nhl"]:
        for category in ["team_stats", "player_trends", "historical_data"]:
            total_records += len(stats_db[sport][category])
    for category in stats_db["trends"].values():
        total_records += len(category)
    for category in stats_db["analytics"].values():
        total_records += len(category)
    
    stats_db["metadata"]["total_records"] = total_records
    
    return stats_db

# Save stats database
stats_database = create_sports_stats_database()
with open('sports_stats_database.json', 'w') as f:
    json.dump(stats_database, f, indent=2)

print(f"✅ Created sports stats database with {stats_database['metadata']['total_records']} records")
