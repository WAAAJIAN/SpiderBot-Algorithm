import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/spider/SpiderBot-Algorithm_ros2_ws/install/gwen'
