import os, sys

py_exe_cmd = r'C:\Anaconda\python.exe'
#py_exe_cmd = r'C:\Python34\python.exe'

code = """import sys;from nose import run_exit;sys.exit(run_exit(argv=[ '', '--with-xunit', '--xunit-file=direct_run.xml']))"""

cmd = '''%s -c "%s"'''%(py_exe_cmd, code)

os.system ( cmd )

#os.popen(cmd).read()
