import unittest
import random
import string

def generateTicketNumber():
    random_string = (''.join(random.choices(string.ascii_letters + string.digits, k = 6))).upper()
    return random_string

class Ticket:

    def __init__(self, time_dict, venue, original_price):
        self.number = generateTicketNumber() # Eg. : A928XZ (six digits)
        self.time_dict = time_dict # Eg. : {"Date":"02-12-2026", "Time": "2 PM"}
        self.venue = venue # Eg. : Michigan Stadium
        self.price = original_price # Eg. : 20

    def __str__(self):
        return f"--------------------------------\n\
        Ticket #{self.number}\n\
        Venue: {self.venue}\n\
        Time: {self.time_dict['Time']} on {self.time_dict['Date']}\n\
        Price: ${self.price}\n"

class MovieTicket(Ticket):

    def __init__(self, time_dict, venue, title, position_dict, original_price):
        super().__init__(time_dict, venue, original_price) 
        self.title = title # E.g. : "3 Idiots"
        self.position_dict = position_dict # E.g. : {"Hall": 4, "Row": "G", "Seat": 23}

    def __str__(self):
        return f"--------------------------------\n\
        Movie Ticket #{self.number}---\n\
        Title: {self.title}\n\
        Venue: {self.venue}\n\
        Time: {self.time_dict['Time']} on {self.time_dict['Date']}\n\
        Position: {self.position_dict['Hall']}, {self.position_dict['Row']}, {self.position_dict['Seat']}\n\
        Price: ${self.price}\n"
    
    def applyDiscount(self, buyer_type):
        # Apply 20% discount if buyer type is Student
        # Apply 25% discount if buyer type is Elderly
        # Return original price if buyer_type is Regular
        
        if buyer_type == "Student":
            self.price = self.price * (1 - 0.20)
        elif buyer_type == "Elderly":
            self.price = self.price * (1 - 0.25)
        return self.price
    
class MuseumTicket(Ticket):

    def __init__(self, time_dict, venue, original_price):
        super().__init__(time_dict, venue, original_price)
        ticket_year = time_dict["Date"][6:] # getting just the year

        special_exhibits = {
            "The Met" : "Fashioning the Empire of Style Art of Native America",
            "MoMA" : "Emerging Ecologies: Architecture and the Environment From the Collection: 1960–1969",
            "AMNH" : "The Nature of Color, Sharks, Dark Universe (Planetarium Show)"
        }

        # TODO: TASK 1
        # If the ticket year is the current year, set self.special_exhibit to 
        # the appropriate value from the above special_exhibits dictionary
        # else set self.special_exhibit to "No special exhibits"

        if ticket_year == "2026":
            self.special_exhibit = special_exhibits[venue]
        else:
            self.speical_exhibit = "No special exhibits"

    
    def applyDiscount(self, buyer_type):
        # TODO: TASK 2 
        # Apply 100% discount if buyer type is Member (ticket is free)
        # Apply 10% discount if buyer type is Corporate
        # Apply 15% surcharge (extra cost) if buyer type is Out-of-State
        # Return original price if buyer_type is NY Resident
        
        if buyer_type == "Member":
            self.price = 0
        elif buyer_type == "Copoerate":
            self.price = self.price * (1-0.10)
        elif buyer_type == "Out-of-State":
            self.price = self.price * (1+0.15)
        return self.price

    def __str__(self):
        return f"--------------------------------\n\
        Museum Ticket #{self.number}---\n\
        Museum Name: {self.venue}\n\
        Special Exhibits: {self.special_exhibit}\n\
        Time: {self.time_dict['Time']} on {self.time_dict['Date']}\n\
        Price: ${self.price}\n"

