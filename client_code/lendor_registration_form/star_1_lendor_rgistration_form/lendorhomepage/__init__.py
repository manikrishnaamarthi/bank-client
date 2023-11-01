from ._anvil_designer import lendorhomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class lendorhomepage(lendorhomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box1")

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.main_form")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box2")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box3")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box4")

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box5")

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box6")

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box7')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box8")

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box9")

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box10")

