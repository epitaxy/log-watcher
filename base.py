from operator import itemgetter


# convertion of Json Data to list by selecting columns
state, time = list( zip(*[ (x['state'], x['last_updated']) for x in raw_data]))

# another converion thorugh itemgetter (a little faster)
state, time = list( zip( *map(itemgetter('state', 'last_updated'), raw_data) ))

# each 
state = list(map(itemgetter('state'), raw_data))