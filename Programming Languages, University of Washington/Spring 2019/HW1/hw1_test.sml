use "hw1.sml";
val test_1__is_older = (is_older((2020,1,31), (2020,1,29)) = false)
val test_1__number_in_month = (number_in_month([(2020, 1, 1), (2020, 2, 1)], 1) = 1)
val test_1__number_in_months = (number_in_months([(2020, 1, 1), (2020, 2, 1), (2020, 3, 1)], [1, 2]) = 2)
val test_1__dates_in_month = (dates_in_month([(2020, 1, 1), (2020, 2, 1)], 1) = [(2020, 1, 1)])
val test_1__dates_in_months = (dates_in_months([(2020, 1, 1), (2020, 2, 1)], [1, 2]) = [(2020, 1, 1), (2020, 2, 1)])
val test_1__get_nth = (get_nth(["a", "b", "c"], 2) = "b")
val test_1__date_to_string = (date_to_string((2015, 9, 10)) = "September-10-2015")
val test_1__number_before_reaching_sum = (number_before_reaching_sum(4, [2, 3, 4]) = 1)
val test_2__number_before_reaching_sum = (number_before_reaching_sum(5, [2, 3, 4]) = 2)
val test_3__number_before_reaching_sum = (number_before_reaching_sum(6, [2, 3, 4]) = 2)
val test_1__what_month = (what_month(80) = 3)
val test_1__month_range = (month_range(80, 330) = [3, 4, 5, 6, 7, 8, 9, 10, 11])
val test_1__oldest = (oldest([(2019, 2, 28), (2018, 12, 1), (2018, 1, 1)]) = SOME (2018, 1, 1) )
val test_1__cumulative_sum = (cumulative_sum([12, 27, 13]) = [12, 39, 52])