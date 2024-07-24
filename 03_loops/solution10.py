# Exponential Backoff
# Implement an exponential backoff startegy that doubles the wait time between retries, starting from 1 second, but stopes after 5 retries

# sabse pehle hume time ko import karna hoga kuki hum time se deal krenge. Ab hume time ko har retry k baad double krna hai. 

import time

wait_time = 1
max_retries = 5
attempts = 0 

while attempts < max_retries:
    print("Attempts", attempts + 1, "Wait Time ", wait_time, "sec")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    
# time.sleep() is used to sleep  the system. taki tab tak sytem kaam na kre. 
# is method k tareeeke ko hum password ko retry krne me, captcha generate krne me use krte hai.
# jab tak attempts jo h wo max_tries se kam hai to loop  me hum wait time ko *2 se badhate rahenge or utni der k lye sytem sleep me chala jaega. fir hum attempts ko bhi increase krte rahenge.
