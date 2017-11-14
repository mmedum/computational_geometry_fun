import copy
import point


def lin_prog_1d(constraints, objective):
    right = float('inf')
    left = float('-inf')

    for constraint in constraints:
        print('Constraint {}'.format(constraint))
        ratio = constraint[0] / constraint[1]
        if constraint[1] > 0:
            left = max(left, ratio)
        else:
            if constraint[1] < 0:
                right = min(right, ratio)
            else:
                if constraint[0] > 0:
                    return None

    if left > right:
        return None

    if objective >= 0:
        return left
    else:
        return right


def lin_prog_2d(constraints, median_element):
    answers = [0, median_element.y]

    for i in range(0, len(constraints)):
        if not satisfy(answers, constraints[i]):
            this_constraint = constraints[i]
            lin_1d_constraints = []
            for temp_constraint in copy.deepcopy(constraints[:i]):
                x = (temp_constraint.x - this_constraint.x)
                y = (temp_constraint.y - this_constraint.y)
                lin_1d_constraints.append((x, y))
            answers[0] = lin_prog_1d(lin_1d_constraints, this_constraint.y)
            answers[1] = answers[0] * this_constraint.y + this_constraint.x

    print('Answer {}'.format(answers))
    return answers


def satisfy(answers, constraint):
    return constraint.y <= answers[0] * constraint.x + answers[1]


if __name__ == '__main__':
    constraints = [point.Point(1, 5), point.Point(3, 2), point.Point(1, 1), point.Point(3, 1)]
    lin_prog_2d(constraints, point.Point(2, 3))
