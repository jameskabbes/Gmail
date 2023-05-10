import kabbes_gmail
import py_starter as ps
c = kabbes_gmail.Client()

c.cfg.print_atts()

e = kabbes_gmail.Email( 
    c, 
    to='james.kabbes@gmail.com', 
    sender='james.kabbes@gmail.com',
    subject='Test', 
    content='Howdy there!' 
)

e.print_atts()
if ps.confirm_raw('This will send a test email. '):
    print ( e.send() )