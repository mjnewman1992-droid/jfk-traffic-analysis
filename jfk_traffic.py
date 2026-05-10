import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt



terminal_passengers = {
    "Terminal 1": 6138662,
    "Terminal 4": 27004135,
    "Terminal 5": 14729507,
    "Terminal 7": 3985801,
    "Terminal 8": 11405882
}

terminal_passengers_df = pd.DataFrame(list(terminal_passengers.items()), columns=['Terminals','Passenger Count'])
terminal_passengers_df.index = terminal_passengers_df.index + 1

annual_airport_volume = np.sum(terminal_passengers_df['Passenger Count'])
terminal_passengers_df['Percent_Share'] = round(terminal_passengers_df['Passenger Count'] / annual_airport_volume * 100, 2)
terminal_passengers_df['Daily Average'] = round(terminal_passengers_df['Passenger Count'] / 365, 0)

print (terminal_passengers_df)

transportation_modt = {
    "Ridesharing (Uber/Lyft)": 21.4,
    "Private Car - Drop-off": 21.7,
    "Taxi/Limo": 17.3,
    "Parking (Private Car)": 14.8,
    "AirTrain/Rail": 13.2,
    "Bus/Shuttle": 3.5,
    "Rental Car": 8.1
}

transportation_modt_df = pd.DataFrame(list(transportation_modt.items()), columns=['Transportation Mode', 'Percentage'])

colors = ['#003366', "#F00000", 'orange', 'gray', 'purple', 'green', 'yellow']
plt.subplot(1, 2, 1)
plt.bar(terminal_passengers_df['Terminals'], terminal_passengers_df['Passenger Count'], color=colors)
plt.title("Passenger Volume Comparison by Terminal in 2024")
plt.xlabel("Terminals")
plt.xticks(rotation=90)
plt.ylabel("Annual Passengers (By the Millions)")

plt.subplot(1, 2, 2)
plt.pie(transportation_modt_df['Percentage'],labels=transportation_modt_df['Transportation Mode'], autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("How Passengers Arrived at JFK Airport in 2024")
plt.tight_layout()

transportation_modt_df
plt.show() 