import os


def test_info_file_created():
    """This tests if request log file is created"""
    logpath = os.path.abspath('app/logs/info.log')
    print(logpath)
    assert os.path.exists(logpath) == True

def test_debug_file_created():
    """This tests if request log file is created"""
    debugpath = os.path.abspath('app/logs/debug.log')
    print(debugpath)
    assert os.path.exists(debugpath) == True