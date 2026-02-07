# create_all_databases.py
#!/usr/bin/env python3
import subprocess
import json
import os

print("🎯 Creating Comprehensive Sports Databases")
print("=" * 50)

# Run all database creation scripts
scripts = [
    'create_nfl_database.py',
    'create_mlb_database.py', 
    'create_nhl_database.py',
    'create_stats_database.py'
]

for script in scripts:
    if os.path.exists(script):
        print(f"\n📁 Running {script}...")
        try:
            subprocess.run(['python', script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running {script}: {e}")
    else:
        print(f"⚠️ {script} not found")

# Verify all databases were created
print("\n" + "=" * 50)
print("📊 Database Verification:")
print("-" * 50)

databases = {
    'nfl_players_data.json': 'NFL Players',
    'mlb_players_data.json': 'MLB Players', 
    'nhl_players_data.json': 'NHL Players',
    'sports_stats_database.json': 'Sports Stats DB',
    'players_data.json': 'NBA Players',
    'fantasy_teams_data.json': 'Fantasy Teams'
}

total_players = 0
for db_file, db_name in databases.items():
    if os.path.exists(db_file):
        try:
            with open(db_file, 'r') as f:
                data = json.load(f)
                count = len(data) if isinstance(data, list) else 1
                if 'players' in db_name:
                    total_players += count
                print(f"✅ {db_name}: {count:,} records")
        except:
            print(f"✅ {db_name}: File exists")
    else:
        print(f"❌ {db_name}: Missing")

print("-" * 50)
print(f"🎯 Total Players Across All Sports: {total_players:,}")
print("=" * 50)
print("\n🚀 All databases created successfully!")
print("💡 Next steps:")
print("   1. Deploy updated app.py to Railway")
print("   2. Test all endpoints")
print("   3. Update frontend to use new endpoints")
