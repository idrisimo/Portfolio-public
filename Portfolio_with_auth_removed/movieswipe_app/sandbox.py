from personal_portfolio.movieswipe_app.ProjectScripts import aws_dynamodb_api as aws
from personal_portfolio.movieswipe_app.ProjectScripts import tmdb_api_wrapper as tmdb
from pprint import pprint
import pandas as pd
movies = tmdb.Movie(genre_codes="28", date_start="2021-01-01", date_end="2021-01-10", watch_region="GBR")
generated_list = movies.discover_movies()

data_frame = pd.DataFrame(generated_list["results"])
keys_wanted = ['title', 'overview', 'poster_path', 'release_date', 'genre_ids', 'id',]
cleaned_data = data_frame[keys_wanted].to_dict('records')


host_key = "DCBA"
host_user = "Eve"
party_planner = aws.Party_planner(host_key=host_key, host_user=host_user, movie_list=cleaned_data)
get_party = party_planner.get_party_list()
add_movie_list = party_planner.store_movie_list()

