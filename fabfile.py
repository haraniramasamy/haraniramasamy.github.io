from fabric.api import *
import os

def compress(filename):
    base, ext = os.path.splitext(filename)
    local('convert %s -resize 1027 %s' % (filename, base + '_1027px' + ext))
