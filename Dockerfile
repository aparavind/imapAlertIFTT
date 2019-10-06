FROM centos/python-27-centos7
COPY getImapHeader.py getImapHeader.py
COPY imaplib_connect.py imaplib_connect.py
COPY imaplib_idlewait.py imaplib_idlewait.py
COPY settings.ini settings.ini