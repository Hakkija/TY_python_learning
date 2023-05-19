class Horse:
    def run(self):
        print("Running...")
    def whinny(self):
        print("Hihihihahahaaa!")

class Pony(Horse):
    def whinny(self):
        print("He-he!")

bobo = Pony()
bobo.run()