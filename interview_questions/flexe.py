### FLEXE ###
def airplane_seat_reservation(N, S):
    total_seats = N * 3
    seats_row = {str(row): 'ABCDEFGHJK' for row in range(1, N + 1)}
    booked_seats = S.split()

    for seat in booked_seats:
        row = seat[0]
        position = seat[1]
        if position in 'ABC':
            seat_remove = 'ABC'

        elif position in 'EF':
            seat_remove = 'DEFG'

        else:
            seat_remove = 'HJK'

        if seat_remove in seats_row[row]:
            seats_row[row] = seats_row[row].replace(seat_remove, "")
            total_seats -= 1

    return total_seats
