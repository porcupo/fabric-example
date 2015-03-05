Examples of [Fabirc](http://www.fabfile.org/) fabfiles

Install with `pip install fabric`

Currently there is `fabfile.py`

See a list of available commands:
```bash
>:3 fab -l
Available commands:

bootstrap
chef_run
chef_zero_run
nuke_mysql
reboot
upgrade
```

You can then run any of the above:
```
fab -u djo -H host.example.com chef_run
```

* *-u*: ssh username
* *-H*: comma-separated list of hostnames to run on

NOTE: fabric does not process `~/.ssh/config`, at least by default
