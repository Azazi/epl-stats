# EPL Stats

English Premier League table data for all teams in the period between 1888 and mid-season 2020.

## Running the application

The provided applicatiton downloads (& caches) the standings tables from [worldfootball.net](https://www.worldfootball.net). It then computes, and prints the top ten teams according to their cummulative points score.

To run the application:

* Ensure that `python 3.7+` is instatlled

* Install the `pip` requirements

```bash
pip install -r requirements.txt
```

* Run the `app.py` script

```bash

python app.py
```

The application starts by checking the `cache` directory for copies of the data for a given season before attempting to download the data. For convenience, the complete data for seasons 1888/1889 throughout 2018/2019 are included. Partial data for the 2019/2020 season is also included. To force the application to use freshly pulled data (from [worldfootball.net](https://www.worldfootball.net)), please nuke the contents of the `cache` directory.

The ouput of the application will be similar to:

```bash
EPL HISTORICAL STANDINGS (POINTS_ADJUSTED)
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| NAME              | PLAYED | WON  | DRAW | LOST | GOALS FOR | GOALS AGAINST | POINTS | POINTS ADJUSTED |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Liverpool FC      | 4155   | 1956 | 1032 | 1167 | 6918      | 5016          | 5746   | 6900            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Everton FC        | 4541   | 1845 | 1140 | 1556 | 7053      | 6288          | 5422   | 6675            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Manchester United | 3740   | 1807 | 927  | 1006 | 6462      | 4672          | 5403   | 6348            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Arsenal FC        | 3819   | 1777 | 985  | 1057 | 6469      | 4698          | 5324   | 6316            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Aston Villa       | 4093   | 1649 | 972  | 1472 | 6637      | 6121          | 4734   | 5919            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Manchester City   | 3643   | 1467 | 876  | 1300 | 5755      | 5244          | 4312   | 5277            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Tottenham Hotspur | 3417   | 1418 | 827  | 1172 | 5395      | 4778          | 4309   | 5081            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Chelsea FC        | 3421   | 1398 | 879  | 1144 | 5248      | 4786          | 4347   | 5073            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Newcastle United  | 3487   | 1345 | 845  | 1297 | 5226      | 5043          | 3952   | 4880            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
| Sunderland AFC    | 3340   | 1260 | 780  | 1300 | 5143      | 5121          | 3507   | 4560            |
+-------------------+--------+------+------+------+-----------+---------------+--------+-----------------+
```

## Collected stats

The stats collected by the application are:

```python
PLAYED = 'PLAYED'
WON = 'WON'
DRAW = 'DRAW'
LOST = 'LOST'
GOALS_FOR = 'GOALS FOR'
GOALS_AGAINST = 'GOALS AGAINST'
GOAL_DIFF = 'GOAL DIFFERENCE'
POINTS = 'POINTS'
POINTS_ADJUSTED = 'POINTS ADJUSTED'
```

The `POINTS ADJUSTED` stat uses a consistent formula for calculating the points by awarding **3 points for a win**, and **1 point for a draw** throughout the league's history. The three-point standard was introduced to English football in 1981, prior to which only 2 points were awarded for a win. This stat is included to account for the biases in calculation that were introduced by the standard change.

## Licensing

Semantic is licensed under the [MIT license](https://github.com/Azazi/epl-stats/blob/master/LICENSE).
