"""Small program to clear cache and cookies from all applications, not just browsers. (Mac)
This program saves time from having to go into the terminal and manually do it. It's
written to be run in the Desktop, otherwise change ../Library"""

from subprocess import Popen, PIPE

pr = Popen(['/bin/bash'], stdin=PIPE)
p = pr.stdin
p.write('cd ../Library\n') #gets into Library from Desktop
p.write('rm -R Cookies\n') #deletes Cookies directory
p.write('rm -R Caches\n')  #deletes possible Caches

#sometimes it will not let you delete certain caches (outputs permission denied)
#run (using Python 2) once every couple weeks or so
