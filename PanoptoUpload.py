'''
Copyright (C) 2016, Blackboard Inc.
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of Blackboard Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY BLACKBOARD INC ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BLACKBOARD INC. BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Created on May 25, 2016

@author: shurrey
'''

'''
Modified on 2021-03-25
@author: Simon Bowie <sb174@soas.ac.uk>
'''

import sys
import os
import getopt
import datetime
import uuid
import json
import urllib.request

import argparse
import ntpath # so we can grab the basename off the end of the full-file-path.
from panopto_oauth2 import PanoptoOAuth2
from panopto_uploader import PanoptoUploader
from upload_and_create_link import UploadAndCreateLink
import time
import urllib3
import Utilidades as ut

# Import Config
import Config


#uploading the recordings

def uploadrecording(recording_list, name):
    for recording in recording_list:
        filename = name + '-' + recording['recording_id'] + '-' + ut.checkLongFilenameVideo(' ', recording['recording_name'])
        fullpath = './downloads/'
        print(fullpath + filename)
        upload_creator = UploadAndCreateLink()
        upload_creator.upload_and_create_link(fullpath + filename)

def uploadrecordingUUID(recording_list):
    filename = recording_list['recordingId'] + '-' + ut.checkLongFilenameVideo(' ', recording_list['recording_name'])
    fullpath = './downloads/'
    print(fullpath + filename)
    upload_creator = UploadAndCreateLink()
    upload_creator.upload_and_create_link(fullpath + filename)
