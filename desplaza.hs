desplaza :: Int -> Char -> Char
desplaza n c 
    | elem c ['a'..'z'] = int2let ((let2int c+n) `mod` 26)
    | otherwise         = c