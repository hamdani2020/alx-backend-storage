-- The ranks country origins of bands
SELECT origin, SUM(fans) AS nb_fans
    FROM meta_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
