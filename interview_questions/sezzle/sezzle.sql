/*
Buses and Passengers Problem
----------------------------

Each bus has:
 - id
 - origin
 - destination
 - time (departure time)

Each passenger has:
 - id
 - origin
 - destination
 - time (arrival time)

A passenger can board a bus only if:
 - bus.origin = passenger.origin
 - bus.destination = passenger.destination
 - bus.time >= passenger.time
 - the passenger must take the earliest possible eligible bus

Goal:
Return, for every bus, how many passengers board it.
Buses with no passengers must still appear with a count of 0.
Output must be sorted by bus.id.

Logic:
For each passenger:
 1) Find buses with the same origin/destination.
 2) Keep only buses where bus.time >= passenger.time.
 3) Select the bus with the smallest time (earliest departure).
 4) Count how many passengers map to each bus.

Two valid SQL approaches:
 - Using a correlated subquery with MIN(bus.time)
 - Using window functions (ROW_NUMBER)

This file may include either version.
*/


## SQL Solution (Simple Version)

SELECT
    b.id AS id,
    COALESCE(COUNT(p.id), 0) AS passengers_on_board
FROM buses b
LEFT JOIN passengers p
  ON p.origin = b.origin
 AND p.destination = b.destination
 AND b.time = (
       SELECT MIN(b2.time)
       FROM buses b2
       WHERE b2.origin      = p.origin
         AND b2.destination = p.destination
         AND b2.time       >= p.time
     )
GROUP BY b.id
ORDER BY b.id;