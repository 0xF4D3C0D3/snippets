import urllib.request, json

class Thanos:

    def __init__(self):
        print('Bye, World!')
        self.MAX_RANDOM = 1024

    def finger_snap(self, world):

        size_world = len(world)
        size_target = size_world//2
        
        count_choice = 0
        idx_choice = []
        while count_choice < size_target:
            count_choice_tmp = min(size_target - count_choice, self.MAX_RANDOM)
            idx_choice += self.get_random(count_choice_tmp)
            count_choice += count_choice_tmp

        for count_kill, idx_kill in enumerate(idx_choice):
            del world[(idx_kill*42 + size_world)%(size_world-count_kill)]

    def get_random(self, length=1):
        with urllib.request.urlopen(f'https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=uint16') as url:
            data = json.loads(url.read().decode())
        return data['data']

thanos = Thanos()

for i in range(10):
    world = ['철수', '영희', 'John', 'Sam', '사람1', '사람2']
    print(f"before snap: {world}")
    thanos.finger_snap(world)
    print(f"after snap: {world}")
    print()
