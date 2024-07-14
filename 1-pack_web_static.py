#!/usr/bin/python3
""" Compress web_static files to send to servers"""


from fabric.api import *
from datetime import datetime
import os
date_ = datetime.now().replace(microsecond=0)
date_ = date_.strftime("%Y%m%d%H%M%S")
name = "web_static_" + date_ + ".tgz"


def do_pack():
    """Pack web_static files in tarball archive"""

    if not os.path.exists("versions"):
        local("mkdir versions")
    local(f"tar -czvf versions/{name} web_static")
    size = os.path.getsize(f'versions/{name}')
    print(f"web_static packed: {name} -> {size}Bytes")
