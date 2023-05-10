from collections import Counter, defaultdict

# PART 1
"""
In MotoGP motorcycle racing, there are 10 races in a season. 

'[
    ["lorenzo", "hayden", "dovizioso", "rossi", "marquez"],
    ["marquez", "hayden", "rossi", "dovizioso", "lorenzo"],
    ["rossi", "lorenzo", "dovizioso", "hayden", "marquez"],
    ["dovizioso", "marquez", "rossi", "lorenzo", "hayden"],
    ["marquez", "dovizioso", "rossi", "lorenzo", "hayden"],
    ["marquez", "dovizioso", "hayden", "rossi", "lorenzo"],
    ["marquez", "dovizioso", "hayden", "lorenzo", "rossi"],
    ["marquez", "rossi", "lorenzo", "hayden", "dovizioso"],
    ["lorenzo", "marquez", "rossi", "dovizioso", "hayden"],
    ["marquez", "dovizioso", "hayden", "lorenzo", "rossi"]
]'


Points are awarded to each rider based on what position they finish in each race.

1st: 15 points
2nd: 10 points
3rd: 5 points

At the end of the season, whoever has the most total points wins the championship.

Print out how many points each rider has at the end of the season. Order is not important.

Expected results (format may vary):
{
    'dovizioso': 65,
    'hayden': 35,
    'lorenzo': 45,
    'marquez': 110,
    'rossi': 45
}
"""


def championship1(races, points):
    racer_points = defaultdict(int)
    for race in races:
        for i, racer in enumerate(race):
            if i == 0:
                racer_points[racer] += points[i]
            elif i == 1:
                racer_points[racer] += points[i]

            elif i == 2:
                racer_points[racer] += points[i]

            else:
                racer_points[racer] += 0
    return dict(sorted(racer_points.items(), key=lambda x: x[1], reverse=True))


"""
Part 2

After each race print the current standings (in order, most points to least points).

Expected results (formatting may vary):

race 1
rider           points
-----------------------
lorenzo         15
hayden          10
dovizioso       5
marquez         0
rossi           0
 
race 2
rider           points
-----------------------
hayden          20
lorenzo         15
marquez         15
dovizioso       5
rossi           5
 
race 3
rider           points
-----------------------
lorenzo         25
hayden          20
rossi           20
marquez         15
dovizioso       10
 
race 4
rider           points
-----------------------
lorenzo         25
dovizioso       25
marquez         25
rossi           25
hayden          20
 
race 5
rider           points
-----------------------
marquez         40
dovizioso       35
rossi           30
lorenzo         25
hayden          20
 
race 6
rider           points
-----------------------
marquez         55
dovizioso       45
rossi           30
lorenzo         25
hayden          25
 
race 7
rider           points
-----------------------
marquez         70
dovizioso       55
hayden          30
rossi           30
lorenzo         25
 
race 8
rider           points
-----------------------
marquez         85
dovizioso       55
rossi           40
lorenzo         30
hayden          30
 
race 9
rider           points
-----------------------
marquez         95
dovizioso       55
lorenzo         45
rossi           45
hayden          30
 
race 10
rider           points
-----------------------
marquez         110
dovizioso       65
lorenzo         45
rossi           45
hayden          35

"""


def championship2(races, points):
    racer_points = defaultdict(int)
    for x, race in enumerate(races):
        print(f"race {x + 1}")
        print("rider           points")
        print("-----------------------")
        for i, racer in enumerate(race):
            if i == 0:
                racer_points[racer] += points[i]
            elif i == 1:
                racer_points[racer] += points[i]

            elif i == 2:
                racer_points[racer] += points[i]

            else:
                racer_points[racer] += 0

        for x, y in Counter(racer_points).most_common():
            print(x + "----------" + str(y))
        print("")


"""
Part 3 

After each race, determine if a rider is already guaranteed to win the championship, and if so, who is the winner.

Expected results (formatting may vary):

race 1
no winner yet
race 2
no winner yet
race 3
no winner yet
race 4
no winner yet
race 5
no winner yet
race 6
no winner yet
race 7
no winner yet
race 8
no winner yet # tie
race 9
we have a winner after 9 races! marquez
race 10
"""


def championship3(races, points):
    def has_winner(standing, races_left):
        is_possible = standing[0][1] <= standing[1][1] + (15 * races_left)
        if is_possible:
            print(f'no winner yet {"# tie" if standing[0][1] == standing[1][1] + (15 * races_left) else ""}')
        else:
            print(f'we have a winner after {10 - races_left} races! {standing[0][0]}')
            return True

    racer_points = defaultdict(int)
    num_races = len(races)
    is_over = False
    for x, race in enumerate(races):
        print(f"race {x + 1}")
        if is_over:
            break
        for i, racer in enumerate(race):
            if i == 0:
                racer_points[racer] += points[i]
            elif i == 1:
                racer_points[racer] += points[i]

            elif i == 2:
                racer_points[racer] += points[i]

            else:
                racer_points[racer] += 0

        num_races -= 1

        standing = sorted(racer_points.items(), key=lambda x: x[1], reverse=True)

        is_over = has_winner(standing, num_races)


if __name__ == "__main__":
    races = [
        ["lorenzo", "hayden", "dovizioso", "rossi", "marquez"],
        ["marquez", "hayden", "rossi", "dovizioso", "lorenzo"],
        ["rossi", "lorenzo", "dovizioso", "hayden", "marquez"],
        ["dovizioso", "marquez", "rossi", "lorenzo", "hayden"],
        ["marquez", "dovizioso", "rossi", "lorenzo", "hayden"],
        ["marquez", "dovizioso", "hayden", "rossi", "lorenzo"],
        ["marquez", "dovizioso", "hayden", "lorenzo", "rossi"],
        ["marquez", "rossi", "lorenzo", "hayden", "dovizioso"],
        ["lorenzo", "marquez", "rossi", "dovizioso", "hayden"],
        ["marquez", "dovizioso", "hayden", "lorenzo", "rossi"]
    ]

    points = {
        0: 15,
        1: 10,
        2: 5
    }

print(championship1(races, points))
print("")
championship2(races, points)
print("")
championship3(races, points)
