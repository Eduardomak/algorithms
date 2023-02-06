def study_schedule(permanence_period: list, target_time: int) -> int:
    """Faça o código aqui."""
    count = 0
    try:
        for _ in permanence_period:
            if target_time >= _[0] and target_time <= _[1]:
                count += 1
    except TypeError:
        return None
    return count
