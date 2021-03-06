# 이진 트리가 주어지면 루트 노드부터 레벨별로 프린트 하시오. 프린트 방식은 홀수 레벨은 왼쪽에서 오른쪽으로, 짝수 레벨은 오른쪽에서 왼쪽으로 프린트 하시오. 루트노드는 레벨 1입니다. 예제를 보시오.
#
# 1
#
# / \
#
# 2 3
#
# / \ / \
#
# 4 5 6 7
#
# 프린트: 1, 3, 2, 4, 5, 6, 7.
def solution(root):
    forward = [root]
    backward = []

    while backward or forward:
        while forward:
            tmp = forward.pop()
            print(tmp.data)

            if tmp.left:
                backward.append(tmp.left)
            if tmp.right:
                backward.append(tmp.right)

        while backward:
            tmp = backward.pop()
            print(tmp.data)

            if tmp.right:
                forward.append(tmp.right)
            if tmp.left:
                forward.append(tmp.left)


#파이썬 트리?