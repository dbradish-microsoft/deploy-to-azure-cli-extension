# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.prompting import prompt
from azext_deploy_to_azure.dev.common.azure_cli_resources import get_default_subscription_info
from azext_deploy_to_azure.dev.common.github_api_helper import check_secret_exists, create_repo_secret

logger = get_logger(__name__)

def get_azure_credentials(repo_name):
    import subprocess
    import json
    _subscription_id, _subscription_name, _tenant_id, _environment_name = get_default_subscription_info()
    print('Creating AZURE_CREDENTIALS secret...')
    if not check_secret_exists(repo_name, 'AZURE_CREDENTIALS'):
        auth_details = subprocess.check_output('az ad sp create-for-rbac --sdk-auth -o json', shell=True)
        auth_details_json = json.loads(auth_details)
        authj_details_string = json.dumps(auth_details_json)
        create_repo_secret(repo_name, 'AZURE_CREDENTIALS', authj_details_string)
    else:
        logger.warning('Skipped creating AZURE_CREDENTIALS as it already exists')
    print('')
    print('Creating REGISTRY_USERNAME and REGISTRY_PASSWORD...')
    sp_details = subprocess.check_output('az ad sp create-for-rbac -o json', shell=True)
    sp_details_json = json.loads(sp_details)
    if not check_secret_exists(repo_name, 'REGISTRY_USERNAME') \
        and not check_secret_exists(repo_name, 'REGISTRY_PASSWORD'):
        sp_details = subprocess.check_output('az ad sp create-for-rbac -o json', shell=True)
        sp_details_json = json.loads(sp_details)
        create_repo_secret(repo_name, 'REGISTRY_USERNAME', sp_details_json['appId'])
        create_repo_secret(repo_name, 'REGISTRY_PASSWORD', sp_details_json['password'])
    else:
        logger.warning('Skipped creating REGISTRY_USERNAME and REGISTRY_PASSWORD as it already exists')


def get_azure_credentials_functionapp(repo_name, app_name):
    import subprocess
    import json
    _subscription_id, _subscription_name, _tenant_id, _environment_name = get_default_subscription_info()
    print('')
    print('Creating AZURE_CREDENTIALS secret...')
    if not check_secret_exists(repo_name, 'AZURE_CREDENTIALS'):
        auth_details = subprocess.check_output(
        'az ad sp create-for-rbac --name {} --role contributor --sdk-auth -o json'.format(app_name),
        shell=True)
        auth_details_json = json.loads(auth_details)
        authj_details_string = json.dumps(auth_details_json)
        create_repo_secret(repo_name, 'AZURE_CREDENTIALS', authj_details_string)
    else:
        logger.warning('Skipped creating AZURE_CREDENTIALS as it already exists')

