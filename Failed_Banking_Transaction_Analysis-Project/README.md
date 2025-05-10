# Failed Banking Transaction Analysis – GCP Project

This project focuses on identifying and analyzing failed banking transactions using Google Cloud services. The data is processed from multiple CSV files collected from 15 branches across 3 cities.

---

## 🔧 Project Setup

- **GCP Project ID**: `tharunteja-project`
- **Bucket Name**: `bank-transaction-data`
- **Cluster Name**: `training-cluster`
- **Region**: `us-central1`

---

## 🧾 Step-by-Step Instructions

### 1. Create a GCS Bucket

```bash
gsutil mb gs://bank-transaction-data/
```

Then upload your files:
- Upload all 15 branch `.csv` files
- Upload PySpark scripts:

```bash
gsutil cp *.csv gs://bank-transaction-data/
gsutil cp clean_and_merge.py gs://bank-transaction-data/scripts/
gsutil cp filter_failed_transactions.py gs://bank-transaction-data/scripts/
```

---

### 2. Set IAM Permissions (Important)

Give required access to the default compute service account:

```bash
gcloud projects add-iam-policy-binding tharunteja-project \
  --member="serviceAccount:633843979185-compute@developer.gserviceaccount.com" \
  --role="roles/dataproc.worker"
```

---

### 3. Create Dataproc Cluster

```bash
gcloud dataproc clusters create training-cluster \ --region=us-central1 \
  --single-node \ --enable-component-gateway \ --image-version=2.1-debian11 \ --project=tharunteja-project
```

---

### 4. Submit PySpark Jobs

Job 1 – Merge and clean data:

```bash
gcloud dataproc jobs submit pyspark gs://bank-transaction data/scripts/clean_and_merge.py \ --cluster=training-cluster \ --region=us-central1
```

Job 2 – Filter failed transactions:

```bash
gcloud dataproc jobs submit pyspark gs://bank-transaction-data/scripts/filter_failed_transactions.py \ --cluster=training-cluster\ --region=us-central1
```

---

### 5. (Optional) Download Output File Locally

```bash
gsutil cp gs://bank-transaction-data/output/failed_transactions/part*.csv D:\failed_data\
```

---

## 🗃️ Cloud SQL Table (Manual Step)

Create the table in MySQL (Cloud SQL):

```sql
CREATE TABLE failed_transactions (
    txn_id VARCHAR(100),
    branch_id VARCHAR(50),
    city VARCHAR(50),
    amount FLOAT,
    transaction_status VARCHAR(20),
    txn_date DATE,
    customer_id VARCHAR(50)
);
```

---

## 📊 BigQuery Analytics (via Console or CLI)

Create Dataset:

```bash
bq mk --dataset --location=us bank_analytics
```

Sample Query:

```sql
SELECT city, COUNT(*) AS failed_txns
FROM failed_transactions
GROUP BY city
ORDER BY failed_txns DESC;
```

---

## 📈 Looker Studio

Used to visualize:
- City-wise transaction failures
- Date-wise amount trends
- Branch & customer-level patterns

---

## 🧠 Key Insights

- ₹3.2M+ failed amount in just 7 days
- Peak failure date: May 7, 2025
- Most failures in Hyderabad

---

## 🔮 Future Scope

- Use ML to predict failure risk
- Real-time alerts for repeated failures
- Historical trend dashboards
- Secure dashboard access by role

---

## 🙏 Thanks

Thanks to mentors, friends, and the GCP ecosystem for supporting this project.
