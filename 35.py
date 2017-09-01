import ftplib
import os
import socket

host = "ftp.scene.org/"
DIRN = '/incoming/ '
file = '1st_readme'


def main():
    try:
        f = ftplib.FTP(host)
    except (socket.error,socket.gaierror) as e:
        print "error: cannot reach %s" % host
        return
    print "connot to host %s" % host

    try:
        f.login()
    except ftplib.error_perm as e:
        print "error:cannot login anonymously"
        f.quit()
        return
    print "logged in as anonymous"

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print "error: connot cd to %s" % DIRN
        f.quit()
        return
    print "change to %s" %DIRN
    
    try:
        f.retrbinary("retr %s" % file,open(file,"wb".write))
    except ftplib.error_perm:
        print "error:cannot read file %s" %file
        os.unlink(file)

    else:
        print "donloaded %s to cwd" %file
    f.quit()
    return
if __name__ == '__main__':
    
    main()
