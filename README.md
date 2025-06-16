# Bigdata based Crypto price prediction model

`Author`:

| Name                 | Roll number| 
| -----------------    | ------------
|Arnav Baweja          |EMBAA24008    |
|Bhargav Pratim Datta  |EMBAA24010    |
|Bishwapriya Deb       |EMBAA2401I    |
|Nikhil Popli          |EMBAA24029    |
|Shradha Varshney      |EMBAA24044    |
|Suvangkar Saha        |EMBAA24052    |



## 1. How to run our project

1. Setup docker, docker-compose
2. Move to root directory of our repository
3. Run this command:
    `docker-compose up --build -d`

Then you can:

- Run command `docker-compose ps -a`: Check containers status
- Run command `docker-compose logs <container-name> -f`: Check `<container-name>` logs
- Run command `docker exec -it <container-name> bash`: Execute and interact with `<container-name>` terminal
- Browse `http://localhost:16010`: Check hbase information
- Browse `http://localhost:9870`: Check HDFS information
- Browse `http://localhost:8080`: Interact with Airflow Web UI
- Browse `http://localhost:5000`: View streaming chart

## 2. Our project

### 2.1. Tools

1. Docker
2. Python
3. Spark
4. Kafka
5. Hadoop HDFS
6. HBase
7. Mysql
8. Airflow
9. Flask
10. PowerBI


### 2.2. System Architecture
The architecture of our crypto price prediction system is structured into several key components: Data Ingestion, Streaming Processing, Batch Processing, Data Serving, and User Interface Applications such as a Flask web app and Power BI dashboard.


### 2.2.1. Data Ingestion Layer
This foundational layer is responsible for supplying raw cryptocurrency data to both the streaming and batch processing pipelines. It utilizes a Kafka Producer to continuously push incoming data to Kafka topics for further downstream consumption.


### 2.2.2. Streaming Layer
The streaming layer handles real-time data flow and predictive analytics. Its operational flow is as follows:

Kafka Consumer subscribes to live data streams.

A pre-trained prediction model is triggered to forecast prices one minute ahead.

Both the actual market price and the predicted value are written into an HBase database for immediate access and visualization.


### 2.2.3. Batch Processing Layer
The batch layer is responsible for historical data handling and long-term model training. It performs the following tasks:

Collects historical price data in its raw form and stores it in a HDFS Datalake and MySQL database.

Leverages PySpark for heavy data processing and loads the refined results into an HDFS Warehouse and MySQL for structured querying.

Periodically trains machine learning models using this curated data to improve future prediction accuracy.



### To automate these workflows, Apache Airflow is deployed to:

Run the data processing pipelines daily.

Trigger monthly model retraining cycles for continuous learning.

