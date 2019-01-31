# CLASSES

from textwrap import dedent

# Player has-a Force
class Player(object):

    def __init__(self):
        self.force = Force()
        # self.weapon eventually too

class Force(object):

    def __init__(self, level):
        self.level = level

class Scene(object):
    print("This scene is incomplete")
    exit(1)

class OpeningScene(Scene):
    def enter(self):
        print("A long time ago in a galaxy far far away...", end='')
        input()
        print("Our hero finds himself in a predicament.", end='')
        input()
        print("After being knocked unconscious and forced into", end='')
        input()
        print("slave labor for several years, he has finally", end='')
        input()
        print("gained a new way to try and escape his captors.", end='')
        input()
        print("A colosseum arena fight is your method of escape.", end='')
        input()
        print("It won't be easy, but our hero must emerge victorious", end='')
        input()
        print("in order to find who he is and where he is from...", end='')
        input()
        return 'weapon_room'

class WeaponRoom(Scene):

    def enter(self):
        print(dedent("""
        Today is the day. The day that you've been waiting for ever since you got stuck in that lousy cell.
        You don't remember who you are, and you barely remember why you're here, but here you are.
        Some might call battling for other's amusements in an audacious Utapaun Colosseum a horror, but you see it as an opportunity.
        An opportunity to leave this god-forsaken planet.
        """))
        input()
        print(dedent("""
        The arena warden grabs your shoulder and harshly pulls you aside to a table with various weapons strewn across it.
        These weapons are clearly not of high quality, and seem more efficient as farm tools than anything.
        Among the dust you see a rusted vibro-ax, a Tusken Raider gaffi stick, and an ancient wooden club.
        Which do you choose?
        """))
        choice = input("> ")
        count_ax = choice.count("ax")
        count_stick = choice.count("stick")
        count_club = choice.count("club")
        if count_ax > 0:
            print(dedent("""
            You reach for the vibro-ax, as it seems to be the most relevant weapon available. If you want a chance, you'll need something with a sharp edge.
            The arena warden shoves you along towards the gates to the arena before the metal bars rise and amidst the headbanging noise of cheering and booing, you enter the arena.
            """))
            return 'arena_intro'
        elif count_stick > 0:
            print(dedent("""
            You grab the Gaderffii, as it seems to be in the best condition regardless of its interesting weapon capabilites. Better to have a functioning weapon than a failing one!
            The arena warden shoves you along towards the gates to the arena before the metal bars rise and amidst the headbanging noise of cheering and booing, you enter the arena.
            """))
            return 'arena_intro'
        elif count_club > 0:
            print(dedent("""
            You aren't sure why, but you felt led to grab the wooden club. Something about it seems to be asking for you to choose it. Sticking with your gut feeling, you pick it up.
            The arena warden shoves you along towards the gates to the arena before the metal bars rise and amidst the headbanging noise of cheering and booing, you enter the arena.
            """))
            # force level increases
            return 'arena_intro'
        else:
            print(dedent("""
            Before you are able to choose, The arena warden shoves you along towards the gates to the arena before the metal bars rise and you are thrown into the arena.
            """))
            return 'arena_intro'

class ArenaIntro(Scene):

    def enter(self):
        pass

class FirstMonster(Scene):

    def enter(self):
        pass

class SecondMonster(Scene):

    def enter(self):
        pass

class ArenaMaster(Scene):

    def enter(self):
        pass

class SceneMap(object):

    scenes = {'opening_scene': OpeningScene(),
        'weapon_room': WeaponRoom(),
        'arena_intro': ArenaIntro(),
        'first_monster': FirstMonster(),
        'second_monster': SecondMonster(),
        'arena_master': ArenaMaster()
        }

        def __init__(self, start):
            self.start = start

        def next_scene(self, next):
            scene = SceneMap.scenes.get(next)
            scene.enter()

        def start_scenes(self):
            return self.next_scene(self.start)
