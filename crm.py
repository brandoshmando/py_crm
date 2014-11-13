import sys
import prompt_text
import rolodex
from contact import Contact

class Crm:
  def __init__(self, name):
    self.name = name
    self.rolodex = rolodex.Rolodex()
    self.main_prompt()

  def main_prompt(self):
    self.clear_term()
    self.print_prompt(prompt_text.MAIN)
    option = self.user_input()
    self.option_caller(option)

  def option_caller(self, option):
    options = { 1: self.new_contact, 2: self.display_contacts, 3: "self.edit_contact()", 4: sys.exit }
    options[int(option)]

  def print_prompt(self, prompt):
    print(prompt)

  def user_input(self):
    return raw_input(prompt_text.ARROW)

  def new_contact(self):
    self.print_prompt(prompt_text.CONTACT_FIRST)
    first_name = self.user_input()

    self.print_prompt(prompt_text.CONTACT_LAST)
    last_name = self.user_input()

    self.print_prompt(prompt_text.CONTACT_EMAIL)
    email = self.user_input()

    self.print_prompt(prompt_text.CONTACT_PHONE)
    phone = self.user_input()

    new_contact = Contact(first_name, last_name, email, phone)

    self.rolodex.add_contact(new_contact)

  def display_contacts(self):
    contacts = self.rolodex.contacts

    if not contacts:
      print_prompt(prompt_text.EMPTY)
    else:
      for contact in contacts:
        self.format_contact(contact)

  def format_contact(self, contact):
    print """
    %(last)s, %(first)s
    -----------------
    Email: %(email)s
    -----------------
    Phone Number: %(phone)s
    """ % \
    { "first": contact.first_name,"last": contact.last_name,"email": contact.email, "phone": contact.phone}

  def clear_term(self):
    print chr(27) + "[2J"


Crm("Rolodex")