import kabbes_client
import kabbes_google
import kabbes_gmail

class Client( kabbes_google.Service ):

    _BASE_DICT = {}

    def __init__( self, dict={}, root_dict={}, **kwargs ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        root_inst = kabbes_client.Root( root_dict=root_dict )
        self.Package = kabbes_client.Package( kabbes_gmail._Dir, dict=d, root=root_inst )
        google_Package = kabbes_google.Client( init_service=False )

        google_Package.cfg.merge( self.Package.cfg )
        self.cfg = google_Package.cfg

        kabbes_google.Service.__init__( self, **kwargs )
