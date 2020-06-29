(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
         | Variable of string
         | UnitP
         | ConstP of int
         | TupleP of pattern list
         | ConstructorP of string * pattern

datatype valu = Const of int
          | Unit
          | Tuple of valu list
          | Constructor of string * valu

fun g f1 f2 p =
    let 
    val r = g f1 f2 
    in
    case p of
        Wildcard          => f1 ()
      | Variable x        => f2 x
      | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
      | ConstructorP(_,p) => r p
      | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
         | UnitT
         | IntT
         | TupleT of typ list
         | Datatype of string

(**** you can put all your code here ****)

fun only_capitals str_lst = 
    List.filter (fn s => Char.isUpper(String.sub(s, 0))) str_lst

fun longest_string1 str_lst = 
    List.foldl (fn (s1, s2) => if String.size s1 > String.size s2 then s1 else s2) "" str_lst

fun longest_string2 str_lst = 
    List.foldl (fn (s1, s2) => if String.size s1 >= String.size s2 then s1 else s2) "" str_lst

fun longest_string_helper f str_lst = 
    List.foldl (fn (s1, s2) => if f(String.size s1, String.size s2) then s1 else s2) "" str_lst

val longest_string3 = longest_string_helper (fn (x, y) => x > y)

val longest_string4 = longest_string_helper (fn (x, y) => x >= y)

val longest_capitalized = longest_string1 o only_capitals

val rev_string = String.implode o List.rev o String.explode

fun first_answer f lst =
    case lst of
        []    => raise NoAnswer
      | x::xs =>
              case f x of
                NONE   => first_answer f xs
              | SOME v => v

fun all_answers f lst = 
    let fun helper acc lst_ =
            case lst_ of
                []    => SOME acc
              | x::xs =>
                      case f x of
                        NONE      => NONE
                      | SOME lstn => helper (acc @ lstn) xs
    in
        helper [] lst
    end

fun count_wildcards p = 
    g (fn () => 1) (fn s => 0) p 

fun count_wild_and_variable_lengths p = 
    g (fn () => 1) String.size p 

fun count_some_var (s, p) =
    g (fn () => 0) (fn s2 => if s = s2 then 1 else 0) p

fun check_pat input_p = 
    let
        fun helper1 p = 
            case p of
                Wildcard          => []
              | Variable x        => [x]
              | TupleP ps         => List.foldl (fn (p,i) => helper1(p) @ i) [] ps
              | ConstructorP(_,p) => helper1(p)
              | _                 => []
        
        fun has_repeats lst = 
            case lst of
                []    => false
              | x::[] => false
              | x::xs => if List.exists (fn s => x = s) xs then true else has_repeats xs

    in
        not ((has_repeats o helper1) input_p)
    end

fun match (input_v, input_p) = 
    case (input_v, input_p) of
        (_, Wildcard) => SOME []
      | (v, Variable s) => SOME [(s, v)]
      | (Unit, UnitP) => SOME []
      | (Const i, ConstP iP) => if i = iP then SOME [] else NONE
      | (Tuple vs, TupleP ps) =>
            if List.length vs = List.length ps
            then all_answers (fn (v, p) => match(v, p)) (ListPair.zip (vs, ps))
            else NONE
      | (Constructor (s1, v), ConstructorP (s2, p)) =>
            if s1 = s2 then match(v, p) else NONE
      | (_, _) => NONE

fun first_match v ps = 
    SOME (first_answer (fn p => match(v, p)) ps) handle NoAnswer => NONE
