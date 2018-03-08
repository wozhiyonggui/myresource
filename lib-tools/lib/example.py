# -*- coding: UTF-8 -*-
from SceneRunner import * #引用框架

# 标识场景模块名字
scene_module_name = u'框架测试'

MAINLAYER = '/AbstractRoot/Canvas/MainPostion/MainLayer'
WARLAYER = '/AbstractRoot/Canvas/WarPostion/WarLayer'

@scene_app.scene_start(u'入口', [u'主界面'], 24, '/AbstractRoot/Canvas/MainPostion/EnterLayer/BeginLayer/BtnEnter')
def enter(nodes_find, previous_scene, scene_yourself):
    '''
    scene[ | _start | _end ]分别明确一般场景开始场景和结束场景
    参数为 本场景名 下游场景列表 进入本场景最大等待时间 本场场景xpath表达式
    :param nodes_find: 注入参数 本场景节点xpath对象
    :param previous_scene: 注入参数 上一场景名
    :param scene_yourself: 注入参数 本场景名
    :return:
    '''
    find_and_press('/AbstractRoot/Canvas/MainPostion/EnterLayer/BeginLayer/BtnEnter')


@scene_app.scene_end(u'主界面', [], 5, '/AbstractRoot/Canvas/MainPostion/MainLayer/Advent//Advent/Event')
def mymain(nodes_find, previous_scene, scene_yourself):
    find_and_press_random(MAINLAYER + '/Advent//Advent/Event')
    find_and_press('/AbstractRoot/Canvas/MainPostion/MainLayer/Advent//Advent/Event/EnterBtn', 0)
    # 日志，可选择log level
    runner_logger(u'日志log日志log日志log')
    # 断言，传入Excel标识列
    runner_assert(u'仙女祝福-1', False,False)#（标识列，条件判断，False不截图）
    runner_assert(u'仙女祝福-2', True)#（标识列，判断条件，默认是截图开启）

if __name__ == '__main__':
    # 本地调试使用，请传入用例Excel路径，Excel不支持中文文件名,可选择使用Debug日志和截图地址
    scene_app.run('yyzy-case.xlsx', log_level=logging.DEBUG)
    # 生成Junit格式xml
    scene_app.output_junit('./xxx.xml')

