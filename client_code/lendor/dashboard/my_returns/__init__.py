# from ._anvil_designer import my_returnsTemplate
# from anvil import *
# import plotly.graph_objects as go
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# from .. import main_form_module as main_form_module

# class my_returns(my_returnsTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)
#     self.user_id = main_form_module.userId

#     # Check if user_id is correctly set
#     print(f"User ID: {self.user_id}")

#     # Any code you write here will run before the form opens.
#     self.create_bar_chart()

#   def create_bar_chart(self):
#     # Fetch investment data for the specific user
#     investments = app_tables.fin_lender.search(customer_id=self.user_id)
    
#     # Debugging: Print fetched investments
#     print(f"Fetched investments for user {self.user_id}: {list(investments)}")
    
#     # Initialize variables to store total investments and returns
#     total_investment = 0
#     total_returns = 0
    
#     for investment in investments:
#       total_investment += investment['investment']
#       total_returns += investment['return_on_investment']

#     # Debugging: Print aggregated values
#     print(f"Total Investment: {total_investment}, Total Returns: {total_returns}")

#     # Prepare data for bar chart
#     categories = ['Investment', 'Returns']
#     values = [total_investment, total_returns]

#     # Create bar chart trace
#     trace = go.Bar(x=categories, y=values, marker_color=['blue', 'green'])

#     # Create a layout
#     layout = go.Layout(
#       title='Investment and Returns for User',
#       xaxis=dict(title='Category'),
#       yaxis=dict(title='Amount'),
#       barmode='group'  # Use group mode to display bars side by side
#     )

#     # Create a figure
#     fig = go.Figure(data=[trace], layout=layout)

#     # Debugging: Print the figure to ensure it's created
#     print(f"Created figure: {fig}")

#     # Debugging: Check if plot_1 is a valid component
#     if hasattr(self, 'plot_1'):
#         print("plot_1 is a valid component")

#     # Set the plot in the Plot component
#     self.plot_1.data = fig

#     # Force re-rendering of the plot component by setting the layout
#     self.plot_1.layout = layout

#     # Debugging: Check if the plot is assigned correctly
#     print(f"Assigned figure to plot_1: {self.plot_1.data}")

#   def button_1_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     open_form('lendor.dashboard')

#   def plot_1_click(self, points, **event_args):
#     """This method is called when a data point is clicked."""
#     self.create_bar_chart()


from ._anvil_designer import my_returnsTemplate
from anvil import *
import plotly.graph_objects as go
from anvil.tables import app_tables
from .. import main_form_module as main_form_module

class my_returns(my_returnsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = main_form_module.userId

    # Check if user_id is correctly set
    print(f"User ID: {self.user_id}")

    # Any code you write here will run before the form opens.
    self.create_bar_chart()

  def create_bar_chart(self):
    # Fetch investment data for the specific user
    investments = app_tables.fin_lender.search(customer_id=self.user_id)
    
    # Debugging: Print fetched investments
    print(f"Fetched investments for user {self.user_id}: {list(investments)}")
    
    # Initialize variables to store total investments and returns
    total_investment = 0
    total_returns = 0
    
    for investment in investments:
      total_investment += investment['investment']
      total_returns += investment['return_on_investment']

    # Debugging: Print aggregated values
    print(f"Total Investment: {total_investment}, Total Returns: {total_returns}")

    # Prepare data for bar chart
    categories = ['Investment', 'Returns']
    values = [total_investment, total_returns]

    # Create bar chart trace
    trace = go.Bar(x=categories, y=values, marker_color=['blue', 'green'])

    # Create a layout
    layout = go.Layout(
      title='Investment and Returns for User',
      xaxis=dict(title='Category'),
      yaxis=dict(title='Amount'),
      barmode='group'  # Use group mode to display bars side by side
    )

    # Create a figure
    fig = go.Figure(data=[trace], layout=layout)

    # Debugging: Print the figure to ensure it's created
    print(f"Created figure: {fig}")

    # Set the plot in the Plot component
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

    # Debugging: Check if the plot is assigned correctly
    print(f"Assigned figure to plot_1: {self.plot_1.data}")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('lendor.dashboard')

  # def plot_1_click(self, points, **event_args):
  #   """This method is called when a data point is clicked."""
  #   self.create_bar_chart()
