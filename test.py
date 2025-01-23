import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    ball_str = input().strip()

    r_cnt = ball_str.count('R')



    r_right = r_cnt
    r_left_move = r_cnt


    b_cnt = ball_str.count('B')
    b_right_move = b_cnt
    b_left_move = b_cnt

    # 양 끝에서 연속된 색상 별 공 카운팅: r_left, r_right, b_left, b_right
    # 각 색상 별 공 카운팅
    # 색 x 방향 별 이동 횟수 계산:
    # r_to_l = r_cnt - r_left


    sys.stdout.write(f"{min(r_move, b_move)}")

solution()