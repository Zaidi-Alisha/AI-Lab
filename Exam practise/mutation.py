# Mutation (Swap shifts for one staff)
def mutate(schedule):
staff = random.randint(0, num_staff - 1)
shift1, shift2 = random.sample(range(num_shifts), 2)
schedule[staff][shift1], schedule[staff][shift2] =
schedule[staff][shift2], schedule[staff][shift1]
return schedule
