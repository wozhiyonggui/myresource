# -*- coding: UTF-8 -*-

from __future__ import print_function  # Only Python 2.x
import subprocess, sys, time, os
import logging

__author__ = 'howtoesc@gmail.com'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('SR')
logger.setLevel(logging.INFO)

gdevice = None


def run_cmd(str, use_gdevice=True):
    if str[:3] == 'adb' and use_gdevice and gdevice:
        str = 'adb -s ' + gdevice + str[3:]

    logger.log(logging.INFO, '=>run_cmd:{}'.format(str))
    p = subprocess.Popen(str, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    ss, i = ([], 0)
    while None is p.poll():
        ss.append(p.stdout.readline())

        if ss[-1] == '':
            ss.pop(-1)
            continue

        if len(ss) > 1 and ss[-1] != ss[-2]:
            logger.log(logging.INFO, '')
            i = 1
        else:
            i = i + 1

        logger.log(logging.INFO, '{} *{}'.format(repr(ss[-1]), i))
        # sys.stdout.write('\r{} *{}'.format(repr(ss[-1]), i))
        # sys.stdout.flush()

    # print('\n=>END.')
    return ss, p.wait()


def gt_cmd(cmd):
    cmd = 'adb shell am broadcast -a com.tencent.wstt.gt.baseCommand{};echo $?'.format(cmd)
    if run_cmd(cmd)[0][-1][0] != '0':
        raise RuntimeError('gt_cmd Fail:{}'.format(cmd))


def install_apk(package_name, apkpath):
    if run_cmd('adb shell pm list packages | grep {}'.format(package_name))[0]:
        if run_cmd('adb uninstall {}'.format(package_name))[0][-1].startswith('Failure '):
            raise RuntimeError('Uninstall Fail')

    if run_cmd('adb install {}'.format(apkpath))[0][-1].startswith('F'):
        raise RuntimeError('Install Fail')

    logger.log(logging.INFO, 'Install Success')


def get_info():
    return run_cmd('adb shell getprop ro.product.model')[0][0] + '|' + run_cmd('adb shell getprop ro.product.brand')[0][
        0] + '| Android' + \
           run_cmd('adb shell getprop ro.build.version.release')[0][0]


def load_app(package_name, package_version, activity):
    run_cmd('adb shell am force-stop {};echo $?'.format(package_name))

    if run_cmd('adb shell am start -W {}/{};echo $?'.format(package_name, activity))[0][-1][0] != '0':
        raise RuntimeError('start_monitor Start App Fail')


def start_monitor(package_name, package_version, activity):
    '''
    dumpsys activity top get activity name
    :param package_name:
    :param package_version:
    :param activity:
    :return:
    '''
    run_cmd('adb shell am force-stop {};echo $?'.format(package_name))

    # gt_cmd('.endTest --es saveFolderName "{}"  --es desc "{}"'.format('aa', 'bb'))
    # run_cmd('adb shell rm -rf /sdcard/GT/GW/{}/{}/{}'.format(package_name, package_version, 'aa', ))

    # gt_cmd('.exitGT')

    if run_cmd('adb shell am start -W -n '
               'com.tencent.wstt.gt/com.tencent.wstt.gt.activity.GTMainActivity;echo $?')[0][-1][0] != '0':
        raise RuntimeError('start_monitor Start GT Fail:{}')

    if run_cmd('adb shell am start -W {}/{};echo $?'.format(package_name, activity))[0][-1][0] != '0':
        raise RuntimeError('start_monitor Start App Fail')

    time.sleep(3)

    gt_cmd('.startTest --es pkgName "{}"  --es verName "{}"'.format(package_name, package_version))

    gt_cmd('.sampleData --ei cpu 1')  # 开启CPU采集
    gt_cmd('.sampleData --ei jif 1')  # 开启CPU时间片采集
    gt_cmd('.sampleData --ei pss 1')  # 开启PSS采集
    gt_cmd('.sampleData --ei pri 1')  # 开启PrivateDirty采集
    gt_cmd('.sampleData --ei net 1')  # 开启NET采集
    gt_cmd('.sampleData --ei fps 1')  # 开启FPS采集
    time.sleep(1)


def end_monitor(package_name, package_version, save_folder, desc, path):
    gt_cmd('.endTest --es saveFolderName "{}"  --es desc "{}"'.format(save_folder, desc))
    gt_cmd('.exitGT')

    run_cmd(
        'adb pull /sdcard/GT/GW/{}/{}/{} {}/{}'.format(package_name, package_version, save_folder, path, save_folder))
    run_cmd('adb shell rm -rf /sdcard/GT/GW/{}/{}/{}'.format(package_name, package_version, save_folder))


def upload2db(path, test_project, test_job, db_uri, test_record):
    from db import TestProject, TestJob, TestRunRecord, PreRecord_CPU, PreRecord_FPS, PreRecord_JIF, PreRecord_Net, \
        PreRecord_PRI, PreRecord_PSS
    from db import connect_to_db
    from sqlobject import AND

    # 数据库准备操作
    try:
        connect_to_db(db_uri)
        record = TestRunRecord.select(AND(TestJob.j.TestProject, TestRunRecord.j.TestJob,
                                          TestProject.q.Name == test_project,
                                          TestJob.q.Name == test_job,
                                          TestRunRecord.q.Name == test_record)).getOne()
    except:
        # raise RuntimeError(u'DataBase Ini Error：{} {} {} {}'.format(db_uri, test_project, test_job, test_record))
        raise

    from datetime import datetime

    class mydate(object):
        def __new__(cls, str):
            return datetime.strptime(str, '%Y-%m-%d_%H:%M:%S.%f')

    class myfloat(object):
        def __new__(cls, str):
            return float(str.strip().strip('%')) / 100

    csv_info = {'Pc': {'l': 11, 'c': PreRecord_CPU,
                       'cs': [('T', mydate),
                              ('V', myfloat)]
                       },
                'FP': {'l': 11, 'c': PreRecord_FPS,
                       'cs': [('T', mydate),
                              ('V', int)]
                       },
                'Pj': {'l': 11, 'c': PreRecord_JIF,
                       'cs': [('T', mydate),
                              ('V', int)]
                       },
                'Pn': {'l': 12, 'c': PreRecord_Net,
                       'cs': [('T', mydate),
                              ('Transmitted', float),
                              ('Transmitted', float)]
                       },
                'Ps': {'l': 12, 'c': PreRecord_PSS,
                       'cs': [('T', mydate),
                              ('Total', int),
                              ('Dalvik', int),
                              ('Native', int), ]
                       },
                'Pr': {'l': 12, 'c': PreRecord_PRI,
                       'cs': [('T', mydate),
                              ('Total', int),
                              ('Dalvik', int),
                              ('Native', int), ]
                       }
                }

    for f in os.listdir(path):
        if f[-3:] != 'csv':
            continue
        logger.log(logging.INFO, 'Upload{}'.format(f))
        f_info = csv_info[f[:2]]
        with open(path + '/' + f, 'r') as fo:
            ff = fo.read().split('\n')
            ds = ff[3].split(',')[1].strip()
            for l in ff[f_info['l']:]:
                l = l.strip()
                if '' == l:
                    continue
                ks, vs = (['TestRunRecord'], [record])
                css = (ds + '_' + l).split(',')
                for i in range(0, len(f_info['cs'])):
                    ks.append(f_info['cs'][i][0])
                    vs.append(f_info['cs'][i][1](css[i]))

                f_info['c'](**dict(zip(ks, vs)))


if __name__ == '__main__':
    upload2db('./csvtest', u'月圆之夜', u'冒烟测试', u'#1',
              'mysql://root:!QAZ2wsx@192.168.93.173/practice?use_unicode=1&charset=utf8')

# install_apk('com.giant.cardvmax', './cardv_17-09-14-20-40.apk')debug=1&
# start_monitor('com.giant.cardvmax', '1.0', 'com.unity3d.player.UnityPlayerActivity')
# time.sleep(100)
# end_monitor('com.giant.cardvmax', '1.0', 'ssssss', 'dddd', './')
