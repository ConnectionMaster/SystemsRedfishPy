# *************************************************************************************
#
# redfishInteractive - Module to run Systems Redfish API commands interactively.
#
# -------------------------------------------------------------------------------------

# Copyright 2019 Seagate Technology LLC or one of its affiliates.
#
# The code contained herein is CONFIDENTIAL to Seagate Technology LLC.
# Portions may also be trade secret. Any use, duplication, derivation, distribution
# or disclosure of this code, for any reason, not expressly authorized in writing by
# Seagate Technology LLC is prohibited. All rights are expressly reserved by
# Seagate Technology LLC.
#
# -------------------------------------------------------------------------------------
#

import sys

from redfishConfig import RedfishConfig
from redfishCommand import RedfishCommand
from trace import TraceLevel, Trace

################################################################################
# RedfishPrompt
################################################################################
class RedfishPrompt():

    aliases = {'rf':'redfish'}

    def cmdloop(self, config, command, prompt='redfish'):

        while 1:
            try:
                print('')
                sys.stdout.write('({}) '.format(prompt))
                sys.stdout.flush()
                line = sys.stdin.readline().strip()

            except KeyboardInterrupt:
                break

            if not line:
                break

            elif (line == 'exit' or line == 'quit'):
                break

            elif (line.startswith('alias')):
                # Add the new alias to the dictionary
                words = line.split(' ')
                if (len(words) == 3):
                    alias = words[1]
                    original = words[2]
                    Trace.log(TraceLevel.INFO, '   ++ CFG: replacing ({}) with the alias ({})'.format(alias, original))
                    self.aliases[alias] = original
                else:
                    Trace.log(TraceLevel.INFO, '   ++ usage: alias <new> <original>')

            elif (line.startswith('!')):
                Trace.log(TraceLevel.TRACE, '   CFG: [{0: >3}] {1}'.format(len(line), line))
                config.execute(line)

            else:
                # Check for the use of any alias
                words = line.split(' ')
                if (len(words) > 1):
                    if (words[0] in self.aliases):
                        line = line.replace(words[0], self.aliases[words[0]], 1)

                Trace.log(TraceLevel.TRACE, '   CMD: [{0: >3}] {1}'.format(len(line), line))
                command.execute(config, line)


################################################################################
# RedfishInteractive
################################################################################
class RedfishInteractive:

    def execute(self):
        Trace.log(TraceLevel.INFO, '[] Run Redfish API commands interactively...')

        # Load configuration settings, which can be overwritten at the command line or in a script file
        config = RedfishConfig('redfishAPI.json')

        # Create an object to handle all commands
        command = RedfishCommand()

        RedfishPrompt().cmdloop(config, command)



