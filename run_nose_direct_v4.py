import os

py_exe_cmd = r'C:\Anaconda\python.exe'
#py_exe_cmd = r'C:\Python34\python.exe'

cmd = r'%s nosetests-script.py --with-xunit --xunit-file=direct_run.xml'%py_exe_cmd

os.system ( cmd )
