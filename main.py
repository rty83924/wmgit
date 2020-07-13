import git
import os
from config import config

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    user = config.user
    passwd = config.passwd               
    tbuser = config.tbuser
    tbpasswd = config.tbpasswd
    domain = config.domain
    worktree = config.worktree
    gitpath = config.gitpath
    conf_path = config.conf_path
    series = config.series
    office = config.office
    while True:
        pro = '%s' % git.WM().pro()
        app = git.WM().apps()
        #url = list()
        for j in app:
            if j == 'tbonline':
                url = ('http://{u}:{p}@{d}/a168/{a}.git'.format(u=tbuser, p=tbpasswd, a=j, d=domain))
            elif j == 'ag':
                url = ('http://{u}:{p}@{d}/gala/a168-{s}.git'.format(u=user, p=passwd, r=pro, a=j, d=domain, s=series))
            else:
                url = ('http://{u}:{p}@{d}/gala/{a}-{s}.git'.format(u=user, p=passwd, r=pro, a=j, d=domain, s=series))
            gitdownload = git.gitdownload(url=url, project=pro, app=j, gitpath=gitpath, worktree=worktree, office=office)
            gitdownload.clone()
            gitdownload.checkout()
            gitdownload.changepath()
                #print(url)
        rsync_conf = git.rsync_conf(conf_path=conf_path, app=app, project=pro)
        rsync_conf.folder()
        rsync_conf.hosts()
        while True:
            b = str(input('其他專案? #yes/no \nEnter: '))
            if b == 'yes':
                break
            elif b == 'no':
                exit()
            else:
                print("請輸入 yes/no")

