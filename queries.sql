-- Junior Analyst Note: This file contains the SQL queries used to build our dashboard

-- 1. Top Earning Artists
-- Goal: Find which artists brought in the most revenue by summing their track sales
SELECT Artist.Name AS ArtistName, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS TotalRevenue
FROM Artist
JOIN Album ON Artist.ArtistId = Album.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
GROUP BY Artist.ArtistId, Artist.Name
ORDER BY TotalRevenue DESC
LIMIT 5;

-- 2. Invoices by Country
-- Goal: Count how many invoices came from each country to identify key markets
SELECT BillingCountry, COUNT(*) AS InvoiceCount
FROM Invoice
GROUP BY BillingCountry
ORDER BY InvoiceCount DESC
LIMIT 10;

-- 3. Top Customers by Spending
-- Goal: Who are our highest spending customers? Perfect for loyalty programs
SELECT CONCAT(Customer.FirstName, ' ', Customer.LastName) AS FullName, SUM(Invoice.Total) AS TotalSpent
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId, Customer.FirstName, Customer.LastName
ORDER BY TotalSpent DESC
LIMIT 5;

-- 4. Top 10 Artists by Track Count
-- Goal: Which artists have the biggest catalogs in our database?
SELECT Artist.Name AS ArtistName, COUNT(Track.TrackId) AS TrackCount
FROM Artist
JOIN Album ON Artist.ArtistId = Album.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
GROUP BY Artist.ArtistId, Artist.Name
ORDER BY TrackCount DESC
LIMIT