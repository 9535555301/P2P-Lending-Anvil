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
        self.data = app_tables.fin_user_profile.search()

        self.result = []
        for user_profile in self.data:
            if user_profile['usertype'] == 'borrower':
                # Retrieve credit limit from fin_borrower table based on customer ID
                borrower_record = app_tables.fin_borrower.get(customer_id=user_profile['customer_id'])
                if borrower_record is not None:
                    credit_limit = borrower_record['credit_limit']
                    ascend = borrower_record['ascend_score']
                else:
                    credit_limit = None
                    ascend = None

                guarantor_record = app_tables.fin_guarantor_details.get(customer_id=user_profile['customer_id'])
                if guarantor_record is not None:
                    guarantor_name = guarantor_record['guarantor_name']
                    guarantor_ph_no = guarantor_record['guarantor_mobile_no']
                    guarantor = guarantor_record['another_person']
                else:
                    guarantor_name = None
                    guarantor_ph_no = None
                    guarantor = None

                loan_details_count = len(
                    app_tables.fin_loan_details.search(
                        q.all_of(
                            loan_updated_status=q.any_of(
                                q.like("disbursed loan%"),
                                q.like("foreclosure%"),
                                q.like("under process%")
                            )
                        ),
                        borrower_customer_id=user_profile['customer_id']
                    )
                )

                self.result.append({
                    'customer_id': user_profile['customer_id'],
                    'full_name': user_profile['full_name'],
                    'email_user': user_profile['email_user'],
                    'usertype': user_profile['usertype'],
                    'last_confirm': user_profile['last_confirm'],
                    'date_of_birth': user_profile['date_of_birth'],
                    'mobile': user_profile['mobile'],
                    'registration_approve': user_profile['registration_approve'],
                    'adhar': user_profile['aadhaar_no'],
                    'credit_limit': credit_limit,
                    'ascend_score': ascend,
                    'guarantor_name': guarantor_name,
                    'guarantor_mobile_no': guarantor_ph_no,
                    'another_person': guarantor,
                    'loan_updated_status': loan_details_count,
                    'user_photo': user_profile['user_photo']
                })

        if not self.result:
            alert("No Borrowers Available!")
        else:
            panel1_data = self.result[::2]  # Every second item starting from index 0
            panel2_data = self.result[1::2]  # Every second item starting from index 1

            self.repeating_panel_1.items = panel1_data
            self.repeating_panel_3.items = panel2_data

            # Set total loan count labels for each borrower
            for item in self.repeating_panel_1.items:
                item['total_open_loan'] = f"Total Loans: {item['loan_updated_status']}"

            for item in self.repeating_panel_3.items:
                item['total_open_loan'] = f"Total Loans: {item['loan_updated_status']}"

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.dashboard')

    def search_borrower(self, **event_args):
        if not self.text_box_1.text.strip():
            alert("The text box cannot be empty. Please enter some text.")
            self.data_grid_1.visible = False
        else:
            self.repeating_panel_2.items = anvil.server.call(
                'search_borrower',
                self.text_box_1.text
            )
            self.data_grid_1.visible = True

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.customer_management.handles_customer_registration')
