# Data Source https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_050_00_5m.json
# Read from a local file
import json
import io

# Use "with ... as ..." to better handle exceptions
# https://stackoverflow.com/questions/30996289/utf8-codec-cant-decode-byte-0xf3
with io.open('assignment-two/data/gz_2010_us_050_00_5m.json', encoding='latin-1') as f:
  data = json.load(f)

print('Number of Counties in US: {}'.format(len(data['features'])))

print(data['features'][1]['properties']['NAME'])


"""
Task 2
Top three counties and their states
"""
features = data['features']

first_feature = features[1]

county_states = dict()
for feature in features:
  properties = feature['properties']
  county_name = properties['NAME']
  state_code = properties['STATE']
  county_states.setdefault(county_name, []).append(state_code)

top_n = 3
top_counties = [None] * top_n

print(first_feature['properties'])
print(county_states['Wade Hampton'])

max_county = ''
max_county_total = 0
for county_state in county_states:
  county_state
