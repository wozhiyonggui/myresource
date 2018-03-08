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


scene_module_name=u'测试'


@scene_app.scene_start(u'主界面', [u'个人主页'], 20, '/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/PlayerInfo')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(4)
    runner_assert(u'本轮昵称', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/InputName/UILabel_1'),'[contains(@txt,\'本轮昵称\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/PlayerInfo')
    time.sleep(4)

@scene_app.scene(u'个人主页', [u'喜欢自己'], 50, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalMainPanel(Clone)/hostloverlist/tx')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalMainPanel(Clone)/hostloverlist/tx')
    time.sleep(4)

@scene_app.scene(u'喜欢自己', [u'喜欢栏'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalMainPanel(Clone)/hostloverlist')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(4)
    runner_assert(u'默认头像', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalMainPanel(Clone)/hostplayer_1'),''), False)
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalMainPanel(Clone)/hostloverlist')
    time.sleep(4)

@scene_app.scene(u'喜欢栏', [u'照片'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao2')
    time.sleep(4)
    runner_assert(u'我的照片', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalPhotoPanel(Clone)/Label'),'[contains(@txt,\'我的照片\')]'), False)
    time.sleep(4)

@scene_app.scene(u'照片', [u'游戏-段位信息'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao3')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao3')
    time.sleep(4)

@scene_app.scene(u'游戏-段位信息', [u'查看全部'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/LevelTab/Info/RewardBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/LevelTab/Info/RewardBtn')
    time.sleep(2)

@scene_app.scene(u'查看全部', [u'拖动中'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/LevelTab/Info/RewardBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(4)
    runner_assert(u'赛季结算奖励',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/SeasonRewardPopPanel(Clone)/Root/title'), '[contains(@txt,\'赛季结算奖励\')]'), False)
    time.sleep(4)

@scene_app.scene(u'拖动中', [u'拖动屏幕'], 20, '/AbstractRoot/UI Root/Camera/SeasonRewardPopPanel(Clone)/Root/ContentRoot/Grid/Item0/Back')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_swipe( '/AbstractRoot/UI Root/Camera/SeasonRewardPopPanel(Clone)/Root/ContentRoot/Grid/Item3/Back',  '/AbstractRoot/UI Root/Camera/SeasonRewardPopPanel(Clone)/Root/ContentRoot/Grid/Item0/Back', '', time_out=None, steps=500,duration=5000)
    time.sleep(4)

@scene_app.scene(u'拖动屏幕', [u'关闭查看全部'], 20, '/AbstractRoot/UI Root/Camera/SeasonRewardPopPanel(Clone)/Root/Close')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/SeasonRewardPopPanel(Clone)/Root/Close')
    time.sleep(4)

@scene_app.scene(u'关闭查看全部', [u'游戏-详细数据'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_1')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(4)
    runner_assert(u'当前段位', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/LevelTab/LevelBigItem/Title'), '[contains(@txt,\'当前段位\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_1')
    time.sleep(4)

@scene_app.scene(u'游戏-详细数据', [u'游戏-个人成就'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_3')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    time.sleep(4)
    runner_assert(u'当前赛季段位', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/DataTab/shuji/sprite_1'), '[contains(@txt,\'当前赛季段位\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_3')
    time.sleep(2)

@scene_app.scene(u'游戏-个人成就', [u'游戏-个人荣誉'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_4')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_4')
    time.sleep(2)

@scene_app.scene(u'游戏-个人荣誉', [u'游戏-比赛记录'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_5')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGamePanel(Clone)/TopTab/anniu_5')
    time.sleep(2)

@scene_app.scene(u'游戏-比赛记录', [u'皮肤-皮肤'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao5')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao5')
    runner_assert(u'皮肤总价值', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/PanelInfo/SkinRoot/title'), '[contains(@txt,\'皮肤总价值\')]'), False)
    time.sleep(2)

@scene_app.scene(u'皮肤-皮肤', [u'皮肤-圣衣'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/PanelBack/banner_2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/PanelBack/banner_2')
    runner_assert(u'圣衣总价值', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/PanelInfo/ShellRoot/title'), '[contains(@txt,\'圣衣总价值\')]'), False)
    time.sleep(2)

@scene_app.scene(u'皮肤-圣衣', [u'皮肤-星空探险'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/PanelBack/banner_3')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/PanelBack/banner_3')
    runner_assert(u'总探险分数', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalSkinPanel(Clone)/Panel'), '[contains(@txt,\'总探险分数\')]'), False)
    time.sleep(2)

@scene_app.scene(u'皮肤-星空探险', [u'礼物-我的礼物'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao6')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao6')
    runner_assert(u'送礼积分', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/GiftListObj/Worth/title'), '[contains(@txt,\'送礼积分\')]'), False)
    time.sleep(2)

@scene_app.scene(u'礼物-我的礼物', [u'礼物-收礼记录'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/anniu_2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/anniu_2')
    time.sleep(2)

@scene_app.scene(u'礼物-收礼记录', [u'礼物-兑换奖品'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/anniu_3')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/anniu_3')
    runner_assert(u'礼物积分', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/GiftExchangeObj/Worth/title'), '[contains(@txt,\'礼物积分\')]'), False)
    time.sleep(2)

@scene_app.scene(u'礼物-兑换奖品', [u'兑换'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/GiftExchangeObj/yuan_1/anniu')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'兑换', find_node_by_xpath(y2z( u'/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/GiftExchangeObj/yuan_1/anniu/title'), '[contains(@txt,\'兑换\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/PersonalGiftPanel(Clone)/GiftExchangeObj/yuan_1/anniu')
    time.sleep(2)

@scene_app.scene(u'兑换', [u'确定'], 20, '/AbstractRoot/UI Root/FxCamera/MessageBoxPanel(Clone)/SureBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'确定', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/FxCamera/MessageBoxPanel(Clone)/SureBtn/Label'),'[contains(@txt,\'确定\')]'), False)
    find_and_press('/AbstractRoot/UI Root/FxCamera/MessageBoxPanel(Clone)/SureBtn')
    time.sleep(2)

@scene_app.scene(u'确定', [u'留言'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao4')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/leibiao4')
    time.sleep(2)

@scene_app.scene(u'留言', [u'留言-发送'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/LeaveMessagePanel(Clone)/MsgSend/SendBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/LeaveMessagePanel(Clone)/MsgSend/SendBtn')
    time.sleep(2)

@scene_app.scene(u'留言-发送', [u'留言-回复'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/LeaveMessagePanel(Clone)/MsgSend/ViewReplyBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/LeaveMessagePanel(Clone)/MsgSend/ViewReplyBtn')
    time.sleep(2)

@scene_app.scene(u'留言-回复', [u'关闭留言-回复'], 20, '/AbstractRoot/UI Root/Camera/LeaveMessagePopPanel(Clone)/PanelButton/close')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/LeaveMessagePopPanel(Clone)/PanelButton/close')
    time.sleep(2)

@scene_app.scene(u'关闭留言-回复', [u'主界面2'], 20, '/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/HonorFrameRoot/goreturn')
def diane(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PersonalHomePanel(Clone)/HonorFrameRoot/goreturn')
    runner_assert(u'开始比赛',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame/UILabel_3'), '[contains(@txt,\'开始比赛\')]'), False)
    time.sleep(2)

@scene_app.scene(u'主界面2', [u'聊天'], 50, '/AbstractRoot/UI Root/Camera/GameName(Clone)/GameCenterPanel(Clone)/PanelButton/ChatTable')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/GameCenterPanel(Clone)/PanelButton/ChatTable')
    time.sleep(2)

@scene_app.scene(u'聊天', [u'发起群聊'], 20, '/AbstractRoot/UI Root/Camera/ChatContactPanel(Clone)/Root/PanelButton/AddGroup')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'搜索', find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/ChatContactPanel(Clone)/Root/PanelButton/Search/root/laber'), '[contains(@txt,\'搜索\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/ChatContactPanel(Clone)/Root/PanelButton/AddGroup')
    time.sleep(2)

@scene_app.scene(u'发起群聊', [u'取消'], 20, '/AbstractRoot/UI Root/Camera/ChatContactPanel(Clone)/Root/PanelButton/BottomBtn/Cancel')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ChatContactPanel(Clone)/Root/PanelButton/BottomBtn/Cancel')
    time.sleep(2)

@scene_app.scene(u'取消', [u'常见问题'], 20, '/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn1')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn1')
    time.sleep(2)

@scene_app.scene(u'常见问题', [u'账号问题'], 20, '/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn2')
    time.sleep(2)

@scene_app.scene(u'账号问题', [u'充值问题'], 20, '/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn3')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn3')
    time.sleep(2)

@scene_app.scene(u'充值问题', [u'其他问题'], 20, '/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn4')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn4')
    time.sleep(2)
    find_and_press('/AbstractRoot/UI Root/Camera/ChatWindowPanel(Clone)/Root/SystemButton/Type_1/QuestionBtn4')
    time.sleep(2)

@scene_app.scene(u'其他问题', [u'主界面3'], 20, '/AbstractRoot/UI Root/Camera/ChatUIPanel(Clone)/GameCenterPanel(Clone)/PanelButton/GameTable')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ChatUIPanel(Clone)/GameCenterPanel(Clone)/PanelButton/GameTable')
    runner_assert(u'开始比赛',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame/UILabel_3'), '[contains(@txt,\'开始比赛\')]'), False)
    time.sleep(2)

@scene_app.scene(u'主界面3', [u'关系'], 20, '/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/Anchor/Relation/RelationBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/Anchor/Relation/RelationBtn')
    runner_assert(u'发现',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/faxianBtn/titleLabel'), '[contains(@txt,\'发现\')]'), False)
    time.sleep(2)

@scene_app.scene(u'关系', [u'关系-发现'], 20, '/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/faxianBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/faxianBtn')
    time.sleep(2)

@scene_app.scene(u'关系-发现', [u'返回关系'], 20, '/AbstractRoot/UI Root/Camera/PhotoDisplayUIPanel(Clone)/Return')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/PhotoDisplayUIPanel(Clone)/Return')
    time.sleep(2)

@scene_app.scene(u'返回关系', [u'粉丝'], 20, '/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/fansBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/fansBtn')
    time.sleep(2)

@scene_app.scene(u'粉丝', [u'官方认证'], 20, '/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/renzhengBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/renzhengBtn')
    time.sleep(2)

@scene_app.scene(u'官方认证', [u'其他'], 20, '/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/otherBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/otherBtn')
    time.sleep(2)
    find_and_press('/AbstractRoot/UI Root/Camera/Relation(Clone)/Togglebtns/otherBtn')
    time.sleep(2)

@scene_app.scene(u'其他', [u'主界面4'], 20, '/AbstractRoot/UI Root/Camera/Relation(Clone)/Return')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Relation(Clone)/Return')
    time.sleep(2)

@scene_app.scene(u'主界面4', [u'排行榜'], 20, '/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/Anchor/Rank/RankBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'开始比赛',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame/UILabel_3'), '[contains(@txt,\'开始比赛\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/Anchor/Rank/RankBtn')
    time.sleep(2)

@scene_app.scene(u'排行榜', [u'段位-全球榜'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'切换省市',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Group_8/ChangeCity'), '[contains(@txt,\'切换省市\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
    time.sleep(2)

@scene_app.scene(u'段位-全球榜', [u'段位-历史最高'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
    time.sleep(2)

@scene_app.scene(u'段位-历史最高', [u'大逃杀排行榜'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_TLife')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_TLife')
    time.sleep(2)

@scene_app.scene(u'大逃杀排行榜', [u'大逃杀排行榜-历史最高'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/HesLevel')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/HesLevel')
    time.sleep(2)

@scene_app.scene(u'大逃杀排行榜-历史最高', [u'粉丝排行榜'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_fensi')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_fensi')
    time.sleep(2)

@scene_app.scene(u'粉丝排行榜', [u'粉丝排行榜-周排行'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_fensi')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_fensi')
    time.sleep(2)

@scene_app.scene(u'粉丝排行榜-周排行', [u'粉丝排行榜-总排行'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
    time.sleep(2)

@scene_app.scene(u'粉丝排行榜-总排行', [u'皮肤排行榜'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_Pifu')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_1/top_Pifu')
    time.sleep(2)

@scene_app.scene(u'皮肤排行榜', [u'皮肤排行榜-赛季排行'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
    time.sleep(2)

@scene_app.scene(u'皮肤排行榜-赛季排行', [u'皮肤排行榜-总价值'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
    time.sleep(2)

@scene_app.scene(u'皮肤排行榜-总价值', [u'战队排行榜'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/headline/headline_2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/headline/headline_2')
    time.sleep(2)

@scene_app.scene(u'战队排行榜', [u'战队排行榜-全球榜'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
    time.sleep(2)

@scene_app.scene(u'战队排行榜-全球榜', [u'战队排行榜-历史最高'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
    time.sleep(2)

@scene_app.scene(u'战队排行榜-历史最高', [u'战队排行榜-粉丝'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_2/top_fensi')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Top_2/top_fensi')
    time.sleep(2)

@scene_app.scene(u'战队排行榜-粉丝', [u'战队排行榜-周排行'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Week')
    time.sleep(2)

@scene_app.scene(u'战队排行榜-周排行', [u'战队排行榜-总排行'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Group/Data/Month')
    time.sleep(2)

@scene_app.scene(u'战队排行榜-总排行', [u'主界面5'], 20, '/AbstractRoot/UI Root/Camera/Rank(Clone)/Return')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/Rank(Clone)/Return')
    time.sleep(2)

@scene_app.scene(u'主界面5', [u'魔法屋'], 20, '/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/Anchor/Shop/ShopBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'开始比赛',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/GameName(Clone)/Box/StartGame/UILabel_3'), '[contains(@txt,\'开始比赛\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/GameName(Clone)/firstRoot/Anchor/Shop/ShopBtn')
    time.sleep(2)

@scene_app.scene(u'魔法屋', [u'魔法屋-宝箱'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/BoxTap')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    runner_assert(u'背包',find_node_by_xpath(y2z(u'/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/BottomRight/BagBtn/Label'), '[contains(@txt,\'背包\')]'), False)
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/BoxTap')
    time.sleep(2)

@scene_app.scene(u'魔法屋-宝箱', [u'魔法屋-皮肤'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/SkinTap')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/SkinTap')
    time.sleep(2)

@scene_app.scene(u'魔法屋-皮肤', [u'魔法屋-皮肤-孢子'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/EquipTypes/3')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/EquipTypes/3')
    time.sleep(2)

@scene_app.scene(u'魔法屋-皮肤-孢子', [u'魔法屋-皮肤-残影'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/EquipTypes/4')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/EquipTypes/4')
    time.sleep(2)

@scene_app.scene(u'魔法屋-皮肤-残影', [u'魔法屋-圣衣'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/ShellTap')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/ShellTap')
    time.sleep(2)

@scene_app.scene(u'魔法屋-圣衣', [u'魔法屋-圣衣-圣殿'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/ShellPage/EquipTypes/2')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/ShellPage/EquipTypes/2')
    time.sleep(2)

@scene_app.scene(u'魔法屋-圣衣-圣殿', [u'魔法屋-魔灵'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/MonglingTTap')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/MonglingTTap')
    time.sleep(2)

@scene_app.scene(u'魔法屋-魔灵', [u'魔法屋-魔灵-移动一次'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/ShopMoLingPanel(Clone)/liebiao/fanye_right')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/ShopMoLingPanel(Clone)/liebiao/fanye_right')
    time.sleep(2)

@scene_app.scene(u'魔法屋-魔灵-移动一次', [u'魔法屋-会员'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/VipTTap')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/TopLeft/VipTTap')
    time.sleep(2)

@scene_app.scene(u'魔法屋-会员', [u'魔法屋-背包'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/BottomRight/BagBtn')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/BottomRight/BagBtn')
    time.sleep(2)

@scene_app.scene(u'魔法屋-背包', [u'关闭魔法屋-背包'], 20, '/AbstractRoot/UI Root/Camera/ShopBagPopUIPanel(Clone)/Root/close')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopBagPopUIPanel(Clone)/Root/close')
    time.sleep(2)

@scene_app.scene(u'关闭魔法屋-背包', [u'主界面'], 20, '/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/BottomRight/Return')
def dian(previous_nodes_find, previous_scene, scene_yourself):
    find_and_press('/AbstractRoot/UI Root/Camera/ShopUIPanel(Clone)/BottomRight/Return')
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

