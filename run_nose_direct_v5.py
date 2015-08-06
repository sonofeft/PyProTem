import os, sys

py_exe_cmd = r'C:\Anaconda\python.exe'
#py_exe_cmd = r'C:\Python34\python.exe'

#print( 'sys.argv =',sys.argv )

cmd = r'%s nosetests-script.py --with-xunit --xunit-file=direct_run.xml'%py_exe_cmd

code = """if __name__ == '__main__':
    import sys
    from nose import run_exit
    nose_argv=[ '', '--with-xunit', '--xunit-file=direct_run.xml']
    sys.exit(run_exit(argv=nose_argv))
"""

cmd = '''%s -c """%s"""'''%(py_exe_cmd, code.replace('\n',';'))

os.system ( cmd )
