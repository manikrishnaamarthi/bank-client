from ._anvil_designer import box10Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class box10(box10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box1')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box2")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box3")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box4")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box5")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box6")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box7")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box8")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.star_1_lendor_rgistration_form.lendorhomepage.box9")
