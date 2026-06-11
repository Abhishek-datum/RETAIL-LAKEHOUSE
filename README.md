# Retail Lakehouse Project

## Architecture

Raw Data → Bronze Layer → Silver Layer → Gold Layer

## Technologies Used

- Python
- PySpark
- Pandas
- MySQL
- VS Code

## Layers

### Bronze Layer
Raw Olist datasets partitioned by order date.

### Silver Layer
Data cleaning, joins, enrichment, revenue calculation.

### Gold Layer
Business metrics:
- Daily Revenue
- Top Product Categories
- Customer Retention
- Average Delivery Time

## SQL Analytics
- Daily Revenue Analysis
- Product Category Analysis
- Customer Retention
- Delivery Performance
- Payment Distribution

## Project Structure
src/
sql/
data/
config/
tests/