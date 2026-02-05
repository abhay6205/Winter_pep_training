from portfolio.models import details
x = details(name="John Doe", email="john.doe@example.com", phone="1234567890", address="123 Main St")
x.save() #saves the instance to the database