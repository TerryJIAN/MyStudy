請先安裝docker
開啟文件更改IP

在運行docker-compose .yaml

指令 docker-compose up -d



常用指令

查看topic
./bin/kafka-topics.sh --list --zookeeper zookeeper:2181

新增topic
./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic testTopic

刪除topic
./bin/kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic Topic_Name

producer
./bin/kafka-console-producer.sh --broker-list kafka:9092 --topic Topic_Name

consumer
./bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic testTopic --from-beginning
