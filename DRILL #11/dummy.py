# class Star:
#     type = "star"
#     x = 100
#     def change():
#         x = 200
#         print('x is',x)
#
# print('x is',Star.x)
# Star.change()
#
# star = Star() # 굳이 객체를 생성하는것도 가능?
# print('x is',star.x) # 객체 변수로 액세스하지만, 뭘로 귀착? 클래스 변수 x를 가리킨다.
# star.change()
#
# class Player:
#     name = 'Player' # 클래스 변수
#
#
#     def __init__(my):
#         my.x = 100
#     def where(my):
#         print(my.x)
#
# player = Player()
# player.where()
#
# print(Player.name) # 클래스 변수 출력
# print(player.name) # name이라는 객체 변수가 없으면, 같은 이름의 클래스 변수가 선택됨.
#
# Player.where(player) # 이게 원칙적인 파이썬의 멤버 함수 호출
# player.where() # ====> Player.where(player) 와 동일

table = {
    "SLEEP" : { "HIT":"WAKE"},
    "WAKE" : {"TIMER10":"SLEEP"}
}

cur_state = "WAKE"
next_state = table[cur_state]["TIMER10"]
print(next_state)