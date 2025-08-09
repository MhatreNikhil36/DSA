SELECT d.driver_id,
       COUNT(r.ride_id) AS cnt
FROM (SELECT DISTINCT driver_id FROM Rides) AS d
LEFT JOIN Rides AS r
       ON d.driver_id = r.passenger_id
GROUP BY d.driver_id;
