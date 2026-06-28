SELECT year, month, soybeans_export_value,
    round(
       avg(soybeans_export_value)
            OVER(ORDER BY year, month
                 ROWS BETWEEN 11 PRECEDING AND CURRENT ROW), 0)
       AS twelve_month_avg
FROM us_exports
ORDER BY year, month;

