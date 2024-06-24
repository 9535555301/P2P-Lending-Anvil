# from ._anvil_designer import mis_reportsTemplate
# from anvil import *
# import plotly.graph_objects as go
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class mis_reports(mis_reportsTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Any code you write here will run before the form opens.
#         self.plot_data()
#         self.plot_loan_data()
#         self.create_user_bar_chart()
#         # self.create_risk_bar_chart()

#     def plot_data(self):
#         # Fetch data from tables
#         loan_details = app_tables.fin_loan_details.search(loan_updated_status=q.any_of('closed loan', 'rejected', 'disbursed loan'))
#         lenders = app_tables.fin_lender.search()
#         users = app_tables.fin_user_profile.search(usertype=q.any_of('lender', 'borrower'))

#         # Calculate metrics
#         no_of_loans_disbursed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'disbursed loan'])
#         no_of_loans_closed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'closed loan'])
#         no_of_loans_rejected = len([loan for loan in loan_details if loan['loan_updated_status'] == 'rejected'])
#         amount_disbursed = sum([loan['lender_returns'] for loan in loan_details])
#         no_of_borrowers = len([user for user in users if user['usertype'] == 'borrower'])
#         no_of_lenders = len([user for user in users if user['usertype'] == 'lender'])
#         lenders_commitment = sum([lender['return_on_investment'] for lender in lenders])

#         # Data for the pie chart
#         values = [
#             no_of_loans_disbursed,
#             no_of_loans_closed,
#             no_of_loans_rejected,
#             amount_disbursed,
#             no_of_borrowers,
#             no_of_lenders,
#             lenders_commitment
#         ]
#         labels = [
#             'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
#             'No of Loans Closed: {}'.format(no_of_loans_closed),
#             'No of Loans Rejected: {}'.format(no_of_loans_rejected),
#             'Amount Disbursed: {}'.format(amount_disbursed),
#             'No of Borrowers: {}'.format(no_of_borrowers),
#             'No of Lenders: {}'.format(no_of_lenders),
#             'Lenders Commitment: {}'.format(lenders_commitment)
#         ]

#         # Create the pie chart
#         fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

#         fig.update_layout(title={'text': 'Financial Loan Details', 'font': {'size': 24, 'color': 'black', 'family': 'Arial', 'bold': True}})

#         # Embed the plot in the Anvil app
#         self.plot_1.figure = fig

#     def plot_loan_data(self):
#         # Fetch data from tables
#         loan_details = app_tables.fin_loan_details.search(loan_updated_status=q.any_of('closed loan', 'rejected', 'disbursed loan', 'foreclosure', 'lost opportunities', 'approved', 'under process', 'extension'))

#         # Calculate metrics
#         no_of_loans_disbursed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'disbursed loan'])
#         no_of_loans_closed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'closed loan'])
#         no_of_loans_rejected = len([loan for loan in loan_details if loan['loan_updated_status'] == 'rejected'])
#         no_of_loans_foreclosed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'foreclosure'])
#         no_of_loans_lost_opportunity = len([loan for loan in loan_details if loan['loan_updated_status'] == 'lost opportunities'])
#         no_of_loans_approved = len([loan for loan in loan_details if loan['loan_updated_status'] == 'approved'])
#         no_of_loans_under_process = len([loan for loan in loan_details if loan['loan_updated_status'] == 'under process'])
#         no_of_extension_loans = len([loan for loan in loan_details if loan['loan_updated_status'] == 'extension'])
        
#         # Data for the pie chart
#         values = [
#             no_of_loans_disbursed,
#             no_of_loans_closed,
#             no_of_loans_rejected,
#             no_of_loans_foreclosed,
#             no_of_loans_lost_opportunity,
#             no_of_loans_approved,
#             no_of_loans_under_process,
#             no_of_extension_loans
#         ]
#         labels = [
#             'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
#             'No of Loans Closed: {}'.format(no_of_loans_closed),
#             'No of Loans Rejected: {}'.format(no_of_loans_rejected),
#             'No of Loans Foreclosed: {}'.format(no_of_loans_foreclosed),
#             'No of Loans Lost Opportunity: {}'.format(no_of_loans_lost_opportunity),
#             'No of Loans Approved: {}'.format(no_of_loans_approved),
#             'No of Loans Under Process: {}'.format(no_of_loans_under_process),
#             'No of Extension Loans: {}'.format(no_of_extension_loans)
#         ]

#         # Create the pie chart
#         fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

#         # Update layout for better appearance
#         fig.update_layout(title={'text': 'Different types of Loans', 'font': {'size': 24, 'color': 'black', 'family': 'Arial', 'bold': True}})

#         # Embed the plot in the Anvil app
#         self.plot_2.figure = fig
    
#     def create_user_bar_chart(self):
#         # Fetch investment data
#         investments = app_tables.fin_lender.search()
        
#         # Debugging: Print fetched investments
#         print(f"Fetched investments: {list(investments)}")
        
#         # Initialize a dictionary to store total return_on_investment for each customer_id
#         customer_returns = {}
        
#         for investment in investments:
#             customer_id = investment['customer_id']
#             if customer_id not in customer_returns:
#                 customer_returns[customer_id] = 0
#             customer_returns[customer_id] += investment['return_on_investment']
        
#         # Convert the dictionary to a list of tuples and sort by return_on_investment in descending order
#         sorted_returns = sorted(customer_returns.items(), key=lambda x: x[1], reverse=True)
        
#         # Prepare data for the bar chart
#         categories = [str(item[0]) for item in sorted_returns]  # customer_ids
#         values = [item[1] for item in sorted_returns]  # return_on_investments
        
#         # Create bar chart trace
#         trace = go.Bar(x=categories, y=values, marker_color='green')
        
#         # Create a layout
#         layout = go.Layout(
#             title=dict(text='Return on Investment by Customer', font=dict(size=16, weight='bold')),
#             xaxis=dict(
#                 title='Customer ID',
#                 tickfont=dict(size=10, weight='bold'),
#                 tickangle=45,
#                 type='category'  # Ensures the x-axis is treated as categorical
#             ),
#             yaxis=dict(title='Return on Investment'),
#             barmode='group'
#         )
        
#         # Create a figure
#         fig = go.Figure(data=[trace], layout=layout)
        
#         # Debugging: Print the figure to ensure it's created
#         print(f"Created figure: {fig}")
        
#         # Set the plot in the Plot component
#         self.plot_3.figure = fig
        
#         # Debugging: Check if the plot is assigned correctly
#         print(f"Assigned figure to plot_3: {self.plot_3.figure}") 


    
#     def create_risk_bar_chart(self):
#         # Fetch investment data
#         investments = app_tables.fin_lender.search()
        
#         # Debugging: Print fetched investments
#         print(f"Fetched investments: {list(investments)}")
        
#         # Initialize a dictionary to store total return_on_investment for each customer_id
#         customer_returns = {}
        
#         for investment in investments:
#             customer_id = investment['customer_id']
#             if customer_id not in customer_returns:
#                 customer_returns[customer_id] = 0
#             customer_returns[customer_id] += investment['return_on_investment']
        
#         # Convert the dictionary to a list of tuples and sort by return_on_investment in descending order
#         sorted_returns = sorted(customer_returns.items(), key=lambda x: x[1], reverse=True)
        
#         # Prepare data for the bar chart
#         categories = [str(item[0]) for item in sorted_returns]  # customer_ids
#         values = [item[1] for item in sorted_returns]  # return_on_investments
        
#         # Create bar chart trace
#         trace = go.Bar(x=categories, y=values, marker_color='green')
        
#         # Create a layout
#         layout = go.Layout(
#             title=dict(text='Return on Investment by Customer', font=dict(size=16, weight='bold')),
#             xaxis=dict(
#                 title='Customer ID',
#                 tickfont=dict(size=10, weight='bold'),
#                 tickangle=45,
#                 type='category'  # Ensures the x-axis is treated as categorical
#             ),
#             yaxis=dict(title='Return on Investment'),
#             barmode='group'
#         )
        
#         # Create a figure
#         fig = go.Figure(data=[trace], layout=layout)
        
#         # Debugging: Print the figure to ensure it's created
#         print(f"Created figure: {fig}")
        
#         # Set the plot in the Plot component
#         self.plot_4.figure = fig
        
#         # Debugging: Check if the plot is assigned correctly
#         print(f"Assigned figure to plot_4: {self.plot_4.figure}")

#     def button_1_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('admin.dashboard.accounting')






from ._anvil_designer import mis_reportsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class mis_reports(mis_reportsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.plot_data()
        self.plot_loan_data()
        self.create_user_bar_chart()
        # self.create_risk_bar_chart()

    def plot_data(self):
        # Fetch data from tables
        loan_details = app_tables.fin_loan_details.search(loan_updated_status=q.any_of('closed loan', 'rejected', 'disbursed loan'))
        lenders = app_tables.fin_lender.search()
        users = app_tables.fin_user_profile.search(usertype=q.any_of('lender', 'borrower'))

        # Calculate metrics
        no_of_loans_disbursed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'disbursed loan'])
        no_of_loans_closed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'closed loan'])
        no_of_loans_rejected = len([loan for loan in loan_details if loan['loan_updated_status'] == 'rejected'])
        amount_disbursed = sum([loan['lender_returns'] for loan in loan_details])
        no_of_borrowers = len([user for user in users if user['usertype'] == 'borrower'])
        no_of_lenders = len([user for user in users if user['usertype'] == 'lender'])
        lenders_commitment = sum([lender['return_on_investment'] for lender in lenders])

        # Data for the pie chart
        values = [
            no_of_loans_disbursed,
            no_of_loans_closed,
            no_of_loans_rejected,
            amount_disbursed,
            no_of_borrowers,
            no_of_lenders,
            lenders_commitment
        ]
        labels = [
            'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
            'No of Loans Closed: {}'.format(no_of_loans_closed),
            'No of Loans Rejected: {}'.format(no_of_loans_rejected),
            'Amount Disbursed: {}'.format(amount_disbursed),
            'No of Borrowers: {}'.format(no_of_borrowers),
            'No of Lenders: {}'.format(no_of_lenders),
            'Lenders Commitment: {}'.format(lenders_commitment)
        ]

        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

        fig.update_layout(title={'text': 'Financial Loan Details', 'font': {'size': 24, 'color': 'black', 'family': 'Arial', 'bold': True}})

        # Embed the plot in the Anvil app
        self.plot_1.figure = fig

    def plot_loan_data(self):
        # Fetch data from tables
        loan_details = app_tables.fin_loan_details.search(loan_updated_status=q.any_of('closed loan', 'rejected', 'disbursed loan', 'foreclosure', 'lost opportunities', 'approved', 'under process', 'extension'))

        # Calculate metrics
        no_of_loans_disbursed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'disbursed loan'])
        no_of_loans_closed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'closed loan'])
        no_of_loans_rejected = len([loan for loan in loan_details if loan['loan_updated_status'] == 'rejected'])
        no_of_loans_foreclosed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'foreclosure'])
        no_of_loans_lost_opportunity = len([loan for loan in loan_details if loan['loan_updated_status'] == 'lost opportunities'])
        no_of_loans_approved = len([loan for loan in loan_details if loan['loan_updated_status'] == 'approved'])
        no_of_loans_under_process = len([loan for loan in loan_details if loan['loan_updated_status'] == 'under process'])
        no_of_extension_loans = len([loan for loan in loan_details if loan['loan_updated_status'] == 'extension'])
        
        # Data for the pie chart
        values = [
            no_of_loans_disbursed,
            no_of_loans_closed,
            no_of_loans_rejected,
            no_of_loans_foreclosed,
            no_of_loans_lost_opportunity,
            no_of_loans_approved,
            no_of_loans_under_process,
            no_of_extension_loans
        ]
        labels = [
            'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
            'No of Loans Closed: {}'.format(no_of_loans_closed),
            'No of Loans Rejected: {}'.format(no_of_loans_rejected),
            'No of Loans Foreclosed: {}'.format(no_of_loans_foreclosed),
            'No of Loans Lost Opportunity: {}'.format(no_of_loans_lost_opportunity),
            'No of Loans Approved: {}'.format(no_of_loans_approved),
            'No of Loans Under Process: {}'.format(no_of_loans_under_process),
            'No of Extension Loans: {}'.format(no_of_extension_loans)
        ]

        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

        # Update layout for better appearance
        fig.update_layout(title={'text': 'Different types of Loans', 'font': {'size': 24, 'color': 'black', 'family': 'Arial', 'bold': True}})

        # Embed the plot in the Anvil app
        self.plot_2.figure = fig
    
    def create_user_bar_chart(self):
        # Fetch investment data
        investments = app_tables.fin_lender.search()
        
        # Debugging: Print fetched investments
        print(f"Fetched investments: {list(investments)}")
        
        # Initialize a dictionary to store total return_on_investment for each customer_id
        customer_returns = {}
        
        for investment in investments:
            customer_id = investment['customer_id']
            if customer_id not in customer_returns:
                customer_returns[customer_id] = 0
            customer_returns[customer_id] += investment['return_on_investment']
        
        # Convert the dictionary to a list of tuples and sort by return_on_investment in descending order
        sorted_returns = sorted(customer_returns.items(), key=lambda x: x[1], reverse=True)
        
        # Prepare data for the bar chart
        categories = [str(item[0]) for item in sorted_returns]  # customer_ids
        values = [item[1] for item in sorted_returns]  # return_on_investments
        
        # Create bar chart trace
        trace = go.Bar(
            x=categories, 
            y=values, 
            marker_color='green',
            text=[f'Rs {value}' for value in values],  # Format text
            textposition='outside'  # Display text outside the bars
        )
        
        # Create a layout
        layout = go.Layout(
            title=dict(text='Highet Return Earner by Customer', font=dict(size=16, weight='bold')),
            xaxis=dict(
                title='Customer ID',
                tickfont=dict(size=10, weight='bold'),
                tickangle=45,
                type='category'  # Ensures the x-axis is treated as categorical
            ),
            yaxis=dict(title='Return on Investment'),
            barmode='group'
        )
        
        # Create a figure
        fig = go.Figure(data=[trace], layout=layout)
        
        # Debugging: Print the figure to ensure it's created
        print(f"Created figure: {fig}")
        
        # Set the plot in the Plot component
        self.plot_3.figure = fig
        
        # Debugging: Check if the plot is assigned correctly
        print(f"Assigned figure to plot_3: {self.plot_3.figure}")


    
    def create_risk_bar_chart(self):
        # Fetch investment data
        investments = app_tables.fin_lender.search()
        
        # Debugging: Print fetched investments
        print(f"Fetched investments: {list(investments)}")
        
        # Initialize a dictionary to store total return_on_investment for each customer_id
        customer_returns = {}
        
        for investment in investments:
            customer_id = investment['customer_id']
            if customer_id not in customer_returns:
                customer_returns[customer_id] = 0
            customer_returns[customer_id] += investment['return_on_investment']
        
        # Convert the dictionary to a list of tuples and sort by return_on_investment in descending order
        sorted_returns = sorted(customer_returns.items(), key=lambda x: x[1], reverse=True)
        
        # Prepare data for the bar chart
        categories = [str(item[0]) for item in sorted_returns]  # customer_ids
        values = [item[1] for item in sorted_returns]  # return_on_investments
        
        # Create bar chart trace
        trace = go.Bar(x=categories, y=values, marker_color='green')
        
        # Create a layout
        layout = go.Layout(
            title=dict(text='Return on Investment by Customer', font=dict(size=16, weight='bold')),
            xaxis=dict(
                title='Customer ID',
                tickfont=dict(size=10, weight='bold'),
                tickangle=45,
                type='category'  # Ensures the x-axis is treated as categorical
            ),
            yaxis=dict(title='Return on Investment'),
            barmode='group'
        )
        
        # Create a figure
        fig = go.Figure(data=[trace], layout=layout)
        
        # Debugging: Print the figure to ensure it's created
        print(f"Created figure: {fig}")
        
        # Set the plot in the Plot component
        self.plot_4.figure = fig
        
        # Debugging: Check if the plot is assigned correctly
        print(f"Assigned figure to plot_4: {self.plot_4.figure}")

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.accounting')
