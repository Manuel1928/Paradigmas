rota :: Int -> [a] -> [a]
rota n (x) = drop n x ++ take n x