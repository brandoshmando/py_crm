class Rolodex:
  def __init__(self):
    self.data = []

  def add_contact(self, contact):
    self.data.append(contact())

  def all_contacts(self):
    return self.data()