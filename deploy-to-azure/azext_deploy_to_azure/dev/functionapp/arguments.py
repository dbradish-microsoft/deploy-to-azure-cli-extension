# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def load_functionapp_arguments(self, _):
    with self.argument_context('functionapp app up') as context:
        context.argument('repository', options_list=('--repository', '-r'))
