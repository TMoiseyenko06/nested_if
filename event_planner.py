#Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
type_of_food = input("What type of food would everyone like to eat?")

#Task 2: Venue Selection
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "Line Array" if attendees > 200 else "Portable speaker setup"
projector = "Basic Projector" if attendees < 150 else "Heavy Duty Projector"

#Task 3: Catering Choices
catering_service = "Veggie Delight Caterers" if type_of_food == "vegetarian" else "Gourmet Meals Caterers"

print(venue,audio_system,projector,catering_service)