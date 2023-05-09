import kabbes_gmail
c = kabbes_gmail.Client()
c.print_atts()

e = kabbes_gmail.Email(
    c,
    to = 'james.kabbes@gmail.com',
    subject = 'test',
    content = ['This is a test']
)
print ( e.send( print_off = True ) )