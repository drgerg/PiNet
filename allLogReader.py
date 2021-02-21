#!/usr/bin/env python3
#
##  allLogReader.py - Supports reading logs across the vast PiNet
#
#     Copyright (c) 2020, 2021 - Gregory Allen Sanders.

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import time,os,logging,argparse,traceback,signal,sys

parserALR = argparse.ArgumentParser()
parserALR.add_argument('-d', '--debug', help="Turn on debugging output to et.log file.", action="store_true")
parserALR.add_argument('-uet', help="Unix Epoch Time value.", action="store")
ALRHome = os.getcwd()
logger = logging.getLogger(__name__)
argsALR = parserALR.parse_args()

logger.debug('Checked for commandline argument: argsALR.uet.')
if argsALR.uet:
    ALRRaw = float(argsALR.uet)
    print(' Input UALR: ' + str(ALRRaw))


if argsALR.debug:
    logging.basicConfig(filename=ALRHome + '/ALR.log', format='[%(name)s]:%(levelname)s: %(message)s. - %(asctime)s', datefmt='%D %H:%M:%S', level=logging.DEBUG)
    logging.info("Debugging output enabled")
else:
    logging.basicConfig(filename=ALRHome + '/ALR.log', format='%(asctime)s - %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', level=logging.INFO)
#
logger.info(" - - - - allLogReader.py DATA LOGGING STARTED - - - - ")
logger.info("  allLogReader.py INITIAL CONFIGURATION COMPLALRE  ")
logger.info("'HOME' path is: " + ALRHome)

#
## - - - - - TEST CODE BELOW HERE - - - -
#

def main():
    logger.info('And so it begins.')
    # 1) Get a list of .log files
    # 2) 


## - - - - - - END TEST CODE - - - - - - - 
#

def SignalHandler(signal, frame):
    if signal == 2:
        sigStr = 'CTRL-C'
        logger.info('* * * ' + sigStr + ' caught. * * * ')
    print("\nSignalHandler invoked")
    logger.info("Shutting down gracefully")
    logger.debug("Wrote to log in SignalHandler")
    logger.info("That's all folks.  Goodbye")
    logger.info(" - - - - allLogReader.py DATA LOGGING STOPPED INTENTIONALLY - - - - ")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, SignalHandler)  ## This one catches CTRL-C from the local keyboard
    signal.signal(signal.SIGTERM, SignalHandler) ## This one catches the Terminate signal from the system    
    try:
        if argsALR.uet:
            main(argsALR.uet)
        else:
            uet = time.time()
            print("\nYou didn't supply a Unix Epoch Time value.  Here's one: " + str(uet) + '\n Learn more by typing "./et.py --help".\n')
            logger.debug('No time value was provided, so we provided this: ' + str(uet))
        pass
        logger.info(" - - - - allLogReader.py COMPLETED ITS MISSION - - - - ")
    except Exception:
        logger.info("Exception caught at bottom of try.", exc_info=True)
        error = traceback.print_exc()
        logger.info(error)
        logger.info("That's all folks.  Goodbye")
        logger.info(" - - - - allLogReader.py DATA LOGGING STOPPED BY EXCEPTION - - - - ")
