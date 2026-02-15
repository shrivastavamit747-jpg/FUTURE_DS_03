# Marketing Funnel & Conversion Performance Analysis
### Future Interns - Data Science & Analytics Internship (Task 3)

## 📌 Project Overview
This project focuses on analyzing marketing funnel data to identify conversion bottlenecks and evaluate the efficiency of various outreach channels. Using Power BI, I developed an interactive "Stealth-Style" dashboard that provides actionable insights for stakeholders to optimize lead-to-customer conversion rates.

## 📊 Key Insights & Analytics
* **Total Funnel Performance:** Out of 4,521 total leads, 11.5% (521) successfully converted.
* **Stage 1 Drop-off (30.50%):** A significant portion of leads are lost between the initial contact and the engagement stage.
* **The Critical Bottleneck (83.42%):** The primary leakage occurs after leads are engaged. Only 16.6% of engaged leads move to the final conversion.
* **Channel Efficiency:** Voice-based channels (**Telephone and Cellular**) are roughly **3x more effective** than "Unknown" methods, with conversion rates hovering around 14-15%.

## 🎨 Dashboard Design Strategy
To ensure professional clarity, I implemented a custom "Lime & Red" high-contrast theme:
* **Success Metrics (Lime Green #C1FF72):** Used for volume and conversion counts to highlight growth.
* **Alert Metrics (Vibrant Red #FF4B4B):** Strategically used for the 83.42% and 30.50% drop-off rates to immediately flag problem areas for stakeholders.
* **Executive Layout:** Utilized a "Glassmorphism" inspired dark mode with rounded containers and horizontal dropdown slicers to maximize canvas space for data visualization.

## 🛠️ Technical Implementation
* **Tool:** Microsoft Power BI
* **DAX Formulas:** Developed custom measures for Stage-to-Stage Drop-off rates and Channel Efficiency.
* **Visuals:** Funnel Chart, Line and Clustered Column Chart, Scatter Plot (Volume vs. Rate), and interactive Slicers.
* `/data`: Contains the marketing dataset (if applicable).
* `/dashboard`: The `.pbix` file and high-resolution screenshots.
* `README.md`: Project documentation and final summary.
