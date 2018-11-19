# EPL Fantasy League Optimal Team Pick Generator

#### Our analysis will be guided by a few key questions:

- Is there a correlation between individual fantasy player stats, their team's table position, and team's total fantasy player points in the English premier league?

- Can we approach individual players as investments to find the underpriced and overpriced players, so we can spend our fantasy budget in a way that generates the best return on investment (ROI), which in this example would represent their total Fantasy points earned to date per player cost?

- If so, can we build an algorithm that picks as many of the highest ROI players as possible to beat the average fantasy player in terms of total fantasy points returned for the £100mil budget that each user starts the season with.

## Procedure:

1. Start by creating an English Premier League table  and arranging teams by actual table position in the league. We will look at the aggregate of points for each team's players to see if that correlates directly to the team table position.

##### Are there any surprises and outliers? How can this information guide our further investigations?

2. Next, look at each team's cumulative player ROI and plot that against the number of players that the coach uses on a regular basis to try to find the teams that have too many expensive and underperforming players and the teams that have a solid core of consistent players that generate a high aggregate ROI.

##### Are there any surprises and outliers? How do the results guide our further investigations?  Where are the "diamonds in the ruff" hiding? Which teams should we try to avoid buying players from?

3. Now we will dive deeper and look at individual player stats, so we can write our algorithm's logic for picking the most optimal combination of individual players. Let's look at a scatter plot of **Player Cost vs. Player Total Fantasy Points.** We want our AI to pick players who provide the best value. On the plot, we would want many players that are as far north-west as possible but also a few that are in the far north-east. Generally, the famous star players are the most expensive and return a decent number of points for the user.

![header](images/player-points-vs-cost.png)

> ###### Does the team data agree with our player data? Do we find a lot of undervalued, high ROI players in those teams whom had a good total_points / total_cost ratio?  


##### What teams have the more overpriced players with a low ROI?

4. Next, we look at the top 20 and bottom 20 players in terms of ROI and compare that to the AVG ROI for all players in the league.

###### We should guide our Algorithm to pick as many of the top 20 as possible and stay away from the bottom 20.

5. Finally, it's time for the most fun part - writing an algorithm and comparing the results of the AI picks vs what an average person might pick as their team.  We also asked a classmate to pick a random team of his own to verify that our random team picker function is somewhat accurate.

### Here are the basic constraints of the EPL Fantasy League:

> 1. Each fantasy player starts with a budget of £100mil

> 2. You need to have 2 goalkeepers, 5 defenders, 5 midfielders and 3 strikers.

> 3. You cannot have more than 3 players from the same club team

So, we start our algorithm with these conditions. Then we add our own conditions and logic on top of that to ensure that each time our algorithm loops through the list of players it can make a valid pick:



###### Algorithm logic steps

1. Check if a player is injured first and if so, skip that player.
2. Pick the top three start players with the most cumulative fantasy points first. We will test the outcome of this condition with different constraints and pick the number of start players that generates the biggest return on investment.
3. Every time we pick a player and add it to our team, we subtract their cost from our £100mil budget and we add their position and team-name to a list, to make sure that we stop buying players for the positions and the teams that hit their constraint limit.
4. Once the optimal number of star players are picked, the algorithm starts going through the list of players with the highest ROI while attempting to acquire as many of the top names as we can, without depleting our budget, over populating any player positions or exceeding the maximum allowed players per club team.
5. Next, the algorithm prints a list of the players it picked and returns us the remaining budget and the total fantasy points of the team.
6. We repeat the same procedure for the Average Joe's team algorithm, which focuses more on star players and players from prestigious teams, who are often overpriced and might not return the highest cumulative ROI for our limited budget.
7. In the end we compare the results of our "Money" Team vs. the Average Joe's team vs. our random classmate's team to see which one performed best and by what margin.

```python
def build_team_by_roi(budget = 100, count_limit = 3, gk = 2, df = 5, md = 5, fwd = 3):
    money_team = []
    budget = budget
    injured = players_by_status('injured')
    positions = {'Goalkeeper': gk, 'Defender': df, 'Midfielder': md, 'Forward': fwd}
    for player in points_top_players():
            if len(money_team) < count_limit and player not in injured and budget >= player.cost and positions[player.position] > 0:
                money_team.append(player)
                budget -= player.cost
                positions[player.position] = positions[player.position] - 1
            else:
                for player in roi_top_players():
                    if player not in money_team and budget >= player.cost and positions[player.position] > 0:
                        money_team.append(player)
                        budget -= player.cost
                        positions[player.position] = positions[player.position] - 1
    final_team = [(item.name, item.position, item.cost) for item in money_team]
    print('Remaining Budget: ' + str(round(budget, 2)))
    print('Your AI has picked the following team:')
    print('GK: '), print([(item[0], item[2]) for item in final_team if item[1] == "Goalkeeper"])
    print('DF: '), print([(item[0], item[2]) for item in final_team if item[1] == "Defender"])
    print('MD: '), print([(item[0], item[2])  for item in final_team if item[1] == "Midfielder"])
    print('FWD: '), print([(item[0], item[2])  for item in final_team if item[1] == "Forward"])
    return money_team
```


* ###### Did our AI return the highest ROI team?  Did it beat the others by a significant margin?

* ###### Did our AI pick players from some middle of the table teams, which we initially identified as undervalued?

* ###### Did the Average Joe pick more expensive players from the top teams and what was their team variety?

![header](images/money-team-epl.png)
> Populated via the [Fantasy Premier League site](https://fantasy.premierleague.com/)


## Conclusion:

Removing any team/player favoritism and biases allows or AI to focus on the important stats. Thus, our AI is able to get the most bang for our buck and beat the average EPL fantasy user by a total of 132 points or 16.25% as a whole.

![header](images/money-team-percentages.png)

### Next steps:

* Keep monitoring the data to see if there are any drastic changes further in the season, when players start getting injured and the battle for table position and silverware intensifies.
* Attempt to build a visual team population with names, stats, and team jersey images.
