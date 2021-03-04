import requests




class Movie(object):
    TMDB_API_KEY = 'TMDB_API_KEY'

    session = requests.session()
    session.params = {}
    session.params['api_key'] = TMDB_API_KEY
    def __init__(self, **kwargs):
        self.id = id
        self.genre_codes = kwargs.get("genre_codes", {})
        self.date_start = kwargs.get("date_start", {})
        self.date_end = kwargs.get("date_end", {})
        self.watch_region = kwargs.get("watch_region", {})
        self.session = Movie.session

    def info(self):
        path = f'https://api.themoviedb.org/3/movie/{self.id}'
        response = self.session.get(path)

        return response.json()

    def discover_movies(self):
        path = f'https://api.themoviedb.org/3/discover/movie?' \
               f'language=en-US' \
               f'&sort_by=popularity.desc' \
               f'&include_adult=false' \
               f'&include_video=false' \
               f'&page=1' \
               f'&primary_release_date.gte={self.date_start}' \
               f'&primary_release_date.lte={self.date_end}' \
               f'&with_genres={self.genre_codes}' \
               f'&watch_region={self.watch_region}'
        response = self.session.get(path)
        return response.json()

    def genre_List(self):
        path = 'https://api.themoviedb.org/3/genre/movie/list'
        response = self.session.get(path)
        return response.json()

    def provider_list(self):
        path = f'https://api.themoviedb.org/3/movie/{self.id}/watch/providers'
        response = self.session.get(path)
        return response.json()

    def country_codes_list(self):
        path = f'https://api.themoviedb.org/3/configuration/countries'
        response = self.session.get(path)
        return response.json()

'''movies = Movie(genre_codes="28", date_start="2021-01-01", date_end="2021-01-10", watch_region="GB")
# genre_list = tmdb.Genre_List()
generated_list = movies.discover_movies()
print(generated_list)'''