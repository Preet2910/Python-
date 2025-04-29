                                                    ## 🏏 IPL Match Data Analysis (2008–2016) ##




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# ─────────────────────────────────────────────
# 1. 🔄 Load & Clean Data
# ─────────────────────────────────────────────
ipl_df = pd.read_excel("IPL dataset for python.xlsx")
ipl_df.columns = ipl_df.columns.str.strip().str.lower().str.replace(" ", "_")

# ─────────────────────────────────────────────
# 2. 🧼 Basic Info
# ─────────────────────────────────────────────
print("Data Overview:")
print(ipl_df.info())
print("\nMissing Values:\n", ipl_df.isnull().sum())
print("\nSample Data:\n", ipl_df.head())


# ─────────────────────────────────────────────
# 3. 📈 Statistical Analysis & Key Questions
# ─────────────────────────────────────────────

# 1. Most successful team
most_wins = ipl_df['winner'].value_counts().idxmax()
most_wins_count = ipl_df['winner'].value_counts().max()
print(f"🏆 Most Successful Team: {most_wins} ({most_wins_count} wins)")

# 2. Top "Player of the Match"
top_player = ipl_df['player_of_match'].value_counts().idxmax()
top_player_awards = ipl_df['player_of_match'].value_counts().max()
print(f"🌟 Top Player of the Match: {top_player} ({top_player_awards} awards)")

# 3. City hosting most matches
top_city = ipl_df['city'].value_counts().idxmax()
top_city_matches = ipl_df['city'].value_counts().max()
print(f"🏙️ Most Matches Hosted in City: {top_city} ({top_city_matches} matches)")

# 4. Most used venue
top_venue = ipl_df['venue'].value_counts().idxmax()
top_venue_matches = ipl_df['venue'].value_counts().max()
print(f"🏟️ Busiest Venue: {top_venue} ({top_venue_matches} matches)")

# 5. Season with most matches
top_season = ipl_df['season'].value_counts().idxmax()
top_season_matches = ipl_df['season'].value_counts().max()
print(f"📅 Season with Most Matches: {top_season} ({top_season_matches} matches)")

# 6. Largest win by runs
largest_win_runs = ipl_df[['winner', 'win_by_runs']].sort_values(by='win_by_runs', ascending=False).head(1)
print(f"💥 Largest Win by Runs: {largest_win_runs.iloc[0]['winner']} ({int(largest_win_runs.iloc[0]['win_by_runs'])} runs)")

# 7. Largest win by wickets
largest_win_wickets = ipl_df[['winner', 'win_by_wickets']].sort_values(by='win_by_wickets', ascending=False).head(1)
print(f"🚀 Largest Win by Wickets: {largest_win_wickets.iloc[0]['winner']} ({int(largest_win_wickets.iloc[0]['win_by_wickets'])} wickets)")



# ─────────────────────────────────────────────
# 4. 📊 Descriptive Visualizations
# ─────────────────────────────────────────────
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Toss Decision Distribution
sns.countplot(data=ipl_df, x='toss_decision', palette='pastel')
plt.title("Toss Decision Distribution")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.show()

# Match Result Type
sns.countplot(data=ipl_df, x='result', palette='Set2')
plt.title("Match Result Types")
plt.xlabel("Result Type")
plt.ylabel("Count")
plt.show()

# Match Wins by Top 10 Teams
top_winners = ipl_df['winner'].value_counts().head(10)
sns.barplot(x=top_winners.values, y=top_winners.index, palette='viridis')
plt.title("Top 10 Teams by Match Wins")
plt.xlabel("Number of Wins")
plt.ylabel("Team")
plt.show()

# Win by Runs and Wickets Distribution
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
sns.histplot(ipl_df['win_by_runs'], bins=30, color='orange', kde=True)
plt.title("Win by Runs Distribution")
plt.subplot(1, 2, 2)
sns.histplot(ipl_df['win_by_wickets'], bins=11, color='green', kde=True)
plt.title("Win by Wickets Distribution")
plt.tight_layout()
plt.show()

# Home Wins Pie Chart
home_win_counts = ipl_df['home_win'].value_counts()
plt.pie(home_win_counts, labels=home_win_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set3'))
plt.title("Home Wins vs Away Wins")
plt.axis('equal')
plt.show()

# Bowling First Win Pie Chart
bowl_first_counts = ipl_df['bowlingfirstwin'].value_counts()
plt.pie(bowl_first_counts, labels=bowl_first_counts.index, autopct='%1.1f%%', colors=sns.color_palette('coolwarm'))
plt.title("Wins When Bowling First")
plt.axis('equal')
plt.show()

# Top Player of the Match Awards
top_players = ipl_df['player_of_match'].value_counts().head(10)
sns.barplot(x=top_players.values, y=top_players.index, palette='rocket')
plt.title("Top 10 Players of the Match")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.show()

# ─────────────────────────────────────────────
# 4. 🧪 Hypothesis Testing
# ─────────────────────────────────────────────

# A. Toss Winner vs Match Winner
toss_vs_win = pd.crosstab(ipl_df['toss_winner'] == ipl_df['winner'], columns='Count')
chi2, p, _, _ = chi2_contingency(toss_vs_win)
print("\n--- Toss Winner = Match Winner Hypothesis Test ---")
print(toss_vs_win)
print(f"Chi2: {chi2:.2f}, P-value: {p:.4f}")
print("Conclusion:", "Significant association ✅" if p < 0.05 else "No significant association ❌")

# B. Bowling First vs Match Result
bowl_win_counts = pd.crosstab(ipl_df['bowlingfirstwin'], columns='Count')
chi2_bowl, p_bowl, _, _ = chi2_contingency(bowl_win_counts)
print("\n--- Bowling First Win Impact Hypothesis Test ---")
print(bowl_win_counts)
print(f"Chi2: {chi2_bowl:.2f}, P-value: {p_bowl:.4f}")
print("Conclusion:", "Significant impact ✅" if p_bowl < 0.05 else "No significant impact ❌")
