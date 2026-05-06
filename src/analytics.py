"""
Calculations for fatigue, recovery, and performance trends to be used throghout our max performance project
"""

import numpy as np
from functools import reduce
import statistics

def calc_acwr(recent, long):
    """
    Calculates ACWR with recent being short-term workload (~7 days)
    and the long_term being long term workload (~28 days)
    """
    if sum(long) == 0:
        return 0
    return sum(recent) / sum(long)

def recovery_status(acwr):     # Recovery status labeled based on ACWR
    
    if acwr < 0.8:
        return "Undertrained"
    elif acwr <= 1.3:
        return "Optimal"
    else:
        return "Overtrained"

def exercise_dist(exercises):     # Returns distribution of exercises as percentages
    
    if not exercises:
        return {}

    total = len(exercises)
    counts = {}

    for ex in exercises:
        if ex in counts:
            counts[ex] += 1
        else:
            counts[ex] = 1

    result = {}
    for ex in counts:
        result[ex] = counts[ex] / total

    return result

def trend_analy(x, y):     # Linear tred analysis, returns slope, intercept, and R^2 value
    
    x = np.array(x)
    y = np.array(y)

    slope, intercept = np.polyfit(x, y, 1)
    y_pred = slope * x + intercept

    residual_ss = np.sum((y - y_pred) ** 2)
    total_ss = np.sum((y - np.mean(y)) ** 2)

    r2 = 1 - (residual_ss / total_ss)

    return slope, intercept, r2


def aggregate_calories(calories):     # Sums calorie values using reduce
    
    if not calories:
        return 0
    return reduce(lambda a, b: a + b, calories)

def describe_series(data):     # Returns basic stats for a dataset
    
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)

    if len(data) > 1:
        stdev_val = statistics.stdev(data)
    else:
        stdev_val = 0

    return {
        "mean": mean_val,
        "median": median_val,
        "stdev": stdev_val
    }