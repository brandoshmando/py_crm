import sys
import os
import prompt_text
class Crm:
  def __init__(self, name):
    self.name = name
    self.main_prompt()

  def main_prompt(self):
    self.print_prompt(prompt_text.MAIN)
    self.user_input()

  def print_prompt(self, prompt):
    print(prompt)

  def user_input(self):
    return raw_input('--->')


Crm("Rolodex")