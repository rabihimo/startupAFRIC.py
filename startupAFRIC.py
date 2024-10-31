import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Sample data: A list of startups with hypothetical metrics
data = {
    'Startup': ['Stripe', 'SpaceX', 'Airbnb', 'Palantir', 'Robinhood'],
    'Funding (millions USD)': [600, 5000, 6000, 2000, 500],
    'Revenue (millions USD)': [2000, 2000, 1500, 400, 300],
    'Growth Rate (%)': [50, 25, 40, 30, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define a scoring function
def score_startup(row):
    return (row['Funding (millions USD)'] * 0.3) + (row['Revenue (millions USD)'] * 0.5) + (row['Growth Rate (%)'] * 0.2)

# Apply the scoring function
df['Score'] = df.apply(score_startup, axis=1)

# Sort startups by score
ranked_startups = df.sort_values(by='Score', ascending=False)

# Plotting the ranked startups
plt.figure(figsize=(10, 6))
plt.barh(ranked_startups['Startup'], ranked_startups['Score'], color='cornflowerblue')
plt.xlabel('Score')
plt.title('Ranking of Startups Based on Score')
plt.grid(axis='x')

# Save the plot as a PNG file
plot_file = 'startup_ranking.png'
plt.savefig(plot_file)
plt.close()  # Close the plot to free up memory

@app.route('/')
def index():
    return render_template('index.html', startups=ranked_startups.to_dict(orient='records'))

@app.route('/plot')
def plot():
    return send_file(plot_file)

if __name__ == '__main__':
    app.run(debug=True)
