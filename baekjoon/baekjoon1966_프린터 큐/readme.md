# BAEKJOON 1966 ํ๋ฆฐํฐ ํ

### [๐ธ๋ฌธ์ ](https://www.acmicpc.net/problem/1966) 

<hr>



### ๐ํ์ด

> ์ฐพ๋ ์์ ํ์ฌ idx๊ฐ 0์ธ์ง ์๋์ง๋ฅผ ๊ตฌ๋ถํด์ ์ ๊ทผํ๋ค.

1. ์ฐพ๋ ์์ idx๊ฐ 0์ด๋ผ๋ฉด
   * pop(0)๊ฐ ์ต๋๊ฐ์ด๋ฉด count๋ฅผ +=1 ํ๊ณ  ์ข๋ฃ
   * ์ต๋๊ฐ์ด ์๋๋ฉด ์ ์ผ ๋ค๋ก ๋ณด๋ด๊ณ  idx๋ฅผ ๋ฐฐ์ด ํฌ๊ธฐ -1 ๋ก ๊ฐฑ์ 
1. ์ฐพ๋ ์์ idx๊ฐ 0์ด ์๋๋ผ๋ฉด
   * idx๋ฅผ ์์ผ๋ก ํ ์นธ ๋น๊ฒจ๋๊ณ  ์์
   * pop(0) ๊ฐ ์ต๋๊ฐ์ด ์๋๋ผ๋ฉด ๋นผ์ ๋ฐฐ์ด์ ์ ์ผ ๋ค๋ก ๋ณด๋
   * pop(0) ๊ฐ ์ต๋๊ฐ์ด๋ผ๋ฉด ๋นผ์ ์์ ์ฃผ๊ณ  count๋ฅผ += 1

<hr>

### ๐์ฝ๋

```python
import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, idx = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    i = 0
    while True:
        if idx == 0:                        # ์ํ๋ ๊ฐ์ idx๊ฐ 0์ผ ๋
            if arr[0] != max(arr):          # ๊ฐ์ด ์ต๋๊ฐ ์๋๋ฉด ๋งจ ๋ค๋ก ๋ณด๋ด๊ณ  idx๋ฅผ ์ ์ผ ๋ง์ง๋ง์ผ๋ก ๊ฐฑ์ 
                arr.append(arr.pop(0))
                idx = len(arr) - 1
            else:                           # ๋ง์ฝ ์ํ๋ ๊ฐ์ด ์ต๋๊ฐ์ด๋ฉด ํ์๋ฅผ ์นด์ดํํ๊ณ  ์ข๋ฃ
                i += 1
                break
        else:                               # ์ํ๋ ๊ฐ์ idx๊ฐ 0์ด ์๋ ๋๋
            idx -= 1                        # idx๋ฅผ ํ๋ ์์ผ๋ก ๋น๊ฒจ์ฃผ๊ณ 
            if arr[0] != max(arr):          # ์ ์ผ ์์ ์๊ฐ ์ต๋๊ฐ์ด ์๋๋ฉด
                arr.append(arr.pop(0))      # ๋นผ์ ์ ์ผ ๋ค๋ก ๋ณด๋ด์ค
            else:                           # ์ ์ผ ์์ ์๊ฐ ์ต๋๊ฐ์ด๋ฉด ๋นผ๊ณ  ํ์๋ฅผ ์นด์ดํ
                arr.pop(0)
                i += 1
    print(i)                                # ์ํ๋ ์๊ฐ pop๋์ ๋ ํ์ฌ๊น์ง ๋ช ๋ฒ์ ์ถ๋ ฅ์ด ์์๋๋ฐ ์นด์ดํํ ๊ฐ์ ์ถ๋ ฅ
```

<hr>





### ๐๊ฒฐ๊ณผ

![image-20220503004816669](readme.assets/image-20220503004816669.png)

์ฐพ๋ ์์ idx๊ฐ 0์ธ์ง ์ฆ, ํ์ฌ ์ถ๋ ฅ ์์น์ ์๋์ง๋ฅผ ํ์ธํ๋ฉด์ ์ฐพ๋ ์์ ์์น๊ฐ ์ด๋ํ  ๋๋ง๋ค ๋ง์ถฐ์ idx๋ฅผ ๊ฐฑ์ ํด์ฃผ๋ฉด ๋๋ค. ๊ณ์ํด์ ๊ฐฑ์ ํด์ฃผ๋ค idx๊ฐ ๋ค์ 0์ผ๋ก ์์ ๋ ์ต๋๊ฐ์ธ์ง ๊ฒ์ฆ ์ด ์์์ ๊ณ์ํด์ ๋ฐ๋ณตํด์ฃผ๋ฉด ์ฝ๊ฒ ํด๊ฒฐ*~~(class2 ๊ฒฉํ ์ฑ๊ณตํ์ฅฌ!)~~*
