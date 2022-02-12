// hw4.fsx by Haley Uyeunten
// February 13, 2022
// CPSC 3400

let rec maxCylinderVolume dim =
    match dim with
    | [] -> 0.0
    | (r, h) :: tail when System.Math.PI * r ** 2.0 * h > maxCylinderVolume tail 
        -> System.Math.PI * r ** 2.0 * h
    | (r, h) :: tail -> maxCylinderVolume tail

let rec elimDuplicatesRec values prev =
    match values with
    | [] -> []
    | h :: t when t = [] -> prev :: elimDuplicatesRec t h
    | h :: t when h = prev -> elimDuplicatesRec t h
    | h :: t -> prev :: elimDuplicatesRec t h

let elimDuplicates values =
    match values with
    | [] -> []
    | h :: t -> elimDuplicatesRec t h

type BST =
    | Empty
    | TreeNode of int * BST * BST

let rec insert value tree = 
    match tree with
    | Empty -> TreeNode(value, Empty, Empty)
    | TreeNode(v, l, r) when value < v -> TreeNode(v, insert value l, r)
    | TreeNode(v, l, r) when value > v -> TreeNode(v, l, insert value r)
    | _ -> tree

let rec search value tree =
    match tree with
    | Empty -> false
    | TreeNode(v, l, r) when value = v -> true
    | TreeNode(v, l, r) when value < v -> search value l
    | TreeNode(v, l, r) when value > v -> search value r
    | _ -> false

let rec count func tree =
    match tree with
    | Empty -> 0
    | TreeNode(v, l, r) when func v -> 1 + count func l + count func r
    | TreeNode(v, l, r) -> count func l + count func r

let evenCount tree = 
    count (fun v -> v % 2 = 0) tree