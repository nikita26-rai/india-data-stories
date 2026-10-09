import duckdb

con = duckdb.connect("ipl.duckdb")

total, overall = con.sql("""
    SELECT COUNT(*), ROUND(100.0 * AVG(toss_winner_won::INT), 1)
    FROM matches
""").fetchone()

rows = con.sql("""
    SELECT toss_decision, COUNT(*), ROUND(100.0 * AVG(toss_winner_won::INT), 1)
    FROM matches
    GROUP BY toss_decision
""").fetchall()
d = {r[0]: (r[1], r[2]) for r in rows}
field_n, field_pct = d["field"]
bat_n, bat_pct = d["bat"]

first, last = con.sql("""
    SELECT MIN(YEAR(match_date)), MAX(YEAR(match_date)) FROM matches
""").fetchone()

print(f"""
TWEET 1 (attach charts/day1_decision.png)
I analyzed {total:,} IPL matches ({first}-{last}).

Winning the toss gives you a {overall}% win rate. Basically a coin flip.

But what captains DO with the toss matters:
Choose to field -> win {field_pct}%
Choose to bat -> win {bat_pct}% 🧵

TWEET 2
Toss winners won {overall}% of all matches. 50% is pure luck, so the coin itself is not the edge.

TWEET 3
The edge is the decision. {field_n} captains chose to field and won {field_pct}%. {bat_n} chose to bat and won {bat_pct}%.

TWEET 4
Caveat: captains choose based on dew, pitch and conditions, so this shows a pattern, not proof that fielding causes wins. Venue-level numbers are too small to trust yet.

TWEET 5
Data: Kaggle IPL dataset (Cricsheet), analyzed with Python + DuckDB. Code on my GitHub: github.com/nikita26-rai/india-data-stories
Which IPL myth should I test next? Reply with one 👇
""")