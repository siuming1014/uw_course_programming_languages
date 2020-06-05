datatype sgn = P | N | Z

fun is_older ((y1, m1, d1), (y2, m2, d2)) =
    let fun is_smaller (x1, x2) = if x1<x2 then P else if x1>x2 then N else Z
    in
        case (is_smaller(y1, y2), is_smaller(m1, m2), is_smaller(d1, d2)) of 
            (P, _, _) => true
          | (N, _, _) => false
          | (Z, P, _) => true
          | (Z, N, _) => false
          | (Z, Z, P) => true
          | (Z, Z, _) => false
    end

fun number_in_month (dates, month) = 
    let fun helper(acc, dates_) =
            case dates_ of
                [] => acc
              | (y, m, d)::tl_dates => helper(acc + (if m = month then 1 else 0), tl_dates)
    in
        helper(0, dates)
    end

fun number_in_months (dates, months) = 
    let fun helper(acc, months_) = 
            case months_ of
                [] => acc
              | m::tl_months => helper(acc + number_in_month(dates, m), tl_months)
    in
        helper(0, months)
    end

fun dates_in_month (dates, month) =
    case dates of
        [] => []
      | (y, m, d)::tl_dates => 
            let val tl_ans = dates_in_month(tl_dates, month)
            in
                if m = month
                then (y, m, d) :: tl_ans
                else tl_ans
            end

fun dates_in_months (dates, months) =
    let fun helper(acc, months_) = 
            case months_ of
                [] => acc
              | m::tl_months => helper(dates_in_month(dates, m) @ acc, tl_months)
    in
        helper([], months)
    end
    
fun get_nth (strs, n) = 
    case strs of
        [] => raise List.Empty
      | str::tl_strs => if n = 1 then str else get_nth(tl_strs, n - 1)

fun date_to_string (date) =
    let val (y, m, d) = date
    in
        let val month_strs = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        in
            get_nth(month_strs, m) ^ "-" ^ Int.toString(d) ^ "-" ^ Int.toString(y)
        end
    end

fun number_before_reaching_sum (sum : int, nums : int list) = 
    case nums of
        [] => raise List.Empty
      | num::tl_nums => if (sum < num) then 0 else 1 + number_before_reaching_sum(sum - num, tl_nums)

fun what_month (day_of_year) = 
    1 + number_before_reaching_sum(day_of_year, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

fun month_range (day1, day2) = 
    let fun int_range(acc, x, y) = 
            if x > y 
            then acc
            else int_range(y::acc, x, y - 1)
    in
        int_range([], what_month(day1), what_month(day2))
    end

fun oldest (dates) = 
    case dates of
        [] => NONE
      | date::tl_dates =>
            case oldest(tl_dates) of
                NONE => SOME date
              | SOME(date_2) => SOME (if is_older(date, date_2) then date else date_2)

fun cumulative_sum (nums) = 
    let fun helper (acc, nums_) =
            case nums_ of
                [] => []
              | num::tl_nums => (acc + num) :: helper(acc + num, tl_nums)
    in
        helper(0, nums)
    end