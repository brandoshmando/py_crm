import sys
import prompt_text
import rolodex
import contact
class Crm:
  def __init__(self, name):
    self.name = name
    self.rolodex = rolodex.Rolodex()
    self.main_prompt()

  def main_prompt(self):
    self.print_prompt(prompt_text.MAIN)
    option = self.user_input()
    self.option_caller(option)

  def option_caller(self, option):
    options = {
                1: new_contact(),
                # 2: all_contacts(),
                # 3: edit_contact(),
                4: sys.exit
                }

  def print_prompt(self, prompt):
    print(prompt)

  def user_input(self):
    return raw_input(prompt_text.ARROW)

  def new_contact(self):
    self.print_prompt(CONTACT_FIRST)
    first_name = user_input()

    self.print_prompt(CONTACT_LAST)
    last_name = user_input()

    self.print_prompt(CONTACT_EMAIL)
    email = user_input()

    self.print_prompt(CONTACT_PHONE)
    phone = user_input()

    contact = contact.Contact(first_name, last_name, email, phone)

Crm("Rolodex")