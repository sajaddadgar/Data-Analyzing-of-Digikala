# 1
select
       city_name_fa,
       avg(hour(time(dateTime_cartfinalize))) as hours
from
     customers
group by
         city_name_fa
order by
         hours;

# 2
select
       sum(quantity_item),
       case
         when
           hour(time (dateTime_cartfinalize)) < 5
           then ' < 5'
         when hour(time (dateTime_cartfinalize)) >19
           then '>19'
         end as x
from
     customers group by x;

# 3
select
       hour(time(dateTime_cartfinalize)) as hours,
       sum(quantity_item) as quantity
from
     customers
group by
         hours
order by
         hours;

# 4
select
       dayofweek(date(dateTime_cartfinalize)) as day_number,
       dayname(date(dateTime_cartfinalize)) as day_name,
       sum(quantity_item) as quantity
from
     customers
group by
         day_name
order by
         day_number;

# 5
select
       case
         when day(date (dateTime_cartfinalize)) < 10
           then '10 روز اول ماه'
         when day(date (dateTime_cartfinalize)) between 10 and 19
           then '10 روز دوم ماه'
         when day(date (dateTime_cartfinalize)) >= 20
           then '10 روز سوم ماه'
         end as days, sum(quantity_item) from customers group by days;


# 6
SELECT
       customers.city_name_fa,
       (count(customers.city_name_fa)/city_population.population) as indicator
from
     customers, city_population
where
      customers.city_name_fa=city_population.name
group by
         customers.city_name_fa
order by
         indicator desc ;

# 7
select distinct year(date(dateTime_cartfinalize)) from customers;
select
       case
         when year(date(dateTime_cartfinalize)) = 2013
           then '1392'
         when year(date(dateTime_cartfinalize)) = 2014
           then '1393'
         when year(date(dateTime_cartfinalize)) = 2015
           then '1394'
         when year(date(dateTime_cartfinalize)) = 2016
           then '1395'
         when year(date(dateTime_cartfinalize)) = 2017
           then '1396'
         else '1397'
         end as years, sum(quantity_item) from customers group by years;

# 8
select
       user_id,
       (sum(likes)-sum(dislikes)) as difference,
       title_en
from
     opinion
group by
         user_id
order by difference desc
limit 10;


# 9
SELECT
       product_id,
       count(product_id) as num
from
     opinion
group by
         product_id
order by num desc limit 10;

# 10
SELECT
       product_id,
       count(product_id) as num
from
     opinion
group by
         product_id
order by num DESC limit 10;
