# BAEKJOON 9095 1, 2, 3 ๋ํ๊ธฐ

### [๐ธ๋ฌธ์ ](https://www.acmicpc.net/problem/9095) 

<hr>



### ๐ํ์ด

> ์ค๋ณต ์์ด์ ์ด์ฉํ์ฌ ๋ฌธ์  ์ ๊ทผ

1. [1, 2, 3] ๋ฐฐ์ด ์์ฑ
1. ์ ๋ฐฐ์ด์์ ์ค๋ณต์ ํ์ฉํด์ ์ซ์๋ฅผ ๋ฝ์์ ๋ฝ์ ์๋ฅผ arr์ ๋ด๊ณ  arr์ ํจ๊ป ๋ค์ ์ฌ๊ท ํธ์ถ
1. ์ ๊ณผ์ ์ ๋ฐ๋ณตํ๋ค arr์ ๋ด๊ธด ์๋ค์ ํฉ์ด ์ฃผ์ด์ง input ๊ฐ๊ณผ ๊ฐ๋ค๋ฉด cnt += 1 ํ ์ฌ๊ท ํธ์ถ ์ข๋ฃ, ๋ง์ฝ cnt๋ฅผ ์ด๊ณผํด๋ฒ๋ ธ๋ค๋ฉด ๋ฐ๋ก ์ฌ๊ท ํธ์ถ ์ข๋ฃ
1. ์ ๊ณผ์ ์ด ์ข๋ฃ๋ ํ cnt๋ฅผ ์ถ๋ ฅํ๋ค.

<hr>

### ๐์ฝ๋

```python
import sys
sys.stdin = open('input.txt')

def get_combi(nums, N, arr):            # ์ค๋ณต ์์ด์ ์ด์ฉํด ๋ฌธ์ ๋ฅผ ํ์
    global cnt                          # ์กฐ๊ฑด์ ๋ง์กฑํ  ๋ cnt += 1
    if sum(arr) > N:                    # ํ์ฌ ๋ด๊ธด ์๋ค์ ํฉ์ด N์ ์ด๊ณผํ๋ค๋ฉด ํจ์ ์ข๋ฃ
        return

    if sum(arr) == N:                   # ํ์ฌ ๋ด๊ธด ์๋ค์ ํฉ์ด N๊ณผ ๊ฐ๋ค๋ฉด cnt += 1 ํ ํจ์ ์ข๋ฃ
        cnt += 1
        return
    for i in nums:                      # [1,2,3] ๋ฐฐ์ด์์ ํ๋์ฉ ์ค๋ณตํด์ ๋นผ์ค๋ฉด์ ์ฌ๊ท ํจ์ ํธ์ถ
        get_combi(nums, N, arr+[i])


N = int(input())
nums = [1,2,3]
for _ in range(N):
    cnt = 0
    get_combi(nums, int(input()), [])
    print(cnt)
```

<hr>





### ๐๊ฒฐ๊ณผ

![image-20220510231632294](readme.assets/image-20220510231632294.png)

์ด๋ป๊ฒ ๋ฌธ์ ๋ฅผ ํ ์ ์์๊น ํ๋ค๊ฐ ์ฒ์์๋ 1์ input์ ํฌ๊ธฐ๋งํผ ๋์ด๋๊ณ  ์ ํ์์ ์ฐพ์๋ณด๋ ค๊ณ  ํ๋ค. ์ ํ์์ ์ฐพ์ผ๋ฉด ๊ท์น์ ํตํด ์ฌ๊ท ๋๋ dp๋ก ๋ฌธ์ ๋ฅผ ํด๊ฒฐ ํ  ์ ์์ ๊ฑฐ๋ผ๊ณ  ์๊ฐํ๋ค. 

ํ์ง๋ง ์๊ฐ๋ณด๋ค ์ฝ์ง ์์๊ณ  ๋ฌธ์ ๋ฅผ ๊ณ์ํด์ ์ฝ๋ค ๋ณด๋ ๊ณ ๋ฑํ๊ต ๋ ๊ณต๋ถํ๋ ์ค๋ณต์ ํ์ฉํ ์์ด์ ํตํด์ ๋ฌธ์ ๋ฅผ ์ ๊ทผํ๋ฉด ์ฝ๊ฒ ํ๋ฆด ๊ฒ ๊ฐ์๋ค. ๋ฐ๋ผ์ ์ค๋ณต์ ํ์ฉํ ์์ด์ ๋ง๋ค๊ณ  ํด๋น ์๋ค์ ํฉ์ด input๊ณผ ๊ฐ๋ค๋ฉด cnt += 1์ ํด์ฃผ๋๋ก ํ์๋ค. 

๋์ค์ ์ฌ๊ท์ ๊น์ด์, ์๊ฐ ์ด๊ณผ๋ฅผ ์ฐ๋ คํด์ ์๋ค์ ํฉ์ด N์ ์ด๊ณผํ  ๋๋ ์ฌ๊ท ํจ์๋ฅผ ์ข๋ฃํ๋๋ก ๊ฐ์ง์น๊ธฐ๋ ์ถ๊ฐํด์ฃผ์๋ค.

๋ฌธ์ ๋ฅผ ํ๊ณ  ๋ค๋ฅธ ์ฌ๋๋ค์ ์ฝ๋๋ฅผ ๋ณด๋ ๊ฑฐ์ ๋๋ถ๋ถ์ด dp ๋ฐฉ์์ผ๋ก ๋ฌธ์ ๋ฅผ ํ์๋ค.. ๋๋ ์คํจํ๋๋ฐ..ใใ ๊ทธ๋๋ ๋ค๋ฅด๊ฒ ํ์๋ค๋ ๋ถ๋ถ์์ ๋ ๊ธฐ์จ์ด ์์๋ค ใใ

์๊ณ ๋ฆฌ์ฆ ๋ฌธ์ ๋ฅผ ํ๋ฉด์ ํญ์ ์ํ์ ์ํ๋ฉด ๋ฌธ์ ๋ฅผ ์ ๋ง ์์๊ฒ, ์ ํ ์ ์๊ฒ ๊ตฌ๋ ๋ผ๋ ์๊ฐ์ด ๋ง์ด ๋ ๋ค. ์ด์ฌํ ์ํ๋ ๊ณต๋ถํ์*~~(๋ผ๋ ๋ง๋ง ๋ช ๋ฌ ์งธ..)~~*
