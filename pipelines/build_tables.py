import duckdb

con = duckdb.connect("ipl.duckdb")

# Raw layer: exact copy of the CSV, never edited
con.sql("""
    CREATE OR REPLACE TABLE raw_matches AS
    SELECT * FROM read_csv_auto('data/raw/archive/matches.csv')
""")

# Clean layer: the table we analyze
con.sql("""
    CREATE OR REPLACE TABLE matches AS
    SELECT
        id                            AS match_id,
        season,
        TRY_CAST(date AS DATE)        AS match_date,
        venue,
        team1,
        team2,
        toss_winner,
        toss_decision,
        winner,
        (toss_winner = winner)        AS toss_winner_won
    FROM raw_matches
    WHERE winner IS NOT NULL
""")

print(con.sql("""
    SELECT COUNT(*) AS matches,
           MIN(match_date) AS first_match,
           MAX(match_date) AS last_match
    FROM matches
"""))