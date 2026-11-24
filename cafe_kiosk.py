class MenuItem:
    """메뉴 한 개를 나타내는 클래스 (음료 / 디저트)"""

    def __init__(self, name, price, is_ice=None):
        self.name = name          # 메뉴명
        self.price = price        # 가격
        self.is_ice = is_ice      # 온도 옵션: True=ICE, False=HOT, None=해당 없음(디저트)

    def get_info(self):
        """메뉴 정보를 문자열로 반환"""
        if self.is_ice is None:
            option = ""
        else:
            option = " (ICE)" if self.is_ice else " (HOT)"
        return f"{self.name}{option}"

    def __str__(self):
        return f"{self.get_info()} - {self.price:,}원"


class Order:
    """장바구니 클래스"""

    def __init__(self):
        self.items = []           # MenuItem 객체들을 저장하는 리스트

    def add_item(self, item):
        """장바구니에 메뉴 객체 추가"""
        self.items.append(item)
        print("\n[장바구니]")
        for i, it in enumerate(self.items, 1):
            print(f" {i}. {it.get_info()}")

    def get_total_price(self):
        """담긴 모든 메뉴 객체의 가격 합산"""
        return sum(item.price for item in self.items)

    def print_receipt(self):
        """주문 내역 및 총액 출력"""
        print("\n" + "=" * 34)
        print("          영  수  증")
        print("=" * 34)
        if not self.items:
            print("주문 내역이 없습니다.")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.get_info():<18}{item.price:>9,}원")
        print("-" * 34)
        print(f"{'총 결제 금액':<18}{self.get_total_price():>9,}원")
        print("=" * 34)
        print("이용해 주셔서 감사합니다!")


class Kiosk:
    """키오스크: 메뉴판을 보여주고 손님의 선택을 장바구니에 담는다 (추가 클래스)"""

    def __init__(self):
        self.drinks = [
            MenuItem("아메리카노", 3000, True),
            MenuItem("카페라떼", 3800, True),
            MenuItem("바닐라라떼", 4300, True),
            MenuItem("녹차라떼", 4500, True),
        ]
        self.desserts = [
            MenuItem("치즈케이크", 5500),
            MenuItem("초코 쿠키", 2500),
            MenuItem("크로플", 4800),
        ]
        self.order = Order()

    def show_menu(self):
        print("\n========== 메뉴판 ==========")
        print("[음료]  ※ HOT/ICE 선택 가능")
        for i, m in enumerate(self.drinks, 1):
            print(f" {i}. {m.name:<10}{m.price:>6,}원")
        print("[디저트]")
        for i, m in enumerate(self.desserts, len(self.drinks) + 1):
            print(f" {i}. {m.name:<10}{m.price:>6,}원")
        print(" 0. 주문 완료 (결제)")
        print("============================")

    def select_item(self, number):
        """번호에 해당하는 메뉴의 복사본(MenuItem 객체)을 만들어 반환"""
        if 1 <= number <= len(self.drinks):
            base = self.drinks[number - 1]
            while True:
                temp = input("  HOT / ICE 선택 (h/i): ").strip().lower()
                if temp in ("h", "i"):
                    return MenuItem(base.name, base.price, temp == "i")
                print("  h 또는 i 를 입력하세요.")
        idx = number - len(self.drinks) - 1
        if 0 <= idx < len(self.desserts):
            base = self.desserts[idx]
            return MenuItem(base.name, base.price)
        return None

    def run(self):
        while True:
            self.show_menu()
            choice = input("메뉴 번호를 입력하세요: ").strip()
            if not choice.isdigit():
                print("숫자를 입력해 주세요.")
                continue
            number = int(choice)
            if number == 0:
                break
            item = self.select_item(number)
            if item is None:
                print("없는 메뉴입니다. 다시 선택해 주세요.")
            else:
                self.order.add_item(item)
        self.order.print_receipt()


if __name__ == "__main__":
    Kiosk().run()
