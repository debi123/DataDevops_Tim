#!/bin/sh

##cp spark-env.sh /home/build-spark/rootfs/usr/spark-2.2.0/conf
##chmod 777 spark-env.sh

cp trial.csv /home
chmod 777 trial.csv

##. /opt/hbase-server > a.out

apt-get -y update

apt-get install -y openssh-server

/opt/hbase/bin/start-hbase.sh

/opt/hbase/bin/hbase-daemons.sh start zookeeper

/opt/hbase-server


##/opt/hbase/bin/start-hbase.sh

# /opt/hbase/bin/zookeepers.sh start

##hbase shell

hbase shell ./sample_commands.txt

hbase shell ./count.txt > count_src.txt

##echo "list" | hbase shell

##ssh gpadmin@10.63.33.203

##ls /*

##cd /home/build-spark

##ls /home/build-spark/*

###ls /home/build-spark/rootfs/usr/hadoop-2.7.3/*

###export HADOOP_HOME=/home/build-spark/rootfs/usr/hadoop-2.7.3
###export PATH=$PATH:/home/build-spark/rootfs/usr/hadoop-2.7.3/bin
###export SPARK_DIST_CLASSPATH=/home/build-spark/rootfs/usr/hadoop-2.7.3/bin/hadoop


##ls /home/build-spark/rootfs/usr/jdk1.8.0_131/*
##ls /home/build-spark/rootfs/usr/java/*

##export JAVA_HOME=/usr/jdk1.8.0_131
##export PATH=$PATH:/usr/jdk1.8.0_131/bin

##ls /home/build-spark/rootfs/*

##ls /home/build-spark/rootfs/usr/spark-2.2.0/*

###hadoop version

###cd /home/build-spark/rootfs/usr/spark-2.2.0/bin

###pyspark

spark-submit  --packages com.hortonworks:shc-core:1.1.1-2.1-s_2.11 --repositories http://repo.hortonworks.com/content/groups/public/ run.py

hbase shell ./list.txt

##spark-submit 

###/rootfs/usr/spark-2.2.0/bin/spark-submit run.py


##3spark-submit run.py

###hbase shell

##cd /opt/phoenix-4.4.0-HBase-1.1-bin/bin

##./sqlline.py localhost:/hbase-unsecure

# cd /home/build-hbase

# ls /*
