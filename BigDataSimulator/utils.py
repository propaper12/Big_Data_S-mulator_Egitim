# utils.py
import graphviz

# --- 1. ARAYÜZ METİNLERİ ---
UI_TEXTS = {
    "en": {
        "sidebar_title": "Stack Builder",
        "select_instr": "Select components from each layer below:",
        "generate_btn": "✨ Auto-Generate Architecture",
        "reset_btn": "🗑️ Clear All",
        "manifest": "📝 Pipeline Manifest",
        "success_gen": "Architecture generated with {n} components.",
        "warning_no_tech": "Please select at least 2 technologies.",
        "error_missing_dep": "❌ **Missing Dependency:** `{tech}` requires `{dep}` to function.",
        "layer_ingest": "Ingestion Layer",
        "layer_store": "Storage / Lake Layer",
        "layer_proc": "Processing / Transformation",
        "layer_db": "Serving / Warehouse / NoSQL",
        "layer_bi": "BI / Visualization Layer",
        "orch_note": "Orchestration & Infrastructure",
        "modernity": "Status",
        "doc_link": "Official Docs",
        "dependency": "⚠️ Dependency Warning"
    },
    "tr": {
        "sidebar_title": "Yığın Oluşturucu",
        "select_instr": "Aşağıdaki katmanlardan bileşenlerinizi seçin:",
        "generate_btn": "✨ Otomatik Mimari Oluştur",
        "reset_btn": "🗑️ Hepsini Temizle",
        "manifest": "📝 Mimari Özeti",
        "success_gen": "{n} bileşen ile mimari oluşturuldu.",
        "warning_no_tech": "Lütfen en az 2 teknoloji seçin.",
        "error_missing_dep": "❌ **Eksik Bağımlılık:** `{tech}` teknolojisinin çalışması için `{dep}` gereklidir.",
        "layer_ingest": "Veri Alım (Ingestion) Katmanı",
        "layer_store": "Depolama / Göl Katmanı",
        "layer_proc": "İşleme / Dönüştürme Katmanı",
        "layer_db": "Veritabanı / Ambar / NoSQL",
        "layer_bi": "BI / Görselleştirme Katmanı",
        "orch_note": "Orkestrasyon ve Altyapı",
        "modernity": "Durum",
        "doc_link": "Resmi Doküman",
        "dependency": "⚠️ Bağımlılık Uyarısı"
    }
}

LAYER_PRIORITY = {
    "Ingestion": 1, "Storage": 2, "Lakehouse": 2,
    "Processing": 3, "Databases": 4, "Serving/BI": 5,
    "Orchestration": 0, "AI/ML": 4
}

