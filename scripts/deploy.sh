
#!/bin/sh
#!/usr/bin/expect -f
##apt-get install ssh

ls

cp run.py /home
chmod 777 run.py

apk update

apk add openssh

apk add sshpass

apk add scp

sshpass -p 'Welcome@321' scp -o "StrictHostKeyChecking no" run.py hduser1@10.63.33.207:/home/hduser1


sshpass -p 'Welcome@321' ssh -o "StrictHostKeyChecking no" hduser1@10.63.33.207 <<!
ls /home/hduser1/*
# psql -a -f "/home/gpadmin/ftp/create_gp.sql"
##psql -c "CREATE schema trial"
##psql -c "CREATE TABLE trial.weather (city int, name varchar(10)) DISTRIBUTED BY (city)"
##psql -c "insert into trial.weather (city,name) values (1,'aaa')"
##psql -c "insert into trial.weather (city,name) values (2,'a1')"
!
