import sys


def lin_prog_1d(constraints, objective):
    right = float('inf')
    left = float('-inf')

    for constraint in constraints:
        ratio = constraint[0] / constraint[1]
        if constraint[1] > 0:
            left = max(left, ratio)
        else:
            if constraint[1] < 0:
                right = min(right, ratio)
            else:
                if constraint[0] > 0:
                    return "INFEASIBLE"

    if left > right:
        return "INFEASIBLE"

    if objective > 0:
        return left
    if objective < 0:
        return right
    else:
        return right


if __name__ == '__main__':
    constraints = [
        (10, 3),
        (8, 3),
        (-4, -1),
    ]
    objective = -3
    optimum = lin_prog_1d(constraints, objective)
    print("Expected is 4", optimum)

    objective = 3
    optimum = lin_prog_1d(constraints, objective)
    print("Expected is 10/3", optimum)
