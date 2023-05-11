from parent_class import ParentClass
import py_starter as ps
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        message = MIMEMultipart()
        message['to'] = self.to
        message['from'] = self.sender
        message['subject'] = self.subject

        message.attach(MIMEText( self.content, 'html'))

        # encoded message
        self.create_message = { 'raw': base64.urlsafe_b64encode(message.as_bytes()).decode() }

    def send( self ):
        self.compose()
        return self.conn.service.users().messages().send(userId="me", body=self.create_message).execute()

    @staticmethod
    def make_html_link( link_address, link_text_to_show ):
        return '<a href="{link_address}">{link_text_to_show}</a>'.format( link_address = link_address, link_text_to_show = link_text_to_show )

