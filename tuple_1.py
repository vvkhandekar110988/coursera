'''The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign
this list to the variable country. '''

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'),
              ('Tokyo', 'Japan', 2020, 'Future')]
country = []

for i in tuples_lst:
    print(len(i))

    if len(i) < 4:
        city_name, country_name, year = i
        country.append(country_name)
    else:
        city_name, country_name, year, forcast = i
        country.append(country_name)

print(country)


