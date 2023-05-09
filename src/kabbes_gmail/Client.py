import kabbes_gmail
import kabbes_client

class Client( kabbes_gmail.Connection ):

    _BASE_DICT = {}

    def __init__( self, *args, dict={}, root_dict={}, **kwargs ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        root_inst = kabbes_client.Root( root_dict=root_dict )
        self.Package = kabbes_client.Package( kabbes_gmail._Dir, dict=d, root=root_inst )
        self.cfg = self.Package.cfg

        kabbes_gmail.Connection.__init__( self, *args, **kwargs )
