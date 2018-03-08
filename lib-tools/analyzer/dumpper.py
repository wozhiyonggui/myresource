# -*- coding: UTF-8 -*-
"""

"""
__author__ = 'howtoesc@gmail.com'

from analyzer.lib.common import *
import mainwindow



def dummper(f):
    '''

    :param f: 保存路径
    :return: 4个文件的句柄
    '''

    # 自动创建文件夹
    try:
        if not os.path.exists(f):
            os.makedirs(f)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

    # 以dirname作为文件名前缀
    fn = f + '/' + f.split('/')[-1]
    fs = (open(fn + '-origin.xml', 'w'), open(fn + '-transp.xml', 'w'),
          open(fn + '-fullpath.txt', 'w'))

    ox = getwtdump()
    tx = etree.fromstring(ox)
    fs[0].write(etree.tostring(tx, method='xml', pretty_print=True))

    p = treetraverse(tx)[0]
    fs[1].write(etree.tostring(tx, method='xml', pretty_print=True))
    fs[2].write(u'\n'.join(p).encode('utf-8').strip())


if __name__ == '__main__':
    dummper('temp/{}'.format(time.time()))
