# BAEKJOON 10828 ์คํ

### [๐ธ๋ฌธ์ ](https://www.acmicpc.net/problem/10828) 

<hr>



### ๐ํ์ด

> input์ sys.stdin.readline์ ํตํด ๋ฐ์์ผ ์๊ฐ ์ด๊ณผ๋ฅผ ํผํ  ์ ์๋ค

1. sys.stdin.readline์ ํตํด input์ ๋ฐ์์จ๋ค.
1. ๋ฌธ์ ์์ ์ฃผ์ด์ง ๋ช๋ น์ด๊ฐ input์ ์กด์ฌํ๋์ง ํ์ธ
1. ํด๋น input์ ๋ฐ๋ฅธ ๊ฒฐ๊ณผ ๊ฐ์ ์ถ๋ ฅ

<hr>

### ๐์ฝ๋

```python
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def stack(data):
    if 'top' in data:
        if len(arr) !=0:
            return(arr[-1])
        else:
            return(-1)
    elif 'size' in data:
        return(len(arr))
    elif 'pop' in data:
        if len(arr)==0:
            return(-1)
        else:
            return(arr.pop())
    else:
        if len(arr) == 0:
            return(1)
        else:
            return(0)

N = int(input())

arr = []
for _ in range(N):
    data = input()
    if 'push' in data:
        arr.append(data.split()[1])
    else:
        print(stack(data))
```

<hr>





### ๐๊ฒฐ๊ณผ

![image-20220425222546166](readme.assets/image-20220425222546166.png)

์ฒ์์ sys.stdin.readline์ ์์ฐ๊ณ  ๊ทธ๋ฅ input์ ๋ฐ์๋๋ ์๊ฐ ์ด๊ณผ์ ๊ฑธ๋ ธ๋ค. ํจ์๋ก ๋ง๋ค์ด์ ์ฝ๋๋ฅผ ์๋์ํค๋ฉด ์๋๊ฐ ๋ ์กฐ๊ธ ๊ฑธ๋ฆฐ๋ค๋ ๊ธ์ ๋ณธ ์ ์ด ์์ด์ ํด๋น ๋ถ๋ถ์ผ๋ก ์งํํด๋ณด์์ง๋ง ์ญ์๋ ์๊ฐ ์ด๊ณผ...

๊ฒฐ๊ตญ์๋ sys.stdin.readline์ ์ฌ์ฉํด์ input ๊ฐ์ ๋ฐ์์ค๋ ๊ฐ๋ฟํ๊ฒ ํต๊ณผํ์๋ค. ์ข๊ตฌ๋ง~
