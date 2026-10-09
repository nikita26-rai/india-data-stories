import duckdb
import matplotlib.pyplot as plt

con = duckdb.connect("ipl.duckdb")

df = con.sql("""
    SELECT season,
           ROUND(100.0 * AVG(toss_winner_won::INT), 1) AS toss_win_pct
    FROM matches
    GROUP BY season
    ORDER BY season
""").df()

overall = con.sql("""
    SELECT ROUND(100.0 * AVG(toss_winner_won::INT), 0) FROM matches
""").fetchone()[0]

fig, ax = plt.subplots(figsize=(8, 8))
ax.bar(df["season"].astype(str), df["toss_win_pct"], color="#1d9bf0")
ax.axhline(50, color="red", linestyle="--", label="Coin flip (50%)")
ax.set_ylim(30, 70)
ax.set_title(f"Toss winners win {overall:.0f}% of IPL matches",
             fontsize=16, weight="bold")
ax.set_ylabel("Toss winner's win %")
plt.xticks(rotation=60)
ax.legend()
plt.figtext(0.5, 0.01, "Data: Kaggle IPL dataset (Cricsheet) | @Nikita26rai",
            ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("charts/day1_toss.png", dpi=200)
print("Saved charts/day1_toss.png")