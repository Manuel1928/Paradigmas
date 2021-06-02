extremos :: Int -> [Int] -> [Int]
extremos n xs = take n xs ++ reverse (take n (reverse xs))