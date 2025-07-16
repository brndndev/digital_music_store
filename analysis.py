
# Junior Analyst Note: This script connects to the Chinook database,
# runs SQL queries, and outputs data in JSON format for Chart.js integration.

import sqlite3
import pandas as pd
import json

# Connect to the database
conn = sqlite3.connect('chinook.db')

# Define queries
queries = {
    'top_earning_artists': """
        SELECT Artist.Name AS ArtistName, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS TotalRevenue
        FROM Artist
        JOIN Album ON Artist.ArtistId = Album.ArtistId
        JOIN Track ON Album.AlbumId = Track.AlbumId
        JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
        GROUP BY Artist.ArtistId
        ORDER BY TotalRevenue DESC
        LIMIT 5;
    """,
    'invoices_by_country': """
        SELECT BillingCountry, COUNT(*) AS InvoiceCount
        FROM Invoice
        GROUP BY BillingCountry
        ORDER BY InvoiceCount DESC
        LIMIT 10;
    """,
    'top_customers': """
        SELECT Customer.FirstName || ' ' || Customer.LastName AS FullName, SUM(Invoice.Total) AS TotalSpent
        FROM Customer
        JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId
        ORDER BY TotalSpent DESC
        LIMIT 5;
    """,
    'tracks_by_top_artists': """
        SELECT Artist.Name AS ArtistName, COUNT(Track.TrackId) AS TrackCount
        FROM Artist
        JOIN Album ON Artist.ArtistId = Album.ArtistId
        JOIN Track ON Album.AlbumId = Track.AlbumId
        GROUP BY Artist.ArtistId
        ORDER BY TrackCount DESC
        LIMIT 10;
    """
}

# Execute queries and store in dictionary
data_for_js = {}
for key, query in queries.items():
    df = pd.read_sql(query, conn)
    data_for_js[key] = {
        'labels': df.iloc[:, 0].tolist(),
        'values': df.iloc[:, 1].tolist()
    }

# Save to JSON
with open('data.json', 'w') as f:
    json.dump(data_for_js, f, indent=4)

conn.close()
print('Data exported to data.json for Chart.js')
