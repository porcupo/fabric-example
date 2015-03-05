from fabric.api import run, sudo, task, put, env, execute
from urllib import urlopen

env.gateway = 'sshhost.example.com'
env.ssh_agent = True

@task
# basic command run
def test():
    run("ls -a")

@task
# put file (as root)
def cp_apt_sources():
    put("sources-digitalocean.list", "/etc/apt/sources.list", use_sudo=True)

@task
# upgrade packages
def upgrade():
    sudo("apt-get update")
    sudo("aptitude -y full-upgrade")

@task
# basic chef run
def chef_run():
    sudo("chef-client --once --no-color")

@task
# chef zero for testing
def chef_zero_run():
    sudo("su -c 'cd /tmp/chef && ./chef-client-localmode'")

@task
# viciously tear out any mysql installations
def nuke_mysql():
    sudo("dpkg -l | grep -E '(percona|galera|mysql)' | awk '{print $2}' | xargs apt-get -y --force-yes purge")
    sudo("find /var -iname '*mysql*' | xargs rm -vrf")
    sudo("find /etc -iname '*mysql*' | xargs rm -vrf")

@task
# return list of webdav entries (works?)
def webdav_read():
    objects = urlopen('http://coderepo.example.com/artifacts/api/').read().split()
    print(objects)

@task
# combined tasks
def full_bootstrap(zone):
    execute(cp_apt_sources)
    execute(upgrade)
    execute(chef_run)
