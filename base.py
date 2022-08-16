from operator import itemgetter
from datetime import datetime, timedelta

# convertion of Json Data to list by selecting columns
state, time = list( zip(*[ (x['state'], x['last_updated']) for x in raw_data]))

# another converion thorugh itemgetter (a little faster)
state, time = list( zip( *map(itemgetter('state', 'last_updated'), raw_data) ))

# each 
state = list(map(itemgetter('state'), raw_data))


def string_2_dict(string_as_dict):
    from ast import literal_eval
    return literal_eval(string_as_dict)


def log_validate(log_time_as_datetime):
    now = datetime.now()
    log_time = datetime.strptime(log_time_as_datetime, "%Y-%m-%d %H:%M:%S")
    delta_t = (now - log_time)
    # print(now, log_time, delta_t)

    if delta_t >= timedelta(seconds=60):
        return "OFF"
    else:
        return "ON"