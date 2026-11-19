# Building a Real-Time Data Infrastructure for Renewable Electricity Curtailment Research in Ireland

## Project Overview

This project implements a real-time streaming data platform for renewable electricity curtailment research in Ireland. The platform continuously generates renewable energy data, streams it through Apache Kafka, processes it using Apache Spark Structured Streaming, stores it in PostgreSQL, and visualizes results through Grafana dashboards. Prometheus is used for monitoring and observability.

---

## System Architecture

```text
Python Producer
      ↓
Apache Kafka
      ↓
Apache Spark Structured Streaming
      ↓
PostgreSQL
      ↓
Grafana Dashboard

Prometheus Monitoring
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Data generation and streaming |
| Apache Kafka | Stream ingestion and message broker |
| Apache Spark Structured Streaming | Real-time stream processing |
| PostgreSQL | Persistent data storage |
| Grafana | Data visualisation and dashboards |
| Prometheus | Monitoring and observability |
| Docker Compose | Container orchestration |
| Java 17 | Spark runtime dependency |

---

## Features

### Real-Time Data Generation

The Python producer continuously generates renewable electricity data consisting of:

- Timestamp
- Wind Generation (MW)
- Electricity Demand (MW)

Example:

```json
{
  "timestamp": "2026-11-19T22:30:10",
  "wind_generation": 2450,
  "electricity_demand": 5200
}
```

---

### Data Streaming

Apache Kafka receives streaming data through the topic:

```text
renewable-energy
```

The producer publishes renewable energy records to Kafka in real time.

---

### Real-Time Processing

Apache Spark Structured Streaming:

- Consumes messages from Kafka
- Parses JSON records
- Converts records into structured columns
- Processes micro-batches in real time
- Writes processed data into PostgreSQL

---

### Data Storage

Renewable energy data is stored in PostgreSQL.

Table:

```sql
renewable_energy
```

Schema:

```sql
CREATE TABLE IF NOT EXISTS renewable_energy (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    wind_generation INTEGER,
    electricity_demand INTEGER
);
```

---

### Data Visualisation

Grafana dashboards provide:

- Wind Generation Over Time
- Electricity Demand Over Time
- Renewable Energy Monitoring

Example Dashboard Panels:

- Wind Generation Trend
- Electricity Demand Trend
- Real-Time Data Visualisation

---

### Monitoring and Observability

Prometheus is used to:

- Monitor service health
- Monitor platform availability
- Collect performance metrics
- Support infrastructure observability

Grafana can also be used to visualize Prometheus metrics.

---

## Project Structure

```text
renewable-curtailment-platform/

├── producer/
│   └── producer.py
│
├── spark/
│   ├── process.py
│   └── test_postgres.py
│
├── postgres/
│   └── init.sql
│
├── prometheus/
│   └── prometheus.yml
│
├── jars/
│   └── postgresql-42.7.13.jar
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ifbd-ca3-jeena
```

---

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

## Starting the Infrastructure

Start all Docker services:

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

Expected services:

```text
kafka
postgres
grafana
prometheus
```

---

## Running the Application

### Terminal 1 – Start the Producer

```bash
source venv/bin/activate

python3 producer/producer.py
```

---

### Terminal 2 – Start Spark Streaming

```bash
source venv/bin/activate

python3 spark/process.py
```

---

## Accessing Services

### Grafana

```text
http://localhost:3000
```

Default credentials:

```text
Username: admin
Password: admin
```

---

### Prometheus

```text
http://localhost:9090
```

---

### PostgreSQL

Connect:

```bash
docker exec -it postgres psql -U admin -d energydb
```

View records:

```sql
SELECT * FROM renewable_energy;
```

Count records:

```sql
SELECT COUNT(*) FROM renewable_energy;
```

---

## Dashboards

### Renewable Energy Monitoring Dashboard

Provides:

- Wind Generation Over Time
- Electricity Demand Over Time
- Live Renewable Energy Metrics

### System Monitoring Dashboard

Provides:

- Prometheus Metrics
- Service Availability Monitoring
- Platform Health Monitoring

---

## Current Status

### Completed

- ✅ Docker Infrastructure
- ✅ Apache Kafka Streaming
- ✅ Python Data Producer
- ✅ Spark Structured Streaming
- ✅ PostgreSQL Persistence
- ✅ Grafana Dashboards
- ✅ Prometheus Monitoring

---

## Testing

Verify data is flowing into PostgreSQL:

```sql
SELECT COUNT(*) FROM renewable_energy;
```

The count should continuously increase while:

```bash
python3 producer/producer.py
```

and

```bash
python3 spark/process.py
```

are running.

---

## AI Usage Statement

Microsoft Copilot was used to assist with:

- Docker Compose configuration
- Apache Kafka setup
- Apache Spark Structured Streaming development
- PostgreSQL integration
- Grafana dashboard configuration
- Prometheus monitoring setup
- Documentation preparation

All generated code and configurations were reviewed, tested, modified where necessary, and validated by the project author before inclusion in the project.

---

## Author

**Jeena Mathai**

Infrastructure for Big Data (IFBD)

South East Technological University (SETU)
