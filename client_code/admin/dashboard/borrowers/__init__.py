from ._anvil_designer import borrowersTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrowers(borrowersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.fin_user_profile.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []
    self.list_7 = []
    self.list_8 = []
    self.user_type = []
    
    for i in self.data:
      a+=1
      self.list_1.append(i['customer_id'])
      self.list_2.append(i['full_name'])
      self.list_3.append(i['email_user'])
      self.list_4.append(i['usertype'])
      self.list_5.append(i['last_confirm'])
      self.list_6.append(i['date_of_birth'])
      self.list_7.append(i['mobile'])
      self.list_8.append(i['registration_approve'])
      self.user_type.append(i['usertype'])
    print(a)

    self.result = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      b = -1
      for i in self.user_type:
        b+=1
        if i == 'borrower' or i == 'Borrower':
          self.index.append(b)
          
      for i in self.index:
        self.result.append({'coustmer_id' : self.list_1[i], 'full_name' : self.list_2[i], 'email_user' : self.list_3[i], 'usertype' : self.list_4[i], 'last_confirm' : self.list_5[i],
                          'date_of_birth' : self.list_6[i], 'mobile' : self.list_7[i], 'registration_approve' : self.list_8[i]})

      self.items = self.result

      print(self.list_1, self.list_2, self.list_3)
      print(self.result)
      print(a)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard')
