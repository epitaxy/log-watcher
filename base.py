from operator import itemgetter


# convertion of Json Data to list
state, time = list( zip(*[ (x['state'], x['last_updated']) for x in raw_data]))

# another converion thorugh itemgetter (a little faster)
state, time = list( zip( *map(itemgetter('state', 'last_updated'), raw_data) ))

state = list(map(itemgetter('state'), raw_data))