class TestTickets(unittest.TestCase):
    
    def test_ticket(self):
        print("Testing Ticket Class...")

        ticket = Ticket({"Date": "02-12-2026", "Time": "2 PM"}, "Michigan Stadium", 20)
        # UNCOMMENT THE PRINT LINE BELOW TO SEE A SUMMARY OF YOUR TICKET 
        # print(ticket) 

        # checking ticket length and uppercase alphanumeric characters
        self.assertEqual(len(ticket.number), 6)
        self.assertTrue(ticket.number.isupper() and ticket.number.isalnum())

        # checking if time_dict gets modified
        self.assertNotEqual(ticket.time_dict.get("Date"), None)
        self.assertNotEqual(ticket.time_dict.get("Time"), None)
        self.assertEqual(ticket.time_dict["Date"], "02-12-2026")
        self.assertEqual(ticket.time_dict["Time"], "2 PM")
        self.assertEqual(ticket.venue, "Michigan Stadium")
        self.assertEqual(ticket.price, 20)
    
    def test_movie_ticket(self):
        print("Testing MovieTicket Class...")
        
        ticket = MovieTicket({"Date": "02-12-2026", "Time": "7 PM"}, "Michigan Theater", "3 Idiots", {"Hall": 4, "Row": "G", "Seat": 23}, 20)
        # UNCOMMENT THE PRINT LINE BELOW TO SEE A SUMMARY OF YOUR TICKET 
        # print(ticket)

        # checking ticket length and uppercase alphanumeric characters
        self.assertEqual(len(ticket.number), 6)
        self.assertTrue(ticket.number.isupper() and ticket.number.isalnum())

        # checking if time_dict gets modified
        self.assertNotEqual(ticket.time_dict.get("Date"), None)
        self.assertNotEqual(ticket.time_dict.get("Time"), None)
        self.assertEqual(ticket.time_dict["Date"], "02-12-2026")
        self.assertEqual(ticket.time_dict["Time"], "7 PM")

        # TODO: TASK 3
        # 3.A Check if the ticket venue and title is as expected
        # 3.B Check the keys in position_dict exist
        # 3.C Check the key value pairs in position_dict
        
        self.assertEqual(ticket.venue,"Michigan Theater")
        self.assertEqual(ticket.title, "3 Idiots")

        self.assertIn("Hall", ticket.position_dict)
        self.assertIn("Row", ticket.position_dict)
        self.assertIn("Seat", ticket.position_dict)

        self.assertEqual(ticket.position_dict["Hall"],4)
        self.assertEqual(ticket.position_dict["Row"],"G")
        self.assertEqual(ticket.position_dict["Seat"],"23")

        # checking if discounts get applied correctly
        self.assertEqual(ticket.price, 20)
        self.assertAlmostEqual((ticket.applyDiscount("Student")), 16)
        
        ticket2 = MovieTicket({"Date": "02-12-2026", "Time": "11 AM"}, "State Theater", "Inception", {"Hall": 4, "Row": "G", "Seat": 19}, 45)
        # UNCOMMENT THE PRINT LINE BELOW TO SEE A SUMMARY OF YOUR TICKET 
        # print(ticket2)
        
        self.assertEqual(ticket2.price, 45)
        self.assertAlmostEqual((ticket2.applyDiscount("Elderly")), 33.75)

    def test_museumticket(self):
        print("Testing MuseumTicket Class...")
        
        ticket1 = MuseumTicket({"Date": "02-12-2026", "Time": "7 PM"}, "AMNH", 30)
        # UNCOMMENT THE PRINT LINE BELOW TO SEE A SUMMARY OF YOUR TICKET 
        # print(ticket1)

        # checking ticket1 length and uppercase alphanumeric characters
        self.assertEqual(len(ticket1.number), 6)
        self.assertTrue(ticket1.number.isupper() and ticket1.number.isalnum())

        # checking if ticket1 time_dict gets modified
        self.assertNotEqual(ticket1.time_dict.get("Date"), None)
        self.assertNotEqual(ticket1.time_dict.get("Time"), None)
        self.assertEqual(ticket1.time_dict["Date"], "02-12-2026")
        self.assertEqual(ticket1.time_dict["Time"], "7 PM")

        # checking if the ticket1's venue and special exhibit are as expected
        self.assertEqual(ticket1.venue, "AMNH")
        self.assertEqual(ticket1.special_exhibit, "The Nature of Color, Sharks, Dark Universe (Planetarium Show)")

        # TODO: TASK 4
        # 4.A Check if the ticket2's venue and special exhibit are as expected
        # 4.B Check if ticket2's Member discount gets applied correctly
        # 4.C Check if ticket3's Corporate discount gets applied correctly
        # 4.D Check if ticket4's Out-of-State discount gets applied correctly
        ticket2 = MuseumTicket({"Date": "01-05-2026", "Time": "1 PM"}, "MoMA", 35)
        ticket3 = MuseumTicket({"Date": "01-05-2026", "Time": "1 PM"}, "MoMA", 35)
        ticket4 = MuseumTicket({"Date": "01-05-2026", "Time": "1 PM"}, "MoMA", 35)

        # UNCOMMENT THE PRINT LINE BELOW TO SEE A SUMMARY OF YOUR TICKETS 
        # print(ticket2,ticket3,ticket4)
        
        # YOUR CODE HERE


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
