class Solution(object):
    def shipWithinDays(self, weights, days):
        


        def check(weights,days,cap):
            day = 1
            current_load = 0
            for weight in weights:

                if weight + current_load > cap:
                    day +=1
                    current_load = weight
                else:
                    current_load += weight
                
            if day <= days:
                return True
            else:
                return False

        sum_weights = sum(weights)
        low,high = max(weights),sum_weights
        answer =  sum_weights

        while low <= high:
            mid = (low + high )//2
            res = check(weights,days,mid)
            if res:
                answer = mid
                high = mid -1
            else:
                low = mid + 1
        return answer


        