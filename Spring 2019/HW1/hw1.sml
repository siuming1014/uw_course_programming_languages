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
    let fun number_in_month_(acc : int, dates_ : (int*int*int) list) =
            if null dates_
            then acc
            else number_in_month_(acc + (if (#2 (hd dates_)) = month then 1 else 0), tl dates_)
    in
        number_in_month_(0, dates)
    end

fun number_in_months (dates : (int*int*int) list, months : int list) = 
    let fun number_in_months_(acc : int, months_ : int list) = 
            if null months_
            then acc
            else number_in_months_(acc + number_in_month(dates, hd months_), tl months_)
    in
        number_in_months_(0, months)
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
        get_nth(month_strs, #2 date) ^ "-" ^ Int.toString(#3 date) ^ "-" ^ Int.toString(#1 date)
    end

fun number_before_reaching_sum (sum : int, num_lst : int list) = 
    if (sum < (hd num_lst))
    then 0
    else 1 + number_before_reaching_sum(sum - (hd num_lst), tl num_lst)

fun what_month (day_of_year : int) = 
    1 + number_before_reaching_sum(day_of_year, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

fun month_range (day1 : int, day2 : int) = 
    let fun int_range(x : int, y : int) = 
            if x > y 
            then []
            else x :: int_range(x + 1, y)
    in
        int_range(what_month(day1), what_month(day2))
    end

fun oldest (dates : (int*int*int) list) = 
    if (null dates)
    then NONE 
    else
        let fun oldest_ (dates : (int*int*int) list) = 
                if null (tl dates)
                then hd dates
                else
                    let val tl_ans = oldest_(tl dates)
                    in
                        if is_older(hd dates, tl_ans)
                        then hd dates
                        else tl_ans
                    end
        in
            SOME (oldest_ dates)
        end

fun cumulative_sum (num_lst : int list) = 
    let fun cum_sum_ (acc : int, nums_ : int list) =
            if null nums_
            then []
            else (acc + hd nums_) :: cum_sum_(acc + hd nums_, tl nums_)
    in
        cum_sum_(0, num_lst)
    end