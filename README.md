# Script for analyzing an interesting math property I found in high school

Apply this algorithm to integer numbers:
* if number > 0 -> compute `number - number with reversed digits` (e.g. 6127-7216)
* if number < 0 -> compute `number + number with reversed digits` (e.g. -9532+2359)
* repeat with the newly calculated number

Most numbers will converge to 0, but there are few exceptions. This script prints the exception numbers from a given start number (start_n) to an end number (end_n)

### Example of execution of the algorithm
1. number = 7234
1. 7234-4327 = 2907
1. 2907-7092 = -4185
1. -4185+5814 = 1629
1. 1629-9261 = -7632
1. -7632+2367 = -5265
1. -5265+5625 = 360
1. 360-63 = 297
1. 297-792 = -495
1. -495+594 = 99
1. 99-99 = **0**