DEPENDENCY_RULES = {
    "Kafka": ["Zookeeper"], "Hadoop MR": ["HDFS", "YARN"], "ClickHouse": ["Zookeeper"],
    "Delta Lake": ["Spark"], "Airflow": ["PostgreSQL"], "HBase": ["HDFS", "Zookeeper"],
    "Hive": ["HDFS", "Hadoop MR"], "Flink": ["Zookeeper"], "dbt": ["Snowflake"],
    "Kubernetes": ["Docker"], "Ozone": ["Hadoop MR"], "Trino": ["S3"],
    "Kubeflow": ["Kubernetes"], "Storm": ["Zookeeper"], "Spark MLlib": ["Spark"],
    "cAdvisor": ["Docker"], "Kibana": ["Elasticsearch"], "Pulsar": ["Zookeeper"],
    "Debezium": ["Kafka"], "Sqoop": ["Hadoop MR"] # Yeni Kurallar
}
# --- DEVASA TEKNOLOJİ ANSİKLOPEDİSİ ---
TECH_STACK = {
"Ingestion": {
        "Kafka": {
            "desc": {"en": "Distributed Event Streaming.", "tr": "Dağıtık Olay Akış Platformu."},
            "detail": {
                "en": """### 1. Definition
Apache Kafka is an open-source, distributed event streaming platform developed for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

### 2. Core Purpose
The primary goal is to process large volumes of data streams in real-time with high throughput and low latency. Unlike traditional queues, it persists data on disk, reducing coupling between systems.

### 3. Architecture
Kafka operates on a distributed "Commit Log" logic.
* **Write:** Data producers send data to the Kafka cluster.
* **Storage:** Kafka keeps this data on disk sequentially.
* **Read:** Consumers can read data from any point in the stream.

### 4. Components
Producer, Consumer, Broker, Topic, Partition, Offset, Consumer Group, ZooKeeper/KRaft.

### 5. Use Cases
Log Aggregation, Stream Processing, Event Sourcing.""",
                "tr": """### 1. Tanım
Apache Kafka; yüksek performanslı veri hatları, akış analitiği ve veri entegrasyonu için geliştirilmiş; açık kaynaklı, dağıtık bir olay akış platformudur.

### 2. Temel Amaç
Büyük hacimli veri akışlarını gerçek zamanlı olarak, yüksek işleme kapasitesi ve düşük gecikme ile işlemektir. Verileri bellekte değil diskte kalıcı saklar.

### 3. Mimari ve Çalışma Prensibi
Kafka, dağıtık bir "Commit Log" (İşlem Günlüğü) mantığıyla çalışır. Veriler, sıralı ve değiştirilemez kayıtlar olarak diske yazılır.
* **Yazma:** Veri üreticileri, veriyi Kafka kümesine gönderir.
* **Saklama:** Kafka bu veriyi konfigüre edilen süre boyunca diskte tutar.
* **Okuma:** Tüketiciler, kaldıkları yerden veriyi okuyabilirler.

### 4. Temel Bileşenler
Producer, Consumer, Broker, Topic (Konu), Partition (Bölüm), Offset, Consumer Group, ZooKeeper/KRaft.

### 5. Kullanım Alanları
Log Toplama, Akış İşleme, Event Sourcing, Mikroservis İletişimi."""
            },
            "link": "https://kafka.apache.org/", "modern": True, "dep": "Zookeeper",
            "code": "producer.send('my-topic', b'Hello World')"
        },
        "Redpanda": {
            "desc": {"en": "C++ Kafka Alternative.", "tr": "Modern C++ Kafka Alternatifi."},
            "detail": {
                "en": """### 1. Definition
Redpanda is a Kafka-compatible streaming platform written in C++. It utilizes a thread-per-core architecture to bypass JVM latency.

### 2. Core Purpose
To maintain high performance while eliminating ZooKeeper dependency and JVM complexity.

### 3. Architecture
Uses Seastar framework for thread-per-core architecture. No Zookeeper (uses internal Raft).""",
                "tr": """### 1. Tanım
Redpanda; modern donanımlar için optimize edilmiş, C++ ile yazılmış, Kafka API uyumlu, yüksek performanslı bir olay akış platformudur.

### 2. Temel Amaç
Kafka'nın sunduğu yüksek veri işleme kapasitesini korurken, ZooKeeper ve JVM karmaşıklığını ortadan kaldırmaktır.

### 3. Mimari
Thread-per-Core mimarisini kullanır. JVM üzerinde çalışmaz, doğrudan donanıma erişir. Kendi içinde Raft algoritmasını barındırır."""
            },
            "link": "https://redpanda.com/", "modern": True, "dep": None,
            "code": "docker run -d --name redpanda -p 9092:9092 vectorized/redpanda start"
        },
        "Logstash": {
            "desc": {"en": "Server-side Data Pipeline.", "tr": "Sunucu Taraflı Veri İşleme Hattı."},
            "detail": {
                "en": """### 1. Definition
Logstash is an open-source server-side data processing pipeline that ingests data from multiple sources simultaneously, transforms it, and then sends it to a "stash" like Elasticsearch. Part of the ELK Stack.

### 2. Core Purpose
To normalize data from different sources (especially logs) into a single format and make it analyzable. It uses "Grok" filters to parse unstructured text into structured fields.

### 3. Architecture
It uses a three-stage pipeline:
* **Input:** Ingests data (File, Syslog, Kafka, Http).
* **Filter:** Processes, enriches, and formats data (The strongest part).
* **Output:** Writes data to the destination (Elasticsearch, Email, File).

### 4. Key Components
* **Pipeline:** Definition of data flow.
* **Grok:** Filter that parses log lines using Regex patterns.
* **Plugins:** Hundreds of input, filter, and output plugins.

### 5. Use Cases
ELK Stack logging, Security data (SIEM) enrichment.

### 6. Pros and Cons
* **Pros:** Powerful transformation (Grok), Flexibility.
* **Cons:** Resource Consumption (JVM based, high RAM usage), Performance bottlenecks in high traffic.""",
                "tr": """### 1. Tanım
Logstash; Elastic (ELK) yığınının bir parçası olan, veriyi anında toplayan, dönüştüren ve istenilen hedefe ("stash") gönderen, sunucu taraflı bir açık kaynaklı veri işleme hattıdır.

### 2. Temel Amaç
Farklı kaynaklardan gelen verileri (özellikle logları) tek bir formatta normalize etmek ve analiz edilebilir hale getirmektir. "Grok" filtreleri sayesinde karmaşık yapıdaki metinleri anlamlı alanlara böler.

### 3. Mimari ve Çalışma Prensibi
Üç aşamalı bir işlem hattı kullanır:
* **Input:** Veriyi alır (Dosya, Syslog, Kafka, Http vb.).
* **Filter:** Veriyi işler, zenginleştirir veya formatlar.
* **Output:** Veriyi hedefe yazar (Elasticsearch, Email, File).

### 4. Temel Bileşenler
Pipeline, Grok (Regex filtresi), Eklentiler (Plugins).

### 5. Kullanım Alanları
ELK Stack log ayrıştırma, SIEM verilerinin zenginleştirilmesi.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Güçlü Dönüşüm, Esneklik.
* **Dezavantajlar:** Kaynak Tüketimi (Java tabanlıdır, fazla RAM tüketir)."""
            },
            "link": "https://www.elastic.co/logstash", "modern": False, "dep": None,
            "code": """# logstash.conf
input {
  file { path => "/var/log/syslog" }
}
filter {
  grok { match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname}" } }
}
output {
  elasticsearch { hosts => ["localhost:9200"] }
}"""
        },
        "Fluentd": {
            "desc": {"en": "Unified Logging Layer.", "tr": "Birleşik Loglama Katmanı."},
            "detail": {
                "en": """### 1. Definition
Fluentd is an open-source, cloud-native data collector for unified logging. It is the standard logger for Kubernetes environments (CNCF project).

### 2. Core Purpose
To solve the "n x m" complexity between data sources and backend systems; structuring log data in JSON format and transporting it.

### 3. Architecture
Written in C and Ruby. Consumes very few resources. Uses a Pluggable architecture. Routes data using **Tags**.
* **Input:** Collects data.
* **Parser:** Converts data to JSON.
* **Buffer:** Buffers data against network failures.
* **Output:** Sends data to destination.

### 4. Key Components
Input Plugins, Parser, Buffer, Output Plugins.

### 5. Use Cases
Kubernetes & Docker logging, IoT data collection (Fluent Bit).

### 6. Pros and Cons
* **Pros:** Lightweight, Cloud-Native standard (CNCF), JSON based.
* **Cons:** Ruby dependency for some plugins, Complex configuration.""",
                "tr": """### 1. Tanım
Fluentd; veri toplama ve tüketimi birleştiren, açık kaynaklı, Cloud-Native (Bulut Yerlisi) bir veri toplayıcıdır. Özellikle Kubernetes ortamlarının standart loglayıcısıdır.

### 2. Temel Amaç
Veri kaynakları ile arka uç sistemleri arasındaki karmaşıklığı çözmek; log verilerini JSON formatında yapılandırarak taşımaktır.

### 3. Mimari ve Çalışma Prensibi
C ve Ruby ile yazılmıştır. Az kaynak tüketir. Veriyi **Etiketler (Tag)** kullanarak yönlendirir.
* **Input Plugins:** Veriyi toplar (tail, http).
* **Parser:** Veriyi JSON'a çevirir.
* **Buffer:** Ağ kesintilerine karşı veriyi tamponlar.
* **Output Plugins:** Veriyi hedefe gönderir.

### 4. Temel Bileşenler
Girdi Eklentileri, Ayrıştırıcı, Tampon, Çıktı Eklentileri.

### 5. Kullanım Alanları
Kubernetes & Docker logları, IoT cihazları (Fluent Bit).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hafiflik, Ekosistem (CNCF standardı).
* **Dezavantajlar:** Ruby Bağımlılığı, Konfigürasyon zorluğu."""
            },
            "link": "https://www.fluentd.org/", "modern": True, "dep": None,
            "code": """# fluent.conf
<source>
  @type tail
  path /var/log/httpd-access.log
  tag apache.access
</source>

<match apache.**>
  @type stdout
</match>"""
        },
        "Debezium": {
            "desc": {"en": "Change Data Capture (CDC).", "tr": "Veri Değişikliği Yakalama (CDC)."},
            "detail": {
                "en": """### 1. Definition
Debezium is a distributed platform for Change Data Capture (CDC), built on top of Apache Kafka Connect. It captures row-level changes in databases.

### 2. Core Purpose
To allow applications to respond almost immediately to database changes (inserts, updates, deletes) without polling. "Turning the database into an event stream."

### 3. Architecture
Debezium reads the database's **Transaction Logs** (e.g., Binlog for MySQL, WAL for Postgres). It converts each change into a JSON message and writes it to a Kafka Topic. This adds no overhead to the database queries.

### 4. Key Components
* **Kafka Connect:** The runtime environment.
* **Connectors:** Database-specific connectors (MySQL, Postgres, Oracle).
* **Schema Registry:** Manages schema evolution.

### 5. Use Cases
Cache Invalidation, Search Indexing, Microservices Data Exchange (Strangler Fig Pattern).

### 6. Pros and Cons
* **Pros:** Zero Data Loss (reads logs), Low Overhead (No polling).
* **Cons:** Complex Management (Needs Kafka), Schema Evolution handling.""",
                "tr": """### 1. Tanım
Debezium; veritabanlarındaki değişiklikleri anlık olarak yakalayan (CDC) ve bunları bir olay akışına dönüştüren, Kafka Connect üzerine inşa edilmiş dağıtık bir platformdur.

### 2. Temel Amaç
Uygulamaların veritabanını sürekli sorgulamasına (polling) gerek kalmadan; veri değiştiğinde anında haberdar olmasını sağlamaktır. "Veritabanını bir olay akışına dönüştürmek" olarak özetlenir.

### 3. Mimari ve Çalışma Prensibi
Debezium, veritabanının **İşlem Günlüklerini (Transaction Logs)** okur (Örn: MySQL Binlog, Postgres WAL). Bu logları okuyarak her değişikliği bir JSON mesajı olarak Kafka Topic'ine yazar. Doğrudan sorgu atmadığı için veritabanını yormaz.

### 4. Temel Bileşenler
Kafka Connect (Çalışma ortamı), Connectors (Bağlayıcılar), Schema Registry.

### 5. Kullanım Alanları
Cache Temizleme (Redis), Arama İndeksleme (Elasticsearch), Mikroservis geçişleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Sıfır Veri Kaybı, Düşük Kaynak Tüketimi.
* **Dezavantajlar:** Yönetim Zorluğu (Kafka bağımlılığı), Şema Değişimleri."""
            },
            "link": "https://debezium.io/", "modern": True, "dep": "Kafka",
            "code": """{
  "name": "inventory-connector",
  "config": {
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "database.hostname": "mysql",
    "database.port": "3306",
    "database.user": "debezium",
    "database.password": "dbz",
    "database.server.id": "184054",
    "database.server.name": "dbserver1",
    "database.include.list": "inventory"
  }
}"""
        },
        "Sqoop": {
            "desc": {"en": "SQL to Hadoop Transfer.", "tr": "SQL'den Hadoop'a Veri Aktarımı."},
            "detail": {
                "en": """### 1. Definition
Apache Sqoop is a tool designed for efficiently transferring bulk data between Apache Hadoop and structured datastores such as relational databases (RDBMS).

### 2. Core Purpose
In the early days of Big Data, it was used to offload enterprise data (Oracle, MySQL) to Hadoop for analysis.

### 3. Architecture
It works on **MapReduce**. It reads database metadata, creates "Mapper" tasks to parallelize the transfer, and writes data to HDFS via JDBC. (No Reduce phase).

### 4. Key Components
Import Tool (RDBMS -> HDFS), Export Tool (HDFS -> RDBMS), JDBC Drivers.

### 5. Use Cases
Data Warehouse Offloading, Nightly Batch Jobs. (Note: Retired project, but still in use in legacy systems).

### 6. Pros and Cons
* **Pros:** Parallelism (Fast bulk transfer), Integration (Hive/HBase creation).
* **Cons:** Legacy Architecture (High latency due to MapReduce), No Streaming support.""",
                "tr": """### 1. Tanım
Apache Sqoop ("SQL to Hadoop"); ilişkisel veritabanları (RDBMS) ile Hadoop ekosistemi (HDFS, Hive, HBase) arasında toplu veri aktarımı (bulk transfer) yapmak için tasarlanmış bir araçtır.

### 2. Temel Amaç
Büyük veri dünyasının ilk dönemlerinde, kurumsal verilerin (Oracle, MySQL) Hadoop ortamına analiz için taşınmasını sağlamaktı.

### 3. Mimari ve Çalışma Prensibi
**MapReduce** tabanlı çalışır. Veritabanı metadatasını okur, aktarımı paralelleştirmek için "Mapper" görevleri oluşturur ve veriyi JDBC üzerinden parçalar halinde çekerek HDFS'e yazar.

### 4. Temel Bileşenler
Import Tool, Export Tool, JDBC Sürücüleri.

### 5. Kullanım Alanları
Veri ambarı verilerini Hadoop'a arşivlemek, Gece çalışan toplu işler (Batch Jobs).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Paralellik (Yüksek hız), Hive entegrasyonu.
* **Dezavantajlar:** Eski Mimari (Hantal MapReduce), Gerçek zamanlı (Streaming) desteği yok."""
            },
            "link": "https://sqoop.apache.org/", "modern": False, "dep": "Hadoop MR",
            "code": """# MySQL'den HDFS'e veri çekme
sqoop import \\
  --connect jdbc:mysql://localhost/db \\
  --username root \\
  --table employees \\
  --target-dir /user/hadoop/employees \\
  -m 1"""
        },
        "RabbitMQ": {
            "desc": {"en": "Traditional Message Broker.", "tr": "Geleneksel Mesaj Kuyruğu."},
            "detail": {
                "en": """### 1. Definition
RabbitMQ is an open-source, traditional message broker that implements the AMQP standard with advanced routing capabilities.

### 2. Core Purpose
To manage complex messaging scenarios between applications and make tasks asynchronous. Unlike Kafka, it focuses on "queue" logic.

### 3. Architecture
Operates on "Smart Broker, Dumb Consumer" principle. Uses Exchanges to route messages to Queues based on Bindings.

### 4. Components
Exchange, Queue, Binding, Erlang Runtime.

### 5. Use Cases
Background tasks, Complex routing, Order processing.

### 6. Pros and Cons
* **Pros:** Flexible Routing, Push Model.
* **Cons:** Lower throughput than Kafka, Messages deleted after consumption.""",
                "tr": """### 1. Tanım
RabbitMQ; gelişmiş yönlendirme (routing) yeteneklerine sahip, AMQP standardını uygulayan, açık kaynaklı, geleneksel bir mesaj aracısıdır (Message Broker).

### 2. Temel Amaç
Uygulamalar arasında karmaşık mesajlaşma senaryolarını yönetmek ve görevleri asenkron hale getirmektir. Kafka'nın aksine "kuyruk" mantığına odaklanır.

### 3. Mimari ve Çalışma Prensibi
"Akıllı Sunucu, Aptal Tüketici" prensibiyle çalışır. Üretici mesajı bir "Exchange"e gönderir, Exchange kurallara göre mesajı ilgili kuyruklara (Queue) dağıtır.

### 4. Temel Bileşenler
Exchange, Queue, Binding, Erlang Runtime.

### 5. Kullanım Alanları
Arka plan işlemleri, Karmaşık yönlendirme gerektiren haberleşmeler.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Esnek Yönlendirme, Push Modeli.
* **Dezavantajlar:** Performans (Kafka'dan düşüktür), Veri Saklama (Tüketilen silinir)."""
            },
            "link": "https://www.rabbitmq.com/", "modern": False, "dep": "Erlang",
            "code": """import pika
connection = pika.BlockingConnection()
channel = connection.channel()
channel.basic_publish(exchange='', routing_key='hello', body='Hello!')"""
        },
        "Pulsar": {
            "desc": {"en": "Cloud-Native Messaging.", "tr": "Bulut Tabanlı Mesajlaşma."},
            "detail": {
                "en": """### 1. Definition
Apache Pulsar is a distributed pub-sub platform designed for cloud-native architectures, combining messaging and streaming.

### 2. Core Purpose
To solve Kafka's scaling challenges by providing multi-tenancy and separation of compute/storage.

### 3. Architecture
Separation of Compute (Stateless Brokers) and Storage (BookKeeper). Allows independent scaling.

### 4. Components
Broker, BookKeeper, ZooKeeper, Pulsar Functions.

### 5. Use Cases
SaaS platforms, Geo-replication, Queuing + Streaming hybrid.

### 6. Pros and Cons
* **Pros:** Tiered Storage, Multi-tenancy.
* **Cons:** Architectural Complexity, Smaller community.""",
                "tr": """### 1. Tanım
Apache Pulsar; bulut tabanlı mimariler için tasarlanmış, hem mesajlaşma hem de olay akışı özelliklerini tek çatıda toplayan platformdur.

### 2. Temel Amaç
Kafka'nın ölçeklenme zorluklarını çözmek ve çok kiracılı (multi-tenant) yapı sunmaktır.

### 3. Mimari ve Çalışma Prensibi
En belirgin özelliği "Hesaplama ve Depolamanın Ayrılması"dır. Broker'lar veriyi işlemez, BookKeeper veriyi saklar.

### 4. Temel Bileşenler
Broker, BookKeeper, ZooKeeper, Pulsar Functions.

### 5. Kullanım Alanları
Büyük ölçekli bulut uygulamaları, Coğrafi dağıtık sistemler.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** S3'e otomatik veri taşıma (Tiered Storage), Bağımsız ölçeklenme.
* **Dezavantajlar:** Mimari karmaşıklık, Popülarite."""
            },
            "link": "https://pulsar.apache.org/", "modern": True, "dep": "Zookeeper",
            "code": """import pulsar
client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')
producer.send(('Hello').encode('utf-8'))"""
        },
        "Airbyte": {
            "desc": {"en": "ELT Data Integration.", "tr": "Açık Kaynak ELT."},
            "detail": {
                "en": """### 1. Definition
Airbyte is an open-source data integration (ELT) platform to extract data from APIs/DBs and load to warehouses.

### 2. Core Purpose
To easily pull data from thousands of "Long-tail" SaaS applications. Open-source alternative to Fivetran.

### 3. Architecture
Container-based (Docker). Runs connectors as isolated containers. Follows ELT (Extract-Load-Transform).

### 4. Components
Source Connectors, Destination Connectors, Worker, Scheduler.

### 5. Use Cases
Marketing data consolidation, DB replication.

### 6. Pros and Cons
* **Pros:** Huge library, Open Source.
* **Cons:** Management overhead, Performance at massive scale.""",
                "tr": """### 1. Tanım
Airbyte; verileri API'lerden ve veritabanlarından alıp veri ambarlarına taşımak için kullanılan açık kaynaklı ELT platformudur.

### 2. Temel Amaç
Binlerce farklı SaaS uygulamasından veriyi kolayca çekebilmek. Fivetran'ın açık kaynaklı alternatifidir.

### 3. Mimari ve Çalışma Prensibi
Konteyner tabanlıdır. Her bağlayıcı izole bir Docker konteyneri olarak çalışır. ELT (Çıkar-Yükle-Dönüştür) mantığını izler.

### 4. Temel Bileşenler
Kaynak Bağlayıcıları, Hedef Bağlayıcıları, Worker, Scheduler.

### 5. Kullanım Alanları
Pazarlama verisi toplama, Modern Veri Yığını kurulumları.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Geniş Konektör Kütüphanesi, Açık Kaynak.
* **Dezavantajlar:** Kendi sunucunda yönetim zorluğu."""
            },
            "link": "https://airbyte.com/", "modern": True, "dep": "Docker",
            "code": "# Airbyte API Call"
        },
        "Fivetran": {
            "desc": {"en": "Managed ELT.", "tr": "Yönetilen ELT."},
            "detail": {
                "en": """### 1. Definition
Fully managed automated data movement platform.

### 2. Core Purpose
Zero-maintenance pipelines. Handles schema drift automatically.

### 3. Architecture
SaaS (Software as a Service). No infrastructure to manage.

### 4. Components
Connectors, Dashboard.

### 5. Use Cases
Enterprise data ingestion without engineering overhead.

### 6. Pros and Cons
* **Pros:** Reliability, Ease of use.
* **Cons:** Cost, Closed source.""",
                "tr": """### 1. Tanım
Tamamen yönetilen, otomatik veri taşıma platformu.

### 2. Temel Amaç
Bakım gerektirmeyen boru hatları. Şema değişikliklerini otomatik yönetir.

### 3. Mimari
SaaS modelidir. Altyapı yönetimi yoktur.

### 4. Temel Bileşenler
Bağlayıcılar, Yönetim Paneli.

### 5. Kullanım Alanları
Mühendislik eforu harcamadan kurumsal veri taşıma.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Güvenilirlik, Kolaylık.
* **Dezavantajlar:** Maliyet, Kapalı kaynak."""
            },
            "link": "https://www.fivetran.com/", "modern": True, "dep": None,
            "code": "# No Code - Managed Service"
        },
        "NiFi": {
            "desc": {"en": "Data Flow Automation.", "tr": "Görsel Veri Akış Otomasyonu."},
            "detail": {
                "en": """### 1. Definition
Apache NiFi is a visual flow-based programming tool for automating data flow. Developed by NSA.

### 2. Core Purpose
Visually design routing, transformation, and mediation of data.

### 3. Architecture
Flow-based. Handles **Backpressure** automatically.

### 4. Components
FlowFile, Processor, Process Group, Flow Controller.

### 5. Use Cases
IoT data collection, Legacy migration.

### 6. Pros and Cons
* **Pros:** Visual Interface, Data Provenance.
* **Cons:** Small file problem, Stateful.""",
                "tr": """### 1. Tanım
Apache NiFi; veri akışını otomatize etmek için tasarlanmış, görsel arayüze sahip bir araçtır. NSA tarafından geliştirilmiştir.

### 2. Temel Amaç
Kod yazmadan veri akışlarını görsel olarak tasarlamak ve yönetmek.

### 3. Mimari ve Çalışma Prensibi
Akış tabanlıdır. Hedef sistem yavaşlarsa "Geri Basınç" (Backpressure) uygulayarak akışı yavaşlatır.

### 4. Temel Bileşenler
FlowFile, Processor, Process Group, Flow Controller.

### 5. Kullanım Alanları
IoT veri toplama, Eski sistemlerden göç.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Görsel Arayüz, Veri Soy Ağacı.
* **Dezavantajlar:** Küçük dosya sorunu, Durumlu (Stateful) yapı."""
            },
            "link": "https://nifi.apache.org/", "modern": True, "dep": "Zookeeper",
            "code": "# Visual Interface"
        },
        "Kinesis": {
            "desc": {"en": "AWS Streaming.", "tr": "AWS Akış Servisi."},
            "detail": {
                "en": """### 1. Definition
Serverless streaming service on AWS.

### 2. Core Purpose
Real-time data streaming without managing servers. Kafka alternative on AWS.

### 3. Architecture
Uses Shards instead of Partitions. Fully managed.

### 4. Components
Data Streams, Firehose, Analytics.

### 5. Use Cases
AWS-centric real-time apps.

### 6. Pros and Cons
* **Pros:** Serverless, AWS Integration.
* **Cons:** Vendor Lock-in, Cost at scale.""",
                "tr": """### 1. Tanım
AWS üzerinde sunulan sunucusuz veri akış servisi.

### 2. Temel Amaç
Sunucu yönetimi olmadan gerçek zamanlı veri akışı sağlamak.

### 3. Mimari
Partition yerine "Shard" kullanır. Tamamen yönetilen bir servistir.

### 4. Temel Bileşenler
Data Streams, Firehose.

### 5. Kullanım Alanları
AWS odaklı gerçek zamanlı uygulamalar.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Sunucusuz, AWS Entegrasyonu.
* **Dezavantajlar:** Sağlayıcı bağımlılığı (Vendor Lock-in), Yüksek ölçekte maliyet."""
            },
            "link": "https://aws.amazon.com/kinesis/", "modern": True, "dep": "AWS",
            "code": "import boto3\nkinesis = boto3.client('kinesis')"
        }
    },
    "Storage": {
        "S3": {
            "desc": {"en": "Object Storage Standard.", "tr": "Nesne Depolama Standardı."},
            "detail": {
                "en": """### 1. Definition
Amazon S3 is an object storage service designed to store data at internet scale. It is the de facto standard and API reference point for the data storage world today.

### 2. Core Purpose
To store any amount of data (structured or unstructured) with 99.999999999% (11 9s) durability and make it accessible over the internet. Unlike classic file systems (hierarchical folder structure), it stores data in a flat addressing space, ensuring infinite scalability.

### 3. Architecture and Working Principle
S3 stores data as "Objects" inside containers called "Buckets".
* **Key-Value:** Each file has a unique key (URL).
* **Flat Structure:** There are no actual folders, it behaves like folders using prefix logic (e.g., logs/2023/file.txt is a single key).
* **Replication:** Data is automatically replicated to at least 3 physically separate data centers (Availability Zones) within a Region.

### 4. Key Components
* **Bucket:** The top-level container where objects are stored.
* **Object:** The data itself (File) + Metadata + Key (ID).
* **Storage Classes:** Classes providing cost optimization based on access frequency (Standard, Glacier, Deep Archive).

### 5. Use Cases
Data Lake (Big Data analytics center), Backup and Archive, Static Website Hosting.

### 6. Pros and Cons
* **Pros:** Infinite Scale, Extreme Durability (11 9s), Universal Integration.
* **Cons:** Latency (Slower than local disks), Egress Cost (Data transfer fees).""",

                "tr": """### 1. Tanım
Amazon S3; internet ölçeğinde veri depolamak için tasarlanmış, nesne tabanlı (object storage) bir bulut depolama servisidir. Günümüzde veri depolama dünyasının fiili (de facto) standardı ve API referans noktasıdır.

### 2. Temel Amaç
Her türlü veriyi (yapısal veya yapısal olmayan), istenilen miktarda, %99.999999999 (11 adet 9) dayanıklılıkla saklamak ve internet üzerinden erişilebilir kılmaktır. Klasik dosya sistemlerinin (hiyerarşik klasör yapısı) aksine, veriyi düz (flat) bir adresleme uzayında tutarak sonsuz ölçeklenebilirlik sağlar.

### 3. Mimari ve Çalışma Prensibi
S3, verileri "Bucket" (kova) adı verilen kaplarda "Object" (nesne) olarak saklar.
* **Key-Value Yapısı:** Her dosyanın benzersiz bir anahtarı (URL) vardır.
* **Düz Yapı:** Gerçekte klasörler yoktur, sadece isimlendirme (prefix) mantığı ile klasör varmış gibi davranır.
* **Replikasyon:** Veri, bir bölgedeki fiziksel olarak ayrı en az 3 farklı veri merkezine otomatik kopyalanır.

### 4. Temel Bileşenler
* **Bucket:** Nesnelerin tutulduğu en üst düzey kapsayıcı.
* **Object:** Verinin kendisi (Dosya) + Metadata (Veri hakkında bilgi) + Key (Kimlik).
* **Storage Classes:** Verinin erişim sıklığına göre maliyet optimizasyonu sağlayan sınıflar (Standard, Glacier).

### 5. Kullanım Alanları
Data Lake (Veri Gölü), Yedekleme ve Arşiv, Statik Web Sitesi sunumu.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Sınırsız Ölçek, Yüksek Dayanıklılık, Kolay Entegrasyon.
* **Dezavantajlar:** Gecikme (Yerel disklere göre yavaştır), Egress Maliyeti (Veri indirme ücreti)."""
            },
            "link": "https://aws.amazon.com/s3/", "modern": True, "dep": None,
            "code": """import boto3

# S3 İstemcisi
s3 = boto3.client('s3')

# Bucket Oluşturma
s3.create_bucket(Bucket='my-data-lake')

# Dosya Yükleme
s3.upload_file('local_data.csv', 'my-data-lake', 'raw/data.csv')
print("Dosya yüklendi.")"""
        },
        "HDFS": {
            "desc": {"en": "Hadoop Distributed File System.", "tr": "Hadoop Dağıtık Dosya Sistemi."},
            "detail": {
                "en": """### 1. Definition
HDFS is a block-based, distributed file system designed to store very large files reliably across clusters of commodity hardware. Inspired by Google's GFS paper.

### 2. Core Purpose
Assuming hardware failure is the "norm" rather than exception, it splits data into chunks and distributes them across servers to ensure high throughput. Fits the "Write Once, Read Many" model.

### 3. Architecture and Working Principle
Uses a Master/Slave architecture. Files are split into blocks (Default 128 MB).
Each block is distributed to different servers (typically 3 copies). When a server fails, the system automatically uses other copies to recover data.

### 4. Key Components
* **NameNode (Master):** The "brain" of the file system. Stores metadata (file locations) in RAM.
* **DataNode (Slave):** Worker servers storing actual data blocks on disk.
* **Secondary NameNode:** Helper that merges metadata updates (checkpoints), not a backup.

### 5. Use Cases
Historical big data analysis (Batch Processing), Primary storage for engines like Spark/Hive, On-premise Data Lakes.

### 6. Pros and Cons
* **Pros:** Cost-effective (Commodity hardware), Data Locality (Compute moves to data), High Throughput.
* **Cons:** Small File Problem (NameNode memory bottleneck), Single Point of Failure (NameNode), Append-only (Files cannot be updated).""",

                "tr": """### 1. Tanım
HDFS; standart (commodity) donanımlardan oluşan kümeler üzerinde çok büyük dosyaları güvenilir bir şekilde saklamak için tasarlanmış, blok tabanlı, dağıtık bir dosya sistemidir. Google'ın GFS makalesinden esinlenerek geliştirilmiştir.

### 2. Temel Amaç
Donanım arızalarının "istisna" değil "kural" olduğu varsayımıyla, veriyi parçalara bölüp farklı sunuculara dağıtarak yüksek işlem hacmi (throughput) sağlamaktır. "Yaz bir kere, oku çok kere" modeline uygundur.

### 3. Mimari ve Çalışma Prensibi
Master/Slave mimarisi kullanır. Dosyalar belirli boyutlardaki bloklara (Varsayılan 128 MB) bölünür. Her blok, kümedeki farklı sunuculara (genellikle 3 kopya olarak) dağıtılır.

### 4. Temel Bileşenler
* **NameNode (Master):** Dosya sisteminin "beyni"dir. Metadata bilgisini RAM'de tutar.
* **DataNode (Slave):** Veri bloklarını fiziksel olarak diskte saklayan işçi sunuculardır.
* **Secondary NameNode:** Metadata güncellemelerini birleştiren yardımcıdır.

### 5. Kullanım Alanları
Tarihsel büyük veri analizi (Batch), Spark/Hive için depolama katmanı, On-premise veri gölleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Maliyet (Ucuz donanım), Veri Yerelliği (Data Locality), Yüksek Throughput.
* **Dezavantajlar:** Küçük Dosya Sorunu (NameNode şişer), Tek Nokta Hatası (SPOF), Güncelleme Zorluğu (Sadece ekleme yapılabilir)."""
            },
            "link": "https://hadoop.apache.org/", "modern": False, "dep": "NameNode",
            "code": """# HDFS CLI Komutları

# Klasör Oluşturma
hdfs dfs -mkdir /user/data

# Dosya Yükleme
hdfs dfs -put local_file.txt /user/data/

# Dosya Listeleme
hdfs dfs -ls /user/data/

# Dosya İçeriği Okuma
hdfs dfs -cat /user/data/local_file.txt"""
        },
        "MinIO": {
            "desc": {"en": "High Performance Object Storage.", "tr": "Yüksek Performanslı Nesne Depolama."},
            "detail": {
                "en": """### 1. Definition
MinIO is a high-performance, open-source object storage server built for Kubernetes, 100% compatible with Amazon S3 API.

### 2. Core Purpose
To provide the S3 experience and API standard with much higher performance on-premise or in private clouds. Optimized for AI/ML and analytics workloads.

### 3. Architecture and Working Principle
Written in Go, very lightweight. No complex NameNode/DataNode separation; symmetric nodes.
* **Erasure Coding:** Uses math algorithms instead of replication (3 copies) to protect data, saving up to 50% disk space.
* **Bitrot Protection:** Prevents silent data corruption over time.

### 4. Key Components
* **MinIO Server:** Runs as a single binary.
* **MinIO Client (mc):** Powerful CLI tool similar to Unix commands.
* **Console:** Web-based management UI.

### 5. Use Cases
Private Cloud (S3 alternative for regulated industries), High Performance AI/ML (Feeding GPUs), Edge Computing.

### 6. Pros and Cons
* **Pros:** Speed (Claims to be world's fastest), Simplicity (Single binary), S3 Compatibility.
* **Cons:** Management (Erasure coding complexity), Scope (Object storage only).""",

                "tr": """### 1. Tanım
MinIO; Kubernetes için oluşturulmuş, Amazon S3 API ile %100 uyumlu, yüksek performanslı, açık kaynaklı bir nesne depolama (Object Storage) sunucusudur.

### 2. Temel Amaç
Şirketlerin kendi veri merkezlerinde (On-premise), Amazon S3'ün sunduğu deneyimi ve API standardını çok daha yüksek performansla sunmaktır. Özellikle AI/ML iş yükleri için optimize edilmiştir.

### 3. Mimari ve Çalışma Prensibi
Go dili ile yazılmıştır, çok hafiftir. Simetrik düğüm yapısı kullanır.
* **Erasure Coding:** Veriyi korumak için klasik replikasyon yerine matematiksel algoritmalar kullanır. %50 disk tasarrufu sağlar.
* **Bitrot Protection:** Verinin zamanla bozulmasını engeller.

### 4. Temel Bileşenler
MinIO Server (Tek binary), MinIO Client (mc), Console (Web Arayüzü).

### 5. Kullanım Alanları
Özel Bulut (Private Cloud), Yüksek Performanslı AI/ML, Edge Computing.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hız, Sadelik, S3 Uyumluluğu.
* **Dezavantajlar:** Yönetim (Dağıtık yapı uzmanlık ister), Sınırlı Kapsam (Sadece Object Storage)."""
            },
            "link": "https://min.io/", "modern": True, "dep": None,
            "code": """# Docker ile MinIO Çalıştırma
docker run -p 9000:9000 -p 9001:9001 \\
  minio/minio server /data --console-address ":9001"

# Python ile Erişim (boto3 kullanılır)
s3 = boto3.client('s3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin')"""
        },
        "Ceph": {
            "desc": {"en": "Unified Storage Platform.", "tr": "Birleşik Depolama Platformu."},
            "detail": {
                "en": """### 1. Definition
Ceph is a unified, open-source storage platform offering Object, Block, and File storage on a single distributed cluster.

### 2. Core Purpose
"One system to store it all" vision; offering a self-managing and self-healing structure scaling to Exabytes without a single point of failure (SPOF).

### 3. Architecture and Working Principle
Heart is RADOS (Reliable Autonomic Distributed Object Store).
* **CRUSH Algorithm:** Ceph's key innovation. Calculates data location algorithmically instead of using a central lookup table (like NameNode), eliminating bottlenecks.

### 4. Key Components
* **OSD:** Daemon storing data on disk.
* **MON:** Monitor maintaining cluster map.
* **MGR:** Manager for metrics.
* **Interfaces:** RadosGW (S3), RBD (Block), CephFS (File).

### 5. Use Cases
OpenStack & Kubernetes persistent storage, Academic Research (CERN), General Purpose Storage.

### 6. Pros and Cons
* **Pros:** Flexibility (Object+Block+File), Decentralization (No bottleneck), Self-Healing.
* **Cons:** Complexity (Steep learning curve), Hardware hungry.""",

                "tr": """### 1. Tanım
Ceph; tek bir dağıtık küme üzerinde Nesne (Object), Blok (Block) ve Dosya (File) depolamayı aynı anda sunan, birleşik (unified), açık kaynaklı bir depolama platformudur.

### 2. Temel Amaç
"Her şeyi saklayabilen tek bir sistem" vizyonuyla; tek bir hata noktası (SPOF) olmadan, Exabyte seviyesine kadar ölçeklenebilen, kendi kendini yönetebilen (self-managing) bir yapı sunmaktır.

### 3. Mimari ve Çalışma Prensibi
Ceph'in kalbinde RADOS bulunur.
* **CRUSH Algoritması:** Merkezi bir tablo (NameNode gibi) kullanmaz. Verinin adresini matematiksel olarak hesaplar. Bu sayede merkezi darboğaz ortadan kalkar.

### 4. Temel Bileşenler
OSD (Disk süreci), MON (İzleme), MGR (Yönetim). Arayüzler: RadosGW (S3), RBD (Blok), CephFS (Dosya).

### 5. Kullanım Alanları
OpenStack & Kubernetes depolama, Akademik Araştırma, Genel Amaçlı Depolama.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Esneklik (3'ü 1 arada), Merkeziyetsizlik, Self-Healing.
* **Dezavantajlar:** Karmaşıklık (Öğrenme eğrisi diktir), Donanım İştahı."""
            },
            "link": "https://ceph.io/", "modern": True, "dep": "Linux",
            "code": """# Ceph Küme Durumu Kontrolü
ceph status

# Yeni bir OSD (Disk) Ekleme
ceph-volume lvm create --data /dev/sdb

# Havuz (Pool) Oluşturma
ceph osd pool create mypool 128"""
        },
        "Ozone": {
            "desc": {"en": "Scalable Object Store.", "tr": "Ölçeklenebilir Nesne Depolama."},
            "detail": {
                "en": """### 1. Definition
Apache Ozone is a scalable, redundant, and distributed object store for Hadoop.

### 2. Core Purpose
Designed to overcome HDFS limitations regarding small files (billions of objects).

### 3. Architecture
Separates namespace management from block management, allowing it to scale significantly better than HDFS.""",
                "tr": """### 1. Tanım
Apache Ozone, Hadoop için geliştirilmiş ölçeklenebilir, dağıtık bir nesne depolama sistemidir.

### 2. Temel Amaç
HDFS'in milyarlarca küçük dosyayı yönetememe (Small Files Problem) sorununu çözmek için tasarlanmıştır.

### 3. Mimari
İsim uzayı (Namespace) yönetimi ile blok yönetimini birbirinden ayırarak HDFS'ten çok daha fazla ölçeklenebilir."""
            },
            "link": "https://ozone.apache.org/", "modern": True, "dep": None,
            "code": "ozone sh volume create /vol1"
        },
        "ADLS Gen2": {
             "desc": {"en": "Azure Data Lake.", "tr": "Azure Veri Gölü."},
             "detail": {
                "en": """### 1. Definition
Microsoft Azure's enterprise data lake solution.

### 2. Core Purpose
Combines the low cost of Blob Storage with a Hierarchical File System structure optimized for analytics.""",
                "tr": """### 1. Tanım
Microsoft Azure'un kurumsal veri gölü çözümüdür.

### 2. Temel Amaç
Blob Storage'ın ucuzluğunu, analitik işlemler için optimize edilmiş Hiyerarşik Dosya Sistemi yapısıyla birleştirir."""
             },
             "link": "https://azure.microsoft.com/", "modern": True, "dep": None,
             "code": "# Azure SDK kullanımı gerektirir"
        },
        "GCS": {
            "desc": {"en": "Google Storage.", "tr": "Google Depolama."},
            "detail": {
                "en": """### 1. Definition
Google Cloud's unified object storage service.

### 2. Core Purpose
To provide consistent, scalable storage. Famous for its strong consistency model.""",
                "tr": """### 1. Tanım
Google Cloud'un birleşik nesne depolama servisidir.

### 2. Temel Amaç
Tutarlı ve ölçeklenebilir depolama sağlamak. Güçlü Tutarlılık (Strong Consistency) modeli ile ünlüdür."""
            },
            "link": "https://cloud.google.com/storage", "modern": True, "dep": None,
            "code": "# Google Cloud SDK kullanımı gerektirir"
        }
    },
"Processing": {
        "Spark": {
            "desc": {"en": "Unified Analytics Engine.", "tr": "Birleşik Büyük Veri Motoru."},
            "detail": {
                "en": """### 1. Definition
Apache Spark is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters. It is the de facto standard for big data processing.

### 2. Core Purpose
To overcome the limitations of the MapReduce model (disk I/O latency) by processing data in-memory. It unifies batch, streaming, SQL, and ML workloads into a single platform.

### 3. Architecture and Working Principle
* **RDD (Resilient Distributed Dataset):** The fundamental data structure. Immutable, distributed collections of objects.
* **DAG (Directed Acyclic Graph):** Spark builds an execution plan (DAG) and optimizes it using the Catalyst Optimizer.
* **Lazy Evaluation:** Transformations are not executed until an Action (like count, save) is called.

### 4. Key Components
Spark Core, Spark SQL, Spark Streaming (Micro-batch), MLlib (Machine Learning), GraphX.

### 5. Use Cases
ETL pipelines, Exploratory Data Analysis (EDA), Machine Learning model training, Real-time dashboards.

### 6. Pros and Cons
* **Pros:** Speed (100x faster than MapReduce), Unified stack, Ease of use (Python/SQL support).
* **Cons:** Memory hungry (OOM errors are common), Complexity in tuning.""",

                "tr": """### 1. Tanım
Apache Spark; veri mühendisliği, veri bilimi ve makine öğrenimi iş yüklerini tek düğümlü makinelerde veya kümelerde yürütmek için tasarlanmış çok dilli bir motordur. Büyük veri işlemenin fiili standardıdır.

### 2. Temel Amaç
MapReduce modelinin disk G/Ç gecikmelerinden kaynaklanan yavaşlığını, veriyi bellek içinde (In-Memory) işleyerek aşmaktır. Toplu (Batch), Akış (Stream), SQL ve Makine Öğrenmesi iş yüklerini tek platformda birleştirir.

### 3. Mimari ve Çalışma Prensibi
* **RDD:** Temel veri yapısıdır. Değiştirilemez ve dağıtık nesne koleksiyonudur.
* **DAG:** Spark, yapılacak işlemleri bir çizge (grafik) olarak planlar ve Catalyst Optimizer ile optimize eder.
* **Tembel Değerlendirme (Lazy Evaluation):** Bir "Eylem" (Action - örn: kaydet, say) çağrılana kadar hiçbir işlem çalıştırılmaz, sadece planlanır.

### 4. Temel Bileşenler
Spark Core, Spark SQL, Spark Streaming (Mikro-yığın), MLlib, GraphX.

### 5. Kullanım Alanları
ETL boru hatları, Keşifsel Veri Analizi, ML model eğitimi, Gerçek zamanlı paneller.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hız (MapReduce'tan 100 kat hızlı), Birleşik yapı, Kullanım kolaylığı (Python/SQL).
* **Dezavantajlar:** Bellek canavarıdır (RAM yetmezliği hataları sıktır), İnce ayar (Tuning) uzmanlık ister."""
            },
            "link": "https://spark.apache.org/", "modern": True, "dep": "Cluster",
            "code": """from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Demo").getOrCreate()

# Veri Okuma
df = spark.read.csv("sales.csv", header=True)

# İşleme (Transformation)
result = df.groupBy("category").count()

# Sonuç (Action)
result.show()"""
        },
        "Flink": {
            "desc": {"en": "Stateful Stream Processing.", "tr": "Durumlu Akış İşleme."},
            "detail": {
                "en": """### 1. Definition
Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams.

### 2. Core Purpose
To process continuous data streams in real-time with ultra-low latency and guarantees of correctness (Exactly-once semantics), unlike Spark's micro-batch approach.

### 3. Architecture and Working Principle
Flink processes data row-by-row as it arrives.
* **Event Time:** Handles data based on when it occurred, not when it arrived.
* **Watermarks:** A mechanism to handle late-arriving data.
* **State Backends:** Stores intermediate state (e.g., in RocksDB) for fault tolerance.

### 4. Key Components
DataStream API, Table API/SQL, Flink CEP (Complex Event Processing).

### 5. Use Cases
Fraud detection, Real-time recommendation, Network monitoring.

### 6. Pros and Cons
* **Pros:** True streaming (Low latency), Powerful state management, Exactly-once guarantee.
* **Cons:** Operational complexity, Steeper learning curve than Spark.""",

                "tr": """### 1. Tanım
Apache Flink; sınırsız ve sınırlı veri akışları üzerinde durumlu (stateful) hesaplamalar yapmak için geliştirilmiş dağıtık bir işlem motorudur.

### 2. Temel Amaç
Spark'ın mikro-yığın yaklaşımının aksine, sürekli veri akışlarını gerçek zamanlı olarak, ultra düşük gecikmeyle ve doğruluk garantisiyle (Tam bir kez işleme) işlemektir.

### 3. Mimari ve Çalışma Prensibi
Flink veriyi geldiği an satır satır işler.
* **Olay Zamanı (Event Time):** Veriyi sunucuya varış zamanına göre değil, oluştuğu zamana göre işler.
* **Watermarks:** Geç gelen verileri yönetmek için kullanılan zaman işaretçileridir.
* **State Backends:** Hata toleransı için ara durumları (State) RocksDB gibi yerlerde saklar.

### 4. Temel Bileşenler
DataStream API, Table API/SQL, Flink CEP.

### 5. Kullanım Alanları
Dolandırıcılık tespiti, Gerçek zamanlı öneri, Ağ izleme.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Gerçek akış (Düşük gecikme), Güçlü durum yönetimi, Exactly-once garantisi.
* **Dezavantajlar:** Operasyonel karmaşıklık, Öğrenme eğrisi Spark'tan diktir."""
            },
            "link": "https://flink.apache.org/", "modern": True, "dep": "Zookeeper",
            "code": """// Java API
DataStream<String> stream = env.socketTextStream("localhost", 9999);

stream.flatMap(new Tokenizer())
      .keyBy(value -> value.f0)
      .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))
      .sum(1)
      .print();"""
        },
        "Trino": {
            "desc": {"en": "Distributed SQL Query Engine.", "tr": "Federatif SQL Motoru."},
            "detail": {
                "en": """### 1. Definition
Trino (formerly PrestoSQL) is a distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources.

### 2. Core Purpose
To separate Compute from Storage. It allows querying data where it lives (S3, Kafka, MySQL, Cassandra) without moving/copying it to a central warehouse.

### 3. Architecture and Working Principle
MPP (Massively Parallel Processing) architecture.
* **Coordinator:** Parses SQL, plans query, manages workers.
* **Workers:** Execute tasks and fetch data from connectors.
* **Connectors:** Adapters for different data sources.

### 4. Key Components
Coordinator, Workers, Connectors.

### 5. Use Cases
Ad-hoc analytics on Data Lakes, Data Federation (Joining Kafka stream with MySQL table).

### 6. Pros and Cons
* **Pros:** Fast interactive queries, No data movement needed, ANSI SQL support.
* **Cons:** Not for OLTP (transactions), Resource intensive in memory.""",

                "tr": """### 1. Tanım
Trino (eski adıyla PrestoSQL); farklı kaynaklara dağılmış büyük veri setlerini sorgulamak için tasarlanmış dağıtık bir SQL motorudur.

### 2. Temel Amaç
Hesaplama (Compute) ile Depolamayı (Storage) ayırmaktır. Veriyi merkezi bir ambara kopyalamadan, olduğu yerde (S3, Kafka, MySQL) sorgulamayı sağlar.

### 3. Mimari ve Çalışma Prensibi
MPP (Devasa Paralel İşleme) mimarisini kullanır.
* **Koordinatör:** SQL'i parçalar, planlar ve işçileri yönetir.
* **İşçiler (Workers):** Veriyi kaynaklardan çeker ve işler.
* **Konektörler:** Farklı veri kaynaklarına (Hive, Postgres) bağlanmayı sağlayan adaptörler.

### 4. Temel Bileşenler
Koordinatör, İşçiler, Konektörler.

### 5. Kullanım Alanları
Veri gölü üzerinde anlık analiz, Veri Federasyonu (Kafka akışını MySQL tablosuyla birleştirme).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hızlı etkileşimli sorgular, Veri taşıma gerektirmez, Standart SQL.
* **Dezavantajlar:** İşlem (Transaction) veritabanı değildir, Bellek kullanımı yüksektir."""
            },
            "link": "https://trino.io/", "modern": True, "dep": "Catalog",
            "code": """-- S3'teki veriyi MySQL ile birleştirme
SELECT 
    u.name, 
    o.amount 
FROM 
    mysql.crm.users u
JOIN 
    hive.sales.orders o 
ON u.id = o.user_id;"""
        },
        "Storm": {
            "desc": {"en": "Real-time Computation.", "tr": "Eski Nesil Akış İşleme."},
            "detail": {
                "en": """### 1. Definition
Apache Storm is a distributed realtime computation system. It pioneered the processing of unbounded streams of data.

### 2. Core Purpose
To provide a simple and robust way to process real-time data streams, similar to how Hadoop processes batch data.

### 3. Architecture and Working Principle
* **Topology:** A graph of computation. Runs forever until killed.
* **Spout:** Source of data streams.
* **Bolt:** Processes input streams and produces new streams.

### 4. Key Components
Nimbus (Master), Supervisor (Worker), Zookeeper.

### 5. Use Cases
Real-time analytics, Online machine learning. (Note: Mostly replaced by Flink/Spark Streaming).

### 6. Pros and Cons
* **Pros:** Extremely low latency, Simple programming model.
* **Cons:** Lacks "Exactly-once" processing guarantees (only At-least-once), Managing state is hard.""",

                "tr": """### 1. Tanım
Apache Storm, dağıtık bir gerçek zamanlı hesaplama sistemidir. Sınırsız veri akışlarını işlemenin öncüsüdür.

### 2. Temel Amaç
Hadoop'un toplu veriler için yaptığını, gerçek zamanlı veriler için yapmaktır: Basit ve güvenilir bir işlem çerçevesi sunmak.

### 3. Mimari ve Çalışma Prensibi
* **Topoloji:** İşlem grafiğidir. Durdurulana kadar sonsuza dek çalışır.
* **Spout:** Veri kaynağı (Musluk).
* **Bolt:** Veriyi işleyen ve dönüştüren birim (Cıvata).

### 4. Temel Bileşenler
Nimbus (Yönetici), Supervisor (İşçi), Zookeeper.

### 5. Kullanım Alanları
Gerçek zamanlı analitik. (Not: Günümüzde yerini Flink ve Spark Streaming'e bırakmıştır).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Çok düşük gecikme, Basit model.
* **Dezavantajlar:** "Tam bir kez" (Exactly-once) işleme garantisi yoktur, Durum (State) yönetimi zordur."""
            },
            "link": "https://storm.apache.org/", "modern": False, "dep": "Zookeeper",
            "code": """// Java Topology
TopologyBuilder builder = new TopologyBuilder();
builder.setSpout("words", new TestWordSpout(), 10);
builder.setBolt("exclaim", new ExclamationBolt(), 3).shuffleGrouping("words");"""
        },
        "Beam": {
            "desc": {"en": "Unified Programming Model.", "tr": "Birleşik Programlama Modeli."},
            "detail": {
                "en": """### 1. Definition
Apache Beam is an advanced unified programming model for defining both batch and streaming data-parallel processing pipelines.

### 2. Core Purpose
"Write once, run anywhere." To decouple the pipeline logic from the execution engine. You write code in Beam, and it runs on Spark, Flink, or Google Dataflow.

### 3. Architecture and Working Principle
* **Pipeline:** The entire data processing task.
* **PCollection:** A dataset (bounded or unbounded).
* **PTransform:** A data processing operation.
* **Runner:** The backend that executes the pipeline (e.g., SparkRunner).

### 4. Key Components
SDKs (Java, Python, Go), Runners.

### 5. Use Cases
Building portable data pipelines, migrating between cloud providers.

### 6. Pros and Cons
* **Pros:** Portability, Unified API for Batch/Stream.
* **Cons:** Debugging can be complex (abstraction layer), Performance overhead compared to native APIs.""",

                "tr": """### 1. Tanım
Apache Beam; hem toplu (batch) hem de akış (stream) veri işleme hatlarını tanımlamak için geliştirilmiş birleşik bir programlama modelidir.

### 2. Temel Amaç
"Bir kez yaz, her yerde çalıştır." Veri işleme mantığını, çalıştırma motorundan ayırmaktır. Kodu Beam ile yazarsınız; Spark, Flink veya Google Dataflow üzerinde çalışır.

### 3. Mimari ve Çalışma Prensibi
* **Pipeline:** Tüm veri işleme görevi.
* **PCollection:** Veri seti (Sınırlı veya sınırsız).
* **PTransform:** Veri işleme operasyonu (Map, Filter).
* **Runner:** Kodu çalıştıran motor (Örn: SparkRunner).

### 4. Temel Bileşenler
SDK'lar (Java, Python), Runner'lar.

### 5. Kullanım Alanları
Taşınabilir veri boru hatları, Bulut sağlayıcıları arası geçiş.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Taşınabilirlik, Batch/Stream için tek API.
* **Dezavantajlar:** Hata ayıklama zordur (Soyutlama katmanı yüzünden), Yerel API'lere göre performans kaybı olabilir."""
            },
            "link": "https://beam.apache.org/", "modern": True, "dep": None,
            "code": """import apache_beam as beam

with beam.Pipeline() as p:
    (p | beam.Create(['Hello', 'World'])
       | beam.Map(print))"""
        },
        "dbt": {
            "desc": {"en": "Data Transformation Tool.", "tr": "Analitik Dönüştürme Aracı."},
            "detail": {
                "en": """### 1. Definition
dbt (data build tool) is a transformation workflow that lets analysts and engineers transform data in their warehouses by simply writing SQL.

### 2. Core Purpose
To bring software engineering best practices (version control, testing, documentation, CI/CD) to the world of data analysts. It owns the "T" in ELT.

### 3. Architecture and Working Principle
dbt compiles code into raw SQL and runs it against your database.
* **Models:** SQL files containing SELECT statements.
* **Jinja:** Templating language to write dynamic SQL (loops, variables).
* **DAG:** dbt automatically infers dependencies between models.

### 4. Key Components
Models, Tests, Seeds, Snapshots, Docs.

### 5. Use Cases
Building data marts, Metrics standardization, Data quality testing.

### 6. Pros and Cons
* **Pros:** SQL-based (Low barrier to entry), Git integration, Automated documentation.
* **Cons:** Requires a powerful Data Warehouse (Snowflake/BigQuery), not for general programming.""",

                "tr": """### 1. Tanım
dbt (data build tool); analistlerin ve mühendislerin sadece SQL yazarak veri ambarlarındaki veriyi dönüştürmelerini sağlayan bir araçtır.

### 2. Temel Amaç
Yazılım mühendisliği prensiplerini (Versiyon kontrolü, Test, CI/CD) analitik dünyasına getirmektir. ELT sürecindeki 'T' (Transformation) harfini sahiplenir.

### 3. Mimari ve Çalışma Prensibi
dbt, yazdığınız kodu ham SQL'e derler ve veritabanında çalıştırır.
* **Modeller:** SELECT sorguları içeren SQL dosyaları.
* **Jinja:** Dinamik SQL yazmak için şablonlama dili.
* **DAG:** Modeller arasındaki bağımlılığı otomatik çözer.

### 4. Temel Bileşenler
Modeller, Testler, Dokümantasyon.

### 5. Kullanım Alanları
Veri pazarları (Data Marts) oluşturma, Veri kalitesi testleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** SQL tabanlı (Kolay öğrenilir), Git entegrasyonu, Otomatik doküman.
* **Dezavantajlar:** Güçlü bir Veri Ambarı gerektirir, genel programlama için değildir."""
            },
            "link": "https://www.getdbt.com/", "modern": True, "dep": "Warehouse",
            "code": """-- models/clean_users.sql
WITH raw_users AS (
    SELECT * FROM {{ source('raw', 'users') }}
)
SELECT 
    id, 
    lower(email) as email 
FROM raw_users"""
        },
        "Databricks": {
            "desc": {"en": "Data Intelligence Platform.", "tr": "Yönetilen Veri Zekası Platformu."},
            "detail": {
                "en": """### 1. Definition
Databricks is a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions. Founded by the creators of Apache Spark.

### 2. Core Purpose
To unify Data Warehousing and Data Lakes into a "Lakehouse" architecture. To provide a collaborative environment for Data Engineers and Data Scientists.

### 3. Architecture and Working Principle
Built on top of open standards (Spark, Delta Lake, MLflow).
* **Control Plane:** Managed by Databricks (Web UI, Notebooks, Job Scheduler).
* **Data Plane:** Your cloud account (AWS/Azure/GCP) where data is processed and stored.

### 4. Key Components
Workspace, Notebooks, Delta Lake, Unity Catalog (Governance).

### 5. Use Cases
Lakehouse implementation, MLOps, Collaborative Data Science.

### 6. Pros and Cons
* **Pros:** Best Spark experience, Unified platform, Lakehouse pioneer.
* **Cons:** Cost (Can be expensive), Complexity for simple tasks.""",

                "tr": """### 1. Tanım
Databricks; kurumsal veri, analitik ve yapay zeka çözümleri geliştirmek için kullanılan birleşik bir platformdur. Apache Spark'ın yaratıcıları tarafından kurulmuştur.

### 2. Temel Amaç
Veri Ambarları ile Veri Göllerini "Lakehouse" mimarisinde birleştirmek. Veri Mühendisleri ve Veri Bilimciler için ortak çalışma alanı sunmak.

### 3. Mimari ve Çalışma Prensibi
Açık standartlar üzerine kuruludur (Spark, Delta Lake).
* **Kontrol Düzlemi:** Databricks tarafından yönetilen arayüz ve notebook'lar.
* **Veri Düzlemi:** Verinin işlendiği ve saklandığı sizin bulut hesabınız.

### 4. Temel Bileşenler
Workspace, Notebooks, Delta Lake, Unity Catalog.

### 5. Kullanım Alanları
Lakehouse kurulumu, MLOps, Ortak Veri Bilimi projeleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** En iyi Spark deneyimi, Birleşik platform, Lakehouse öncüsü.
* **Dezavantajlar:** Maliyet (Pahalı olabilir), Basit işler için karmaşık kaçabilir."""
            },
            "link": "https://www.databricks.com/", "modern": True, "dep": "Cloud",
            "code": """# Databricks Notebook Kodu
# Delta Tablosu okuma
df = spark.read.format("delta").load("/mnt/delta/events")
display(df)"""
        },
        "Hadoop MR": {
            "desc": {"en": "Legacy Batch Processing.", "tr": "Eski Nesil Toplu İşleme."},
            "detail": {
                "en": """### 1. Definition
MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

### 2. Core Purpose
To allow processing of data that is too large to fit into a single machine's memory by leveraging disk storage and processing power of multiple machines.

### 3. Architecture and Working Principle
* **Map Phase:** Filters and sorts data.
* **Shuffle & Sort:** Transfers data between nodes.
* **Reduce Phase:** Aggregates data.
It writes intermediate results to disk, making it fault-tolerant but slow.

### 4. Key Components
Mapper, Reducer, JobTracker (Legacy), TaskTracker.

### 5. Use Cases
Massive batch jobs where speed is not critical (e.g., nightly indexing). (Replaced by Spark).

### 6. Pros and Cons
* **Pros:** Scalability, Fault Tolerance, Simplicity of model.
* **Cons:** High Latency (Disk I/O), Verbose code (Java), Hard to manage chain of jobs.""",

                "tr": """### 1. Tanım
MapReduce; büyük veri setlerini paralel ve dağıtık bir algoritma ile işlemek için kullanılan bir programlama modelidir.

### 2. Temel Amaç
Tek bir makinenin belleğine sığmayacak kadar büyük verileri, çok sayıda makinenin disk ve işlemci gücünü kullanarak işlemek.

### 3. Mimari ve Çalışma Prensibi
* **Map Fazı:** Veriyi filtreler ve sıralar.
* **Shuffle & Sort:** Veriyi düğümler arası taşır.
* **Reduce Fazı:** Veriyi özetler (Toplar).
Her adımda ara sonuçları diske yazar, bu onu güvenilir ama yavaş yapar.

### 4. Temel Bileşenler
Mapper, Reducer.

### 5. Kullanım Alanları
Hızın kritik olmadığı devasa toplu işler. (Yerini Spark'a bırakmıştır).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Ölçeklenebilirlik, Hata Toleransı.
* **Dezavantajlar:** Yüksek Gecikme (Disk I/O), Çok kod yazma gereği (Java)."""
            },
            "link": "https://hadoop.apache.org/", "modern": False, "dep": "HDFS, YARN",
            "code": """public class WordCount {
  public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable>{...}
  public static class IntSumReducer extends Reducer<Text,IntWritable,Text,IntWritable>{...}
}"""
        }
    },
"Databases": {
        "Snowflake": {
            "desc": {"en": "Cloud Data Warehouse.", "tr": "Bulut Veri Ambarı."},
            "detail": {
                "en": """### 1. Definition
Snowflake is a cloud-native Modern Data Warehouse offered as SaaS, which completely separates storage and compute layers.

### 2. Core Purpose
To solve the flexibility issues of traditional data warehouses (Oracle Exadata, Teradata) and utilize the limitless resources of the cloud to automate data management (tuning, indexing) and increase concurrent query performance.

### 3. Architecture and Working Principle
Snowflake's revolutionary feature is the "Multi-Cluster Shared Data" architecture.
* **Storage:** Data is stored centrally on S3, Azure Blob, or GCS (Shared Data).
* **Compute:** Queries run on virtual clusters called "Virtual Warehouses".
* **Separation:** Storage and compute are independent. Different departments (Finance, Marketing) can work on the same data with different sized virtual machines without slowing each other down.

### 4. Key Components
* **Virtual Warehouse:** Compute power processing queries (measured in T-shirt sizes like XS, M, XL).
* **Snowpipe:** Service for continuous data ingestion.
* **Time Travel:** Ability to query data as it existed in the past (e.g., 5 hours ago).

### 5. Use Cases
Modern Data Sharing, BI Reporting (Tableau backend).

### 6. Pros and Cons
* **Pros:** Zero Management (No indexing/vacuuming), Concurrency (Scales instantly).
* **Cons:** Cost Control (Pay-as-you-go can lead to surprise bills), Vendor Lock-in (Cloud only).""",

                "tr": """### 1. Tanım
Snowflake; bulut için sıfırdan tasarlanmış (Cloud-Native), depolama ve hesaplama katmanlarını birbirinden tamamen ayıran, Hizmet Olarak Yazılım (SaaS) modeliyle sunulan bir Modern Veri Ambarıdır.

### 2. Temel Amaç
Geleneksel veri ambarlarının esneklik sorunlarını çözmek ve bulutun sınırsız kaynağını kullanarak; veri yönetimini otomatize etmek ve eşzamanlı (concurrency) sorgu performansını artırmaktır.

### 3. Mimari ve Çalışma Prensibi
Snowflake'in devrimsel özelliği "Multi-Cluster Shared Data" mimarisidir.
* **Depolama:** Veri S3, Azure Blob veya GCS üzerinde merkezi olarak durur.
* **Hesaplama:** Sorgular "Virtual Warehouse" adı verilen sanal kümelerde çalışır.
* **Ayrım:** Depolama ve işlemci bağımsızdır. Veriyi kopyalamadan, farklı departmanlar aynı veri üzerinde birbirini yavaşlatmadan çalışabilir.

### 4. Temel Bileşenler
Virtual Warehouse (Sanal Ambar), Snowpipe (Anlık Veri Alımı), Time Travel (Zamanda Yolculuk).

### 5. Kullanım Alanları
Modern Veri Paylaşımı, BI Raporlama.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Sıfır Yönetim (Bakım yok), Concurrency (Yavaşlama yok).
* **Dezavantajlar:** Maliyet Kontrolü (Sürpriz fatura riski), Vendor Lock-in (Sadece bulutta çalışır)."""
            },
            "link": "https://www.snowflake.com/", "modern": True, "dep": None,
            "code": """-- JSON veriyi sorgulama (Variant Type)
SELECT 
    v:device_type as device,
    v:location.city as city
FROM raw_logs
WHERE v:temperature > 20;"""
        },
        "PostgreSQL": {
            "desc": {"en": "Advanced RDBMS.", "tr": "Gelişmiş İlişkisel Veritabanı."},
            "detail": {
                "en": """### 1. Definition
PostgreSQL is an open-source Object-Relational Database Management System (ORDBMS) with over 30 years of active development, strictly adhering to SQL standards.

### 2. Core Purpose
To manage complex queries and large transactions faultlessly by prioritizing Data Integrity and reliability above all else.

### 3. Architecture and Working Principle
It has a classic "Process-based" architecture.
* **MVCC (Multiversion Concurrency Control):** While one user reads data, another can update it. Readers do not wait for locks; they see the old version. This ensures high concurrency.
* **WAL (Write-Ahead Logging):** Data is written to a log before disk, preventing data loss even during power failures.

### 4. Key Components
* **Postmaster:** The main managing process.
* **Shared Buffers:** Common memory area.
* **Extensions:** Features added later (Most famous: PostGIS for geospatial data).

### 5. Use Cases
Metadata Store (Airflow, Hive metastore), OLTP Systems (E-commerce, Banking).

### 6. Pros and Cons
* **Pros:** ACID Compliance, Extensibility (JSON, Geo), Horizontal Scaling (Read Replicas).
* **Cons:** Write Scaling (Sharding is hard), Speed (Slower than Redis for simple KV lookups).""",

                "tr": """### 1. Tanım
PostgreSQL; 30 yılı aşkın süredir geliştirilen, SQL standartlarına sıkı sıkıya bağlı, açık kaynaklı Nesne-İlişkisel Veritabanı Yönetim Sistemidir (ORDBMS).

### 2. Temel Amaç
Veri tutarlılığını (Data Integrity) ve güvenilirliği her şeyin üstünde tutarak, karmaşık sorguları ve büyük işlemleri (Transaction) hatasız yönetmektir.

### 3. Mimari ve Çalışma Prensibi
Klasik "Process-based" mimariye sahiptir.
* **MVCC:** Bir kullanıcı veriyi okurken, diğer kullanıcı güncelleyebilir. Okuyan kişi kilitlenmeyi beklemez, eski versiyonu görür.
* **WAL:** Veri diske yazılmadan önce günlüğe yazılır, veri kaybını önler.

### 4. Temel Bileşenler
Postmaster (Ana Süreç), Shared Buffers (Ortak Bellek), Extensions (Eklentiler - örn: PostGIS).

### 5. Kullanım Alanları
Metadata Store (Airflow, Hive vb.), OLTP Sistemler.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** ACID Uyumu, Genişletilebilirlik (JSON, Geo), Güvenilirlik.
* **Dezavantajlar:** Yazma Ölçeklenmesi (Sharding zordur), Hız (Basit okumalarda NoSQL'den yavaştır)."""
            },
            "link": "https://www.postgresql.org/", "modern": True, "dep": None,
            "code": """-- JSONB kullanımı
CREATE TABLE orders (
    id serial PRIMARY KEY,
    info jsonb
);

INSERT INTO orders (info) VALUES ('{"customer": "John", "items": ["book", "pen"]}');

SELECT info->>'customer' FROM orders WHERE info->'items' ? 'book';"""
        },
        "Neo4j": {
            "desc": {"en": "Graph Database.", "tr": "Graf Veritabanı."},
            "detail": {
                "en": """### 1. Definition
Neo4j is a Graph Database that treats relationships between data as first-class citizens.

### 2. Core Purpose
To performantly solve deep connection and relationship queries (like "movies my friend's friend liked") where relational databases (SQL) struggle.

### 3. Architecture and Working Principle
Stores data as "Nodes" and "Relationships" instead of tables.
* **Index-Free Adjacency:** Each node knows the physical address of the connected node. Navigating (hopping) between millions of connections takes milliseconds.

### 4. Key Components
* **Node:** Entity (e.g., John).
* **Relationship:** Connection (e.g., KNOWS).
* **Property:** Attribute (e.g., Age: 30).
* **Cypher:** SQL-like query language specific to graphs.

### 5. Use Cases
Fraud Detection, Social Networks, Recommendation Engines.

### 6. Pros and Cons
* **Pros:** Relationship Performance (No JOINs needed), Visual Mental Model.
* **Cons:** Scaling (Sharding graph data is very hard), Niche Use Case.""",

                "tr": """### 1. Tanım
Neo4j; veriler arasındaki ilişkileri (relationships) birinci sınıf vatandaş olarak ele alan, grafik tabanlı (Graph Database) bir veritabanıdır.

### 2. Temel Amaç
İlişkisel veritabanlarının (SQL) çok zorlandığı çok derin bağlantı ve ilişki sorgularını performanslı bir şekilde çözmektir.

### 3. Mimari ve Çalışma Prensibi
Veriyi tablolar yerine "Nodes" (Düğümler) ve "Relationships" (İlişkiler) olarak saklar.
* **Index-Free Adjacency:** Her düğüm, bağlı olduğu diğer düğümün adresini bilir. Milyonlarca bağlantı arasında gezinmek milisaniyeler sürer.

### 4. Temel Bileşenler
Node (Varlık), Relationship (İlişki), Property (Özellik), Cypher (Sorgu Dili).

### 5. Kullanım Alanları
Dolandırıcılık Tespiti, Sosyal Ağlar, Öneri Motorları.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** İlişki Performansı (JOIN gerektirmez), Görsellik.
* **Dezavantajlar:** Ölçeklenme (Sharding zordur), Niş Kullanım."""
            },
            "link": "https://neo4j.com/", "modern": True, "dep": None,
            "code": """// Cypher Sorgu Dili
MATCH (user:Person)-[:FRIEND]->(friend:Person)-[:LIKES]->(movie:Movie)
WHERE user.name = 'Ahmet'
RETURN movie.title"""
        },
        "Hive": {
            "desc": {"en": "SQL on Hadoop.", "tr": "Hadoop Veri Ambarı."},
            "detail": {
                "en": """### 1. Definition
Apache Hive is a data warehouse infrastructure built on top of Hadoop HDFS to query and analyze massive datasets using SQL-like language (HiveQL).

### 2. Core Purpose
To allow data analysts who do not know Java to query Petabytes of data on Hadoop using SQL, without writing complex MapReduce code.

### 3. Architecture and Working Principle
Hive is a "translator", not a database.
* User writes SQL.
* Hive translates this into MapReduce, Tez, or Spark jobs.
* Jobs run on the cluster and return results.

### 4. Key Components
* **Metastore:** Central database storing table definitions.
* **Driver:** Plans and optimizes queries.
* **Execution Engine:** The engine running the job (MapReduce, Tez, Spark).

### 5. Use Cases
ETL Processes, Batch Reporting.

### 6. Pros and Cons
* **Pros:** SQL Ease, Scalability (Petabytes).
* **Cons:** High Latency (Not real-time), Limited Transactions.""",

                "tr": """### 1. Tanım
Apache Hive; Hadoop HDFS üzerinde tutulan devasa veri setlerini sorgulamak ve analiz etmek için geliştirilmiş, SQL benzeri (HiveQL) bir veri ambarı altyapısıdır.

### 2. Temel Amaç
Java bilmeyen veri analistlerinin, karmaşık MapReduce kodları yazmadan, bildikleri SQL dilini kullanarak Hadoop üzerindeki veriyi sorgulayabilmesini sağlamaktır.

### 3. Mimari ve Çalışma Prensibi
Hive bir veritabanı değil, bir "çevirmen"dir. Kullanıcı SQL yazar, Hive bunu arka planda MapReduce veya Spark işlerine dönüştürür.

### 4. Temel Bileşenler
Metastore (Tablo tanımları), Driver (Planlayıcı), Execution Engine (İşlem Motoru).

### 5. Kullanım Alanları
ETL İşlemleri, Batch (Toplu) Raporlama.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** SQL Kolaylığı, Ölçeklenebilirlik.
* **Dezavantajlar:** Yüksek Gecikme (Gerçek zamanlı değildir), Transaction kısıtlıdır."""
            },
            "link": "https://hive.apache.org/", "modern": False, "dep": "HDFS, Hadoop MR",
            "code": """-- HiveQL
CREATE TABLE sales (
    id INT, 
    amount DOUBLE
) STORED AS ORC;

SELECT SUM(amount) FROM sales;"""
        },
        "BigQuery": {
            "desc": {"en": "Serverless Data Warehouse.", "tr": "Sunucusuz Veri Ambarı."},
            "detail": {
                "en": """### 1. Definition
BigQuery is a serverless, highly scalable, and cost-effective enterprise data warehouse offered on Google Cloud Platform (GCP).

### 2. Core Purpose
To query Terabytes of data in seconds using SQL without worrying about infrastructure management or capacity planning.

### 3. Architecture and Working Principle
Separates storage and compute.
* **Colossus:** Google's distributed file system.
* **Borg:** Cluster management system.
* **Columnar Storage:** Stores data in columns for compression and speed.

### 4. Key Components
* **Slots:** BigQuery's processing unit (Virtual CPU).
* **Project/Dataset/Table:** Data hierarchy.

### 5. Use Cases
Log Analytics, Real-time Analytics.

### 6. Pros and Cons
* **Pros:** Speed (Scans billions of rows in seconds), Serverless (No ops).
* **Cons:** Cost Uncertainty (Pay per query), Lock-in (GCP only).""",

                "tr": """### 1. Tanım
BigQuery; Google Cloud Platform (GCP) üzerinde sunulan, sunucusuz (serverless), yüksek ölçeklenebilir ve uygun maliyetli bir kurumsal veri ambarıdır.

### 2. Temel Amaç
Altyapı yönetimi ile uğraşmadan; saniyeler içinde Terabyte'larca veriyi SQL ile sorgulayabilmektir.

### 3. Mimari ve Çalışma Prensibi
Depolama ve hesaplamayı birbirinden ayırır.
* **Colossus:** Google'ın dağıtık dosya sistemi.
* **Borg:** Küme yönetim sistemi.
* **Columnar Storage:** Veriyi sütun bazlı saklar.

### 4. Temel Bileşenler
Slots (İşlem birimi), Dataset/Table hiyerarşisi.

### 5. Kullanım Alanları
Log Analitiği, Gerçek Zamanlı Analitik.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hız, Serverless (Sıfır operasyonel yük).
* **Dezavantajlar:** Maliyet Belirsizliği (Sorgu başına ücret), Lock-in."""
            },
            "link": "https://cloud.google.com/bigquery", "modern": True, "dep": "GCP",
            "code": """SELECT 
    start_station_name, 
    COUNT(*) as trips
FROM `bigquery-public-data.london_bicycles.cycle_hire`
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;"""
        },
        "CockroachDB": {
            "desc": {"en": "Distributed SQL.", "tr": "Dağıtık SQL (NewSQL)."},
            "detail": {
                "en": """### 1. Definition
CockroachDB is a cloud-native, distributed SQL database designed to be resilient against disasters.

### 2. Core Purpose
Named after the resilience of cockroaches; to survive disk, machine, rack, and even datacenter failures without data loss and keep running.

### 3. Architecture and Working Principle
Combines SQL features (JOIN, ACID) with NoSQL scalability.
* **Raft Consensus:** Ensures data consistency.
* **Ranges:** Splits data into 64MB chunks and distributes them automatically.

### 4. Key Components
Gateway Node, KV Store (RocksDB).

### 5. Use Cases
Global Applications (Multi-region), Financial Ledgers.

### 6. Pros and Cons
* **Pros:** Survivability (Resilient to failure), Geo-Partitioning.
* **Cons:** Performance (Higher latency than single-node Postgres), Resource intensive.""",

                "tr": """### 1. Tanım
CockroachDB; bulut tabanlı, dağıtık ve özellikle felaketlere karşı dayanıklı (resilient) olacak şekilde tasarlanmış bir Dağıtık SQL veritabanıdır.

### 2. Temel Amaç
İsmini hamamböceklerinin dayanıklılığından alır. Veri merkezi çökse bile veri kaybı yaşatmamak ve sistemi durdurmadan çalışmaya devam etmektir.

### 3. Mimari ve Çalışma Prensibi
SQL özelliklerini (ACID, JOIN) NoSQL ölçeklenebilirliği ile birleştirir.
* **Raft:** Veri tutarlılığını sağlar.
* **Ranges:** Veriyi 64MB'lık parçalara böler ve dağıtır.

### 4. Temel Bileşenler
Gateway Node, KV Store (RocksDB).

### 5. Kullanım Alanları
Global Uygulamalar, Finansal Kayıt Sistemleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hayatta Kalma (Felaket kurtarma), Geo-Partitioning (Veriyi ülkesinde tutma).
* **Dezavantajlar:** Performans (Gecikme daha yüksektir), Kaynak kullanımı."""
            },
            "link": "https://www.cockroachlabs.com/", "modern": True, "dep": None,
            "code": """-- Multi-region tablo
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    city STRING,
    name STRING
) LOCALITY REGIONAL BY ROW AS city;"""
        },
        "Druid": {
            "desc": {"en": "Real-time Analytics.", "tr": "Gerçek Zamanlı Analitik."},
            "detail": {
                "en": """### 1. Definition
Apache Druid is a high-performance data store designed for real-time analytics on large datasets with sub-second response times.

### 2. Core Purpose
To fill the gap of "interactive analytics" where data warehouses are too slow and operational databases lack analytical power. Optimized for Event data.

### 3. Architecture and Working Principle
Uses a Lambda-like architecture.
* **Real-time Nodes:** Ingest stream data immediately.
* **Historical Nodes:** Store deep storage data.
* **Broker:** Routes queries.

### 4. Key Components
Segment, Coordinator, Overlord.

### 5. Use Cases
Clickstream Analysis, APM (Application Performance Monitoring), Digital Advertising.

### 6. Pros and Cons
* **Pros:** Ultra Speed (Sub-second), Live Data querying.
* **Cons:** No Transactions (Updates are hard), Operational Overhead (Many components).""",

                "tr": """### 1. Tanım
Apache Druid; büyük veri setleri üzerinde milisaniyenin altında yanıt süreleri ile gerçek zamanlı analitik yapabilmek için tasarlanmış yüksek performanslı bir veri deposudur.

### 2. Temel Amaç
Veri ambarlarının yavaş kaldığı "etkileşimli analiz" boşluğunu doldurmaktır. Özellikle "Olay" (Event) verisi için optimize edilmiştir.

### 3. Mimari ve Çalışma Prensibi
Lambda mimarisine benzer.
* **Real-time Nodes:** Akan veriyi anında alır ve sorgulanabilir kılar.
* **Historical Nodes:** Eski verileri saklar.
* **Broker:** Sorguyu dağıtır.

### 4. Temel Bileşenler
Segment, Coordinator, Overlord.

### 5. Kullanım Alanları
Clickstream (Tıklama) Analizi, Uygulama Performans İzleme (APM), Dijital Reklamcılık.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Ultra Hız, Canlı Veri Sorgulama.
* **Dezavantajlar:** Transaction Yok, Operasyonel Yük (Çok fazla bileşen)."""
            },
            "link": "https://druid.apache.org/", "modern": True, "dep": "Zookeeper",
            "code": """// JSON tabanlı sorgu (Native)
{
  "queryType": "timeseries",
  "dataSource": "sample_data",
  "intervals": [ "2023-01-01/2023-01-02" ],
  "granularity": "hour"
}"""
        },
        "ClickHouse": {
            "desc": {"en": "Real-time OLAP.", "tr": "Hızlı Analitik DB."},
            "detail": {
                "en": "A column-oriented database management system aimed at interactive analytics. It allows querying billions of rows in milliseconds.",
                "tr": "Analitik sorgular için optimize edilmiş sütun tabanlı veritabanı. Milyarlarca satır üzerinde saniyeler içinde toplama (Sum, Avg) işlemi yapar. Log analitiği için harikadır."
            },
            "link": "https://clickhouse.com/", "modern": True, "dep": "Zookeeper",
            "code": "SELECT Region, SUM(Sales) FROM orders GROUP BY Region;"
        },
        "Cassandra": {
            "desc": {"en": "Wide-Column.", "tr": "Geniş Sütunlu NoSQL."},
            "detail": {
                "en": "Distributed NoSQL database designed for handling large amounts of data across many commodity servers. Masterless architecture.",
                "tr": "Merkezi olmayan (Masterless) mimari. Sunuculardan biri çökse bile sistem çalışır. Yazma hızı çok yüksektir. Facebook tarafından geliştirilmiştir."
            },
            "link": "https://cassandra.apache.org/", "modern": True, "dep": None,
            "code": "SELECT * FROM users WHERE user_id = 123;"
        },
        "HBase": {
            "desc": {"en": "Hadoop DB.", "tr": "Hadoop Veritabanı."},
            "detail": {
                "en": "Modeled after Google BigTable. Runs on top of HDFS. Provides random read/write access to Big Data.",
                "tr": "HDFS üzerinde çalışan, rastgele erişim sağlayan NoSQL veritabanı. Petabaytlarca veriyi saklayabilir."
            },
            "link": "https://hbase.apache.org/", "modern": False, "dep": "HDFS, Zookeeper",
            "code": "put 'table', 'row1', 'cf:col', 'value'"
        },
        "MongoDB": {
            "desc": {"en": "Document DB.", "tr": "Doküman NoSQL."},
            "detail": {
                "en": "Stores data in JSON-like documents. Flexible schema allows for rapid iteration and handling unstructured data.",
                "tr": "Veriyi JSON benzeri (BSON) dokümanlar olarak saklar. Esnek şeması sayesinde uygulama geliştirmeyi hızlandırır."
            },
            "link": "https://www.mongodb.com/", "modern": True, "dep": None,
            "code": "db.collection.find({ 'status': 'A' })"
        },
        "Redis": {
            "desc": {"en": "In-Memory.", "tr": "Bellek İçi."},
            "detail": {
                "en": "In-memory key-value store used as a database, cache, and message broker. Offers sub-millisecond response times.",
                "tr": "Veriyi RAM'de tutan anahtar-değer deposu. Önbellek (Cache) olarak kullanılır. Mikrosaniye seviyesinde yanıt verir."
            },
            "link": "https://redis.io/", "modern": True, "dep": None,
            "code": "SET user:100 'Omer'\nGET user:100"
        },
        "Elasticsearch": {
            "desc": {"en": "Search Engine.", "tr": "Arama Motoru."},
            "detail": {
                "en": "Distributed search engine built on Lucene. Stores data as JSON and uses inverted indices for fast full-text search.",
                "tr": "Lucene tabanlı metin arama ve analiz motorudur. Ters dizin mantığıyla çok hızlı arama yapar. Log analitiği için kullanılır."
            },
            "link": "https://www.elastic.co/", "modern": True, "dep": None,
            "code": "GET /_search?q=message:error"
        }
    },
    "Orchestration": {
        "Airflow": {
            "desc": {"en": "Workflow Orchestrator.", "tr": "İş Akışı Yöneticisi."},
            "detail": {
                "en": """### 1. Definition
Apache Airflow is an open-source workflow orchestration platform to programmatically author, schedule, and monitor workflows. Developed by Airbnb.

### 2. Core Purpose
To manage dependencies like "Do task A, if successful do B, else do C". Adopts the "Configuration as Code" principle.

### 3. Architecture and Working Principle
Airflow is based on the concept of **DAG** (Directed Acyclic Graph).
* **Scheduler:** Triggers scheduled tasks.
* **Executor:** Determines where tasks run (Local, Kubernetes, Celery).
* **Web Server:** Provides a UI to monitor tasks.

### 4. Key Components
* **DAG:** Workflow definition in Python code.
* **Operator:** Template determining what a task does (PythonOperator, BashOperator).
* **Task:** A running instance of an Operator.
* **Metadata Database:** Stores the state of all tasks.

### 5. Use Cases
ETL Automation, ML Pipelines.

### 6. Pros and Cons
* **Pros:** Python based, Huge community, Extensible.
* **Cons:** Not real-time (Batch focused), Data Awareness limited (Task-based, not data-based).""",

                "tr": """### 1. Tanım
Apache Airflow; karmaşık veri iş akışlarını (workflows) programatik olarak oluşturmak, zamanlamak ve izlemek için geliştirilmiş, Python tabanlı, açık kaynaklı bir iş akışı orkestrasyon platformudur. Airbnb tarafından geliştirilmiştir.

### 2. Temel Amaç
Veri mühendisliğinde "Önce A işini yap, biterse B'yi yap, hata alırsa C'yi yap" şeklindeki bağımlılıkları (dependency) yönetmektir. "Configuration as Code" (Kod olarak konfigürasyon) prensibini benimser.

### 3. Mimari ve Çalışma Prensibi
Airflow'un kalbinde **DAG** (Yönlü Döngüsüz Çizge) kavramı yatar.
* **Scheduler:** Planlanan zamanı gelen işleri tetikler.
* **Executor:** İşin nerede çalışacağını belirler (Local, Kubernetes, Celery vb.).
* **Web Server:** İşlerin durumunu izlemek için görsel arayüz sunar.

### 4. Temel Bileşenler
* **DAG:** İş akışının Python kodu ile tanımı.
* **Operator:** Bir işin ne yapacağını belirleyen şablon (PythonOperator, BashOperator).
* **Task:** Operator'ün çalışan hali.
* **Metadata Database:** Tüm işlerin durumunu tutan veritabanı.

### 5. Kullanım Alanları
ETL Otomasyonu, ML Pipeline (Model eğitimi).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Python tabanlı, Geniş topluluk.
* **Dezavantajlar:** Gecikme (Batch odaklıdır), Veri Farkındalığı düşüktür (İş bitti der, veri doğru mu bilmez)."""
            },
            "link": "https://airflow.apache.org/", "modern": True, "dep": "DB",
            "code": """from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('my_pipeline', start_date=datetime(2023, 1, 1)) as dag:
    
    t1 = BashOperator(
        task_id='extract',
        bash_command='python extract.py'
    )

    t2 = BashOperator(
        task_id='load',
        bash_command='python load.py'
    )

    t1 >> t2  # t1 bittikten sonra t2 başlasın"""
        },
        "Kubernetes": {
            "desc": {"en": "Container Orchestration.", "tr": "Konteyner Orkestrasyonu."},
            "detail": {
                "en": """### 1. Definition
Kubernetes (K8s) is an open-source container orchestration system for automating application deployment, scaling, and management. Developed by Google.

### 2. Core Purpose
To manage hundreds or thousands of containers like a "conductor". If a server fails, it automatically restarts containers on another server (Self-healing).

### 3. Architecture and Working Principle
Works on the "Desired State" principle.
* **Control Plane (Master):** The brain making decisions.
* **Worker Nodes:** Servers where the work happens.

### 4. Key Components
* **Pod:** The smallest unit in K8s. Holds one or more containers.
* **Kubelet:** Agent running on each node ensuring Pods are healthy.
* **etcd:** Key-value store holding cluster data.
* **Service:** Network layer exposing Pods.

### 5. Use Cases
Microservices, Big Data on K8s (Spark, Flink).

### 6. Pros and Cons
* **Pros:** Portability, Auto-scaling, Self-healing.
* **Cons:** Steep learning curve, Complexity overhead.""",

                "tr": """### 1. Tanım
Kubernetes; konteynerize edilmiş uygulamaların dağıtımını, ölçeklendirilmesini ve yönetimini otomatize eden, açık kaynaklı bir konteyner orkestrasyon sistemidir. Google tarafından geliştirilmiştir.

### 2. Temel Amaç
Yüzlerce konteyneri bir "orkestra şefi" gibi yönetmektir. Bir sunucu çökerse, üzerindeki konteynerleri otomatik olarak başka sunucuda başlatır (Self-healing).

### 3. Mimari ve Çalışma Prensibi
"Arzulanan Durum" (Desired State) prensibiyle çalışır.
* **Control Plane (Master):** Beyin takımıdır. Kararları verir.
* **Worker Nodes:** İşin yapıldığı sunuculardır.

### 4. Temel Bileşenler
* **Pod:** Kubernetes'in en küçük birimidir. İçinde bir veya daha fazla konteyner barındırır.
* **Kubelet:** Her sunucuda çalışan ajan.
* **etcd:** Kümenin tüm bilgilerini tutan anahtar-değer deposu.
* **Service:** Ağ katmanı.

### 5. Kullanım Alanları
Mikroservisler, K8s üzerinde Big Data (Spark, Flink).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Taşınabilirlik, Otomatik Ölçekleme.
* **Dezavantajlar:** Karmaşıklık, Öğrenme eğrisi çok diktir."""
            },
            "link": "https://kubernetes.io/", "modern": True, "dep": "Docker",
            "code": """# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80"""
        },
        "Docker": {
            "desc": {"en": "Containerization.", "tr": "Konteynerleştirme."},
            "detail": {
                "en": """### 1. Definition
Docker is a platform that packages applications with all their dependencies into standardized units called containers.

### 2. Core Purpose
To solve the "it works on my machine" problem (Dependency Hell). Provides lightweight isolation compared to VMs.

### 3. Architecture and Working Principle
Shares the OS Kernel but isolates processes.
* **Image:** Read-only template of the application.
* **Container:** Running instance of an image.

### 4. Key Components
* **Dockerfile:** Recipe for building an image.
* **Docker Daemon:** Background process managing containers.
* **Docker Hub:** Registry for images.

### 5. Use Cases
CI/CD, Microservices.

### 6. Pros and Cons
* **Pros:** Speed (Starts in seconds), Efficiency.
* **Cons:** Security (Shared kernel), Ephemeral data.""",

                "tr": """### 1. Tanım
Docker; uygulamaları tüm bağımlılıkları ile birlikte paketleyerek her ortamda aynı şekilde çalışmasını sağlayan konteynerizasyon platformudur.

### 2. Temel Amaç
"Benim makinemde çalışıyordu" sorununu ortadan kaldırmaktır. Sanal makinelere (VM) göre çok daha hafif bir izolasyon sağlar.

### 3. Mimari ve Çalışma Prensibi
İşletim sistemi çekirdeğini (Kernel) paylaşır, süreçleri izole eder.
* **Image (İmaj):** Uygulamanın dondurulmuş şablonudur.
* **Container:** İmajın çalışan halidir.

### 4. Temel Bileşenler
* **Dockerfile:** İmaj reçetesi.
* **Docker Daemon:** Konteynerleri yöneten motor.
* **Docker Hub:** İmaj deposu.

### 5. Kullanım Alanları
CI/CD, Mikroservisler.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hız (Saniyeler içinde başlar), Verimlilik.
* **Dezavantajlar:** Güvenlik (Kernel paylaşımı), Kalıcılık (Konteyner silinince veri gider)."""
            },
            "link": "https://www.docker.com/", "modern": True, "dep": None,
            "code": """# Dockerfile Örneği
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app.py"]"""
        },
        "Dagster": {
            "desc": {"en": "Data Orchestrator.", "tr": "Veri Odaklı Orkestratör."},
            "detail": {
                "en": """### 1. Definition
Dagster is a next-generation data orchestrator designed around data assets (tables, ML models) rather than tasks.

### 2. Core Purpose
To solve the "Data Awareness" problem of Airflow. Instead of "Task A -> Task B", it focuses on "Table A updated -> Produce Table B".

### 3. Architecture and Working Principle
Uses "Asset-based Orchestration". Focuses on the produced data (Asset).

### 4. Key Components
* **Asset:** The data produced.
* **Op:** The function processing data.
* **Dagit:** Advanced UI.

### 5. Use Cases
Modern Data Stack, Data Quality testing.

### 6. Pros and Cons
* **Pros:** Data-centric, Testability.
* **Cons:** Newer ecosystem than Airflow.""",

                "tr": """### 1. Tanım
Dagster; veri varlıklarını (Data Assets - Tablolar, ML Modelleri) merkeze alan, yeni nesil bir veri orkestratörüdür.

### 2. Temel Amaç
Airflow'un "Veri Farkındalığı" eksiğini çözmektir. Görev sırasına değil, üretilen veriye (Asset) odaklanır. Yazılım mühendisliği prensiplerini veri dünyasına getirir.

### 3. Mimari ve Çalışma Prensibi
"Varlık tabanlı orkestrasyon" (Asset-based Orchestration) kullanır.

### 4. Temel Bileşenler
* **Asset:** Üretilen veri (Örn: users_table).
* **Op:** Veriyi işleyen fonksiyon.
* **Dagit:** Görsel arayüz.

### 5. Kullanım Alanları
Modern Data Stack, Veri Kalitesi testleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Veri Odaklı, Test Edilebilirlik.
* **Dezavantajlar:** Popülarite (Henüz Airflow kadar yaygın değil)."""
            },
            "link": "https://dagster.io/", "modern": True, "dep": None,
            "code": """from dagster import asset

@asset
def my_table():
    return [1, 2, 3]

@asset
def derived_table(my_table):
    return [x * 2 for x in my_table]"""
        },
        "Zookeeper": {
            "desc": {"en": "Distributed Coordination.", "tr": "Merkezi Koordinasyon Servisi."},
            "detail": {
                "en": """### 1. Definition
Apache ZooKeeper is a high-performance coordination service for distributed applications.

### 2. Core Purpose
Solves hard problems like Synchronization, Leader Election, and Configuration Management in distributed systems.

### 3. Architecture and Working Principle
Uses a file-system-like namespace. Keeps data in RAM for speed.
* **Leader/Follower:** One leader handles writes, others follow.

### 4. Key Components
* **Znode:** Data node.
* **Ensemble:** Cluster of ZooKeeper servers.

### 5. Use Cases
Kafka metadata management, Hadoop HA.

### 6. Pros and Cons
* **Pros:** Reliability, Simplicity.
* **Cons:** Management complexity (Java based), Modern tools are replacing it.""",

                "tr": """### 1. Tanım
Apache ZooKeeper; dağıtık uygulamalar için yüksek performanslı bir koordinasyon servisidir.

### 2. Temel Amaç
Dağıtık sistemlerdeki Senkronizasyon, Lider Seçimi ve Konfigürasyon Yönetimi gibi zor problemleri çözer. Kafka ve Hadoop'un "trafik polisi"dir.

### 3. Mimari ve Çalışma Prensibi
Dosya sistemine benzer bir yapı kullanır. Veriyi RAM'de tutar.
* **Leader/Follower:** Yazma işlemlerini Lider yapar, diğerleri takip eder.

### 4. Temel Bileşenler
* **Znode:** Veri düğümü.
* **Ensemble:** ZooKeeper kümesi.

### 5. Kullanım Alanları
Kafka (Eski sürümler), Hadoop HA.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Güvenilirlik.
* **Dezavantajlar:** Yönetim Zorluğu, Eskime (Yerini KRaft ve etcd alıyor)."""
            },
            "link": "https://zookeeper.apache.org/", "modern": False, "dep": "JVM",
            "code": """# Zookeeper CLI
ls /brokers/ids
get /config/topics/my-topic"""
        },
        "YARN": {
            "desc": {"en": "Resource Manager.", "tr": "Kaynak Yöneticisi."},
            "detail": {
                "en": """### 1. Definition
YARN (Yet Another Resource Negotiator) is Hadoop's resource management layer.

### 2. Core Purpose
To manage RAM and CPU resources in a cluster and share them among different applications like Spark, MapReduce, Hive.

### 3. Architecture
* **ResourceManager:** Master. Manages global resources.
* **NodeManager:** Slave. Runs on each node.

### 4. Key Components
ResourceManager, NodeManager, ApplicationMaster.

### 5. Use Cases
Hadoop Clusters (Multi-tenant).

### 6. Pros and Cons
* **Pros:** Efficiency, Multi-tenancy.
* **Cons:** Declining popularity due to K8s.""",

                "tr": """### 1. Tanım
YARN; Hadoop ekosisteminin kaynak yönetim katmanıdır. "Big Data'nın İşletim Sistemi" olarak anılır.

### 2. Temel Amaç
Bir sunucu kümesindeki RAM ve CPU kaynaklarını yönetmek ve bunları farklı uygulamalar (Spark, Hive) arasında paylaştırmaktır.

### 3. Mimari
* **ResourceManager:** Patron (Master).
* **NodeManager:** İşçi (Slave).

### 4. Temel Bileşenler
ResourceManager, NodeManager, ApplicationMaster.

### 5. Kullanım Alanları
Hadoop Kümeleri.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Verimlilik, Çoklu Kiracı.
* **Dezavantajlar:** Modernite (Kubernetes karşısında popülaritesi azalıyor)."""
            },
            "link": "https://hadoop.apache.org/", "modern": False, "dep": None,
            "code": """# YARN CLI
yarn application -list
yarn node -list"""
        },
        "Prometheus": {
            "desc": {"en": "Monitoring System.", "tr": "Sistem İzleme Aracı."},
            "detail": {
                "en": """### 1. Definition
Prometheus is an open-source systems monitoring and alerting toolkit. Standard for K8s monitoring.

### 2. Core Purpose
To collect and store time-series data (metrics) and alert on issues.

### 3. Architecture and Working Principle
Uses a **Pull Model**. It scrapes metrics from targets. Stores data in its own TSDB.

### 4. Key Components
* **Server:** Collects and stores data.
* **Exporters:** Agents that expose metrics.
* **Alertmanager:** Handles alerts.

### 5. Use Cases
Kubernetes Monitoring, Infrastructure Monitoring.

### 6. Pros and Cons
* **Pros:** Speed, K8s native.
* **Cons:** Long-term storage (Needs Thanos), Visualization (Needs Grafana).""",

                "tr": """### 1. Tanım
Prometheus; özellikle mikroservis ve konteyner yapıları için tasarlanmış, açık kaynaklı sistem izleme ve uyarı aracıdır.

### 2. Temel Amaç
Zaman serisi verilerini (CPU, RAM, Request Count) toplamak ve sorun olduğunda uyarı vermektir.

### 3. Mimari ve Çalışma Prensibi
**Pull Model (Çekme)** kullanır. Hedeflere gidip veriyi kendisi alır. Veriyi kendi özel veritabanında saklar.

### 4. Temel Bileşenler
Prometheus Server, Exporters (Veri ajanları), Alertmanager.

### 5. Kullanım Alanları
Kubernetes İzleme, Altyapı İzleme.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hız, K8s Uyumu.
* **Dezavantajlar:** Uzun Süreli Saklama (Thanos gerekir), Görsellik (Grafana gerekir)."""
            },
            "link": "https://prometheus.io/", "modern": True, "dep": None,
            "code": """# prometheus.yml
scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']"""
        },
        "cAdvisor": {
            "desc": {"en": "Container Monitoring.", "tr": "Konteyner Kaynak İzleme."},
            "detail": {
                "en": """### 1. Definition
cAdvisor (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers.

### 2. Core Purpose
To collect real-time metrics (RAM, CPU) from individual containers.

### 3. Architecture
Runs as a daemon on each node. Scrapes data from Docker.

### 4. Components
Web UI, REST API.

### 5. Use Cases
Source for Prometheus scraping.

### 6. Pros and Cons
* **Pros:** Simple, Auto-discovery.
* **Cons:** No Storage (Needs DB).""",

                "tr": """### 1. Tanım
cAdvisor; çalışan konteynerlerin kaynak kullanımını ve performans özelliklerini analiz eden hafif bir ajandır.

### 2. Temel Amaç
Tekil bir sunucu üzerindeki konteynerlerin anlık CPU/RAM bilgilerini toplamaktır.

### 3. Mimari
Her sunucuda bir tane çalışır. Docker ile konuşur.

### 4. Temel Bileşenler
Web UI, REST API.

### 5. Kullanım Alanları
Prometheus için veri kaynağı.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Basitlik, Otomatik Keşif.
* **Dezavantajlar:** Depolama Yok (Veriyi saklamaz, sadece anlık gösterir)."""
            },
            "link": "https://github.com/google/cadvisor", "modern": True, "dep": "Docker",
            "code": """# Docker ile Çalıştırma
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  google/cadvisor:latest"""
        }
    },
    "Serving/BI": {
        "Streamlit": {
            "desc": {"en": "Data Apps Framework.", "tr": "Veri Uygulama Çatısı."},
            "detail": {
                "en": """### 1. Definition
Streamlit is an open-source app framework designed specifically for Data Scientists and Machine Learning Engineers to create interactive web apps using only Python.

### 2. Core Purpose
To allow data scientists to turn their analysis, charts, or ML models into shareable web apps ("Data Apps") in seconds without needing to know HTML, CSS, or JavaScript (Frontend).

### 3. Architecture and Working Principle
Streamlit relies on the "Script-run" principle.
* When a user interacts with a widget, Streamlit reruns the entire Python script from top to bottom.
* It uses React.js in the background but abstracts it away from the developer.

### 4. Key Components
* **Widgets:** Buttons, sliders, text inputs.
* **Caching:** Mechanism (@st.cache) to prevent re-running heavy computations.
* **Session State:** Persists variables across reruns.

### 5. Use Cases
ML Model Prototyping, Internal Tools.

### 6. Pros and Cons
* **Pros:** Speed (Build an app in 50 lines), Pure Python.
* **Cons:** Customization limits (Layout is rigid), Not for massive enterprise apps.""",

                "tr": """### 1. Tanım
Streamlit; özellikle Veri Bilimciler ve Makine Öğrenimi mühendisleri için tasarlanmış, sadece Python kodu yazarak interaktif web uygulamaları oluşturmayı sağlayan açık kaynaklı bir uygulama çatısıdır.

### 2. Temel Amaç
Bir veri bilimcinin, Frontend (HTML/CSS/JS) bilmesine gerek kalmadan; analizlerini veya ML modellerini saniyeler içinde paylaşılabilir bir web uygulamasına ("Data App") dönüştürmesini sağlamaktır.

### 3. Mimari ve Çalışma Prensibi
Streamlit'in çalışma mantığı "Script-run" prensibine dayanır.
* Kullanıcı bir etkileşimde bulunduğunda, Streamlit tüm Python kodunu baştan sona tekrar çalıştırır.
* Arka planda React.js kullanır ancak geliştirici sadece saf Python yazar.

### 4. Temel Bileşenler
* **Widgets:** Butonlar, kaydırıcılar, metin kutuları.
* **Caching:** Ağır işlemleri tekrar yapmamak için önbellek mekanizması (@st.cache).
* **Session State:** Etkileşimler sırasında değişkenlerin değerini koruyan yapı.

### 5. Kullanım Alanları
ML Model Prototipleme, Şirket İçi Araçlar.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Hız (50 satırla uygulama), Sadece Python bilgisi yeterli.
* **Dezavantajlar:** Özelleştirme kısıtlıdır, Çok büyük uygulamalar için uygun değildir."""
            },
            "link": "https://streamlit.io/", "modern": True, "dep": "Python",
            "code": """import streamlit as st
import pandas as pd

st.title("Veri Analiz Paneli")
st.write("Veri setinizi yükleyin:")

uploaded_file = st.file_uploader("CSV Seç", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.bar_chart(df.select_dtypes(include=['number']))"""
        },
        "Superset": {
            "desc": {"en": "Modern Open Source BI.", "tr": "Modern Açık Kaynak İş Zekası."},
            "detail": {
                "en": """### 1. Definition
Apache Superset is an enterprise-grade open-source Business Intelligence (BI) platform designed for modern data stacks to explore and visualize large-scale data.

### 2. Core Purpose
To provide a powerful open-source alternative to expensive proprietary BI tools (Tableau, PowerBI) and enable SQL-savvy users to deeply analyze data.

### 3. Architecture and Working Principle
It has a Cloud-native architecture. Uses Python (Flask) for the backend.
* **SQLAlchemy:** Uses this ORM to connect to almost any SQL-speaking database.
* **Caching:** Caches query results to improve performance.

### 4. Key Components
* **SQL Lab:** Advanced SQL editor.
* **Semantic Layer:** Layer to define virtual metrics and calculated columns.
* **Explore:** No-code chart creation interface.

### 5. Use Cases
Modern Data Teams (Airbnb, Netflix), Big Data Visualization (Geo-spatial).

### 6. Pros and Cons
* **Pros:** Huge connectivity (Hive, Presto, Druid), Rich visualizations (Deck.gl).
* **Cons:** Learning curve (Technical), Complex JOINs are harder in UI.""",

                "tr": """### 1. Tanım
Apache Superset; modern veri yığınları için geliştirilmiş, büyük ölçekli verileri keşfetmeye ve görselleştirmeye yarayan, kurumsal seviyede açık kaynaklı bir İş Zekası (BI) platformudur.

### 2. Temel Amaç
Pahalı lisanslı BI araçlarına güçlü bir açık kaynak alternatif sunmak; SQL bilen kullanıcıların veritabanındaki veriyi derinlemesine analiz etmesini sağlamaktır.

### 3. Mimari ve Çalışma Prensibi
Bulut tabanlı bir mimariye sahiptir. Web sunucusu olarak Python (Flask) kullanır.
* **SQLAlchemy:** Veritabanı bağlantıları için bu kütüphaneyi kullanır, SQL konuşan her şeye bağlanır.
* **Caching:** Sorgu sonuçlarını önbelleğe alır.

### 4. Temel Bileşenler
* **SQL Lab:** Gelişmiş SQL editörü.
* **Semantic Layer:** Sanal metrik tanımlama katmanı.
* **Explore:** Kod yazmadan grafik oluşturma arayüzü.

### 5. Kullanım Alanları
Modern Veri Ekipleri, Büyük Veri Görselleştirme.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Geniş Bağlantı (Hive, Presto, Snowflake), Zengin Görsellik.
* **Dezavantajlar:** Öğrenme Eğrisi (Teknik bilgi ister), Arayüzde JOIN yapmak zordur."""
            },
            "link": "https://superset.apache.org/", "modern": True, "dep": None,
            "code": """-- SQL Lab Sorgusu
SELECT 
    country_name,
    COUNT(*) as user_count
FROM users
WHERE signup_date >= '2023-01-01'
GROUP BY country_name
ORDER BY user_count DESC
LIMIT 10;"""
        },
        "Tableau": {
            "desc": {"en": "Visual Analytics Platform.", "tr": "Görsel Analitik Platformu."},
            "detail": {
                "en": """### 1. Definition
Tableau is a market-leading visual analytics platform that makes data analysis accessible via a drag-and-drop interface. Owned by Salesforce.

### 2. Core Purpose
To help people "see and understand data". Enables non-technical users to create their own reports (Self-Service BI) without IT support.

### 3. Architecture and Working Principle
Powered by **VizQL** (Visual Query Language).
* When a user drags a field, VizQL converts this action into an optimized database query and renders the result as a chart.
* Supports **Live** connection or **Extract** (Hyper Engine).

### 4. Key Components
Desktop, Server/Cloud, Prep (Data cleaning).

### 5. Use Cases
Executive Dashboards, Financial Reporting.

### 6. Pros and Cons
* **Pros:** Ease of use, Huge Community.
* **Cons:** High Cost, Performance on massive live data.""",

                "tr": """### 1. Tanım
Tableau; veriyi analiz etmeyi ve görselleştirmeyi herkes için erişilebilir kılan, sürükle-bırak mantığıyla çalışan, pazar lideri bir görsel analitik platformudur.

### 2. Temel Amaç
İnsanların veriyi "görmesini ve anlamasını" sağlamaktır. Teknik olmayan kullanıcıların kendi raporlarını (Self-Service BI) hazırlamasına olanak tanır.

### 3. Mimari ve Çalışma Prensibi
Kalbinde **VizQL** teknolojisi yatar.
* Kullanıcı ekrana bir tabloyu sürüklediğinde, VizQL bunu arka planda optimize edilmiş bir veritabanı sorgusuna dönüştürür ve grafiği çizer.
* **Canlı (Live)** veya **Özet (Extract)** modunda çalışabilir.

### 4. Temel Bileşenler
Tableau Desktop, Server/Cloud, Prep (Veri temizleme).

### 5. Kullanım Alanları
Yönetici Dashboardları, Finansal Raporlama.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Kullanım Kolaylığı, Geniş Topluluk.
* **Dezavantajlar:** Yüksek Maliyet, Çok büyük canlı verilerde performans."""
            },
            "link": "https://www.tableau.com/", "modern": True, "dep": None,
            "code": """# Tableau Prep Flow (Kavramsal)
Input(Sales_Data) -> Clean(Remove Nulls) -> Aggregate(Sum Sales by Region) -> Output(Hyper File)"""
        },
        "Grafana": {
            "desc": {"en": "Observability Platform.", "tr": "Gözlemlenebilirlik Paneli."},
            "detail": {
                "en": """### 1. Definition
Grafana is an open-source Observability platform used to query, visualize, and alert on metrics, logs, and traces regardless of where they are stored.

### 2. Core Purpose
To monitor the health of systems, servers, apps, or IoT devices from a "Single Pane of Glass". Focuses on "Operational Data" (CPU, RAM) rather than Business Data.

### 3. Architecture and Working Principle
Grafana does not store data itself. It pulls data from sources in real-time.
* **Plugin Architecture:** Connects to dozens of sources (Prometheus, InfluxDB, MySQL) simultaneously.

### 4. Key Components
Dashboard, Alerting Engine, Loki/Tempo (Logs/Traces).

### 5. Use Cases
DevOps Monitoring (K8s), Industrial IoT.

### 6. Pros and Cons
* **Pros:** Flexibility, Visualization (Dark mode friendly).
* **Cons:** No Data Storage (Relies on source), Learning curve for queries.""",

                "tr": """### 1. Tanım
Grafana; metrikleri, logları ve izleri nerede tutulduklarına bakılmaksızın sorgulamak, görselleştirmek ve uyarı üretmek için kullanılan açık kaynaklı bir Gözlemlenebilirlik platformudur.

### 2. Temel Amaç
Sistemlerin, sunucuların veya IoT cihazlarının sağlığını tek bir ekrandan izlemektir. "İş verisi"nden ziyade "Operasyonel veri"ye (CPU, RAM) odaklanır.

### 3. Mimari ve Çalışma Prensibi
Grafana veriyi kendisi saklamaz. Veriyi kaynağından anlık çeker.
* **Plugin Mimarisi:** Prometheus, InfluxDB, Elasticsearch gibi onlarca kaynağa aynı anda bağlanabilir.

### 4. Temel Bileşenler
Dashboard, Alerting Engine (Uyarı Motoru), Loki/Tempo.

### 5. Kullanım Alanları
DevOps İzleme (K8s), Endüstriyel IoT.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Esneklik (Her veritabanını birleştirir), Görsellik.
* **Dezavantajlar:** Veri Saklamaz, Kaynağa bağımlıdır."""
            },
            "link": "https://grafana.com/", "modern": True, "dep": None,
            "code": """// PromQL Sorgusu (Grafana Panelinde)
rate(http_requests_total{status="500"}[5m]) > 10"""
        },
        "Metabase": {
            "desc": {"en": "Simple BI.", "tr": "Basit İş Zekası."},
            "detail": {
                "en": """### 1. Definition
Metabase is a user-friendly, open-source BI tool that installs in minutes and lets non-technical users ask questions about data.

### 2. Core Purpose
To solve the "Data Bottleneck". Enables Marketing or HR teams to ask their own questions (Democratization of Data) instead of waiting for the data team.

### 3. Architecture and Working Principle
Java (Clojure) based. Runs as a single .jar file or Docker image. Scans database schema to understand relationships.

### 4. Key Components
* **Query Builder:** Visual interface to filter, group, and summarize without code.
* **Pulse:** Automated reporting via Email/Slack.

### 5. Use Cases
Startups, Simple operational reporting.

### 6. Pros and Cons
* **Pros:** Extremely simple setup and usage, Free open-source version.
* **Cons:** Limited depth for very complex queries.""",

                "tr": """### 1. Tanım
Metabase; kurulumu dakikalar süren, teknik olmayan kullanıcıların basit sorular sorarak veriye ulaşmasını sağlayan, kullanıcı dostu ve açık kaynaklı bir BI aracıdır.

### 2. Temel Amaç
Şirketlerdeki "Veri darboğazını" çözmektir. Ekiplerin kendi raporlarını kendilerinin hazırlamasını (Verinin Demokratikleşmesi) hedefler.

### 3. Mimari ve Çalışma Prensibi
Java (Clojure) tabanlıdır. Tek bir dosya veya Docker imajı olarak çalışır. Veritabanı şemasını tarar.

### 4. Temel Bileşenler
Query Builder (Görsel Sorgu Oluşturucu), Pulse (Otomatik Raporlama).

### 5. Kullanım Alanları
Startup'lar, Basit Analizler.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Basitlik (En kolay BI aracı), Ücretsiz versiyon.
* **Dezavantajlar:** Derinlik (Karmaşık veri modellerinde yetersiz kalabilir)."""
            },
            "link": "https://www.metabase.com/", "modern": True, "dep": None,
            "code": """# Docker ile Metabase Çalıştırma
docker run -d -p 3000:3000 --name metabase metabase/metabase"""
        },
        "Kibana": {
            "desc": {"en": "ES Visualization.", "tr": "Elasticsearch Görselleştirme."},
            "detail": {
                "en": """### 1. Definition
Kibana is the visualization and management interface for the Elastic Stack (ELK), designed specifically for Elasticsearch data.

### 2. Core Purpose
To facilitate "searching for a needle in a haystack" within billions of log lines or text documents; visualizing search results.

### 3. Architecture and Working Principle
Talks directly to the Elasticsearch API. Node.js based.
* **Discovery:** Exploring raw data over time.
* **Lens:** Drag-and-drop chart builder.

### 4. Key Components
Index Pattern, KQL (Kibana Query Language).

### 5. Use Cases
Log Analysis, Cyber Security (SIEM).

### 6. Pros and Cons
* **Pros:** Unbeatable for text/log analysis, Native ELK integration.
* **Cons:** Tightly coupled with Elasticsearch (cannot connect to SQL DBs).""",

                "tr": """### 1. Tanım
Kibana; Elasticsearch verileri için özel olarak tasarlanmış, Elastic Stack (ELK) ailesinin görselleştirme ve yönetim arayüzüdür.

### 2. Temel Amaç
Milyarlarca satırlık log verisi veya metin içinde aramayı kolaylaştırmak ve sonuçları grafiğe dökmektir.

### 3. Mimari ve Çalışma Prensibi
Doğrudan Elasticsearch API'si ile konuşur. Node.js tabanlıdır.
* **Discovery:** Ham veriyi zaman ekseninde inceleme.
* **Lens:** Sürükle-bırak grafik oluşturma.

### 4. Temel Bileşenler
Index Pattern, KQL (Kibana Sorgu Dili).

### 5. Kullanım Alanları
Log Analizi, Siber Güvenlik (SIEM).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Metin analizinde rakipsizdir, ELK ile hazır gelir.
* **Dezavantajlar:** Bağımlılık (Sadece Elasticsearch ile çalışır)."""
            },
            "link": "https://www.elastic.co/kibana", "modern": True, "dep": "Elasticsearch",
            "code": """# KQL Örneği
status:500 AND host:"web-server-1" AND NOT message:"timeout" """
        },
        "Looker": {
            "desc": {"en": "Enterprise Data Platform.", "tr": "Kurumsal Veri Platformu."},
            "detail": {
                "en": """### 1. Definition
Looker is a cloud-native enterprise data platform with its own modeling language (LookML). Owned by Google.

### 2. Core Purpose
To prevent "Metric Chaos" (different definitions for the same metric). Provides a "Single Source of Truth" via LookML layer.

### 3. Architecture and Working Principle
**In-database** architecture. Looker does not store data; it generates SQL and pushes it to the database (BigQuery, Snowflake).
* **LookML:** A code-based modeling layer that abstracts SQL.

### 4. Key Components
LookML Project, Explore, Looks/Dashboards.

### 5. Use Cases
Data Governance, Embedded Analytics.

### 6. Pros and Cons
* **Pros:** Consistency (Single source of truth), Git integration.
* **Cons:** High Cost, Learning curve (LookML language).""",

                "tr": """### 1. Tanım
Looker; veriyi veritabanından çıkarmadan işleyen, kendine has bir modelleme dili (LookML) olan, bulut tabanlı modern bir kurumsal veri platformudur.

### 2. Temel Amaç
"Metrik Kargaşası"nı önlemektir. LookML katmanı sayesinde, bir metrik bir kere tanımlanır ve tüm şirket o tanımı kullanır (Tek Gerçeklik Kaynağı).

### 3. Mimari ve Çalışma Prensibi
Looker'ın kendi veritabanı yoktur. Sorguyu canlı olarak veritabanına atar.
* **LookML:** SQL'i soyutlayan kod tabanlı modelleme katmanıdır.

### 4. Temel Bileşenler
LookML Projesi, Explore, Dashboards.

### 5. Kullanım Alanları
Veri Yönetişimi, Gömülü Analitik (Embedded).

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Tutarlılık, Versiyon kontrolü (Git).
* **Dezavantajlar:** Yüksek Maliyet, Öğrenme gereksinimi (LookML)."""
            },
            "link": "https://looker.com/", "modern": True, "dep": None,
            "code": """# LookML Örneği
view: orders {
  dimension: id {
    primary_key: yes
    type: number
    sql: ${TABLE}.id ;;
  }
  measure: total_revenue {
    type: sum
    sql: ${sale_price} ;;
  }
}"""
        }
    },
    "AI/ML": {
        "MLflow": {
            "desc": {"en": "ML Lifecycle Management.", "tr": "ML Yaşam Döngüsü Yönetimi."},
            "detail": {
                "en": """### 1. Definition
MLflow is an open-source platform designed to manage the machine learning lifecycle, developed by Databricks.

### 2. Core Purpose
To solve the problems of Experiment Tracking ("Which parameter gave the best result?"), Reproducibility ("Who trained this model?"), and Deployment ("How do I serve this model?").

### 3. Architecture and Working Principle
Modular structure. Can run locally or on a server.
* **Tracking:** Records parameters and metrics.
* **Projects:** Packages code for reproducibility.
* **Models:** Standardizes model packaging.
* **Registry:** Manages model versions (Staging -> Production).

### 4. Key Components
Tracking Server, Model Registry, Projects.

### 5. Use Cases
Experiment Tracking, Model Serving.

### 6. Pros and Cons
* **Pros:** Universal (works with any library), Simple setup.
* **Cons:** Security (RBAC is weak in open-source version).""",

                "tr": """### 1. Tanım
MLflow; makine öğrenimi yaşam döngüsünü (Lifecycle) yönetmek için geliştirilmiş, platformdan bağımsız, açık kaynaklı bir MLOps platformudur. Databricks tarafından geliştirilmiştir.

### 2. Temel Amaç
Veri bilimcilerin en büyük sorunu olan "Hangi parametreyle en iyi sonucu aldım?", "Bu modeli kim ne zaman eğitti?" ve "Modeli nasıl canlıya alırım?" sorularını (Experiment Tracking) çözmektir.

### 3. Mimari ve Çalışma Prensibi
Modüler bir yapıya sahiptir. İster tek başına (Local), ister bir sunucuda çalışabilir. Dört ana bileşenden oluşur.

### 4. Temel Bileşenler
* **MLflow Tracking:** Deneylerin parametrelerini ve sonuçlarını kaydeder.
* **MLflow Projects:** Kodu paketleyip her yerde aynı şekilde çalışmasını sağlar.
* **MLflow Models:** Modeli farklı formatlarda paketler.
* **Model Registry:** Modellerin versiyonlanmasını yönetir.

### 5. Kullanım Alanları
Deney Takibi, Model Dağıtımı.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Evrensellik (Her kütüphane ile çalışır), Basitlik.
* **Dezavantajlar:** Güvenlik (Açık kaynak sürümde yetkilendirme zayıftır)."""
            },
            "link": "https://mlflow.org/", "modern": True, "dep": None,
            "code": """import mlflow

# Deney Başlatma
mlflow.start_run()

# Parametre Kaydetme
mlflow.log_param("learning_rate", 0.01)

# Metrik Kaydetme
mlflow.log_metric("accuracy", 0.95)

# Modeli Kaydetme
mlflow.sklearn.log_model(model, "model")

mlflow.end_run()"""
        },
        "Spark MLlib": {
            "desc": {"en": "Scalable ML Library.", "tr": "Ölçeklenebilir ML Kütüphanesi."},
            "detail": {
                "en": """### 1. Definition
Spark MLlib is Apache Spark's scalable machine learning library designed to run on large-scale data using in-memory processing.

### 2. Core Purpose
Unlike Scikit-learn which runs on a single machine, MLlib is designed for Distributed Training on Terabytes of data across hundreds of servers.

### 3. Architecture and Working Principle
Built on Spark DataFrames.
* **Transformer:** Algorithm that transforms data.
* **Estimator:** Algorithm that learns from data and produces a model.
* **Pipeline:** Chaining these stages together.

### 4. Key Components
Classification, Regression, Clustering, Collaborative Filtering (ALS).

### 5. Use Cases
Recommendation Systems, Churn Prediction.

### 6. Pros and Cons
* **Pros:** Scalability ( scales with data), Unified stack (ETL + ML).
* **Cons:** Deep Learning support is weak, Latency (Not for real-time inference).""",

                "tr": """### 1. Tanım
Spark MLlib; Apache Spark'ın bellek içi (in-memory) işlem gücünü kullanan, büyük ölçekli veriler üzerinde çalışmak için tasarlanmış ölçeklenebilir makine öğrenimi kütüphanesidir.

### 2. Temel Amaç
Scikit-learn gibi kütüphaneler tek bir bilgisayarın RAM'ine sığan verilerle çalışırken; MLlib, Terabyte'larca veriyi yüzlerce sunucuya dağıtarak modelleri eğitmek (Distributed Training) için geliştirilmiştir.

### 3. Mimari ve Çalışma Prensibi
Spark'ın DataFrame yapısı üzerine kuruludur.
* **Transformer:** Veriyi dönüştüren algoritma.
* **Estimator:** Veriden öğrenen ve model üreten algoritma.
* **Pipeline:** Bu parçaların zincirleme bağlanması.

### 4. Temel Bileşenler
Sınıflandırma, Regresyon, Kümeleme, Öneri Sistemleri (ALS).

### 5. Kullanım Alanları
Öneri Sistemleri (Netflix/Spotify tarzı), Müşteri Kaybı Tahmini.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Ölçeklenebilirlik, Entegrasyon (Veri temizleme ve modelleme aynı yerde).
* **Dezavantajlar:** Derin Öğrenme (Zayıftır), Gecikme (Anlık tahmin için hantaldır)."""
            },
            "link": "https://spark.apache.org/mllib/", "modern": True, "dep": "Spark",
            "code": """from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)

pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])
model = pipeline.fit(training_data)"""
        },
        "TensorFlow": {
            "desc": {"en": "Deep Learning Framework.", "tr": "Derin Öğrenme Kütüphanesi."},
            "detail": {
                "en": """### 1. Definition
TensorFlow is an end-to-end open-source platform for machine learning, developed by Google.

### 2. Core Purpose
To build and deploy complex neural networks for tasks like image recognition and NLP, running on everything from massive servers to mobile devices.

### 3. Architecture and Working Principle
Named after multidimensional data arrays (Tensors) flowing through a computation graph. Supports both Static Graphs and Eager Execution.

### 4. Key Components
Tensor, Keras (High-level API), TensorBoard (Visualization), TF Lite (Mobile).

### 5. Use Cases
Computer Vision, NLP, AlphaGo.

### 6. Pros and Cons
* **Pros:** Production Ready, TFX Ecosystem.
* **Cons:** Steeper learning curve than PyTorch, Debugging static graphs can be hard.""",

                "tr": """### 1. Tanım
TensorFlow; Google tarafından geliştirilen, derin öğrenme ve yapay sinir ağları odaklı, uçtan uca açık kaynaklı bir makine öğrenimi platformudur.

### 2. Temel Amaç
Görüntü işleme, ses tanıma gibi karmaşık problemleri çözmek için çok katmanlı sinir ağlarını oluşturmak, eğitmek ve bunları hem sunucularda hem de mobil cihazlarda çalıştırabilmektir.

### 3. Mimari ve Çalışma Prensibi
İsmini verilerin (Tensors) bir işlem grafiği boyunca akmasından (Flow) alır. Hem Statik Grafik hem de Eager Execution (Anında çalıştırma) destekler.

### 4. Temel Bileşenler
Tensor, Keras (Yüksek seviyeli API), TensorBoard (Görselleştirme), TensorFlow Lite (Mobil).

### 5. Kullanım Alanları
Bilgisayarlı Göru (Computer Vision), NLP.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Canlıya alma (Production) gücü, Ekosistem (TFX).
* **Dezavantajlar:** Öğrenme Eğrisi (PyTorch'a göre daha diktir)."""
            },
            "link": "https://www.tensorflow.org/", "modern": True, "dep": None,
            "code": """import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])"""
        },
        "PyTorch": {
            "desc": {"en": "Deep Learning Framework.", "tr": "Derin Öğrenme Kütüphanesi."},
            "detail": {
                "en": """### 1. Definition
PyTorch is an open-source machine learning library developed by Meta (Facebook) AI. Known for flexibility and speed.

### 2. Core Purpose
To allow researchers to experiment rapidly. It is the standard for academic research and GenAI (LLMs).

### 3. Architecture and Working Principle
Uses **Dynamic Computational Graphs**. The graph is built at runtime, making it very Pythonic and easy to debug.

### 4. Key Components
Torch.nn, Autograd (Automatic differentiation), TorchScript.

### 5. Use Cases
GenAI (LLMs like GPT), Academic Research.

### 6. Pros and Cons
* **Pros:** Ease of use (Pythonic), Debugging, Community.
* **Cons:** Mobile deployment is less mature than TF (but improving).""",

                "tr": """### 1. Tanım
PyTorch; Meta (Facebook) AI Research ekibi tarafından geliştirilen, esnekliği ve hızı ile bilinen, açık kaynaklı bir derin öğrenme kütüphanesidir.

### 2. Temel Amaç
Araştırmacıların yeni algoritmaları hızlıca denemelerini sağlamak ve Python doğasına uygun (Pythonic) bir yapı sunmaktır. GenAI ve LLM dünyasının standardıdır.

### 3. Mimari ve Çalışma Prensibi
**Dinamik Hesaplama Grafiği** kullanır. Grafik kod çalışırken oluşturulur. Bu, if-else gibi yapıları model içinde kullanmayı kolaylaştırır.

### 4. Temel Bileşenler
Torch.nn, Autograd (Otomatik türev alma), TorchScript.

### 5. Kullanım Alanları
GenAI (LLM), Akademik Araştırma.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Kullanım Kolaylığı, Hata Ayıklama, Topluluk.
* **Dezavantajlar:** Mobil dağıtım (TensorFlow kadar olgun değil)."""
            },
            "link": "https://pytorch.org/", "modern": True, "dep": None,
            "code": """import torch
import torch.nn as nn

# Basit bir Sinir Ağı
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)"""
        },
        "Kubeflow": {
            "desc": {"en": "ML Toolkit for K8s.", "tr": "Kubernetes ML Araç Seti."},
            "detail": {
                "en": """### 1. Definition
Kubeflow is a Cloud-Native MLOps toolkit dedicated to making deployments of ML workflows on Kubernetes simple, portable and scalable.

### 2. Core Purpose
To solve the "works on my machine but not on cluster" problem. Combines the ML lifecycle with the power of Kubernetes.

### 3. Architecture and Working Principle
Microservices on top of Kubernetes. Each step (Training, Serving) runs as a separate Pod.

### 4. Key Components
Pipelines, Notebook Servers, Katib (Hyperparameter tuning), KServe.

### 5. Use Cases
Enterprise MLOps, Scalable Training.

### 6. Pros and Cons
* **Pros:** Standardization, Scalability.
* **Cons:** Complexity (Requires K8s expertise), Heavy/Overkill for small teams.""",

                "tr": """### 1. Tanım
Kubeflow; makine öğrenimi iş akışlarını Kubernetes üzerinde dağıtmak, ölçeklendirmek ve yönetmek için geliştirilmiş, Cloud-Native bir MLOps araç setidir.

### 2. Temel Amaç
Model geliştirme ve dağıtım sürecini Kubernetes'in gücüyle birleştirmek ve standartlaştırmaktır.

### 3. Mimari ve Çalışma Prensibi
Kubernetes üzerine kurulu mikroservislerden oluşur. Her adım (Eğitim, Sunum) ayrı bir Pod olarak çalışır.

### 4. Temel Bileşenler
Kubeflow Pipelines, Notebook Servers, Katib (Hiperparametre optimizasyonu), KServe.

### 5. Kullanım Alanları
Kurumsal MLOps, Ölçeklenebilir Eğitim.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Standartlaşma, Ölçeklenebilirlik.
* **Dezavantajlar:** Karmaşıklık (Kubernetes uzmanlığı ister), Ağır kurulum."""
            },
            "link": "https://www.kubeflow.org/", "modern": True, "dep": "Kubernetes",
            "code": """import kfp
from kfp import dsl

@dsl.pipeline(name='My Pipeline')
def my_pipeline():
    train_op = dsl.ContainerOp(
        name='Train',
        image='gcr.io/my-image/train',
        arguments=['--epochs', '50']
    )"""
        },
        "Ray": {
            "desc": {"en": "Distributed AI Compute.", "tr": "Dağıtık Yapay Zeka İşlemcisi."},
            "detail": {
                "en": """### 1. Definition
Ray is a unified framework for scaling AI and Python applications.

### 2. Core Purpose
To scale Python code from a single machine to a massive cluster with minimal code changes. Famous for training GPT models (OpenAI).

### 3. Architecture and Working Principle
Uses the **Actor Model**. Creates lightweight tasks and distributes them dynamically across the cluster.

### 4. Key Components
Ray Core, Ray Train, Ray Tune, Ray Serve, RLlib.

### 5. Use Cases
LLM Training, Reinforcement Learning.

### 6. Pros and Cons
* **Pros:** Pythonic, Performance (Low latency), Flexibility.
* **Cons:** Memory management in large clusters can be tricky.""",

                "tr": """### 1. Tanım
Ray; Python uygulamalarını ve özellikle yapay zeka iş yüklerini ölçeklendirmek için geliştirilmiş, birleşik bir dağıtık hesaplama çerçevesidir.

### 2. Temel Amaç
Tek bir bilgisayarda yazılan Python kodunu, neredeyse hiç değiştirmeden binlerce sunucudan oluşan bir kümeye yaymaktır.

### 3. Mimari ve Çalışma Prensibi
**Actor Model** kullanır. Hafif görevler oluşturur ve bunları dinamik olarak sunuculara dağıtır.

### 4. Temel Bileşenler
Ray Core, Ray Train, Ray Tune, Ray Serve, RLlib.

### 5. Kullanım Alanları
LLM Eğitimi (GPT), Pekiştirmeli Öğrenme.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Pythonic (Kolay öğrenilir), Performans, Esneklik.
* **Dezavantajlar:** Kaynak Yönetimi (Büyük kümelerde zorlaşabilir)."""
            },
            "link": "https://www.ray.io/", "modern": True, "dep": None,
            "code": """import ray

ray.init()

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))"""
        },
        "Hugging Face": {
            "desc": {"en": "The AI Community.", "tr": "Yapay Zeka Topluluk Platformu."},
            "detail": {
                "en": """### 1. Definition
Hugging Face is the "GitHub of AI". A platform for sharing and collaborating on ML models, datasets, and demos.

### 2. Core Purpose
To democratize AI. Making state-of-the-art models (BERT, GPT) accessible to everyone.

### 3. Architecture and Working Principle
Central Model Hub and open-source libraries (Transformers).

### 4. Key Components
Model Hub, Datasets, Spaces (Demos), Transformers Library.

### 5. Use Cases
Transfer Learning, NLP & Vision tasks.

### 6. Pros and Cons
* **Pros:** Accessibility, Standardization.
* **Cons:** Hardware requirements for running large models.""",

                "tr": """### 1. Tanım
Hugging Face; yapay zeka modellerini paylaşmak, keşfetmek ve kullanmak için oluşturulmuş, "AI dünyasının GitHub'ı" olarak bilinen platformdur.

### 2. Temel Amaç
Makine öğrenimini demokratikleştirmek. Devasa modelleri (BERT, GPT) herkesin kullanımına sunmak.

### 3. Mimari ve Çalışma Prensibi
Merkezi bir Model Deposu (Hub) ve açık kaynak kütüphanelerden oluşur.

### 4. Temel Bileşenler
Model Hub, Datasets, Spaces, Transformers Kütüphanesi.

### 5. Kullanım Alanları
Transfer Learning (Hazır model kullanımı), NLP ve Görüntü işleme.

### 6. Avantajlar ve Dezavantajlar
* **Avantajlar:** Erişilebilirlik, Standartlaşma.
* **Dezavantajlar:** Donanım (Büyük modeller GPU ister)."""
            },
            "link": "https://huggingface.co/", "modern": True, "dep": None,
            "code": """from transformers import pipeline

# Duygu Analizi
classifier = pipeline("sentiment-analysis")
result = classifier("I love using Hugging Face!")
print(result)"""
        }

    }
}

