def get_previous_rental_id(rental_id):
    if rental_id > 1:
        return 'Ren-{} ID'.format(rental_id - 1)
    else:
        return '-'
