def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + \
        phone_number[len(phone_number)-4:len(phone_number)]
    return answer
