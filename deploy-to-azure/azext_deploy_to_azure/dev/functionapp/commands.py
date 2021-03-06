# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType

functionappops = CliCommandType(
    operations_tmpl='azext_deploy_to_azure.dev.functionapp.up#{}'
)


def load_functionapp_commands(self, _):
    with self.command_group('functionapp app', command_type=functionappops, is_preview=True) as g:
        g.command('up', 'functionapp_deploy')
