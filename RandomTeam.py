import random
 
items = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers',
         'Chicago Bears', 'Cincinatti Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Detroit Lions',
         'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 
         'Kansas City Chiefs', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 
         'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles',
         'Pittsburgh Steelers', 'St. Louis Rams', 'San Diego Chargers', 'San Francisco 49ers',
         'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
 
rand_items = random.sample(items, 2)

print rand_items