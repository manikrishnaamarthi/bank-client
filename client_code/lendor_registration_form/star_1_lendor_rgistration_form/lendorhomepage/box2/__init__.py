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

        # Query your data
        data = app_tables.view_bor_loan_requests.get()   # Assuming you want the first record

        if data:
            initial_commitment = data['Initial Commitment']
            top_up = data['Top Up']
            total_loan_disbursed = data['Total Loan Disbursed']

            available_balance = initial_commitment + top_up - total_loan_disbursed

            self.output_lbl.text = str(available_balance)
        else:
            self.output_lbl.text = "No data available"

    # ... (your other methods)

    

   # anvil.server.call('view_bor_loan_requests', view_available_balance)


   

    '''def button_1_click(self, **event_args):
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
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box10")'''
