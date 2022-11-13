import sys
sys.stdin = open('input.txt')

def get_pallindrome(S):
    length = len(S)
    cnt = 0
    for i in range(length):
        if cnt == 0:    # 문자열 idx를 아직 이동하지 않았을 때
            if S == S[::-1]:    # idx를 아직 이동하지 않고 기존 문자열과 뒤집은 문자열이 같으면 회문
                return length
        elif S[cnt:] == S[::-1][:-cnt]: # idx를 이동하면서 뒤집은 문자열과 기존 문자열 비교
            return length + cnt # 같아면 기존 문자열 길이에 이동한 idx만큼 추가
        cnt += 1
S = input()
print(get_pallindrome(S))
