import duckdb

con = duckdb.connect("ipl.duckdb")

print("DISTINCT WINNER VALUES THAT LOOK ODD")
print(con.sql("""
    SELECT winner, COUNT(*) AS n
    FROM matches
    WHERE winner NOT IN (team1, team2)
    GROUP BY winner
"""))

print("DATE RANGE")
print(con.sql("SELECT MIN(match_date), MAX(match_date) FROM matches"))