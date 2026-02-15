import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# 1. LOAD AND CLEAN DATA
# Removing outer quotes and using semicolon separator specific to bank.csv
with open('bank.csv', 'r') as f:
    content = f.read().replace('"', '')

df = pd.read_csv(io.StringIO(content), sep=';')

# 2. DEFINE FUNNEL STAGES
# Stage 1: Awareness (Total Leads)
total_leads = len(df)

# Stage 2: Engagement (Interest)
# We define 'Engaged' as a call duration > 120 seconds (meaningful interaction)
engaged_leads = len(df[df['duration'] > 120])

# Stage 3: Conversion (Action)
conversions = len(df[df['y'] == 'yes'])

funnel_metrics = pd.DataFrame({
    'Stage': ['Total Leads', 'Engaged Leads', 'Conversions'],
    'Count': [total_leads, engaged_leads, conversions]
})

# 3. CALCULATE DROP-OFFS
funnel_metrics['Retention_Rate'] = (funnel_metrics['Count'] / funnel_metrics['Count'].shift(1).fillna(total_leads)) * 100
funnel_metrics['Drop_off_Rate'] = 100 - funnel_metrics['Retention_Rate']

# 4. CHANNEL PERFORMANCE ANALYSIS
# Identifying which contact method has the highest conversion rate
channel_conv = df.groupby('contact')['y'].apply(lambda x: (x == 'yes').mean() * 100).reset_index()
channel_conv.columns = ['Contact_Method', 'Conversion_Rate']
channel_conv = channel_conv.sort_values(by='Conversion_Rate', ascending=False)

# 5. VISUALIZATION
plt.style.use('seaborn-v0_8-muted')

# Plot A: Funnel Chart
plt.figure(figsize=(10, 6))
plt.barh(funnel_metrics['Stage'][::-1], funnel_metrics['Count'][::-1], color=['#2ca02c', '#ff7f0e', '#1f77b4'])
for index, value in enumerate(funnel_metrics['Count'][::-1]):
    plt.text(value, index, f' {value} ({round(value/total_leads*100, 1)}%)', va='center', fontweight='bold')
plt.title('Marketing Funnel: Lead-to-Conversion drop-offs', fontsize=14)
plt.xlabel('Number of Customers')
plt.tight_layout()
plt.savefig('funnel_analysis.png')

# Plot B: Conversion by Channel
plt.figure(figsize=(10, 5))
sns.barplot(data=channel_conv, x='Contact_Method', y='Conversion_Rate', palette='viridis')
plt.title('Conversion Rate by Communication Channel (%)', fontsize=14)
plt.ylabel('Conversion %')
plt.tight_layout()
plt.savefig('channel_performance.png')

# 6. EXPORT FINAL DATA FOR POWER BI / PORTFOLIO
df['Is_Converted'] = df['y'].apply(lambda x: 1 if x == 'yes' else 0)
df.to_csv('marketing_funnel_final_data.csv', index=False)

print("Analysis Complete. Funnel metrics and visualizations generated.")
print(funnel_metrics)