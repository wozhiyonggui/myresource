# -*- coding: UTF-8 -*-

import os
import time
from string import maketrans
from lxml import etree
import random
import sys
from lib.common import *
from lib.SceneRunner import *
import lib.engine as engine
reload(sys)
sys.setdefaultencoding('utf-8')

#默认需要老主界面

scene_module_name=u'观战测试'

@scene_app.scene_start(u'主界面', [u'观战按钮', u'主界面'], 200, '/AbstractRoot/UI Root/Camera/GameName(Clone)/rightButtonTF/RightButtonPanel(Clone)/FirstGrid/Grid1/guanzhanBtn')
def check(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'更多',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/MoreRoom/Label'), '[contains(@txt,\'更多\')]'), False)
    time.sleep(2)
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/rightButtonTF/RightButtonPanel(Clone)/FirstGrid/Grid1/guanzhanBtn')
    time.sleep(2)

@scene_app.scene(u'观战按钮', [u'观战界面', u'主界面'], 200, '/AbstractRoot/UI Root/Camera/GuanZhanPanel(Clone)/Top/TopLabel_1')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'推荐房间',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GuanZhanPanel(Clone)/Top/TopLabel_1'), '[contains(@txt,\'推荐房间\')]'), False)
    time.sleep(2)

@scene_app.scene(u'观战界面', [u'开始观战1', u'观战界面', u'主界面'], 100, '/AbstractRoot/UI Root/Camera/GuanZhanPanel(Clone)/Content_2/Itemhot_1/guanzhanBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    try:
        time.sleep(3)
        find_and_press('/AbstractRoot/UI Root/FxCamera/MessageBoxPanel(Clone)/SureBtn')
        time.sleep(3)
        find_and_press('/AbstractRoot/UI Root/Camera/RegisterInputPopPanel(Clone)/CloseBtn')
        time.sleep(3)
    except:
        pass
    time.sleep(2)
    find_and_press('/AbstractRoot/UI Root/Camera/GuanZhanPanel(Clone)/RandomBtn')
    time.sleep(2)
    find_and_press('/AbstractRoot/UI Root/Camera/GuanZhanPanel(Clone)/Content_2/Itemhot_1/guanzhanBtn')
    time.sleep(2)

@scene_app.scene(u'开始观战1', [u'恭喜人气提升', u'团战-队伍排名', u'大逃杀-退出观战', u'大逃杀-本轮结束', u'生存-退出比赛', u'自建-退出观战', u'猎魔失败', u'猎魔返回', u'开始观战2', u'返回大厅', u'迅游加速', u'观战界面', u'主界面'], 100, '/AbstractRoot/UI Root/Camera/ViewerInGame(Clone)/DanMuPanel/SendRoot/ShowHide')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    try:
       os.popen('adb shell input tap 800 600')
       time.sleep(5)
    except:
        pass

@scene_app.scene(u'开始观战2', [u'恭喜人气提升', u'团战-队伍排名', u'大逃杀-退出观战', u'大逃杀-本轮结束', u'生存-退出比赛', u'自建-退出观战', u'猎魔失败', u'猎魔返回', u'开始观战1', u'返回大厅', u'迅游加速', u'观战界面', u'主界面'], 100, '/AbstractRoot/UI Root/Camera/ViewerInGame(Clone)/DanMuPanel/SendRoot/ShowHide')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    try:
       os.popen('adb shell input tap 800 600')
       time.sleep(5)
    except:
        pass

@scene_app.scene(u'恭喜人气提升', [u'恭喜人气提升', u'团战-队伍排名', u'大逃杀-退出观战', u'大逃杀-本轮结束', u'生存-退出比赛', u'自建-退出观战', u'猎魔失败', u'猎魔返回', u'开始观战1', u'返回大厅', u'迅游加速', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/GameResultZhuBoReward(Clone)/titlex_2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'礼物数量',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameResultZhuBoReward(Clone)/SongliNum/titlex_3'), '[contains(@txt,\'礼物数量\')]'), False)
    time.sleep(2)
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultZhuBoReward(Clone)/titlex_2')
    time.sleep(2)

@scene_app.scene(u'大逃杀-退出观战', [u'大逃杀-退出观战', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/Grid/EscWatch')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/Grid/EscWatch')
    time.sleep(3)

@scene_app.scene(u'生存-退出比赛', [u'生存-退出比赛', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/FlashOver(Clone)/Root/Group/Exit')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/FlashOver(Clone)/Root/Group/Exit')
    time.sleep(3)

@scene_app.scene(u'迅游加速', [u'迅游加速', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/FxCamera/MessageBoxPanel(Clone)/CancelBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/FxCamera/MessageBoxPanel(Clone)/CancelBtn')
    time.sleep(3)

@scene_app.scene(u'团战-队伍排名', [u'团战-队伍排名',u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/GameResultRankDetails(Clone)/returnBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultRankDetails(Clone)/returnBtn')
    time.sleep(3)

@scene_app.scene(u'大逃杀-本轮结束', [u'大逃杀-本轮结束', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/close')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/close')
    time.sleep(3)

@scene_app.scene(u'自建-退出观战', [u'自建-退出观战', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/FlashCreateDeath(Clone)/Root/Group/Cotinue')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/FlashCreateDeath(Clone)/Root/Group/Cotinue')
    time.sleep(3)

@scene_app.scene(u'猎魔失败', [u'猎魔失败', u'猎魔返回', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/FxCamera/GameBossWinPop(Clone)/banner/laber_1')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/FxCamera/GameBossWinPop(Clone)/banner/laber_1')
    time.sleep(3)

@scene_app.scene(u'猎魔返回', [u'猎魔返回', u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/BossResultRankUIPanel(Clone)/OverBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/BossResultRankUIPanel(Clone)/OverBtn')
    time.sleep(3)

@scene_app.scene(u'返回大厅', [u'观战界面', u'主界面'], 20, '/AbstractRoot/UI Root/Camera/GameResultRank(Clone)/Root/Group/Over')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultRank(Clone)/Root/Group/Over')
    time.sleep(2)

@scene_app.scene_end(u'账号昵称', [u'选服'], 5, '/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/InputName/Name')
def input_account(previous_nodes_find, previous_scene, scene_yourself):
    while 1:
        find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/ChangeName')
        time.sleep(1)
        print 'tap'

@scene_app.scene(u'选服', [u'登录'], 5, '/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/Sever')
def server(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/Sever')
    time.sleep(1)

if __name__ == '__main__':
    scene_app.run('qqdzz.xlsx','./111',log_level=logging.INFO, device= '69T7N16A17001569',port= 52293)
    scene_app.output_junit('xxx.xml')


