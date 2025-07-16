-- Query 1: Top 5 Earning Artists
-- Just trying to find the artists who made the most money
SELECT 
    Artist.Name AS ArtistName,
    SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS TotalRevenue
FROM Artist
JOIN Album ON Artist.ArtistId = Album.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
GROUP BY Artist.ArtistId
ORDER BY TotalRevenue DESC
LIMIT 5;

-- Query 2: Countries with Most Invoices
-- Wanted to see which countries buy the most music
SELECT 
    BillingCountry,
    COUNT(*) AS InvoiceCount
FROM Invoice
GROUP BY BillingCountry
ORDER BY InvoiceCount DESC;

-- Query 3: Top 5 Customers by Spending
-- These are our most valuable customers based on total purchases
SELECT 
    Customer.FirstName || ' ' || Customer.LastName AS FullName,
    SUM(Invoice.Total) AS TotalSpent
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpent DESC
LIMIT 5;

-- Query 4: Top 10 Artists by Number of Tracks
-- Curious about which artists have the biggest catalogs
SELECT 
    Artist.Name AS ArtistName,
    COUNT(Track.TrackId) AS TrackCount
FROM Artist
JOIN Album ON Artist.ArtistId = Album.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
GROUP BY Artist.ArtistId
ORDER BY TrackCount DESC
LIMIT 10;
