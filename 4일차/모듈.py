# *모듈
# =>여러 변수, 함수를 가지고 있는 집합체로 표준 모듈, 외부 모듈이 있음
# =>표준 모듈: 파이썬에 기본적으로 내장되어 있음
# =>외부 모듈: 외부 또는 다른 사람이 만들어 공개, 배포 해둔 모듈
# =>모듈을 사용할땐 반드시 import를 사용함

# import math
# =>모듈을 불러와서 메서드를 연결하여 사용할 수 있는 불러오는 방식

from math import cos,tan, floor, ceil
# =>여러 모듈을 한번에 불러올 때 from을 사용함

# math에서 가져왔다는걸 말했기 때문에 밑에서 생략해서 코드의 양을 줄일 수 있다.

from math import *
# =>math의 모든 메서드를 가져오지만 비효율적
# => 모든 내용을 가져오기 때문에 상황에 따라 코드의 충돌이 있을 수도 있음

import math as m
# =>모듈의 이름을 바꿔먹을 수 있음

print(m.cos(1))

print(m.tan(1))

print(m.floor(3.5))

print(m.ceil(3.5))
# -> 페이지네이션에서 다루기도 함

print(round(3.7))