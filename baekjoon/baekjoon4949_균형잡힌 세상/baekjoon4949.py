import sys
import re
sys.stdin = open('input.txt')
text = sys.stdin.readline().rstrip()

dic = {
    '[':']',
    '(':')'
}

while text != '.' :                                 # input이 .이 나오면 종료
    stack = []
    text = re.sub('[^\\[\\]\\(\\)]','',text)        # [,],(,) 을 제외한 모든 문자 제거

    if len(text)%2:                                 # 문자열이 홀수면 괄호의 짝이 맞지 않기 때문에 다음 문자열을 받아 놓고 no 출력
        text = sys.stdin.readline().rstrip()
        print('no')
        continue

    for i in text:                                  # '(','[' 와 같이 열린 괄호면 stack에 추가
        if i == '(' or i == '[':
            stack.append(i)
        elif not stack or dic[stack.pop()] != i:    # 열린 괄호가 아닐 때 stack이 비어있거나 괄호 짝이 맞지 않다면 no 출력 후 다음 input 받기
            print('no')
            text = sys.stdin.readline().rstrip()
            break
    else:                                           # 위 검정 과정을 모두 통과했을 때 stack에 남은 괄호가 있다면 no 아니면 yes 출력
        if stack:
            print('no')
        else:
            print('yes')
        text = sys.stdin.readline().rstrip()