(* CSE 341, HW2 Provided Code *)

(* main datatype definition we will use throughout the assignment *)
datatype json =
         Num of real (* real is what SML calls floating point numbers *)
       | String of string
       | False
       | True
       | Null
       | Array of json list
       | Object of (string * json) list

(* some examples of values of type json *)
val json_pi    = Num 3.14159
val json_hello = String "hello"
val json_false = False
val json_array = Array [Num 1.0, String "world", Null]
val json_obj   = Object [("foo", json_pi), ("bar", json_array), ("ok", True)]

(* some provided one-liners that use the standard library and/or some features
   we have not learned yet. (Only) the challenge problem will need more
   standard-library functions. *)

(* dedup : string list -> string list -- it removes duplicates *)
fun dedup xs = ListMergeSort.uniqueSort String.compare xs

(* strcmp : string * string -> order compares strings alphabetically
   where datatype order = LESS | EQUAL | GREATER *)
val strcmp = String.compare                                        
                        
(* convert an int to a real *)
val int_to_real = Real.fromInt

(* absolute value of a real *)
val real_abs = Real.abs

(* convert a real to a string *)
val real_to_string = Real.toString

(* return true if a real is negative : real -> bool *)
val real_is_negative = Real.signBit

(* We now load 3 files with police data represented as values of type json.
   Each file binds one variable: small_incident_reports (10 reports), 
   medium_incident_reports (100 reports), and large_incident_reports 
   (1000 reports) respectively.

   However, the large file is commented out for now because it will take 
   about 15 seconds to load, which is too long while you are debugging
   earlier problems.  In string format, we have ~10000 records -- if you
   do the challenge problem, you will be able to read in all 10000 quickly --
   it's the "trick" of giving you large SML values that is slow.
*)

(* Make SML print a little less while we load a bunch of data. *)
       ; (* this semicolon is important -- it ends the previous binding *)
Control.Print.printDepth := 3;
Control.Print.printLength := 3;

use "parsed_small_police.sml";
use "parsed_medium_police.sml";

(* (* uncomment when you are ready to do the problems needing the large report*)
use "parsed_large_police.sml"; 

val large_incident_reports_list =
    case large_incident_reports of
        Array js => js
      | _ => raise (Fail "expected large_incident_reports to be an array")
*)

val large_incident_reports_list =
    case medium_incident_reports of
        Array js => js
      | _ => raise (Fail "expected large_incident_reports to be an array")


