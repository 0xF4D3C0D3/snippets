As of now, 2021-01-30, DynamoDB doesn't support for both identifying row with secondary index and sorting rows by arbitrary column.
So why does it matter? If you want to sort posts with created date you have two options one is creating just one big partition key and set created date as a sort key and
another one is partitioning with appropriate type like a date and setting created date as a sort key.

And you also need to create global secondary index for querying row with its id.

But whichever you choose, you can't sort and indexing together because deleteItem or updateItem in DynamoDB only works with primary key. So you have to query twice..
