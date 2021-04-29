-- 2-fans.sql / 0x0C. MySQL advanced /  Web Stack programming ― Back-end
-- Ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT `origin`, SUM(`fans`) AS `nb_fans`
FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
