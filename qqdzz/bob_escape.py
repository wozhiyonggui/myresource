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


scene_module_name=u'大逃杀'

@scene_app.scene_start(u'飞船查看', [u'光环'], 100, '/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/EquipButton')
def checkship(previous_nodes_find, previous_scene, scene_yourself):
    if find_node_by_xpath(y2z('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_0/GoTo'),'')[0] is not None:
        runner_assert(u'开始逃杀', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_0/GoTo'),'')[0])
        find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_0/GoTo')
        time.sleep(1)
    else:
        runner_assert(u'飞船界面',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/EquipButton'),''))
        find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/EquipButton')
        time.sleep(1)

@scene_app.scene(u'光环', [u'光环关闭'], 5, '/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/top')
def halo(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/anniu_1')
    runner_assert(u'光环界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/title_1'),'[contains(@txt,\'光环\')]'))
    time.sleep(1)

@scene_app.scene(u'光环关闭', [u'圣衣'], 5, '/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
def halo_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
    time.sleep(1)

@scene_app.scene(u'圣衣', [u'孢子'], 5, '/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/top')
def armor(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/anniu_2',time_out=3)
    runner_assert(u'圣衣', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/FxCamera/TaiJinShengYiTempPanel(Clone)/Scroll/Center/TaiJinShellItem(Clone)'),''))
    time.sleep(1)

@scene_app.scene(u'孢子', [u'孢子关闭'], 5, '/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/top')
def spore(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/anniu_3',time_out=3)
    runner_assert(u'孢子界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/title_1'),'[contains(@txt,\'孢子\')]'))
    time.sleep(1)

@scene_app.scene(u'孢子关闭', [u'残影'], 5, '/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
def spore_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
    time.sleep(1)

@scene_app.scene(u'残影', [u'残影关闭'], 5, '/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/top')
def ghost(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/anniu_4')
    runner_assert(u'残影界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/title_1'),'[contains(@txt,\'残影\')]'))
    time.sleep(1)

@scene_app.scene(u'残影关闭', [u'关键词'], 5, '/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
def ghost_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
    time.sleep(1)

@scene_app.scene(u'关键词', [u'关键词关闭'], 5, '/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/top')
def keywords(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/anniu_5')
    runner_assert(u'关键词界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/title_1'),'[contains(@txt,\'关键词\')]'))
    time.sleep(1)

@scene_app.scene(u'关键词关闭', [u'飞船关闭'], 5, '/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
def keywords_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinGuangHuanTempPanel(Clone)/close')
    time.sleep(1)


@scene_app.scene(u'飞船关闭', [u'排行榜'], 5, '/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/close')
def ship_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ZhanJianPopPanel(Clone)/close')
    time.sleep(1)

@scene_app.scene(u'排行榜', [u'周排行'], 5, '/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/Rank')
def rank(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/Rank')
    runner_assert(u'排行榜界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/title_1'),'[contains(@txt,\'排行榜\')]'))
    time.sleep(1)

@scene_app.scene(u'周排行', [u'飞船排行'], 5, '/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/Group/Data/Week')
def week_rank(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/Group/Data/Week')
    runner_assert(u'周排行', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/Group/Data/Week'),'[@img=\'xxj_61\']'))
    time.sleep(1)

@scene_app.scene(u'飞船排行', [u'排行关闭'], 5, '/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/anniu_2')
def ship_rank(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/anniu_2')
    runner_assert(u'飞船排行', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/Group/Data/Total/title'),'[contains(@txt,\'总排行\')]'))
    time.sleep(1)

@scene_app.scene(u'排行关闭', [u'宝箱'], 5, '/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/close')
def rank_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinRankPanel(Clone)/close')
    time.sleep(1)

@scene_app.scene(u'宝箱', [u'宝箱关闭'], 5, '/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/BaoXiang')
def chest(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/BaoXiang')
    runner_assert(u'宝箱界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinChestsCenterPanel(Clone)/Return'),''))
    time.sleep(1)

@scene_app.scene(u'礼包1', [u'礼包关闭'], 5, '/AbstractRoot/UI Root/Camera/TaiJinChestsCenterPanel(Clone)/Scroll View/top')
def chest1(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinChestsCenterPanel(Clone)/Scroll View/top', '/*[position()=1]')
    time.sleep(1)

@scene_app.scene(u'礼包关闭', [u'宝箱关闭'], 5, '/AbstractRoot/UI Root/Camera/TaiJinBagInfoPanel(Clone)/close')
def chest1_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinBagInfoPanel(Clone)/close')
    time.sleep(1)

@scene_app.scene(u'宝箱关闭', [u'组队界面'], 5, '/AbstractRoot/UI Root/Camera/TaiJinChestsCenterPanel(Clone)/close')
def chest_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinChestsCenterPanel(Clone)/close')
    time.sleep(1)


@scene_app.scene(u'组队界面', [u'组队关闭'], 5, '/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/FeiChuan_CX/FeiChuan_01/FeiChuan/Root/jia')
def chest_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/FeiChuan_CX/FeiChuan_01/FeiChuan/Root/jia')
    runner_assert(u'组队界面', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TaiJinQRCodePopPanel(Clone)/QRCode'),''))
    time.sleep(1)

@scene_app.scene(u'组队关闭', [u'开始逃生'], 5, '/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/InvitingObj/Inviting/Texture')
def chest_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/InvitingObj/Inviting/Texture')
    time.sleep(1)

@scene_app.scene(u'开始逃生', [u'战斗中'], 60, '/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/feichuan/StartBtn')
def start_escape(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/CreatTLifeUIPanel(Clone)/jiemian_2/feichuan/StartBtn')
    runner_assert(u'开始逃生', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/TLifeFreeReadyUIPanel(Clone)/kuang_4/Title'),'[contains(@txt,\'本轮参与\')]'))
    time.sleep(3)

@scene_app.scene(u'战斗中', [u'点击屏幕',u'结算关闭',u'移动方向1'], 300, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping')
def in_fight(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(5)
    runner_assert(u'战斗中', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping'),''))
    pass


@scene_app.scene(u'移动方向1', [u'点击屏幕',u'结算关闭',u'移动方向2'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping')
def move1(previous_nodes_find, previous_scene, scene_yourself):
    find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/DanMuPanel/Root/DanMuGiftItem/IconRoot/Icon','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Skills/DevideRoot/Center', '', time_out=None, steps=100,duration=10000)

@scene_app.scene(u'移动方向2', [u'点击屏幕',u'结算关闭',u'移动方向3'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping')
def move2(previous_nodes_find, previous_scene, scene_yourself):
    find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/DanMuPanel/Root/DanMuGiftItem/IconRoot/Icon','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Setting', '', time_out=None, steps=100,duration=10000)

@scene_app.scene(u'移动方向3', [u'点击屏幕',u'结算关闭',u'移动方向4'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping')
def move3(previous_nodes_find, previous_scene, scene_yourself):
    find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/DanMuPanel/Root/DanMuGiftItem/IconRoot/Icon','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/LeftRoot/MicButton', '', time_out=None, steps=100,duration=10000)

@scene_app.scene(u'移动方向4', [u'点击屏幕',u'结算关闭',u'移动方向1'], 5, '/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/Info/RightRoot/Rank/Ping')
def move4(previous_nodes_find, previous_scene, scene_yourself):
    find_and_swipe('/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/DanMuPanel/Root/DanMuGiftItem/IconRoot/Icon','/AbstractRoot/UI Root/Camera/PlayerInGame(Clone)/TouchControl/Stick', '', time_out=None, steps=100,duration=10000)


@scene_app.scene(u'点击屏幕', [u'点击屏幕',u'结算关闭',u'结算面板'], 5, '/AbstractRoot/UI Root/FxCamera//label_1')
def tap_screen(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/FxCamera//label_1')
    time.sleep(1)


@scene_app.scene(u'结算面板', [u'结算关闭',u'查看宝箱'], 5, '/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/ContinueTips')
def close_pannel(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/ContinueTips')
    time.sleep(1)

@scene_app.scene(u'查看宝箱', [u'解锁宝箱'], 5, '/AbstractRoot/UI Root/FxCamera/RewardTaiJinChestPop(Clone)/Pag2/LookBtn')
def check_chest(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/FxCamera/RewardTaiJinChestPop(Clone)/Pag2/LookBtn')
    time.sleep(1)

@scene_app.scene(u'解锁宝箱', [u'宝箱返回'], 5, '/AbstractRoot/UI Root/Camera/TaiJinChestsResultPanel(Clone)/Root/Right/Root/PersonalBtns/OpenBtn')
def chest_unlock(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinChestsResultPanel(Clone)/Root/Right/Root/PersonalBtns/OpenBtn')
    time.sleep(1)

@scene_app.scene(u'宝箱返回', [u'结算关闭'], 5, '/AbstractRoot/UI Root/Camera/TaiJinChestsResultPanel(Clone)/Root/Right/BottomRight/Return')
def chest_return(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TaiJinChestsResultPanel(Clone)/Root/Right/BottomRight/Return')
    time.sleep(1)

@scene_app.scene_end(u'结算关闭', [u'结算关闭',u'开始逃生'], 5, '/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/close')
def pannel_close(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/TLResultPanel(Clone)/close')
    time.sleep(1)


@scene_app.scene(u'账号昵称', [u'选服'], 5, '/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/InputName/Name')
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



