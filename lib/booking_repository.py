from lib.booking import Booking
import datetime

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_bookings(self, user_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE user_id = %s', [user_id])
        bookings = []
        for row in rows:
            bookings.append(Booking(row["id"], row["datetime"], row["gig_id"], row["user_id"], row["ticket_count"]))
        return bookings

    def get_by_id(self, booking_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [booking_id])
        if rows == []:
            return None
        else:
            row = rows[0]
            return Booking(row["id"], row["datetime"], row["gig_id"], row["user_id"], row["ticket_count"])

    def make_booking(self, gig_id, user_id, ticket_count):
        booking_datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self._connection.execute('INSERT INTO bookings (datetime, gig_id, user_id, ticket_count) VALUES (%s, %s, %s, %s)', [booking_datetime_str, gig_id, user_id, ticket_count])

    def cancel_booking(self, booking_id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [booking_id])
