# BAEKJOON 11723 ์งํฉ

### [๐ธ๋ฌธ์ ](https://www.acmicpc.net/problem/11723) 

<hr>



### ๐ํ์ด

> set() ์๋ฃ ๊ตฌ์กฐ๋ฅผ ์ฌ์ฉํ๋ค

1. set ์๋ฃ ๊ตฌ์กฐ๋ฅผ ์์ฑ
1. input์ ๋ฐ๊ณ  ํน์  ๋จ์ด๊ฐ input์ ๋ค์ด์๋์ง ํ์ธ
1. ํน์  ๋จ์ด๊ฐ input์ ๋ค์ด์๋ค๋ฉด ๊ทธ์ ํด๋นํ๋ ์กฐ๊ฑด์ ์ฒ๋ฆฌ

<hr>

### ๐์ฝ๋

```python
import sys
sys.stdin = open('input.txt')

N = int(input())

sset = set()

for i in range(N):

    data = input()
    if 'add' in data:
        sset.add(int(data.split()[1]))
    elif 'remove' in data:
        if int(data.split()[1]) in sset:
            sset.remove(int(data.split()[1]))
    elif 'check' in data:
        if int(data.split()[1]) in sset:
            print(1)
        else:
            print(0)
    elif 'toggle' in data:
        if int(data.split()[1]) in sset:
            sset.remove(int(data.split()[1]))
        else:
            sset.add(int(data.split()[1]))
    elif 'all' in data:
        sset = set((range(1,21)))
    elif 'empty' in data:
        sset = set()
```

<hr>





### ๐๊ฒฐ๊ณผ

![image-20220503233458635](readme.assets/image-20220503233458635.png)

ํ์ด์ฌ์๋ set()์ด๋ผ๋ ์งํฉ์ ์ฒ๋ฆฌํ  ์ ์๋ ์๋ฃ๊ตฌ์กฐ๊ฐ ์์ด์ ์ฝ๊ฒ ํด๊ฒฐ์ด ๊ฐ๋ฅํ๋ค.

๋๋ถ๋ถ์ ์ฐ์ฐ์ set์ ํตํด ํด๊ฒฐ ํ  ์ ์๋ค. *~~(ํ์ด์ฌ ์ถฉ์ฑ!)~~*
