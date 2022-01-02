# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def convert_damage(data):
  damages_conv = []
  for x in data:
    if x == 'Damages not recorded':
      damages_conv.append(x)
    elif 'B' in x:
      damage = float(x[:-1]) * conversion['B']
      damages_conv.append(damage)
    else:
      damage = float(x[:-1]) * conversion['M']
      damages_conv.append(damage)
  return damages_conv
# test function by updating damages
# print(convert_damage(damages))

# 2 
# Create a Table
def table():
  master_list = list(zip(names,months,years,max_sustained_winds,areas_affected,convert_damage(damages),deaths))
  hurricanes = {}
  for x in master_list:
    if x[0] not in hurricanes:
      hurricanes[x[0]] = {}
    for elem in x:
      hurricanes[x[0]]['Name'] = x[0]
      hurricanes[x[0]]['Month'] = x[1]
      hurricanes[x[0]]['Year'] = x[2]
      hurricanes[x[0]]['Max Sustained Wind'] = x[3]
      hurricanes[x[0]]['Areas Affected'] = x[4]
      hurricanes[x[0]]['Damage'] = x[5]
      hurricanes[x[0]]['Deaths'] = x[6]
  return hurricanes
# Create and view the hurricanes dictionary
# print(table())


# 3
# Organizing by Year
def convert_year():
  hurricanes = table(names,months,years,max_sustained_winds,areas_affected,convert_damage(damages),deaths)
  hurricane_years = {}
  for x in years:
    if x not in hurricane_years:
      hurricane_years[x] = []
    for v, u in hurricanes.items():
      if u['Year'] == x:
         hurricane_years[x].append(u)
  return hurricane_years
# create a new dictionary of hurricanes with year and key
# print(convert_year())


# 4
# Counting Damaged Areas
def area_count():
  areas = set()
  area_dict = {}
  hurricanes = table()
  for x in areas_affected:
    for place in x:
      areas.add(place)
  for x in areas:
    if x not in area_dict:
      area_dict[x] = 0
    for key,val in hurricanes.items():
      if x in val['Areas Affected']:
        area_dict[x] += 1
  return area_dict
# create dictionary of areas to store the number of hurricanes involved in
# print(area_count())

# 5 
# Calculating Maximum Hurricane Count
def max_area_count():
  area_counter = area_count()
  max = sorted(area_counter.items(),key=lambda x: x[1],reverse=True)
  return max[0]
# find most frequently affected area and the number of hurricanes involved in
# print(max_area_count())


# 6
# Calculating the Deadliest Hurricane
def death():
  hurricanes = table()
  death_count = []
  for key,val in hurricanes.items():
    death_count.append((key,val['Deaths']))
  return death_count
def max_deaths():
  death_count = deaths()
  max = sorted(death_count,key=lambda x:x[1],reverse=True)
  return max[0]
# find highest mortality hurricane and the number of deaths
# print(max_deaths())

# 7
# Rating Hurricanes by Mortality
def mortality_scale():
  death_count = death()
  hurricanes = table()
  mortality = {}
  for num in range(1,6):
    if num not in mortality:
      mortality[num] = []
  for key,val in death_count:
    if val <= 100:
      mortality[1].append(hurricanes[key])
    elif val <= 500 and val > 100:
      mortality[2].append(hurricanes[key])
    elif val <= 1000 and val > 500:
      mortality[3].append(hurricanes[key])
    elif val <= 10000 and val > 1000:
      mortality[4].append(hurricanes[key])
    else:
      mortality[5].append(hurricanes[key])
  return mortality
# categorize hurricanes in new dictionary with mortality severity as key
# print(mortality_scale())


# 8 Calculating Hurricane Maximum Damage
def cost():
  hurricanes = table()
  costs = []
  for key,val in hurricanes.items():
    if type(val['Damage']) == float:
      costs.append((key,val['Damage']))
    else:
      pass
  return costs
def max_cost():
  costs = cost()
  max = sorted(costs,key=lambda x:x[1],reverse=True)
  return max[0]
# find highest damage inducing hurricane and its total cost
# print(max_cost())


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def damage_scale():
  costs = cost()
  hurricanes = table()
  damage_cost = {}
  for num in range(1,6):
    if num not in damage_cost:
      damage_cost[num] = []
  for key,val in costs:
    if val <= 100000000:
      damage_cost[1].append(hurricanes[key])
    elif val <= 1000000000 and val > 100000000:
      damage_cost[2].append(hurricanes[key])
    elif val <= 10000000000 and val > 1000000000:
      damage_cost[3].append(hurricanes[key])
    elif val <= 50000000000 and val > 10000000000:
      damage_cost[4].append(hurricanes[key])
    else:
      damage_cost[5].append(hurricanes[key])
  return damage_cost
# categorize hurricanes in new dictionary with damage severity as key
print(damage_scale())
