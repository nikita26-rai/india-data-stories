import duckdb

con = duckdb.connect("ipl.duckdb")

chase_pct, n = con.sql("""
    SELECT
        ROUND(100.0 * AVG(
            CASE
                WHEN toss_decision = 'field' THEN toss_winner_won::INT
                ELSE (NOT toss_winner_won)::INT
            END
        ), 1),
        COUNT(*)
    FROM matches
""").fetchone()

print(f"Chasing team won {chase_pct}% of {n:,} matches")