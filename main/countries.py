import requests

class NotFoundException(Exception):
    pass

class Country:

    def __init__(self, name, capital, languages):
        self.name = name
        self.capital = capital
        self.languages = languages

    def get_name(self):
        return self.name

    def get_capital(self):
        return self.capital

    def get_languages(self):
        return self.languages


class CountriesService:
    
    base_url = 'https://restcountries.com/v3.1'

    def all(self):
        response = requests.get(f'{self.base_url}/all')
        if response.status_code == 404:
            raise NotFoundException()
        return response.json()

    def by_name(self, name):
        response = requests.get(f'{self.base_url}/name/{name}')
        if response.status_code == 404:
            raise NotFoundException()
        return response.json()

    def by_capital(self, capital):
        response = requests.get(f'{self.base_url}/capital/{capital}')
        if response.status_code == 404:
            raise NotFoundException()
        return response.json()

    def by_language(self, lang):
        response = requests.get(f'{self.base_url}/lang/{lang}')
        if response.status_code == 404:
            raise NotFoundException()
        return response.json()

class CountriesSearch:
    def __init__(self, service):
        self.service =  service

    def get_country_from_json(self, json):
        name = json['name']['common']
        capital = json['capital'][0]
        languages = json['languages'].values()
        return Country(name, capital, languages)

    def handle_404(default = []):
        def safe_call(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except NotFoundException:
                    return default
            return wrapper
        return safe_call

    @handle_404()
    def all(self):
        json = self.service.all()
        return list(map(self.get_country_from_json, json))

    @handle_404()
    def by_name(self, name):
        json = self.service.by_name(name)
        return list(map(self.get_country_from_json, json))

    @handle_404()
    def by_capital(self, capital):
        json = self.service.by_capital(capital)
        return list(map(self.get_country_from_json, json))

    @handle_404()
    def by_language(self, lang):
        json = self.service.by_language(lang)
        return list(map(self.get_country_from_json, json))

class BadCountriesSearch:
    def by_name(self, name):
        response = requests.get(f'https://restcountries.com/v3.1/name/{name}')
        if response.status_code == 404:
            return []
        json = response.json()
        countries = []
        for js in json:
            name = js['name']['common']
            capital = js['capital'][0]
            languages = js['languages'].values
            countries.append(Country(name, capital, languages))
        return countries