import sys
import prompt_text
import rolodex
from contact import Contact
from IPython import embed

class Crm:
  def __init__(self, name):
    self.name = name
    self.rolodex = rolodex.Rolodex()
    self.main_prompt()

  def main_prompt(self):
    while True:
      self.clear_term()
      self.print_prompt(prompt_text.MAIN)
      option = int(self.user_input())
      self.option_caller(option)

  def option_caller(self, option):
    options = { 1: self.new_contact,
                2: self.display_contacts,
                3: self.edit_contact,
                4: sys.exit }
    options[int(option)]()

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
    return

  def display_contacts(self):
    self.clear_term()
    contacts = self.rolodex.contacts
    if not contacts:
      self.print_prompt(prompt_text.EMPTY)
    else:
      for idx, contact in enumerate(contacts):
        self.format_contact(contact, idx)
    self.hold()

  def format_contact(self, contact, index):
    print """
    -----------------------
    [%(idx)s] %(last)s, %(first)s
    -----------------------
    Email: %(email)s
    -----------------------
    Phone Number: %(phone)s
    -----------------------
    """ % \
    { "first": contact.first_name,"last": contact.last_name,"email": contact.email, "phone": contact.phone, "idx": index+1}

  def edit_contact(self):
    self.display_contacts()
    self.print_prompt(prompt_text.SELECT_CONTACT)
    contact_id = int(self.user_input())
    contact = self.rolodex.contacts[contact_id - 1]
    field = self.select_field()
    value = self.new_value()
    fields = { 1: "first_name",
               2: "last_name",
               3: "email",
               4: "phone"}
    setattr(contact, fields[field], value)
    return

  def select_field(self):
    self.print_prompt(prompt_text.FIELDS)
    selection = int(self.user_input())
    while True:
      if selection < 1 and selection > 4:
        self.print_prompt(prompt_text.INVALID_SELECTION)
      else:
        return selection

  def new_value(self):
    self.print_prompt(prompt_text.NEW_VAL)
    return self.user_input()

  def clear_term(self):
    print chr(27) + "[2J"

  def hold(self):
    self.print_prompt(prompt_text.HOLD)
    self.user_input()
    return

Crm("Rolodex")