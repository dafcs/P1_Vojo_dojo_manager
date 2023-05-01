class Member():
    def __init__(self,first_name,last_name,membership_type = 'Standard',account_status = True, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_type = membership_type
        self.account_status = account_status
        self.id = id


    def toggle_status(self):
        if self.account_status:
            self.account_status = False
        else:
            self.account_status = True
        return self.account_status
    
    def return_status(self):
        return self.account_status
    
    def return_membership_type(self):
        return self.membership_type

    def change_membership_type_to_premium(self):
        self.membership_type = 'Premium'
        
    def change_membership_type_to_standard(self):
        self.membership_type = 'Standard'
    
