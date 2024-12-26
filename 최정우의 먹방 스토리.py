import time

# 정우의 대사 및 흐름을 담당하는 클래스
class GameCharacter:
    def __init__(self, name, intro):
        self.name = name
        self.intro = intro

    def speak(self, text):
        print(f"{self.name}: {text}")
        time.sleep(1)

    def ask_question(self, question):
        print(f"\n{self.name}: {question}")
        choice = input("예 또는 아니요로 대답하세요: ").strip().lower()
        while choice not in ['예', '아니요']:
            print("잘못된 입력입니다. '예' 또는 '아니요'로 대답하세요.")
            choice = input("예 또는 아니요로 대답하세요: ").strip().lower()
        return choice == '예'

# 게임의 주요 흐름
def game():
    # 캐릭터 생성
    character = GameCharacter("최정우", "여러 음식들이 나타나고 있어!")

    # 게임 시작
    print("최정우 먹방 스토리에 오신 것을 환영합니다!\n")
    time.sleep(1)

    # 상황 설명
    character.speak(character.intro)
    
    # 음식 1: 칠리새우
    character.speak("앞에 찰리새우가 나타났어! 먹을 수 있을까?")
    if character.ask_question("이 음식 먹을까요?"):
        character.speak("맛있었다! 하지만 아직 배고파.")
        outcome1 = "먹었다!"
    else:
        character.speak("느낌이 이상해! 그냥 먹지 말자.")
        outcome1 = "음식을 먹지않고 떠났다."
    
    # 음식 2: 햄버거
    character.speak("커다란 햄버거 세트가 나타났어! 어떻게 할까?")
    if character.ask_question("이 햄버거를 먹을까요?"):
        character.speak("역시 맛있었다! 아주 큰 음식이었지만 아직 배고파.")
        outcome2 = "통째로 삼켰다!"
    else:
        character.speak("뭔가 수상해! 식중독에 걸릴지 몰라.")
        outcome2 = "햄버거 세트를 지나쳤다!"
    
    # 장애물 3: 양념치킨
    character.speak("눈앞에 맛있는 양념치킨이 나타났어! 먹을까?")
    if character.ask_question("이 치킨을 먹을까요?"):
        character.speak("치킨을 맛있게 먹었어! 치킨을 빼앗긴 사람이 저항했지만 맛있게 먹었어.")
        outcome3 = "사람까지 먹었다!"
    else:
        character.speak("이 치킨은 주인이 있어! 어쩔 수 없네 이건 먹지말자.")
        outcome3 = "양념치킨을 지나쳤다!"

    # 장애물 4: 짜장면과 군만두
    character.speak("짜장면과 군만두를 들고 있는 배달부가 지나가고 있어! 먹을 수 있을까?")
    if character.ask_question("이 사람을 덮칠까요"):
        character.speak("잘 먹었다! 하지만 배달부는 너무 빨라서 못 먹었어.")
        outcome4 = "짜장면 세트를 먹었다!"
    else:
        character.speak("배달부가 동민이네, 불쌍하니 먹지말자.")
        outcome4 = "배달부 동민이를 지나쳤다!"

    # 정우의 결말
    print("\n--- 정우의 먹방 스토리 종료 ---")
    
# 게임 실행
if __name__ == "__main__":
    game()