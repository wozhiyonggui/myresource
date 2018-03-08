# -*- coding: UTF-8 -*-
"""

"""
__author__ = 'Steven howtoesc@gmail.com'

from sqlobject import *


class TestProject(SQLObject):
    Name = StringCol()
    # TODO Need More
    TestJobs = MultipleJoin('TestJob')


class TestJob(SQLObject):
    Name = StringCol()
    JenkinsURL = StringCol()
    TestProject = ForeignKey('TestProject')
    TestRunRecords = MultipleJoin('TestRunRecord')


class TestRunRecord(SQLObject):
    Name = StringCol()
    Info = StringCol()
    Start = DateTimeCol()
    End = DateTimeCol()
    TestJob = ForeignKey('TestJob')
    TestCaseModules = MultipleJoin('TestCaseModule')


class TestCaseModule(SQLObject):
    Name = StringCol()
    TestRunRecord = ForeignKey('TestRunRecord')
    TestCases = MultipleJoin('TestCase')


class TestCase(SQLObject):
    Name = StringCol()
    TestCaseModule = ForeignKey('TestCaseModule')
    TestStepsSets = MultipleJoin('TestStepsSet')


class TestStepsSet(SQLObject):
    Name = StringCol()
    Steps = StringCol()
    ExpectedResult = StringCol()
    TestCase = ForeignKey('TestCase')
    TestRealResults = MultipleJoin('TestRealResult')


class TestRealResult(SQLObject):
    SceneModule = StringCol()
    Scene = StringCol()
    LastScene = StringCol()
    Assert = BoolCol()
    Start = DateTimeCol()
    During = IntCol()
    TestScreenshotsID = StringCol()
    FileName = StringCol()
    LineNumber = IntCol()
    FunctionName = StringCol()
    Line = StringCol()
    TestStepsSet = ForeignKey('TestStepsSet')


class PreRecord_CPU(SQLObject):
    T = DateTimeCol()
    V = FloatCol()
    TestRunRecord = ForeignKey('TestRunRecord')


class PreRecord_JIF(SQLObject):
    T = DateTimeCol()
    V = FloatCol()
    TestRunRecord = ForeignKey('TestRunRecord')


class PreRecord_Net(SQLObject):
    T = DateTimeCol()
    Transmitted = IntCol()
    Transmitted = IntCol()
    TestRunRecord = ForeignKey('TestRunRecord')


class PreRecord_PSS(SQLObject):
    T = DateTimeCol()
    Total = IntCol()
    Dalvik = IntCol()
    Native = IntCol()
    TestRunRecord = ForeignKey('TestRunRecord')


class PreRecord_PRI(SQLObject):
    T = DateTimeCol()
    Total = IntCol()
    Dalvik = IntCol()
    Native = IntCol()
    TestRunRecord = ForeignKey('TestRunRecord')


class PreRecord_FPS(SQLObject):
    T = DateTimeCol()
    V = IntCol()
    TestRunRecord = ForeignKey('TestRunRecord')


def connect_to_db(uri):
    connection = connectionForURI(uri)
    sqlhub.processConnection = connection
    for i in [TestProject, TestJob, TestRunRecord, TestCaseModule, TestCase, TestStepsSet, TestRealResult,
              PreRecord_FPS, PreRecord_PSS, PreRecord_PRI, PreRecord_Net, PreRecord_JIF, PreRecord_CPU]:
        i.createTable(ifNotExists=True)


if __name__ == '__main__':
    connect_to_db('mysql://root:!QAZ2wsx@192.168.93.96/practice?debug=1&use_unicode=1&charset=utf8')

    # print TestRealResult.sqlmeta.columnDefinitions
