from flask import *

from TSMRS import *

import random

a = Flask(__name__)

@a.route('/user')

def khb():

    k = 'kiuygfvbnjutrdcgytdrcugtr'

    rr = random.choice(k)

    rdr = random.choice(k)

    mo = rr+rr+'_'+rdr+rr+rdr

    s = check()

    v = s.Telegram(mo)

    if v == '404':

        return {

            'user':mo,

            'result':'true'

            

        }

    else:

        return {

            'user':mo,

            'result':'False'

            

        }

a.run()
