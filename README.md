🏨 Hotel Booking Cancellation Analysis

📌 Overview



This project analyzes hotel booking data to identify the key factors influencing reservation cancellations and provides actionable insights to reduce cancellation rates. The analysis focuses on improving revenue efficiency and optimizing hotel operations for both City Hotels and Resort Hotels.



🎯 Business Problem



Hotels are experiencing high cancellation rates, leading to:



Reduced revenue

Inefficient room utilization

Poor demand forecasting



The goal of this project is to:



Understand the drivers of cancellations

Provide strategies to reduce cancellations

Assist hotels in pricing and marketing decisions

❓ Research Questions

What factors influence hotel booking cancellations?

How can hotels reduce cancellation rates?

How can pricing and promotions be optimized?

🧠 Hypotheses

Higher prices lead to higher cancellation rates

Longer waiting lists increase cancellations

Most bookings come through travel agents (especially offline/online intermediaries)

📊 Dataset

Source: Kaggle

Dataset: Hotel Booking Demand

Time Period: 2015 – 2017

🛠️ Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

Jupyter Notebook

🔍 Key Insights

1\. Cancellation Trends

Nearly 50% of bookings are canceled

City hotels have higher cancellation rates than resort hotels

2\. Pricing Impact

Higher Average Daily Rate (ADR) is strongly correlated with higher cancellations

3\. Seasonal Patterns

January → Highest cancellations \& highest prices

August → Lowest cancellations \& lowest prices

4\. Booking Channels

Online bookings: \~47% (largest share)

Offline agents: \~20%

Direct bookings: \~10%

5\. Geographic Insights

Portugal shows the highest number of cancellations

📈 Visualizations



The project includes:



Cancellation distribution plots

Hotel type comparison (City vs Resort)

Monthly booking and cancellation trends

ADR (Average Daily Rate) analysis

Country-wise cancellation distribution

💡 Recommendations

1\. Pricing Strategy

Reduce prices during high cancellation periods (e.g., January)

Offer discounts and dynamic pricing models

2\. Marketing Campaigns

Increase promotional efforts in high-risk months

Target customer segments prone to cancellation

3\. Operational Improvements

Improve service quality in high-cancellation regions (e.g., Portugal)

Encourage direct bookings to reduce dependency on intermediaries

🚀 How to Run the Project

\# Clone the repository

git clone https://github.com/your-username/hotel-booking-analysis.git



\# Navigate to the project folder

cd hotel-booking-analysis



\# Install dependencies

pip install -r requirements.txt



\# Run Jupyter Notebook

jupyter notebook

📂 Project Structure

hotel-booking-analysis/

│

├── data/                 # Dataset files

├── notebooks/            # Jupyter notebooks

├── visuals/              # Generated plots

├── README.md             # Project documentation

└── requirements.txt      # Dependencies

📌 Future Improvements

Build a machine learning model to predict cancellations

Implement real-time pricing optimization

Deploy as a dashboard (Streamlit / Tableau)

🤝 Contributing



Feel free to fork this repo and submit pull requests for improvements.

