 Advanced Design - Personal Wise

 1. Architecture

This project implements a Databricks Lakehouse pipeline using managed Delta tables.

Bronze – raw ingestion  
Silver – standardized and validated data  
Gold – business KPIs

All data resides in the workspace catalog under the slooze_db schema.

 2. Ingestion Strategy

Instead of live scraping, ingestion models a structured marketplace feed.
This reflects real enterprise integration patterns where data is exchanged through APIs or batch exports.

The ingestion layer is isolated from downstream transformations to avoid pipeline failures due to upstream instability.

 3. Bronze Layer

Purpose:
- Preserve source structure
- Minimal transformation
- Schema inference from feed

No deduplication or filtering is applied in this layer.

 4. Silver Layer

Responsibilities:

- Remove duplicates using business keys
- Enforce correct data types
- Apply mandatory field validation
- Prepare data for analytics

This layer acts as the contract for downstream consumers.

 5. Gold Layer

Gold tables expose business-ready aggregates.

Current KPIs:
- Product count per category
- Average price per category

These tables are designed for BI tools and dashboards.

 6. Schema Evolution

Delta Lake supports schema evolution through mergeSchema.

This allows new attributes such as ratings, MOQ, or supplier identifiers to be added without breaking the pipeline.

 7. Data Quality Strategy

Recommended checks:

- product_name must not be null
- supplier_name must not be null
- price must be non-negative

Invalid records can be redirected to a quarantine table.

 8. Failure Handling

Ingestion is isolated from transformation layers.

In production, failed ingestion runs would not overwrite the latest validated Silver snapshot.

 9. Orchestration

The pipeline is designed to be orchestrated using Databricks Workflows.

Task order:
1. ingestion_bronze
2. etl_cleaning
3. gold_aggregations
4. eda_analysis (optional)

 10. Monitoring

Recommended metrics:

- record count in Bronze
- record count in Silver
- number of duplicates removed
- null percentage per column

These metrics can be persisted in an audit table.

 11. Performance

All transformations are implemented using Spark APIs.

The design supports:

- horizontal scaling
- partitioning of Gold tables
- Z-ordering for frequently filtered dimensions

 12. Security

Using a dedicated schema allows controlled access.

Recommended access model:
- read access to Gold tables for analytics users
- restricted write access for ETL users

 13. Future Enhancements

- streaming ingestion
- incremental merge logic
- automated expectations using Delta Live Tables
- BI dashboards