(* Now make SML print more again so that we can see what we're working with. *)
; Control.Print.printDepth := 20;
Control.Print.printLength := 20;

(**** PUT PROBLEMS 1-8 HERE ****)
fun make_silly_json (i) = 
    let fun helper (acc, i_) = 
            if i_ = i + 1
            then acc
            else helper(Object [("n", Num (int_to_real i_)), ("b", True)] :: acc, i_ + 1)
    in
        Array(helper([], 1))
    end

fun assoc (k, xs) = 
  case xs of
      [] => NONE
    | (k1, v1)::xs_ =>
        if k = k1
        then SOME v1
        else assoc (k, xs_)

fun dot (j, k) = 
    case j of
        Object xs => assoc(k, xs)
      | _ => NONE

fun one_fields (j) = 
    case j of
        Object xs =>
            let fun helper(acc, xs_) = 
                    case xs_ of
                        [] => acc
                      | (k, v)::xs__ => helper(k::acc, xs__)
            in
                helper([], xs)
            end
      | _ => []

fun no_repeats (strs) = 
    length(strs) = length(dedup(strs))

fun recursive_no_field_repeats(j) = 
    case j of
        Object sj_lst => 
            let fun helper1(acc, sj_lst_) = 
                    case sj_lst_ of
                        [] => acc
                      | ((s, j_)::xs) => helper1(acc andalso recursive_no_field_repeats(j_), xs)
            in
                helper1(no_repeats(one_fields(j)), sj_lst)
            end
      | Array j_lst =>
            let fun helper2(acc, j_lst_) = 
                    case j_lst_ of
                        [] => acc
                      | (j_::js) => helper2(acc andalso recursive_no_field_repeats(j_), js)
            in
                helper2(true, j_lst)
            end
      | _ => true

fun count_occurrences(strs, e) = 
    let fun helper(acc, cur_count, cur_str, strs_) = 
            case strs_ of
                [] => if cur_count > 0 then (cur_str, cur_count) :: acc else acc
              | (s::xs) => 
                  case (strcmp(cur_str, s)) of
                      LESS => helper(if cur_count > 0 then (cur_str, cur_count) :: acc else acc, 1, s, xs)
                    | EQUAL => helper(acc, cur_count + 1, cur_str, xs)
                    | GREATER => raise e
    in 
        helper([], 0, "", strs)
    end
    
fun string_values_for_field(target_str, j_lst) =
    let fun helper(acc, js_) = 
            case js_ of
                [] => acc
              | j_::js_t => helper((case dot(j_, target_str) of SOME(String(vs)) => vs::acc | _ => acc), js_t)
    in 
        helper([], j_lst)
    end

(* histogram and historgram_for_field are provided, but they use your 
   count_occurrences and string_values_for_field, so uncomment them 
   after doing earlier problems *)

(* histogram_for_field takes a field name f and a list of objects js and 
   returns counts for how often a string is the contents of f in js. *)

exception SortIsBroken

fun histogram (xs : string list) : (string * int) list =
  let
    fun compare_strings (s1 : string, s2 : string) : bool = s1 > s2

    val sorted_xs = ListMergeSort.sort compare_strings xs
    val counts = count_occurrences (sorted_xs,SortIsBroken)

    fun compare_counts ((s1 : string, n1 : int), (s2 : string, n2 : int)) : bool =
      n1 < n2 orelse (n1 = n2 andalso s1 < s2)
  in
    ListMergeSort.sort compare_counts counts
  end

fun histogram_for_field (f,js) =
  histogram (string_values_for_field (f, js))


(**** PUT PROBLEMS 9-11 HERE ****)

;Control.Print.printDepth := 3;
Control.Print.printLength := 3;

fun filter_field_value(target_field, target_value, j_lst) = 
    let fun helper(acc, js_) = 
            case js_ of
                [] => acc
              | j_::js_t => helper((case dot(j_, target_field) of SOME(String(s)) => if s = target_value then j_::acc else acc | _ => acc), js_t)
    in
        helper([], j_lst)
    end

val large_event_clearance_description_histogram = histogram_for_field("event_clearance_description", large_incident_reports_list)
val large_hundred_block_location_histogram = histogram_for_field("hundred_block_location", large_incident_reports_list)

(**** PUT PROBLEMS 12-15 HERE ****)

;Control.Print.printDepth := 20;
Control.Print.printLength := 20;

val forty_third_and_the_ave_reports = filter_field_value("hundred_block_location", "43XX BLOCK OF UNIVERSITY WAY NE", large_incident_reports_list)
val forty_third_and_the_ave_event_clearance_description_histogram = histogram_for_field("event_clearance_description", forty_third_and_the_ave_reports)

val nineteenth_and_forty_fifth_reports = filter_field_value("hundred_block_location", "45XX BLOCK OF 19TH AVE NE", large_incident_reports_list)
val nineteenth_and_forty_fifth_event_clearance_description_histogram = histogram_for_field("event_clearance_description", nineteenth_and_forty_fifth_reports)

(**** PUT PROBLEMS 16-19 HERE ****)

fun concat_with(separator, strs) = 
    let fun helper(acc, strs_) = 
            case strs_ of
                [] => acc
              | x::[] => helper(acc ^ x, [])
              | x::xs => helper(acc ^ x ^ separator, xs)
    in
        helper("", strs)
    end

fun quote_string(s) = "\"" ^ s ^ "\""

fun real_to_string_for_json(x) =
    if x > 0.0
    then real_to_string(x)
    else "-" ^ real_to_string(real_abs(x))

(* For CHALLENGE PROBLEMS, see hw2challenge.sml *)

