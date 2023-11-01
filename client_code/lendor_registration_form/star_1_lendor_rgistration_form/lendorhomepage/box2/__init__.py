from ._anvil_designer import box2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class box2(box2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_vb.items = app_tables.view_bor_loan_requests.search()

  def calculate(self, **event_args):
    #view_available_balance = float(view_available_balance)
    initial_commitment = float(initial_commitment.text)
    view_available_balance = int(initial_commitment+0)-(12)

    self.output_lbl.text = f"{view_available_balance}"
    

   # anvil.server.call('view_bor_loan_requests', view_available_balance)

  #def edit_view_available_balance(self):
    #view_available_balance =  self.view_available_balance

    #self.output_lbl.text = f"{view_available_balance}"
  # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box1")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box3")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box4")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box5")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box6")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box7")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box8")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box9")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box10")
