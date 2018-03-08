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


scene_module_name=u'自由模式测试'


@scene_app.scene_start(u'主界面', [u'自由模式'], 20, '/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(1)
    runner_assert(u'开始比赛',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame/UILabel_3'), '[contains(@txt,\'开始比赛\')]'), False)
    time.sleep(1)
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame')
    time.sleep(1)

@scene_app.scene(u'自由模式', [u'移动方向1', u'死亡复活', u'移动方向1'], 20, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back')
def in_fight(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(1)
    try:
       runner_assert(u'游戏中', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping'),''))
    except:
       pass

@scene_app.scene(u'移动方向1', [u'死亡复活', u'最大体重', u'名次展示', u'胜利界面', u'失败界面', u'返回大厅', u'移动方向2'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back')
def move1(previous_nodes_find, previous_scene, scene_yourself):
    try:
       find_and_press('/AbstractRoot//UI Root/Camera/PlayerInGame(Clone)/Skills/SpitRoot/SpitButton')
       time.sleep(1)
       find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Skills/SpitRoot/SpitButton', '', time_out=None, steps=10,duration=5000)
    except:
        pass

@scene_app.scene(u'移动方向2', [u'死亡复活', u'最大体重', u'名次展示', u'胜利界面', u'失败界面', u'返回大厅', u'移动方向3'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back')
def move2(previous_nodes_find, previous_scene, scene_yourself):
    try:
        find_and_press('/AbstractRoot//UI Root/Camera/PlayerInGame(Clone)/Skills/SpitRoot/SpitButton')
        time.sleep(1)
        find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/LeftRoot/MicButton', '', time_out=None, steps=10,duration=5000)
    except:
        pass

@scene_app.scene(u'移动方向3', [u'死亡复活', u'最大体重', u'名次展示', u'胜利界面', u'失败界面', u'返回大厅', u'移动方向1'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back')
def move3(previous_nodes_find, previous_scene, scene_yourself):
    try:
        find_and_press('/AbstractRoot//UI Root/Camera/PlayerInGame(Clone)/Skills/SpitRoot/SpitButton')
        time.sleep(1)
        find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Back','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Setting', '', time_out=None, steps=10,duration=5000)
    except:
        pass


@scene_app.scene(u'死亡复活', [u'死亡复活', u'移动方向1',u'最大体重', u'名次展示', u'胜利界面', u'失败界面', u'返回大厅'], 5, '/AbstractRoot/UI Root/Camera/GameResult(Clone)/Root/Group/RestartName')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/GameResult(Clone)/Root/Group/RestartName')
    time.sleep(1)


@scene_app.scene(u'最大体重', [u'名次展示', u'胜利界面', u'失败界面', u'返回大厅'], 5, '/AbstractRoot/UI Root/Camera/GameResultWeightPop(Clone)/Title')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultWeightPop(Clone)/Title')
    time.sleep(3)

@scene_app.scene(u'名次展示', [u'胜利界面', u'失败界面', u'返回大厅'], 5, '/AbstractRoot/UI Root/Camera/GameResultRankPop(Clone)/banner/laber_1')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultRankPop(Clone)/banner/laber_1')
    time.sleep(3)

@scene_app.scene(u'胜利界面', [u'返回大厅'], 5, '/AbstractRoot/UI Root/Camera/LevelUpUIPanel(Clone)/Root/Back')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/LevelUpUIPanel(Clone)/Root/Back')
    time.sleep(3)

@scene_app.scene(u'失败界面', [u'返回大厅'], 5, '/AbstractRoot/UI Root/Camera/GameResultRankPop(Clone)/Faile/Texture')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultRankPop(Clone)/Faile/Texture')
    time.sleep(3)

@scene_app.scene(u'返回大厅', [u'广告', u'限时巨惠', u'主界面'], 5, '/AbstractRoot/UI Root/Camera/GameResultRank(Clone)/Root/Group/Over')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/GameResultRank(Clone)/Root/Group/Over')
    time.sleep(3)

@scene_app.scene(u'广告', [u'限时巨惠', u'主界面'], 5, '/AbstractRoot/UI Root/FxCamera/NormalAdPop(Clone)/Title')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/FxCamera/NormalAdPop(Clone)/Title')
    time.sleep(3)

@scene_app.scene(u'限时巨惠', [u'广告', u'主界面'], 5, '/AbstractRoot/UI Root/Camera/NewbieGiftUIPanel(Clone)/Root/close')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(3)
    find_and_press('/AbstractRoot/UI Root/Camera/NewbieGiftUIPanel(Clone)/Root/close')
    time.sleep(3)


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