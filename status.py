#!/usr/bin/env python

"""
SYNOPSIS

    status

DESCRIPTION

    This generates a random status message.

EXAMPLES

    # status
    > Formatting lesson plans.
    
    or 
    
    from status import status
    message = status()

AUTHOR

    Andrew Kraut <opie@cybyl.com>

LICENSE

    This script is in the public domain.

VERSION

    1.0
"""

import sys
import os
import traceback
import optparse
import time
import string
from random import choice
#from pexpect import run, spawn

# Uncomment the following section if you want readline history support.
#import readline, atexit
#histfile = os.path.join(os.environ['HOME'], '.TODO_history')
#try:
#    readline.read_history_file(histfile)
#except IOError:
#    pass
#atexit.register(readline.write_history_file, histfile)

actions = [
    "simulating",
    "stimulating",
    "discovering",
    "refactoring",
    "engineering",
    "opening",
    "retracting",
    "expanding",
    "extending",
    "improving",
    "establishing",
    "inventing",
    "concealing",
    "erasing",
    "reformatting",
    "formatting",
    "tracing",
    "building",
    "compiling",
    "reducing",
    "inducing",
    "massaging",
    "writing",
    "deleting",
    "defenestrating",
    "analyzing",
    "checking",
    "smelling",
    "dancing",
    "stuffing",
    "finding",
    "hiding",
    "moving",
    "burying",
    "excavating",
    "calculating",
    "comparing",
    "eating",
    "listening to",
    "updating",
    "pushing"
]

statuses = [
    "{} the meaning of life",
    "{} pod bay doors",
    "{} harmonies",
    "{} body fat percentage",
    "{} lyric quality",
    "{} number of Dewey Decimal places",
    "knarfling Garthok",
    "{} formal statutes",
    "{} grade book",
    "{} lesson plans",
    "{} roses",
    "{} docking clamps",
    "{} storage requirements",
    "{} killer space drones",
    "{} life",
    "stuffing ballot box",
    "checking for cavities",
    "cutting green wire",
    "reticulating splines",
    "{} thank you notes",
    "{} letter to grandma",
    "{} shopping cart"
]

def status():
    """docstring for status"""
    message = choice(statuses)
    message = message.format(choice(actions))
    message = message.split()
    message[0] = message[0].capitalize()
    message = string.join(message) + "."
    return message

def main ():

    global options, args

    print status()

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(
                formatter=optparse.TitledHelpFormatter(),
                usage=globals()['__doc__'],
                version='$Id: py.tpl 332 2008-10-21 22:24:52Z root $')
        parser.add_option ('-v', '--verbose', action='store_true',
                default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()
        exit_code = main()
        if exit_code is None:
            exit_code = 0
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(exit_code)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)

# vim:set sr et ts=4 sw=4 ft=python fenc=utf-8: // See Vim, :help 'modeline'
