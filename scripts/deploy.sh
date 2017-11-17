
#!/bin/sh
#!/usr/bin/expect -f
##apt-get install ssh

ls

cp run.py /home
chmod 777 run.py

cp run.sh /home
chmod 777 run.py

cp sample_commands.txt /home
chmod 777 run.py

cp list.txt /home
chmod 777 run.py

apk update

apk add openssh

apk add sshpass

apk add scp

sshpass -p 'Welcome@321' scp -o "StrictHostKeyChecking no" run.py hduser1@10.63.33.207:/home/hduser1
sshpass -p 'Welcome@321' scp -o "StrictHostKeyChecking no" run.sh hduser1@10.63.33.207:/home/hduser1
sshpass -p 'Welcome@321' scp -o "StrictHostKeyChecking no" sample_commands.txt hduser1@10.63.33.207:/home/hduser1
sshpass -p 'Welcome@321' scp -o "StrictHostKeyChecking no" list.txt hduser1@10.63.33.207:/home/hduser1


sshpass -p 'Welcome@321' ssh -o "StrictHostKeyChecking no" hduser1@10.63.33.207 <<!
ls /home/hduser1/*
. /home/hduser1/run.sh
# psql -a -f "/home/gpadmin/ftp/create_gp.sql"
##psql -c "CREATE schema trial"
##psql -c "CREATE TABLE trial.weather (city int, name varchar(10)) DISTRIBUTED BY (city)"
##psql -c "insert into trial.weather (city,name) values (1,'aaa')"
##psql -c "insert into trial.weather (city,name) values (2,'a1')"
!
