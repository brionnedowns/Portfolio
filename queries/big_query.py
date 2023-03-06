query1 = '''SELECT MIN(date)
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
LIMIT 5;'''


query2 = '''SELECT *
FROM `bigquery-public-data.bls.cpsaat18` LIMIT 5;'''

query3 = '''SELECT *
FROM `bigquery-public-data.fda_food.food_events` LIMIT 5;'''

query3 = '''SELECT *
FROM `bigquery-public-data.github_repos.commits` LIMIT 5;'''

query4 = '''SELECT *
FROM `bigquery-public-data.google_trends.top_terms` LIMIT 10
ORDER BY refresh_date DESC;'''

query5 ='''SELECT *
FROM `bigquery-public-data.chicago_crime.crime`
LIMIT 5'''