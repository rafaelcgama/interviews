/*
Buses and Passengers Problem
----------------------------

CREATE TABLE bus (
    id
    origin
    destination
    time
    UNIQUE (origin, destination, time)
);

CREATE TABLE passenger (
    id
    origin
    destination
    time
);

Each row of table buses contains information about a single bus’s origin (origin), destination (destination) and time
of departure (time).

Each row of table passengers describes a single passenger and contains information about the station they’re traveling
from (origin), the station they’re traveling to (destination) and the time they will arrive at the departure
station (time). Passengers will board the earliest possible bus that travels directly to their desired destination.
Passengers can still board a bus if it departs in the same minute that they arrive at the station.
All passengers who are still at the station at 23:59 and don’t board any of the 23:59 buses will leave the platform
without boarding any bus.

You can assume that no two buses with the same origin and destination depart at the same time.

Write an SQL query that, for each bus, returns the number of passengers boarding it. For each bus you should provide
its id (id) and the number of passengers on board (passengers_on_board). Rows should be ordered by the
id column (in ascending order).

Time is represented as a string in the format HH:MM.
*/


/* SQL Solution (Simple Version) */

SELECT b.id                     AS id,
    COALESCE(COUNT(p.id), 0) AS passengers_on_board
FROM buses b
    LEFT JOIN passengers p
    ON p.origin = b.origin
    AND p.destination = b.destination
    AND b.time = (SELECT MIN(b2.time)
                  FROM buses b2
                  WHERE b2.origin = p.origin
                  AND b2.destination = p.destination
                  AND b2.time >= p.time
                 )
GROUP BY b.id
ORDER BY b.id;