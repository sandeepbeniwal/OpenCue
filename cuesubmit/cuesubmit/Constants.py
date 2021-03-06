#  Copyright (c) 2018 Sony Pictures Imageworks Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import os

from cuesubmit import Config

config = Config.getConfigValues()

UP_KEY = 16777235
DOWN_KEY = 16777237
TAB_KEY = 16777217

UI_NAME = config.get('UI_NAME', 'OPENCUESUBMIT')
SUBMIT_APP_WINDOW_TITLE = config.get('SUBMIT_APP_WINDOW_TITLE', 'OpenCue Submit')

MAYA_RENDER_CMD = config.get('MAYA_RENDER_CMD', 'Render')
NUKE_RENDER_CMD = config.get('NUKE_RENDER_CMD', 'nuke')
FRAME_TOKEN = config.get('FRAME_TOKEN', '#IFRAME#')

DIR_PATH = os.path.dirname(__file__)
