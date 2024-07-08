from ._anvil_designer import forgot_passwordTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class forgot_password(forgot_passwordTemplate):
  def __init__(self, email, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = "no-scroll"
    self.text_box_1.text = email

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    password = self.text_box_2.text.strip()
    retype_password = self.text_box_2_copy.text.strip()
    email = self.text_box_1.text.strip()

    if password != retype_password:
      self.error_label.text = 'Passwords do not match. Please re-enter.'
      self.error_label.visible = True
      return

    user = app_tables.users.get(email=email)
    if user:
      user['password_hash'] = anvil.users.encrypt_password(password)
      self.error_label.text = 'Password updated successfully.'
      open_form('bank_users.main_form.basic_registration_form')
    else:
      self.error_label.text = 'User not found.'
    
    self.error_label.visible = True

  def check_box_1_change(self, **event_args):
    self.password_visible = self.check_box_1.checked
    if self.password_visible:
      self.text_box_2.hide_text = False  # Show decrypted password
      self.text_box_2_copy.hide_text = False
    else:
      self.text_box_2.hide_text = True
      self.text_box_2_copy.hide_text = True
