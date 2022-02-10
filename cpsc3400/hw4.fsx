// hw4.fsx by Haley Uyeunten
// February 13, 2022
// CPSC 3400

(* Write about the function here *)
let rec maxCylinderVolume dim =
    match dim with
    | [] -> 0.0
    | (r, h) :: tail when System.Math.PI * r ** 2.0 * h > maxCylinderVolume tail 
        -> System.Math.PI * r ** 2.0 * h
    | (r, h) :: tail -> maxCylinderVolume tail

let rec elimDuplicatesRec values prev =
    match values with
    | [] -> []
    | h :: t when h = prev -> elimDuplicatesRec t h
    | h :: t -> prev :: elimDuplicatesRec t h

let elimDuplicates values =
    let h :: t = values
    elimDuplicatesRec t h

// let insert value tree = 
// let search value tree = 
// let count func tree =
// let evenCount tree = 
// i don't like BSTs 

let average a b c = 
    float (a + b + c) / 3.0 
 
let compare x y = 
    if x > y then "GREATER" 
    elif x < y then "LESS" 
    else "EQUAL" 