# 해결방법
 스택이용하기.
 해당 좌표의 value에 존재하는 값만큼 이동했을 때 종료되지 않으면 계속 진행
    종료되면 최대 값 변수에 저장

# 자동차 미니 게임

N* M 사이즈의 미니 게임판이 있습니다. 미니 게임은 자동차를 게임판에서 주행하는 게임입니다.

미니게임에서 자동차가 주행하는 방법은 다음과 같습니다.

- 게임판은 칸마다 0에서 9까지의 숫자가 적혀있습니다.
- 자동차는 한번에 각 칸에 적힌 숫자만큼 이동하며 →, ↓, ←, ↑방향 중 하나를 골라 움직일 수 있습니다.
- 자동차가 다음으로 움직일 칸이 게임판 밖으로 나가거나 ‘0’이 적힌 칸인 경우 게임은 종료됩니다.
- 왼쪽 위(0,0)는 자동차의 출발지이며, 칸에 적힌 숫자가 0이 될 수 없습니다.

미니 게임판을 줬을 때 자동차가 출발 전, 정차할 칸이 가장 많은 경로를 정합니다. 게임이 종료될 때까지 정차한 칸의 개수를 출력하는 프로그램을 작성하세요.

※출발 칸도 정차한 칸의 개수에 포함합니다.

## [입력]
- 첫 번째 줄에 게임판의 세로의 길이인 자연수 N, 가로의 길이인 자연수 M을 입력합니다.
```(1≤N, M≤50)```

- 두 번째 줄부터 게임판의 모양대로 숫자를 입력합니다.

## [출력]
- 첫 번째 줄에 자동차가 정차한 칸의 개수 최댓값을 출력합니다.
※ 자동차가 게임판에서 움직일 수 있는 칸이 무한대인 경우 ‘-1’을 출력합니다.

## [입력 예시]
3 5
21012
51213
61133

## [출력 예시]
2