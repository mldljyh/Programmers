def solution(bridge_length, weight, truck_weights):
    answer = 1
    on_trucks = []
    on_trucks.append([truck_weights.pop(0), 1])
    while len(truck_weights):
        truck = truck_weights.pop(0)
        pre_weight = 0
        for i in on_trucks:
            pre_weight += i[0]
        if pre_weight + truck <= weight:
            j = 0
            while j < len(on_trucks):
                on_trucks[j][1] += 1
                if on_trucks[j][1] > bridge_length:
                    on_trucks.pop(0)
                    j -= 1
                j += 1
            answer += 1
        else:
            while pre_weight + truck > weight:
                on_truck_weight, length = on_trucks.pop(0)
                time_length = bridge_length - length + 1
                for j in on_trucks:
                    j[1] += time_length
                answer += time_length
                pre_weight -= on_truck_weight
        on_trucks.append([truck, 1])

    while len(on_trucks):
        on_truck_weight, length = on_trucks.pop(0)
        time_length = bridge_length - length + 1
        for j in on_trucks:
            j[1] += time_length
        answer += time_length
    return answer
