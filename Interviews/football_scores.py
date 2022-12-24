# Goldman Sachs 2022

"""The number of goals achieved by two football
teams in matches in a league is given in the form
of two lists. For each match of team B, compute
the total number of matches of team A where
team A has scored less than or equal to the
number of goals scored by team B in that match.
"""
def scores(teamA, teamB):

    teamA.sort()
    for i, v in enumerate(teamB):
        # Binary search
        l, r = 0, len(teamA) - 1
        while l <= r:
            mid = (l + r) // 2
            if teamA[mid] > v:
                r = mid - 1
            else:
                l = mid + 1
        teamB[i] = l

    return teamB