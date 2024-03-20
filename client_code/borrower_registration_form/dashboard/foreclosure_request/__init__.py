from ._anvil_designer import foreclosure_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class foreclosure_request(foreclosure_requestTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Fetch the current user during form initialization
        user = anvil.users.get_user()
        # Check if a user is logged in
        if user:
            # Fetch the userprofile record based on the current user's email
            user_profile = app_tables.fin_user_profile.get(email_user=user['email'])
            # Check if the user profile record is found
            if user_profile:
                # Access the user ID from the userprofile record
                user_id = user_profile['customer_id']
                print(user_id)
                # Filter loan_details table based on the current user's ID
                try:
                    customer_loans = app_tables.fin_loan_details.search(borrower_customer_id=user_id)
                    loans = []
                    for loan in customer_loans:
                        if user_profile is not None:
                            loan_data = {
                                'mobile': user_profile['mobile'],
                                'interest_rate': loan['interest_rate'],
                                'loan_amount': loan['loan_amount'],
                                'tenure': loan['tenure'],
                                'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                                'product_name': loan['product_name'],
                                'product_description': loan['product_description'],
                                'lender_full_name': loan['lender_full_name'],
                                'product_id': loan['product_id'],
                                'loan_id': loan['loan_id'],
                                'loan_updated_status': loan['loan_updated_status'],
                                'emi_payment_type': loan['emi_payment_type'],
                                'credit_limit' : loan['credit_limit'],
                                'foreclosure_type' : loan['foreclosure_type'],
                                'borrower_full_name' : loan['borrower_full_name']
                                # 'eligible': self.is_loan_eligible(loan)
                            }
                            loans.append(loan_data)


                    self.repeat.items = loans
                except anvil.tables.TableError as e:
                    print(f"Error: {e}")
            else:
                # Handle the case when no user profile record is found
                print("User profile record not found for the current user.")
        else:
            # Handle the case when no user is logged in
            print("No user logged in")

  
    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard')


