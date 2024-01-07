
# subnet mask 
# starting sequence number - configure multiple prefix-list, this is the starting sequence number
# increment 0 starting value
mask = 22
start_seq = 100
increment = 0

# advertise_prefix: insert/edit list of prefixes to be configured 
advertise_prefix = ['10.10.10.0', '20.20.20.0','30.30.30.0', '40.40.40.0']


# Keys iterated from advertise_prefix list. start_seq is value.
prefix_seq = {prefix:start_seq for prefix in advertise_prefix}


"""
For loop in dictionary for each key, each value would be added by the value of 'increment' which starts from 0, then increased by 10 per iteration.
resulting dictionary would be a key:value pair of a prefix with its respective incrementing sequence number.
"""
for key in prefix_seq:
    prefix_seq[key]+=increment
    increment+=10


#convert the generated dictionary to a list of tuple for the jinja2 environment to accept the values
prefix_seq_input = prefix_seq.items()


