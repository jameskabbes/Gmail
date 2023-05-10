from parent_class import ParentClass
import py_starter as ps
import base64
from email.message import EmailMessage

class Email( ParentClass ):

    _IMP_ATTS = ['to','sender','subject','content']

    def __init__( self, conn, to=None, sender=None, subject=None, content=None ):

        ParentClass.__init__( self )
        self.conn = conn
        self.to = to
        self.sender = sender
        self.subject = subject
        self.content = content

    def compose( self ):
        message = EmailMessage()
        message.set_content( self.content )
        message['To'] = self.to
        message['From'] = self.sender
        message['Subject'] = self.subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        self.create_message = { 'raw': encoded_message }
        # pylint: disable=E1101


    def send( self ):
        self.compose()
        return self.conn.service.users().messages().send(userId="me", body=self.create_message).execute()

    @staticmethod
    def make_html_link( link_address, link_text_to_show ):
        return '<a href="{link_address}">{link_text_to_show}</a>'.format( link_address = link_address, link_text_to_show = link_text_to_show )

