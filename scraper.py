import pandas as pd

def scrape_mock_market_data():
    # Public dataset with real airline route data
    url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"

    try:
        df = pd.read_csv(url, header=None)
    except Exception as e:
        print("Failed to fetch data:", e)
        return []

    data = []
    for _, row in df.head(10).iterrows():  # Taking just first 10 for demo
        try:
            source = row[2]         # Source airport code
            destination = row[4]    # Destination airport code

            if pd.isnull(source) or pd.isnull(destination):
                continue

            route = f"{source} → {destination}"
            price = 100 + (_ % 50)        # Simulated price
            demand = 60 + (_ * 3 % 40)    # Simulated demand

            data.append({
                "route": route,
                "price": price,
                "demand": demand
            })
        except:
            continue

    return data


