'''
In order to get the Learn credentials, they do not to open a case on behind the blackboard nor email developers@blackboard.com.

They need to go to developer.blackboard.com and register from there to grab the Learn credentials for their application, it is also imperative to remind them that they are creating an application based on your code, so they need to register as a developer.

Now, for Collaborate production they CAN and MUST create a ticket on behind the blackboard requesting their credentials.
'''

'''
Copy this file to a new file called Config.py. Do not put active API credentials in a file tracked by git!
'''

credenciales = {
    "verify_certs" : "True",
    "learn_rest_fqdn" : "learn URL",
    "learn_rest_key" : "Learn API Key",
    "learn_rest_secret" : "Learn API Secret",
    "collab_key": "Collab Key",
    "collab_secret": "Collab Secret",
    "collab_base_url": "us.bbcollab.com/collab/api/csa",
    "ppto_server" : "panoptoServer",
    "ppto_folder_id" : "panoptoFolderId", 
    "ppto_client_id" : "panoptoClientId",
    "ppto_client_secret" : "panoptoClientSecret",
    "ppto_username" : "panoptoUserName",
    "ppto_password" : "panoptoPassword"
}