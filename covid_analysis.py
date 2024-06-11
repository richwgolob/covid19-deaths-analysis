import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from local CSV file
def fetch_data(file_path):
    data = pd.read_csv(file_path)
    return data

#Processing and cleaning the data
def process_data(df, country):
    df = df[df['location'] == country]
    df['date'] = pd.to_datetime(df['date'])
    df = df[['date', 'total_deaths']]
    df.rename(columns={'date': 'Date', 'total_deaths': 'Deaths'}, inplace=True)
    df.set_index('Date', inplace=True)
    return df

#Visualizing the data
def visualize_data(df, country):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Deaths')
    plt.title(f'COVID-19 Deaths in {country}')
    plt.xlabel('Date')
    plt.ylabel('Deaths')
    plt.show()

#Basic analysis
def analyze_data(df, country):
    total_deaths = df['Deaths'].sum()
    latest_death_count = df['Deaths'].iloc[-1]
    print(f"Total deaths in {country}: {total_deaths}")
    print(f"Latest death count in {country}: {latest_death_count}")

#Main
def main():
    country = "United States" 
    file_path = "C:/Users/Richard G/Desktop/covid_analysis/owid-covid-data.csv"
    data = fetch_data(file_path)
    df = process_data(data, country)
    visualize_data(df, country)
    analyze_data(df, country)

if __name__ == "__main__":
    main()

