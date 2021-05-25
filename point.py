class Point:
    # 클래스 멤버
    instance_count = 0

    #   클래스 이름 공간에 생성, 모든 인스턴스에서 객체가 공유된다
    # 인스턴스 메서드의 첫 번쨰 인자는 항상 self
    def setX(self, x):
        self.x = x #self는 인스턴스 자신

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y
