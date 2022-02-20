# ETL_demo
 Digital_Video
 ETL, which stands for extract, transform, and load, is the process data engineers use to extract data from different sources, transform the data into a usable and trusted resource, and load that data into the systems end-users can access and use downstream to solve business problems
L
et's dive in and learn how to convert raw data into insights through the three-step data ETL process.
1st Step – Extraction. ...
2nd Step – Transformation. ...
3rd Step – Loading.

There are three steps in the ETL process: Extraction: Data is taken from one or more sources or systems. The extraction locates and identifies relevant data, then prepares it for processing or transformation. Extraction allows many different kinds of data to be combined and ultimately mined for business intelligence.

To build an ETL pipeline with batch processing, you need to:

Create reference data: create a dataset that defines the set of permissible values your data may contain. For example, in a country data field, specify the list of country codes allowed.
Extract data from different sources: the basis for the success of subsequent ETL steps is to extract data correctly. Take data from a range of sources, such as APIs, non/relational databases, XML, JSON, CSV files, and convert it into a single format for standardized processing.
Validate data: Keep data that have values in the expected ranges and reject any that do not. For example, if you only want dates from the last year, reject any values older than 12 months. Analyze rejected records, on an on-going basis, to identify issues, correct the source data, and modify the extraction process to resolve the problem in future batches.
Transform data: Remove duplicate data (cleaning), apply business rules, check data integrity (ensure that data has not been corrupted or lost), and create aggregates as necessary. For example, if you want to analyze revenue, you can summarize the dollar amount of invoices into a daily or monthly total. You need to program numerous functions to transform the data automatically. 
Stage data: You do not typically load transformed data directly into the target data warehouse. Instead, data first enters a staging database which makes it easier to roll back if something goes wrong. At this point, you can also generate audit reports for regulatory compliance, or diagnose and repair data problems.
Publish to your data warehouse: Load data to the target tables. Some data warehouses overwrite existing information whenever the ETL pipeline loads a new batch - this might happen daily, weekly, or monthly. In other cases, the ETL workflow can add data without overwriting, including a timestamp to indicate it is new. You must do this carefully to prevent the data warehouse from “exploding” due to disk space and performance limitations.

You now know three ways to build an Extract Transform Load process, which you can think of as three stages in the evolution of ETL:

Traditional ETL batch processing - meticulously preparing and transforming data using a rigid, structured process.
ETL with stream processing - using a modern stream processing framework like Kafka, you pull data in real-time from source, manipulate it on the fly using Kafka’s Stream API, and load it to a target system such as Amazon Redshift.
Automated data pipeline without ETL - use Panoply’s automated data pipelines, to pull data from multiple sources, automatically prep it without requiring a full ETL process, and immediately begin analyzing it using your favorite BI tools. Get started with Panoply in minutes.
Traditional ETL works, but it is slow and fast becoming out-of-date. If you want your company to maximize the value it extracts from its data, it’s time for a new ETL workflow.

Panoply is a secure place to store, sync, and access all your business data. Panoply can be set up in minutes, requires minimal on-going maintenance, and provides online support, including access to experienced data architects. Try Panoply free for 14 days.
