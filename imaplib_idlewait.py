import imaplib
import pprint
import imaplib_connect
import subprocess

imaplib.Debug = 4
c = imaplib_connect.open_connection()
try:
    c.select('INBOX', readonly=True)
    c.send("%s IDLE\r\n"%(c._new_tag()))
    print ">>> waiting for new mail..."
    while True:
      line = c.readline().strip();
      print line
      if line.startswith('* BYE ') or (len(line) == 0):
        print ">>> leaving..."
        break
      if line.endswith('EXISTS'):
        x = line.split(' ')[1]
        print "Recieved the " + x
        data = subprocess.Popen(["/usr/bin/python", "/home/aravind/projects/imap/getImapHeader.py",x], shell=None,stdin=None, stdout=None, stderr=None, close_fds=True)
finally:
    try:
        print ">>> closing..."
        c.close()
    except:
        pass
    c.logout()
