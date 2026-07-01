SELECT
    date_part('hour', tpep_pickup_datetime
	AT TIME ZONE 'America/New_York') AS trip_hour,
    count(*)
FROM nyc_yellow_taxi_trips
GROUP BY trip_hour
ORDER BY trip_hour;
