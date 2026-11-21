# Cognistream
Developer Flow-State and Cognitive Load Analytics.
In this project we are building a dashboard which helps the HR improve and monitor the employee about their productivity and the distractions occurs during the work time 
This can be used in any small scale or big scale companies. Which will help the manager keep tabs on the employees.
The project can also be used in the top IIT colleges 
Let's include more features to this project so that it will be usefull.
Now we are building some basic implementation and use case and in the future we'll try to implement new features in this project 

 System Architecture 
 
DATA SOURCES
  ┌────────┬────────┬────────┬────────┐
  │ GitHub │ Slack  │ Jira   │ VS Code│
  └────────┴────────┴────────┴────────┘
                    |
                    ▼
          DATA INGESTION LAYER
          Python Mock/API Scripts
                    |
                    ▼
             RAW DATA STORAGE
             JSON Event Files
                    |
                    ▼
          DATA PROCESSING LAYER
              Python + Polars
          Cleaning & Transformation
                    |
                    ▼
             APACHE AIRFLOW
           Workflow Orchestration
                    |
                    ▼
              CLICKHOUSE
          Analytical Database
                    |
                    ▼
          ANALYTICS & METRICS
        Context Switching Analysis
          Cognitive Load Patterns
                    |
                    ▼
           REACT DASHBOARD
              + TREMOR
          Interactive Visualizations


Flow Structure 

              Mock Event Sources
                    |
                    ▼
              clean_events.py
                    |
                    ▼
              cleaned_events.csv
                    |
                    ▼
              load_to_clickhouse.py
                    |
                    ▼
              ClickHouse developer_events
                    |
                    ▼
              SQL Verification
