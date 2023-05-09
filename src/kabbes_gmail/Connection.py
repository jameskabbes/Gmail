from parent_class import ParentClass
import kabbes_account_manager
import yagmail

class Connection( ParentClass ):

    def __init__( self, **kwargs ):

        ParentClass.__init__( self )
        if self.cfg['load_credentials']:
            email_address, app_password = self.load_credentials()
            print (email_address)
            print (app_password)
            self.conn = self.get_connection( email_address, app_password )
        
        else:
            self.conn = self.get_connection( **kwargs )

    def load_credentials( self ):
        if self.cfg['accounts_manager.client.inst'] == None:
            args, kwargs = self.cfg['accounts_manager.client'].get_args(), self.cfg['accounts_manager.client'].get_kwargs()
            self.cfg.get_node('accounts_manager.client.inst').set_value( kabbes_account_manager.Client( *args, **kwargs ) )

        GmailAccount = self.cfg['accounts_manager.client.inst'].Accounts.Accounts[ self.cfg['accounts_manager.id'] ]

        email = GmailAccount.Entries.get_Entry( 'email' ).Value.val
        password = GmailAccount.Entries.get_Entry( 'password' ).Value.val
        return email, password

    @staticmethod
    def get_connection( gmail_address=None, app_password=None ):
        return yagmail.SMTP( gmail_address, app_password )

