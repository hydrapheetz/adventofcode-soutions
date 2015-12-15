import System.IO
import Data.Char (toUpper)
floorDirection :: Char -> Int
floorDirection ')' = -1
floorDirection '(' = 1

main :: IO ()
main = do 
    farts <- readFile "input.txt"
    print $ sum $ map floorDirection farts
