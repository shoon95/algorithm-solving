# BAEKJOON 11047 λμ  0

### [πΈλ¬Έμ ](https://www.acmicpc.net/problem/11047) 

<hr>



### πνμ΄

> λλκΈ° ν λͺ«κ° λλ¨Έμ§λ₯Ό μ΄μ©

1. λμ μ΄ μ£Όμ΄μ§ μλ³΄λ€ ν°μ§ μμμ§ νμ
1. μ£Όμ΄μ§ μλ³΄λ€ κ°κ±°λ μμ λλ§ λ°°μ΄μ λ€μμλΆν° μ±μ(λμ€μ λ€μ΄μ¨ μκ° μμΌλ‘ λ°°μΉ)
1. λ°°μ΄μ μννλ©° ν΄λΉ λμ μΌλ‘ μ£Όμ΄μ§ μλ₯Ό λλλ€
1. λλ λͺ«μ΄ ν΄λΉ λμ μ λ΄μΌνλ κ°μ
1. λλ λλ¨Έμ§κ° λ¨μ λμ μΌλ‘ λ΄μΌνλ λ
1. λͺ¨λ  μνλ₯Ό λλ΄κ³  λμ μ λ΄μΌνλ μ΄ κ°μλ₯Ό λν΄μ€

<hr>

### πμ½λ

```python
import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

arr = []
for _ in range(N):
    value = int(sys.stdin.readline().rstrip())
    if M >= value:                              # λμ μ κ°μ΄ Mλ³΄λ€ κ°κ±°λ μμΌλ©΄ λ°°μ΄μ λ΄κΈ°
        arr = [value] + arr                     # ν° λμ μ΄ μμΌλ‘ μ€λλ‘ λ°°μ΄μ λ€μ§μ΄μ λ°μμ€λ€.

cnt = 0
for i in arr:                                   # λ°°μ΄μ μν
    cnt += M//i                                 # λμ μΌλ‘ λλ λͺ«μ΄ ν΄λΉ λμ μ λ΄λ μ
    M %= i                                      # λμ μΌλ‘ λλ λλ¨Έμ§κ° λ¨μ λμ λ€λ‘ λ΄μΌλλ λ¨μ κ°
print(cnt)                                      # λͺ¨λ  λμ μ λ΄λ μλ₯Ό λν΄μ μΆλ ₯
```

<hr>





### πκ²°κ³Ό

![image-20220513225424749](readme.assets/image-20220513225424749.png)

μ²μμλ dfsλ₯Ό μ΄μ©ν΄μ νμ΄λ³ΌκΉ μκ°νλ€. νμ§λ§ μμ μκ° μ£Όμ΄μ‘μ λ dfsλ₯Ό λλ¬΄ λ§μ΄ λμμ μ€ν¨νλλ° μ§κΈ μκ°ν΄λ³΄λ λ°°μ΄μ λ€μ§μ΄μ dfs νμμ μμνκ³  μ²μμΌλ‘ λμ μ κ°κ³Ό λμΌνκ² μμ±λμ λ λ°λ‘ μ’λ£ μμΌλ²λ¦°λ€λ©΄ κ°λ₯ν  κ² κ°κΈ°λ νλ€. νμ§λ§ μ§κΈ νμ΄κ° ν¨μ¬ λ κ°κ²°νκ³  κΉλνκ² νμ΄μ§ κ² κ°μμ μμ£Όμμ£Ό λ§μ‘±μ€λ½λ€ γγ! *~~(μνμ₯¬!)~~*
