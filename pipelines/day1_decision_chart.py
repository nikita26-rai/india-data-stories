import duckdb
import matplotlib.pyplot as plt

con = duckdb.connect("ipl.duckdb")

df = con.sql("""
    SELECT toss_decision,
           COUNT(*) AS matches,
           ROUND(100.0 * AVG(toss_winner_won::INT), 1) AS win_pct
    FROM matches
    GROUP BY toss_decision
    ORDER BY toss_decision DESC
""").df()

labels = ["Chose to " + d for d in df["toss_decision"]]

fig, ax = plt.subplots(figsize=(8, 8))
bars = ax.bar(labels, df["win_pct"], color=["#1d9bf0", "#f4a261"])
ax.axhline(50, color="red", linestyle="--", label="Coin flip (50%)")
ax.set_ylim(30, 65)
ax.set_ylabel("Toss winner's win %")
ax.set_title("IPL toss winners: bat or field?", fontsize=18, weight="bold")
ax.legend()

for bar, pct, n in zip(bars, df["win_pct"], df["matches"]):
    ax.text(bar.get_x() + bar.get_width() / 2, pct + 0.8,
            f"{pct}%\n({n} matches)", ha="center", fontsize=13, weight="bold")

plt.figtext(0.5, 0.01, "Data: Kaggle IPL dataset (Cricsheet) | @Nikita26rai",
            ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("charts/day1_decision.png", dpi=200)
print("Saved charts/day1_decision.png")