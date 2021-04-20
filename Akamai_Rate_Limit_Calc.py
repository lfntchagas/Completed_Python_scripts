'''
25/01 12:00AM to 25/01 11:59PM
Calc based in one IP: 45.237.169.39
1 day = 37.550 req/24h
1 hour(20:00 to 21:00) = 3.196req/1h
5 min (20:00 to 20:05) = 295req/5min
1 min (20:00to 20:01) = 59 req/1min = 0.98req/sec | 118req/2min = 0.98
5 sec = 5req/sec
'''


def burst_threshold(req):
    result = req * 5 #5 seconds
    return result
    
def average_threshold(req):
    result = req * 120 # 2 minutes
    return result

def req_min_to_seconds(req, minutes):
    result = req / (minutes * 60)  # how much requests per minutes a user is doing.
    return print(f"The user is doing {result} reqs/sec in {minutes} minute")


def akamai_rate_control_rule_test(a_burst, a_average, u_burst, u_average):
    akamai_total_burst = burst_threshold(a_burst)
    akamai_total_average = average_threshold(a_average)

    user_total_burst = burst_threshold(u_burst)
    user_total_average = average_threshold(u_average)

    if user_total_burst > akamai_total_burst or user_total_average > akamai_total_average:
        print(f"\nAkamai might be BLOCKED the traffic")
        print(f"\nThe Akamai total rate-burst limit: {akamai_total_burst} requests in 5 seconds")
        print(f"The Akamai total rate-average limit: {akamai_total_average} requests in 2 minutes")
        print(f"\nThe User total rate-burst: {user_total_burst} requests in 5 seconds")
        print(f"The user total rate-average: {user_total_average} requests in 2 minutes")
    else:
        print(f"\nAkamai has NOT blocked the traffic")
        print(f"\nThe Akamai total rate-burst limit: {akamai_total_burst} requests in 5 seconds")
        print(f"The Akamai total rate-average limit: {akamai_total_average} requests in 2 minutes")
        print(f"\nThe User total rate-burst: {user_total_burst} requests in 5 seconds")
        print(f"The user total rate-average: {user_total_average} requests in 2 minutes")

req_min_to_seconds(15000,1)

'''
akamai_rate_control_rule_test(15,10,10,10)

1 - Check rate limit control rule 
2 - check how much requests/sec an IP is doing. 
'''
