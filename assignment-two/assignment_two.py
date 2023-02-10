# Read from a local file
import json
import io
import time

"""Task 1
Open geojson file
"""
# Use "with ... as ..." to better handle exceptions
# https://stackoverflow.com/questions/30996289/utf8-codec-cant-decode-byte-0xf3
# Data Source https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_050_00_5m.json
with io.open('assignment-two/data/gz_2010_us_050_00_5m.json', encoding='latin-1') as f:
  data = json.load(f)

print('Number of Counties in US: {}'.format(len(data['features'])))

print(data['features'][1]['properties']['NAME'])


"""
Task 2
Top three counties and their states
"""

features = data['features']
county_states = dict()
for feature in features:
  properties = feature['properties']
  county_name = properties['NAME']
  state_code = properties['STATE']
  county_states.setdefault(county_name, []).append(state_code)


def get_county_totals(county_states):
  """Reformat the counties and state list objects into a tuple of counties and their totals

  Arguments:
  county_states dict[str, list<str>] -- County name as the key and the list of state codes as the value

  Returns:
  tuple[str, int] -- The counties and the total number of states that use them.
  """
  county_totals = [(None, None)] * len(county_states) 
  i = 0
  for county, states in county_states.items():
    county_total = (county, len(states))
    county_totals[i] = county_total
    i+=1

  return county_totals


def test_get_county_totals():
  mock_county_states = {
    "A": ['0'],
    "B": ['0', '1'],
    "C": ['0', '1', '2']
  }
  expected_count_totals = [('A', 1), ('B', 2), ('C', 3)]
  assert(get_county_totals(mock_county_states) == expected_count_totals)

test_get_county_totals()

def top_k_sort_k(totals, k):
  """Find the top k values in a tuple of objects and their counts.
  
  Arguments:
  totals tuple[str, int]-- Item Name and total 
  k int -- the number of items to rank

  Returns:
  tuple[str, int] -- Top k items and their counts
  
  Note:
  This function iterates through the list of items, only sorting the list of rankings
  """
  top_k = [(None, 0)]*k
  for total in totals:
    total_val = total[1]
    bottom_k_val = top_k[0][1]
    if total_val > bottom_k_val:
      top_k[0] = total
      top_k.sort(key=lambda a: a[1])

  return top_k

def test_top_k_sort_k():
  mock_county_totals = [("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4), ("F", 4)]
  expected_top_k = [("D", 3), ("F", 4), ("E", 4)]
  
  assert(top_k_sort_k(mock_county_totals, 3) == expected_top_k)

test_top_k_sort_k()

def top_k_sort_all(totals, k):
  """Find the top k values in a tuple of objects and their counts.
    
    Arguments:
    totals tuple[str, int]-- Item Name and total 
    k int -- the number of items to rank

    Returns:
    tuple[str, int] -- Top k items and their counts
    
    Note:
    This function sorts the whole list and then takes the top k results
  """
  totals.sort(key = lambda a: a[1])
  return totals[-k:]

def test_top_k_sort_all():
  mock_county_totals = [("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4), ("F", 4)]
  expected_top_k = [("D", 3), ("E", 4), ("F", 4)]
  assert(top_k_sort_all(mock_county_totals, 3) == expected_top_k)

test_top_k_sort_all()

county_totals = get_county_totals(county_states)
"""
1. Find the top counties.
2. Compare the two algorithims to determine which has better performance.

Findings: sorting the rankings list is generally faster when k is less than 25.
Sorting the whole list of counties and taking the top is generally faster when k is more than 25.
"""
# k = 3 
# start_time = time.perf_counter()
# top_counties = top_k_sort_k(county_totals, k)
# stop_time = time.perf_counter()
# print(f"top counties: {top_counties}")
# print(f"top counter time: {stop_time - start_time}")

# start_time = time.perf_counter()
# top_counties_alt = top_k_sort_all(county_totals, k)
# stop_time = time.perf_counter()
# print(f"top counties alt: {top_counties_alt}")
# print(f"top counter alt time: {stop_time - start_time}")


"""Task 3

Basic statistics by state
"""

features = data['features']
first_features = features[100]
print(first_features['properties'])

"""Task 3, part one

The number of counties in each state
"""
def get_state_counties_total(features):
  """Find the total number of counties in each state

  Arguments:
  features list[str, dict] -- each county has a set of properties, state code is most relevant

  Returns:
  dict -- key is state code and value is the total number of counties 
  """
  
  totals = {}
  for feature in features:
    properties = feature['properties']
    state_code = properties['STATE']
    totals[state_code] = totals.get(state_code, 0) + 1

  return totals


def test_get_state_counties_total():
  mock_features = [{
    'type': 'Feature',
    "properties": {
      'GEO_ID': '0500000US01087',
      'STATE': '01',
      'COUNTY': '087',
      'NAME': 'Macon',
      'LSAD': 'County',
      'CENSUSAREA': 608.885
    },
    "geometry": None,
  }, {
    'type': 'Feature',
    "properties": {
      'GEO_ID': '0500000US02275',
      'STATE': '02',
      'COUNTY': '275',
      'NAME': 'Wrangell',
      'LSAD': 'Cty&Bor',
      'CENSUSAREA': 2541.483
    },
    "geometry": None,
  }, {
    "type": "Feature",
    "properties": {
      'GEO_ID': '0500000US01087',
      'STATE': '01',
      'COUNTY': '087',
      'NAME': 'Macon',
      'LSAD': 'County',
      'CENSUSAREA': 608.885
    },
    "geometry": None,
  }] 

  expected_totals = {
    '01': 2,
    '02': 1
  }

  obs = get_state_counties_total(mock_features)
  print(f"obs: {obs}")
  assert(get_state_counties_total(mock_features) == expected_totals)

test_get_state_counties_total()
state_counties_totals = get_state_counties_total(features)
print(f"List of {len(state_counties_totals)} states' county totals: {state_counties_totals}")

"""Task 3, part two

Name and size of the biggest and smallest county in each state, by area
"""

"""Task 3, part three

The total and average area of counties in each state
"""