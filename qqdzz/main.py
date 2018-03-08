# -*- coding: UTF-8 -*-
import glob
import logging
import os
import re
import sys
from collections import OrderedDict
from datetime import datetime
from os.path import dirname
import time
from lib import TestRunner
reload(sys)
sys.setdefaultencoding('utf-8')

def run(BuildNO, xUnixtFile, cpFolder, device, port):
    # os.system("wget ftp://192.168.93.35:2222/cardv_17-09-14-20-40.apk")
    start = datetime.now()
    TestRunner.gdevice = device
    # TestRunner.install_apk('com.giant.cardvmax', './cardv_17-09-14-20-40.apk')
    TestRunner.load_app('com.ztgame.bob', '1.0', '.UnityPlayerNativeActivity')

    time.sleep(60)

    for f in glob.glob("./bob_*.py"):
        __import__(re.split('[/\\\\]', f[:-3])[-1])

    from lib.SceneRunner import scene_app

    module_list = OrderedDict({k: 0 for k in scene_app.SceneModules})
    module_list[u'大逃杀'] = 0

    for k in module_list:
        if 'X' == k[-1]:
            module_list[k] = 0.5

    scene_app.prepare(device, port, dirname(__file__) + './qqdzz.xlsx', cpFolder, log_level=logging.INFO)

    while module_list[u'大逃杀'] == 0:
        time.sleep(3)
        for k in module_list:
            if scene_app.run_scenes([k], 0):
                continue
            else:
                if 'X' != k[-1]:
                    module_list[k] += 1
                    module_list = OrderedDict(sorted(module_list.iteritems(), key=lambda t: t[1]))

                break

    scene_app.output_junit(cpFolder + '/' + xUnixtFile)

    info = TestRunner.get_info()

    #上传数据库
    scene_app.upload2db(u'球球大作战', u'bob', info,
                   'mysql://root:!QAZ2wsx@192.168.93.96/practice?debug=1&use_unicode=1&charset=utf8',
                   BuildNO, start,
                   datetime.now())


if __name__ == '__main__':
    B = '#' + os.environ["BUILD_NUMBER"] + os.environ["NODE_NAME"]
    cpFolder = os.environ["WORKSPACE"] + '/' + B

    if not os.path.exists(cpFolder):
        os.mkdir(cpFolder)

    fh = logging.FileHandler('{}/{}.log'.format(cpFolder, B))
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger = logging.getLogger('SR').addHandler(fh)

    run(B, B + '.xml', cpFolder, os.environ["DID"], os.environ["LPORT"])
