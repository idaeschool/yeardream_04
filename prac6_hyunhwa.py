# prac6.py
import random

# 캐릭터 클래스
class Character:
    # 생성자(이름, 체력)
    def __init__(self, name, health):
        self.name = name        # 이름
        self.health = health    # 체력

    # 캐릭터 생존 여부 확인 메서드
    def is_alive(self):
        # 캐릭터의 체력이 0보다 크면 살아있음. 반대는 죽음.
        return self.health > 0

    # 캐릭터 공격 메서드()
    def attack(self, other):
        raise NotImplementedError("하위 클래스에서 구현할 예정.")

# 플레이어 클래스
class Player(Character):
    # 생성자(이름, 체력)
    def __init__(self, name, health=100):
         # 부모 클래스 캐릭터에서 생성자 호출
         super().__init__(name, health)

    # 공격 메서드
    def attack(self, other):
        # 데미지 = 5~20 사이의 랜덤 값
        damage = random.randint(5, 20)

        # 몬스터 체력 감소
        other.health -= damage
        
        # 플레이어가 공격 후 몬스터 스탯 변화 출력
        print(f"{self.name}은(는) {other.name}을(를) {damage:2d} 데미지로 공격했다. {other.name}의 현재 체력 : {other.health:2d}")

# 몬스터 클래스
class Monster(Character):
    # 생성자(이름, 체력)
    def __init__(self, name, health=50):
        # 부모 클래스 캐릭터에서 생성자 호출
         super().__init__(name, health)

    def attack(self, other):
        # 데미지 = 5~20 사이의 랜덤 값
        damage = random.randint(3, 10)

        # 플레이어 체력 감소
        other.health -= damage

        # 몬스터가 공격 후 플레이어 스탯 변화 출력
        print(f"{self.name}은(는) {other.name}을(를) {damage:2d} 데미지로 공격했다. {other.name}의 현재 체력 : {other.health:2d}")

# 게임 플레이 메서드
def game_loop():
    # 플레이어 생성
    player = Player("팥지")

    # 몬스터 생성
    monster = Monster("오크")

    # 플레이어와 몬스터 중 하나가 죽을 때까지 반복
    while player.is_alive() and monster.is_alive():
        # 플레이어 공격
        player.attack(monster)

        # 몬스터 생존 여부 체크
        if monster.is_alive():
            # 몬스터가 살아있으면 플레이어 공격
            monster.attack(player)

    # 플레이어 생존 여부 체크
    if player.is_alive():
        # 플레이어와 몬스터 이름 출력
        print(f"{player.name} 승리! {monster.name} 개같이 패배!")
    else:
        print("당신은 괴물에게 패배했습니다...")

if __name__ == "__main__":
    game_loop()