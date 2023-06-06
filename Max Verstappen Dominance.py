import numpy as np
import regression_model
from driver_scores import driver_points
from points import POINTS, SPRINT_POINTS, FASTEST_LAP_POINTS
from season2023 import races_left, sprint_races

drivers = list(driver_points.keys())

talent_scores = [0.70, 0.07, 0.05, 0.07, 0.05, 0.015, 0.015, 0.011, 0.0034, 0.0033, 0.0033, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]

car_performance = [1.0, 1.0, 0.6, 0.8, 0.8, 0.5, 0.5, 0.6, 0.4, 0.4, 0.3, 0.1, 0.3, 0.2, 0.2, 0.15, 0.1, 0.12, 0.15, 0.12]

labels = [1.0, 1.0, 0.6, 0.8, 0.8, 0.5, 0.5, 0.6, 0.4, 0.4, 0.3, 0.1, 0.3, 0.2, 0.2, 0.15, 0.1, 0.12, 0.15, 0.12] #placeholder data

probabilities = regression_model.find_prob(talent_scores, car_performance, labels)
print(probabilities)
races_cnt = len(races_left)
sprint_cnt = len(sprint_races)
for race in races_left:
    races_cnt -= 1
    # Simulate the race result for each driver
    race_results = np.random.choice(drivers, size=len(drivers), replace=False, p=probabilities)

    for i, driver in enumerate(race_results):
        driver_points[driver] += POINTS[i]
        if driver == 'Verstappen':
            driver_points[driver] += FASTEST_LAP_POINTS  # Only Verstappen gets fastest lap points, because ofc he does

    # Handle sprint races
    if race in sprint_races:
        sprint_cnt -= 1
        sprint_results = np.random.choice(drivers, size=len(drivers), replace=False, p=probabilities)
        for i, driver in enumerate(sprint_results):
            driver_points[driver] += SPRINT_POINTS[i]

    # Check if Verstappen has more points than all other drivers and that lead can't be overcome
    max_remaining_points = races_cnt * POINTS[0] + sprint_cnt * SPRINT_POINTS[0] + FASTEST_LAP_POINTS * races_cnt
    if all(driver_points['Verstappen'] > driver_points[other_driver] + max_remaining_points for other_driver in driver_points if other_driver != 'Verstappen'):
        print(f"Verstappen could secure the championship in {race} if the results follow this simulation.")
        break
