import unittest
from unittest.mock import Mock
from main.countries import *

brazil = {
        'name': {
          'common': 'Brazil'
        },
        'capital': ['Brasília'],
        'languages': {'pt': 'Portuguese'}
      }

class MockCountriesService:
  def by_name(self, name):
    if name == 'Brazil':
      return [brazil]
    else:
      return []

class CountriesSearchTest(unittest.TestCase):

  def setUp(self):
    # self.service = CountriesService()
    self.service = MockCountriesService()
    self.search = CountriesSearch(self.service)

  def test_get_country_from_json(self):
    country = self.search.get_country_from_json(brazil)
    self.assertEqual('Brazil', country.get_name())
    self.assertEqual('Brasília', country.get_capital())
    self.assertIn('Portuguese', country.get_languages())

  def test_search_by_name_with_invalid_country(self):
    countries = self.search.by_name("Wakanda")
    self.assertEqual([], countries)

  def test_search_by_name_with_specific_country(self):
    countries = self.search.by_name("Brazil")
    self.assertEqual(len(countries), 1)
    self.assertIn("Brasília", countries[0].capital)

  def test_search_by_name_with_specific_country_using_unittest_mock(self):
    service = Mock()
    search = CountriesSearch(service)
    service.by_name.return_value = [brazil]
    countries = search.by_name("Brazil")
    service.by_name.assert_called_once_with('Brazil')
    self.assertEqual(len(countries), 1)

