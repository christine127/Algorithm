def solution(number, k):
    stack = list()
    num_list = list(number)

    for num in num_list:
      while stack and stack[-1] < num and k> 0: #while stack --> stack이 비어있지 않을 때
        del stack[-1]
        k -= 1
      else:
        stack.append(num)

    if k>0:
        stack = stack[:len(stack)-k]

    return''.join(stack)