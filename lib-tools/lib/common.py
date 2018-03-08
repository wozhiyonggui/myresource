# -*- coding: UTF-8 -*-
"""

"""
__author__ = 'Steven howtoesc@gmail.com'

import os
import time
from string import maketrans

from lxml import etree

from engine import GameEngine
from TestRunner import run_cmd
import logging
import random
import re

UNSPT = u'[] ()-:\uff08\uff09@'
UNSPT_P = ['___ZL___','___ZR___','___KG___','___XL___','___XR___','___HX___','___MH___','___QXL___','___QXR___','___AT___']
_local_port = 53001
_sdk_port = 27019

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('SR')
logger.setLevel(logging.INFO)


# def adb_forward(device=None, port=None):
#     '''
#     默认单Device的情况下，使用53001
#     多Device的情况下，请指明Device ID
#     未指明端口时，将随机分配当前未使用端口
#     :param port:
#     :param device:
#     :param engine_type:
#     :return:
#     '''
#
#     if not device:
#         if not port:
#             port = _local_port
#
#         if run_cmd("adb forward tcp:{0} tcp:{1}".format(port, _sdk_port))[1]:
#             # raise RuntimeError('adb forward fail')
#             pass
#     else:
#         if not port:
#             my_port = random.randint(53000, 54000)
#         else:
#             my_port = port
#
#         run_cmd("adb forward --remove-all")
#
#         while run_cmd("adb forward tcp:{1} tcp:{2}".format(device, port, _sdk_port))[1]
#
#             ps = []
#             for pp in run_cmd("adb forward --list")[0][:-1:]:
#                 p = int(pp.split(' ')[1].split(':')[1])
#
#                 if device == pp.split(' ')[0]:
#                     port = p
#                     logger.log(logging.INFO, '使用已存在端口映射{}'.format(pp))
#
#                     break
#                 else:
#                     ps += [p]
#
#             if not port:
#                 while not port or port in ps:
#                     port = random.randint(53000, 54000)
#
#                 logger.log(logging.INFO, '随机生成未占用端口:{}'.format(port))
#
#         if run_cmd("adb forward tcp:{1} tcp:{2}".format(device, port, _sdk_port))[1]:
#             # raise RuntimeError('adb forward fail')
#             pass

def get_engine(port=_local_port):
    run_cmd("adb forward --remove-all")
    run_cmd("adb forward tcp:{} tcp:{}".format(port, _sdk_port))
    return GameEngine('127.0.0.1', int(port))

def y2z(str):
    # print str,"y2z"
    # str = "ef_gw_lumianzhiying(Clone)"
    # if str == "ef_gw_lumianzhiying(Clone)":
    #     print re.sub('[{}]'.format(re.escape(UNSPT)), lambda m: dict(zip(UNSPT, UNSPT_P))[m.group()], str)

    str = re.sub(u'/([0-9])',  lambda m: '/_' + m.group(1), str)
    str = re.sub(u'^([0-9][^/]*)',  lambda m: '_' + m.group(1), str)
    return re.sub(u'[{}]'.format(re.escape(UNSPT)), lambda m: dict(zip(UNSPT, UNSPT_P))[m.group()], str)



def z2y(str):
    str = re.sub(u'/_([0-9])'.format(re.escape(UNSPT)),  lambda m: '/' + m.group(1), str)

    return re.sub('___..___'.format(re.escape(UNSPT)), lambda m: dict(zip(UNSPT_P,UNSPT, ))[m.group()], str)

def treetraverse(n, tt=['']):
    if n.get('name') is not None:
        # print type(n.get('name')), n.get('name')
        # if n.get('name') == u'NPC8000BOSS\uff08\u9690\u85cfBOSS\uff0910000622':
        #     print n.get('name')
        #     print type(n.get('name'))
        #     print 'aaa'
        #     a = n.get('name')
        #     b = str(a)
        #     print b
        #     print y2z(b)
        # if type(n.get('name')) is not str:
        #     print type(n.get('name')),n.get('name')
        #     str(n.get('name'))
        #     print type(n.get('name')),n.get('name')

        #for i in n.get('name'):
        #    print type(n.get('name')),n.get('name')
        #tag = n.get('name').translate(maketrans(UNSPT, '_' * len(UNSPT)))
        tag=y2z(n.get('name'))
        n.tag = tag


    r = ['/'.join(tt + [n.tag]) + '(' + '/'.join((list)(n.attrib.values())) + ')']

    for c in n:
        r += treetraverse(c, tt + [n.tag])[0]

    return (r, n)


def get_wt_dump(engine):
    return engine._get_dump_tree()['xml'].encode('utf-8')


'''


def save_wt_dump(f):
    f.write(etree.tostring(etree.fromstring(get_wt_dump()), method='xml', pretty_print=True))


def load_wt_dump(f):
    r, n = treetraverse(etree.parse(f).getroot())
    return n

'''
def get_node_by_path(engine,x, t=1):
    for i in range(0, t):
        r = treetraverse(etree.fromstring(get_wt_dump(engine)))[1].xpath(x)
        if r is not None:
            return (r, i)
        else:
            time.sleep(1)
    return (None, t)


if __name__ == '__main__':
    pass
    # tf = '../temp/{0}.xml'.format(time.time())
    # save_wt_dump(open(tf, 'w'))
