fun is_older (date_1 : int*int*int, date_2 : int*int*int) =
    if (#1 date_1) < (#1 date_2)
    then true
    else if (#1 date_1) > (#1 date_2)
    then false
    else if (#2 date_1) < (#2 date_2)
    then true
    else if (#2 date_1) > (#2 date_2)
    then false
    else if (#3 date_1) < (#3 date_2)
    then true
    else false

fun number_in_month (dates : (int*int*int) list, month : int) = 
    let fun helper(acc : int, dates_ : (int*int*int) list) =
            if null dates_
            then acc
            else helper(acc + (if (#2 (hd dates_)) = month then 1 else 0), tl dates_)
    in
        helper(0, dates)
    end

fun number_in_months (dates : (int*int*int) list, months : int list) = 
    let fun helper(acc : int, months_ : int list) = 
            if null months_
            then acc
            else helper(acc + number_in_month(dates, hd months_), tl months_)
    in
        helper(0, months)
    end

fun dates_in_month (dates : (int*int*int) list, month : int) =
    if null dates
    then []
    else 
        let val tl_ans = dates_in_month(tl dates, month)
        in
            if (#2 (hd dates)) = month
            then (hd dates) :: tl_ans
            else tl_ans
        end

fun dates_in_months (dates : (int*int*int) list, months : int list) =
    if (null months)
    then []
    else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)
    
fun get_nth (strs : string list, n : int) = 
    if n = 1
    then hd strs
    else get_nth(tl strs, n - 1)

fun date_to_string (date : (int*int*int)) =
    let val month_strs = ["January", "February", "March", "April", "May", "June", 
                          "July", "August", "September", "October", "November", "December"]
    in
        get_nth(month_strs, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
    end

fun number_before_reaching_sum (sum : int, nums : int list) = 
    let fun helper(acc : int, acc_sum : int, nums_ : int list) = 
        if (null nums_)
        then acc
        else
            if sum <= acc_sum + (hd nums_)
            then acc
            else helper(acc + 1, acc_sum + (hd nums_), tl nums_)
    in
        helper(0, 0, nums)
    end

fun what_month (day_of_year : int) = 
    1 + number_before_reaching_sum(day_of_year, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

fun month_range (day1 : int, day2 : int) = 
    let fun helper(acc : int list, x : int, y : int) =
            if x > y 
            then acc
            else helper(what_month(y) :: acc, x, y - 1)
    in
        helper([], day1, day2)
    end

fun oldest (dates : (int*int*int) list) = 
    if (null dates)
    then NONE 
    else
        let fun oldest_notnone (dates : (int*int*int) list) = 
                if null (tl dates)
                then hd dates
                else
                    let val tl_ans = oldest_notnone(tl dates)
                    in
                        if is_older(hd dates, tl_ans)
                        then hd dates
                        else tl_ans
                    end
        in
            SOME (oldest_notnone dates)
        end