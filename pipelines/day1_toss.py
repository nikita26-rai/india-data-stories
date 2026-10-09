import duckdb

con = duckdb.connect("ipl.duckdb")

print("OVERALL")
print(con.sql("""
    SELECT COUNT(*) AS matches,
           ROUND(100.0 * AVG(toss_winner_won::INT), 1) AS toss_win_pct
    FROM matches
"""))

print("BY TOSS DECISION")
print(con.sql("""
    SELECT toss_decision,
           COUNT(*) AS matches,
           ROUND(100.0 * AVG(toss_winner_won::INT), 1) AS toss_win_pct
    FROM matches
    GROUP BY toss_decision
"""))

print("BY VENUE (20+ matches)")
print(con.sql("""
    SELECT venue,
           COUNT(*) AS matches,
           ROUND(100.0 * AVG(toss_winner_won::INT), 1) AS toss_win_pct
    FROM matches
    GROUP BY venue
    HAVING COUNT(*) >= 20
    ORDER BY toss_win_pct DESC
"""))