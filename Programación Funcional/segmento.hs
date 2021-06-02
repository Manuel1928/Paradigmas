segmento :: Int -> Int -> [Int] -> [Int]
segmento m n xs = drop (m - 1) (take n xs)