#! python3
# Tabulates population & number of census tracts for each county

import openpyxl, pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

county_data = {}


for row in range(2, sheet.max_row + 1):
    # each row in sheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # make sure key for state exists
    county_data.setdefault(state, {})
    # make sure key for country in state exists
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # each row represents one census tract
    county_data[state][county]['tracts'] += 1
    # increase county pop by the pop in census tract
    county_data[state][county]['pop'] += int(pop)

# open new text file and write contents of county_data to it
print('Writing results...')

result_file = open('census2020.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()

print('Done.')


