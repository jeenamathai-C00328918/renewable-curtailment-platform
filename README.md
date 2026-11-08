
# Building a Real-Time Data Infrastructure for Renewable Electricity Curtailment Research in Ireland

## Project Overview

Ireland is rapidly increasing the use of renewable energy sources, particularly wind power. However, there are periods when the electricity grid cannot accommodate all available renewable generation due to factors such as high renewable output, low electricity demand, or transmission constraints. This situation is known as **renewable electricity curtailment**.

The aim of this project is to design and implement a real-time data infrastructure that can collect, process, store, visualize, and monitor renewable energy and electricity grid data. The platform will provide the technical foundation for future machine learning research on renewable electricity curtailment prediction in Ireland.

This project is being developed as part of a Big Data Infrastructure module.

---

## Project Objectives

The project will:

- Collect renewable energy and electricity grid data.
- Stream data in real time using Apache Kafka.
- Process incoming data using Apache Spark.
- Store processed data in PostgreSQL.
- Display key metrics using Grafana dashboards.
- Monitor system health using Prometheus.
- Demonstrate failure and recovery scenarios.
- Deploy all components using Docker Compose.
- Create a reusable platform suitable for future machine learning applications.

---

## Research Context

### Current Literature Review

**Machine Learning Applications for Renewable Electricity Curtailment Prediction: A Literature Review with Implications for Ireland**

### Future Dissertation Topic

**Explainable Machine Learning for Renewable Electricity Curtailment Prediction in Ireland: Investigating the Impact of Weather Conditions, Electricity Demand, and Grid Constraints**

### Relationship to This Project

This project focuses on building the underlying data infrastructure required for future machine learning research. While no predictive model is developed in this project, the platform is designed to provide a scalable and reliable data pipeline that can later support machine learning and explainable AI solutions.

---

## System Architecture

```text
EirGrid Data / Simulated Data
            │
            ▼
     Python Producer
            │
            ▼
          Kafka
            │
            ▼
          Spark
            │
            ▼
       PostgreSQL
            │
            ▼
         Grafana

Prometheus monitors all services
```

---

## Technology Stack

| Component             | Technology     |
|-----------------------|----------------|
| Containerisation      | Docker Compose |
| Data Collection       | Python         |         
| Data Streaming        | Apache Kafka   |
| Data Processing       | Apache Spark   |
| Database              | PostgreSQL     |
| Visualisation         | Grafana        |
| Monitoring            | Prometheus     |
| Version Control       | Git & GitHub   |

---

## Planned Data Sources

### Preferred Source

- EirGrid Open Data

Potential data includes:

- Wind generation
- Electricity demand
- System load
- Grid performance metrics

### Alternative Source

If direct integration is unavailable during development, realistic simulated renewable-energy data will be generated using Python.

---

## Project Development Roadmap

### Phase 1: Project Setup

- [x] Install Docker Desktop
- [x] Create project structure
- [x] Create Git repository
- [x] Create README documentation

### Phase 2: Data Streaming

- [x] Configure Apache Kafka
- [x] Create Kafka topic
- [x] Develop Python data producer

### Phase 3: Data Processing

- [ ] Configure Apache Spark
- [ ] Process incoming Kafka data
- [ ] Generate aggregated metrics

### Phase 4: Data Storage

- [ ] Configure PostgreSQL
- [ ] Store processed records
- [ ] Validate stored data

### Phase 5: Visualisation

- [ ] Configure Grafana
- [ ] Build monitoring dashboard
- [ ] Create renewable energy charts

### Phase 6: Monitoring

- [ ] Configure Prometheus
- [ ] Monitor service health
- [ ] Collect infrastructure metrics

### Phase 7: Resilience Testing

- [ ] Simulate service failures
- [ ] Demonstrate service recovery
- [ ] Validate monitoring alerts

### Phase 8: Documentation

- [ ] Technical report
- [ ] Architecture documentation
- [ ] Screencast demonstration

---

## Project Structure

```text
renewable-curtailment-platform/
│
├── docker-compose.yml
├── README.md
│
├── producer/
│   └── producer.py
│
├── spark/
│   └── process.py
│
├── postgres/
│   └── init.sql
│
├── prometheus/
│   └── prometheus.yml
│
├── grafana/
│
└── docs/
```

---

## Assignment Requirements Coverage

| Requirement | Solution |
|------------|-----------|
| Data Ingestion | Python Producer |
| Data Streaming | Kafka |
| Data Processing | Spark |
| Data Storage | PostgreSQL |
| Data Visualisation | Grafana |
| Monitoring | Prometheus |
| Containerised Deployment | Docker Compose |
| Failure & Recovery | Service restart testing |
| Infrastructure as Code | Docker Compose |
| Documentation | README, Report, Screencast |

---

## Expected Outcomes

By the completion of this project, the platform will be capable of:

- Collecting renewable energy data in real time.
- Processing and storing energy data efficiently.
- Visualising key energy trends and metrics.
- Monitoring system health and performance.
- Demonstrating resilience through failure and recovery testing.
- Providing a foundation for future machine learning research on renewable electricity curtailment in Ireland.

---

## Author

**Jeena Mathai**

MSc Data Science

South East Technological University (SETU)

Academic Year 2026/2027