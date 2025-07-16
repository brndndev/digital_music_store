# As a junior analyst, I'm using Python to run SQL queries and create charts
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the database
conn = sqlite3.connect("chinook.db")

# Step 2: Run queries and store results in dataframes
queries = {
    "Top Earning Artists": """
        SELECT Artist.Name AS ArtistName, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS TotalRevenue
        FROM Artist
        JOIN Album ON Artist.ArtistId = Album.ArtistId
        JOIN Track ON Album.AlbumId = Track.AlbumId
        JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
        GROUP BY Artist.ArtistId
        ORDER BY TotalRevenue DESC
        LIMIT 5;
    """,
    "Invoices by Country": """
        SELECT BillingCountry, COUNT(*) AS InvoiceCount
        FROM Invoice
        GROUP BY BillingCountry
        ORDER BY InvoiceCount DESC;
    """,
    "Top Customers": """
        SELECT Customer.FirstName || ' ' || Customer.LastName AS FullName, SUM(Invoice.Total) AS TotalSpent
        FROM Customer
        JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId
        ORDER BY TotalSpent DESC
        LIMIT 5;
    """,
    "Tracks by Top Artists": """
        SELECT Artist.Name AS ArtistName, COUNT(Track.TrackId) AS TrackCount
        FROM Artist
        JOIN Album ON Artist.ArtistId = Album.ArtistId
        JOIN Track ON Album.AlbumId = Track.AlbumId
        GROUP BY Artist.ArtistId
        ORDER BY TrackCount DESC
        LIMIT 10;
    """
}

# Step 3: Loop through queries, create charts
for name, query in queries.items():
    df = pd.read_sql(query, conn)
    
    # Chart Title will match the query name
    plt.figure(figsize=(8,5))
    plt.bar(df.iloc[:,0], df.iloc[:,1])
    plt.title(name)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.xticks(rotation=30)
    plt.tight_layout()
    
    # Save chart to images folder
    filename = f"images/{name.replace(' ', '_').lower()}.png"
    plt.savefig(filename)
    print(f"Saved {filename}")

# Close connection
conn.close()