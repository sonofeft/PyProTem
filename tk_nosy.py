
"""
Watch for changes in all .py files. If changes, run nosetests.
"""
# pylint: disable=R0914, R0902, R0912, R0915

from __future__ import print_function
import sys
if sys.version_info < (3,):
    from future import standard_library
    standard_library.install_aliases()
    import tkFileDialog

#  Need to redefine object here
# pylint: disable=W0622
from builtins import object

import tkinter.font
#from tkinter import *
from tkinter import Menu, StringVar, Label, SUNKEN, SW, X, BOTTOM, Frame, NE,\
    BOTH, TOP, Button, W, LEFT, SE, Scrollbar, VERTICAL, Text, RIGHT, Y, END, Tk
import tkinter.filedialog

import platform
#import nose
#print( 'nose.__file__ =',nose.__file__ )
#print( ' sys.executable =', sys.executable)

from xml.etree import ElementTree as ET

import stat
import os, fnmatch


LICENSE = """
tk_nosy  Copyright (C) 2013-2015  Charlie Taylor
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""


__author__ = 'Charlie Taylor'
__copyright__ = 'Copyright (c) 2013 Charlie Taylor'
__license__ = 'GPL-3'  # see file LICENSE.TXT
__version__ = '1.0'
__email__ = "charlietaylor@users.sourceforge.net"
__status__ = "Development"  # "Prototype", "Development", or "Production"


#    I like extra spaces inside parens and sometimes camelCase
# pylint: disable=C0326
# pylint: disable=C0103

fileD = {} # key=file name, value=(size, modified time)
changedFileL = []

def walkLocate(pattern, topDir=os.curdir):
    """Locate all files matching supplied filename pattern in and below
    supplied topDir directory."""
    # pylint: disable=W0612
    for path, _dirL, fileL in os.walk(os.path.abspath(topDir)):

        if '.tox' in path.split(os.sep):
            #print 'Skipping',path
            continue
        for filename in fnmatch.filter(fileL, pattern):
            yield os.path.join(path, filename)

def numberOfChangedFiles( dirname ):
    """ Return number of .py files that have changed since last check."""
    del changedFileL[:]
    numFilesChanged = 0
    numFilesExamined = 0
    for f in walkLocate('*.py', topDir=dirname):
        numFilesExamined += 1
        size, mtime = fileD.get(f,(0,0))
        stats = os.stat (f)
        sizeNow, mtimeNow = stats[stat.ST_SIZE], stats[stat.ST_MTIME]
        if size!=sizeNow or mtime!=mtimeNow:
            numFilesChanged += 1
            changedFileL.append( f )
        fileD[f] = (sizeNow, mtimeNow)

    if numFilesExamined != len(fileD): # new or deleted file
        numFilesChanged += abs(numFilesExamined - len(fileD))
        fileD.clear()
    return numFilesChanged

def run_nosetests(numNosyCalls):
    """Run nosetests, create xml file of output, parse the xml file
       to determine the results.

       Return the results to the calling method.
    """

    #print 'Current Dir:',os.curdir
    if platform.system()=="Windows":
        nose_path = os.path.split( sys.executable )[0]
        full_nosetests_name = os.path.join( nose_path, 'Scripts', 'nosetests' )
    elif platform.system()=="Linux":
        if sys.version_info < (3,):
            #full_nosetests_name = '/usr/local/bin/nosetests'
            full_nosetests_name = 'nosetests'
        else:
            #full_nosetests_name = '/usr/local/bin/nosetests3'
            full_nosetests_name = 'nosetests3'

    else:
        print('EEEEEK... I do not know what to do.')


    print( 'full_nosetests_name =',full_nosetests_name)
    #print("Path at terminal when executing this file")
    #print("    " + os.getcwd() + "\n")
    #system_rtn = os.system (full_nosetests_name + ' --with-xunit')
    os.system (full_nosetests_name + ' --with-xunit')

    #print 'system_rtn = ',system_rtn
    #system_rtn = nose.run( argv=['nosetests', '-v', '--with-xunit'])
    #system_rtn = nose.main(argv=['nosetests', '-v', '--with-xunit'])

    #s = 'UNITTEST RUN# %i'%numNosyCalls
    s = 'tk_nosy UNITTEST RUN# %i'%numNosyCalls
    outputTextL = [ s.center(40,'_') + '\n\n']

    tree = ET.parse('nosetests.xml')

    numFailed = 0
    numErrors = 0
    numSkipped = 0
    numTests = 0

    for e in tree.getiterator('testsuite'):
        #print '%i)'%ie,e.items()
        numErrors += int( e.get('errors',0) )
        numFailed += int( e.get('failures',0) )
        numSkipped += int( e.get('skip',0) )
        numTests += int( e.get('tests',0) )

    numPassed = numTests - numFailed - numErrors - numSkipped

    iText = 1
    for testcase in tree.getiterator('testcase'):
        #print 'len(testcase)=',len(testcase)

        label = ''
        if len(testcase) > 0:
            title = "{Item #%i} "%iText + testcase.get('name','')

            ssL = []
            for  child in testcase:
                if not label:
                    label = child.get('type','')

                sL = child.text.strip().split('\n')
                for isL,s in enumerate(sL):
                    sL[isL] = s.rstrip()

                ssL.append( sL )
                print()
            print(title + ', %s'%label)
            outputTextL.append( title + ', %s'%label + '\n' )
            for sL in ssL:
                #print '\n'.join(sL)
                outputTextL.append( '\n'.join(sL) + '\n\n' )
            iText += 1

    passedAllTests = (numTests - numSkipped == numPassed) and (numFailed==0) and (numErrors==0)
    return passedAllTests, numPassed, numFailed, numErrors, numSkipped, outputTextL


class _Tk_Nosy(object):
    """This class is the tkinter GUI object"""
    def __init__(self, master):
        self.dirname = os.path.abspath( os.curdir )

        self.initComplete = 0
        self.master = master
        self.x, self.y, self.w, self.h = -1,-1,-1,-1

        # bind master to <Configure> in order to handle any resizing, etc.
        # postpone self.master.bind("<Configure>", self.Master_Configure)
        self.master.bind('<Enter>', self.bindConfigure)

        self.menuBar = Menu(master, relief = "raised", bd=2)


        top_Directory = Menu(self.menuBar, tearoff=0)
        top_Directory.add("command", label = "Change Dir", command = self.menu_Directory_Change_Dir)
        self.menuBar.add("cascade", label="Directory", menu=top_Directory)


        #top_Snippet = Menu(self.menuBar, tearoff=0)

        self.menuBar.add("command", label = "Run", command = self.menu_Run)

        master.config(menu=self.menuBar)

        # make a Status Bar
        self.statusMessage = StringVar()
        self.statusMessage.set(self.dirname)
        self.statusbar = Label(self.master, textvariable=self.statusMessage, bd=1, relief=SUNKEN)
        self.statusbar.pack(anchor=SW, fill=X, side=BOTTOM)

        self.statusbar_bg = self.statusbar.cget('bg') # save bg for restore

        myFont = tkinter.font.Font(family="Arial", size=12, weight=tkinter.font.BOLD)
        self.statusbar.config( font=myFont )


        frame = Frame(master)
        frame.pack(anchor=NE, fill=BOTH, side=TOP)

        self.Pass_Fail_Button = Button(frame,text="Pass/Fail Will Be Shown Here",
                                       image="", width="15", background="green",
                                       anchor=W, justify=LEFT, padx=2)
        self.Pass_Fail_Button.pack(anchor=NE, fill=X, side=TOP)
        self.Pass_Fail_Button.bind("<ButtonRelease-1>", self.Pass_Fail_Button_Click)

        #self.master.title("tk_nosy")
        self.master.title('Python %s.%s.%s '%sys.version_info[:3])
        self.oscillator = 1 # animates character on title
        self.oscillator_B = 0 # used to return statusbar to statusbar_bg

        self.lbframe = Frame( frame )
        self.lbframe.pack(anchor=SE, side=LEFT, fill=BOTH, expand=1)

        scrollbar = Scrollbar(self.lbframe, orient=VERTICAL)
        self.Text_1 = Text(self.lbframe, width="80", height="24", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Text_1.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Text_1.pack(side=LEFT, fill=BOTH, expand=1)

        self.master.resizable(1,1) # Linux may not respect this

        self.numNosyCalls = 0
        self.need_to_pick_dir = 1

        if len(sys.argv)>1:
            #  I don't care what the exception is, if there's a problem, bail
            # pylint: disable=W0702
            try:
                dirname = os.path.abspath( sys.argv[1] )
                self.try_change_to_new_dir( dirname )
            except:
                pass # let Alarm force dir selection
        else:
            try:
                if os.path.isdir(os.path.join( self.dirname, 'tests' )):
                    self.try_change_to_new_dir( self.dirname )
            except:
                pass # let Alarm force dir selection
                

        print(LICENSE)
        self.Alarm()


    def try_change_to_new_dir(self, dirname):
        """A legal abspath will switch to dirname."""
        #  I don't care what the exception is, if there's a problem, bail
        # pylint: disable=W0702
        if dirname:
            try:
                dirname = os.path.abspath( dirname )
            except:
                return # let Alarm force dir selection
        else:
            return

        self.dirname = dirname
        print('Selected dirname    =',dirname)
        fileD.clear()
        os.chdir( self.dirname )
        self.reset_statusbar_bg()
        self.need_to_pick_dir = 0

        #with open(NOSY_USER_DATA_FILE, 'w') as text_file:
        #    text_file.write( self.dirname )

        self.numNosyCalls = 0


    def reset_statusbar_bg(self):
        """Return status bar to default state"""
        self.statusbar.config(bg=self.statusbar_bg)
        self.statusMessage.set(self.dirname)

    def set_statusbar_bg(self, c):
        """Set status bar to show new color and message"""
        self.statusbar.config(bg=c)
        self.oscillator_B = 1 # will return to initial color after a few cycles

    def menu_Directory_Change_Dir(self):
        """Menu selection to set directory in which to run nosetests"""
        dirname = self.AskDirectory( title='Choose Directory For Nose Tests', initialdir=".")
        if dirname:
            self.try_change_to_new_dir( dirname )
        # >>>>>>insert any user code below this comment for section "menu_Directory_Change_Dir"
        # replace, delete, or comment-out the following
        print("called menu_Directory_Change_Dir")


    def menu_Run(self):
        """User initiates a nosetests run, not file change detection."""
        print("called menu_Run")
        self.callNosy()

    def callNosy(self):
        """Run nosetests and display results"""
        self.numNosyCalls += 1
        self.Text_1.delete(1.0, END)

        # turn indicator button gray while running the tests
        myFont = tkinter.font.Font(family="Arial", size=12, weight=tkinter.font.BOLD)
        self.Pass_Fail_Button.config(background="#999999", text='TESTING...', font=myFont)
        self.master.update()
        self.master.update_idletasks()

        # pylint: disable=W0201
        self.passedAllTests, numPassed, numFailed, numErrors, numSkipped, outputTextL = \
            run_nosetests(self.numNosyCalls)

        max_len_s = 42
        num_lines = 1
        for s in outputTextL:
            self.Text_1.insert(END, s)
            sL = s.split('\n')
            for ss in sL:
                max_len_s = max(max_len_s, len(ss))
                num_lines += 1


        if self.numNosyCalls % 2:
            myFont = tkinter.font.Font(family="Arial", size=12, weight=tkinter.font.BOLD)
        else:
            myFont = tkinter.font.Font(family="Arial", size=12)

        if self.passedAllTests:
            s = 'PASSED'
            if numPassed > 1:
                s = 'PASSED ALL %i TESTS'%numPassed
            elif numPassed == 1:
                s = 'PASSED ONE TEST'


            bg="#00ff00"
            if numSkipped==1:
                s = 'passed with 1 SKIP'
                bg = "#00cc00"
            elif numSkipped > 1:
                s = 'passed with %i SKIPS'%numSkipped
                bg = "#00cc00"
            elif numPassed==0:
                s = 'No Tests Found'
                bg="#ff8000"
            self.Pass_Fail_Button.config(background=bg, text=s, font=myFont)

            #self.master.geometry('200x50')
        else:
            s = 'FAILED %i, ERRORS %i, SKIP %i, PASSED %i'%(numFailed,
                                                            numErrors, numSkipped, numPassed)
            self.Pass_Fail_Button.config(background="#ff0000", text=s, font=myFont)
            #self.master.geometry('516x385')


        # Show list of files being watched.
        #self.Text_1.insert(END, '_'*40+'\n')
        self.Text_1.insert(END, 'WATCHED *.py FILES'.center(40,'_') + '\n' )
        self.Text_1.insert(END, '%s%s..\n\n'%(self.dirname,os.path.sep) )
        num_lines += 3

        len_dirname = len( self.dirname )

        keyL = list(fileD.keys())
        keyL.sort()
        lastdir = ''
        for key in keyL:
            dn = os.path.dirname( key )
            if dn != lastdir:
                self.Text_1.insert(END, '..'+dn[len_dirname:] + '\n')
                max_len_s = max(max_len_s, len(dn)+1)
                lastdir = dn
                num_lines += 1
            s = '    ' +os.path.basename( key )
            self.Text_1.insert(END, s + '\n')
            max_len_s = max(max_len_s, len(s)+1)
            num_lines += 1

        self.Text_1.config(width=max_len_s)
        self.Text_1.config(height=min(40, num_lines))
        self.master.winfo_toplevel().wm_geometry("")


    def bindConfigure(self, event):
        """Part of goofy main window setup in tkinter."""
        #  tkinter requires arguments, but I don't use them
        # pylint: disable=W0613
        if not self.initComplete:
            self.master.bind("<Configure>", self.Master_Configure)
            self.initComplete = 1



    # return a string containing directory name
    def AskDirectory(self, title='Choose Directory', initialdir="."):
        """Run pop-up menu for user to select directory."""
    #    This is not an error
    # pylint: disable=E1101

        if sys.version_info < (3,):
            dirname = tkFileDialog.askdirectory(parent=self.master,
                                                initialdir=initialdir,title=title)
        else:
            dirname = tkinter.filedialog.askdirectory(parent=self.master,
                                                      initialdir=initialdir,title=title)
        return dirname # <-- string


    def Master_Configure(self, event):
        """Part of tkinter main window initialization"""

        if event.widget != self.master:
            if self.w != -1:
                return
        x = int(self.master.winfo_x())
        y = int(self.master.winfo_y())
        w = int(self.master.winfo_width())
        h = int(self.master.winfo_height())
        if (self.x, self.y, self.w, self.h) == (-1,-1,-1,-1):
            self.x, self.y, self.w, self.h = x,y,w,h


        if self.w!=w or self.h!=h:
            #print "Master reconfigured... make resize adjustments"
            self.w=w
            self.h=h

    def Pass_Fail_Button_Click(self, event):
        """Place-holder routine for user clicking Pass/Fail Button"""
        pass

    # alarm function is called after specified number of milliseconds
    def SetAlarm(self, milliseconds=1000):
        """Reinitialize tkinter alarm mechanism as well as update seconds
           counter in main window title bar.
        """
        self.master.after( milliseconds, self.Alarm )

        self.oscillator += 1
        if self.oscillator > 5:
            self.oscillator = 0

        if self.oscillator_B>0:
            self.oscillator_B += 1
        if self.oscillator_B>5:
            self.oscillator_B = 0
            self.reset_statusbar_bg()

        pad = '|'*self.oscillator

        #self.master.title("%i) tk_nosy "%self.numNosyCalls + pad )
        s = '%s.%s.%s '%sys.version_info[:3]
        self.master.title('%i) Python %s '%(self.numNosyCalls , s + pad ))


    def Alarm(self):
        """Look for changed files every second, then reset alarm"""
        if self.need_to_pick_dir:
            dirname = self.AskDirectory( title='Choose Directory For Nose Tests', initialdir=".")
            self.try_change_to_new_dir( dirname )

        #first call to numberOfChangedFiles will be > 0 if any .py files are found
        elif numberOfChangedFiles( self.dirname ) > 0: # or self.numNosyCalls==0
            self.callNosy()

        self.SetAlarm()

def main():
    """Run Main Window"""
    root = Tk()
    _Tk_Nosy(root)
    root.mainloop()


if __name__ == '__main__':
    main()
