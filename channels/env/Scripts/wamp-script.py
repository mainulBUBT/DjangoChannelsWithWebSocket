#!f:\python\djangochannelswithwebsocket\channels\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autobahn==22.2.2','console_scripts','wamp'
__requires__ = 'autobahn==22.2.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autobahn==22.2.2', 'console_scripts', 'wamp')()
    )
