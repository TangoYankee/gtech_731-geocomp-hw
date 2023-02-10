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
