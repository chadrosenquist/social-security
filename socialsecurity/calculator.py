TIER_0_RATE = 0.9
TIER_0_MAX = 14088.0

TIER_1_RATE = 0.32
TIER_1_MAX = 84936.0

TIER_2_RATE = 0.15
TIER_2_MAX = 168600.0

def benefit_at_67(salary: float):
    """
    https://www.ssa.gov/oact/cola/piaformula.html
    :param salary:
    :return:
    """
    if salary > TIER_2_MAX:
        raise ValueError(f'Salary of {salary} exceeds maximum of {TIER_2_MAX}')

    benefit = 0.0
    if salary <= TIER_0_MAX:
        benefit += salary * TIER_0_RATE
    elif salary <= TIER_1_MAX:
        benefit += TIER_0_RATE * TIER_0_MAX
        leftover = salary - TIER_0_MAX
        benefit += leftover * TIER_1_RATE
    else:
        benefit += TIER_0_RATE * TIER_0_MAX
        benefit += TIER_1_RATE * (TIER_1_MAX - TIER_0_MAX)
        leftover = salary - TIER_1_MAX
        benefit += TIER_2_RATE * leftover
    return benefit
