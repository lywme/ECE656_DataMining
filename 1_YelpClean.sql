#### 1.Check no user/review/tip is before Yelp's foundation or in the future
# Once found that the select clause return non-empty set, delete corresponding rows.

SELECT review_id FROM review WHERE date<'2004-06-01' or date>'2019-04-20';
DELETE FROM review WHERE date<'2004-06-01' or date>'2019-04-20';

SELECT date FROM tip WHERE date<'2004-06-01' or date>'2019-04-20';
DELETE FROM tip WHERE date<'2004-06-01' or date>'2019-04-20';

SELECT yelping_since FROM `user` WHERE date<'2004-06-01' or date>'2019-04-20';
DELETE FROM `user` WHERE date<'2004-06-01' or date>'2019-04-20';

SELECT user_id FROM user_elite WHERE year<2004 or year>2019;
DELETE FROM user_elite WHERE year<2004 or year>2019;

#### 2.The business_id in `review` table must already be existes in `business` table
select R.business_id from review as R left join business as B on R.business_id = B.business_id where B.business_id is null;

-- This query return an non-empty set, so data cleaning is necessary
delete review from review inner join 
     (select R.business_id from review as R left join business as B on R.business_id = B.business_id where B.business_id is null) as T1
on review.business_id = T1.business_id;

# The user_id in `review` table must already be existes in `user` table
delete review from review inner join 
     (select R.user_id from review as R left join `user` as U on R.user_id = U.user_id where U.user_id is null) as T1
on review.user_id = T1.user_id;

# In a similiar way, the user_id in `user_elite` table must already be existes in `user` table
delete user_elite from user_elite inner join 
     (select E.user_id from user_elite as E left join `user` as U on E.user_id = U.user_id where U.user_id is null) as T1
on user_elite.user_id = T1.user_id;

#### 3. The year in user_elite table must be less than the yelping_since in user table 
SELECT user_id from user_elite inner join `user` using (user_id) where year<yelping_since;