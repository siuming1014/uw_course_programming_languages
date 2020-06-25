(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
    string), then you avoid several of the functions in problem 1 having
    polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
fun all_except_option(s, input_slst) = 
    let
        fun helper1(acc, slst) = 
            case slst of
                [] => acc
              | x::xs => helper1(x::acc, xs)
        
        fun helper2(acc, slst) = 
            case slst of
                [] => NONE
              | x::xs =>
                    if same_string(x, s)
                    then SOME(helper1(acc, xs))
                    else helper2(x::acc, xs)
    in
        helper2([], input_slst)
    end

fun all_except_option(s, slst) = 
    let 
        fun not_same_as_s(s2) = not (same_string(s, s2))
        val filtered_slst = List.filter not_same_as_s slst
    in
        if (List.length slst) = (List.length filtered_slst)
        then NONE
        else SOME filtered_slst
    end

fun get_substitutions1(substitutions, s) = 
    case substitutions of
        [] => []
      | lst::tlstlst => 
            case all_except_option(s, lst) of
                NONE => get_substitutions1(tlstlst, s)
              | SOME lst2 => get_substitutions1(tlstlst, s) @ lst2

fun get_substitutions2(substitutions, s) = 
    let fun combine_list(acc, lstlst) = 
            case lstlst of
                [] => acc
              | lst::tlstlst => 
                    case all_except_option(s, lst) of
                        NONE => combine_list(acc, tlstlst)
                      | SOME lst2 => combine_list(acc @ lst2, tlstlst)
    in
        combine_list([], substitutions)
    end

fun similar_names(substitutions, {first=f, last=l, middle=m}) = 
    let
        val subs_lst = get_substitutions2(substitutions, f)
        fun helper(acc, subs_lst_) =
            case subs_lst_ of
                [] => acc
              | x::xs => helper({first=x, last=l, middle=m}::acc, xs)
    in
        {first=f, last=l, middle=m}::helper([], subs_lst)
    end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color(card: card) = 
    case card of
        (Clubs, _) => Black
      | (Spades, _) => Black
      | (Diamonds, _) => Red
      | (Hearts, _) => Red

fun card_value(card: card) = 
    case card of
        (_, Num x) => x
      | (_, Ace) => 11
      | (_, _) => 10

fun remove_card(cs, c, e) =
    let
        fun helper1(acc, cs_) = 
            case cs_ of
                [] => acc
              | x::xs => helper1(x::acc, xs)
        
        fun helper2(acc, cs_) = 
            case cs_ of
                [] => raise e
              | x::xs =>
                    if x = c
                    then helper1(acc, xs)
                    else helper2(x::acc, xs)
    in
        helper2([], cs)
    end

fun all_same_color(cs) = 
    case cs of
        [] => true
      | c::[] => true
      | c1::(c2::rest) => if card_color(c1) = card_color(c2) then all_same_color(c2::rest) else false

fun sum_cards(cs) = 
    let fun helper(acc, cs_) = 
            case cs_ of
                [] => acc
              | x::xs => helper(card_value(x) + acc, xs)
    in
        helper(0, cs)
    end

fun score(hc, goal) = 
    let
        val diff = sum_cards(hc) - goal
        val prelim_score = if diff > 0 then 3 * diff else ~diff
        val act_score = if all_same_color(hc) then prelim_score div 2 else prelim_score
    in
        act_score
    end

fun officiate(initial_card_lst, initial_mv_lst, goal) = 
    let fun play(hc, card_lst, mv_lst) = 
            case mv_lst of
                [] => score(hc, goal)
              | (Discard c)::mv_rest => play(remove_card(hc, c, IllegalMove), card_lst, mv_rest)
              | Draw::mv_rest =>
                    case card_lst of
                        [] => score(hc, goal)
                      | c::c_rest =>
                            let val next_hc = c::hc
                            in
                                if sum_cards(next_hc) > goal
                                then score(next_hc, goal)
                                else play(next_hc, c_rest, mv_rest)
                            end
    in
        play([], initial_card_lst, initial_mv_lst)
    end