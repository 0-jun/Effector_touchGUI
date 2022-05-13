import sys
import os
import platform


PATH_DESKTOP = os.path.join(os.environ["HOMEPATH"], "Desktop")

if getattr(sys, 'frozen', False):
    PATH_ROOT = os.path.abspath(os.path.dirname(sys.executable))
    PATH_RESOURCE = PATH_ROOT + '/lib/resource/'
else:
    PATH_ROOT = os.path.abspath(os.path.dirname(__file__))
    PATH_RESOURCE = PATH_ROOT + '/Resource/'


PATH_LOCALE = PATH_RESOURCE + 'locale/'
PATH_IMAGE = PATH_RESOURCE + 'images/'

PATH_SAVE_DIR = ''

try:
    if platform.system() == 'Windows':  # windows
        PATH_SAVE_DIR = PATH_DESKTOP
        if not os.path.isdir(PATH_SAVE_DIR):
            os.mkdir(PATH_SAVE_DIR)

    elif platform.system() == 'Darwin':
        pass
    elif platform.system() == 'Linux':
        pass

except Exception as e:
    print(e)
    print("Error : Folder is not created")
