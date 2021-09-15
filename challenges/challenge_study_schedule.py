def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if not (isinstance(target_time, int) and target_time >= 0):
        return None
    for period in permanence_period:
        if not (
            isinstance(period, tuple)
            and isinstance(period[0], int)
            and isinstance(period[1], int)
        ):
            return None
        if period[0] <= target_time and period[1] >= target_time:
            counter += 1
    return counter