# --- YARDIMCI FONKSİYONLAR ---
CATEGORY_COLORS = {
    "Ingestion": "#90EE90", "Storage": "#FFD700", "Lakehouse": "#00CED1",
    "Processing": "#FF6347", "Databases": "#ADD8E6", "Serving/BI": "#DDA0DD",
    "Orchestration": "#D3D3D3", "AI/ML": "#FF69B4"
}


def get_category(node_name):
    for cat, items in TECH_STACK.items():
        if node_name in items:
            return cat
    return "Unknown"


def validate_stack(selected_nodes, lang="en"):
    errors = []
    for tech in selected_nodes:
        if tech in DEPENDENCY_RULES:
            required_deps = DEPENDENCY_RULES[tech]
            for dep in required_deps:
                if dep not in selected_nodes:
                    msg_template = UI_TEXTS[lang].get("error_missing_dep", "Missing dependency: {tech} needs {dep}")
                    errors.append(msg_template.format(tech=tech, dep=dep))
    return errors


def auto_connect_nodes(selected_nodes):
    layered_nodes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for node in selected_nodes:
        cat = get_category(node)
        priority = LAYER_PRIORITY.get(cat, 3)
        layered_nodes[priority].append(node)

    edges = []
    active_layers = [i for i in range(1, 6) if layered_nodes[i]]
    for i in range(len(active_layers) - 1):
        current_idx = active_layers[i]
        next_idx = active_layers[i + 1]
        sources = layered_nodes[current_idx]
        targets = layered_nodes[next_idx]
        for s in sources:
            for t in targets:
                edges.append((s, t))
    return layered_nodes, edges