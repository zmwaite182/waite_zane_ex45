# CLASSES

from textwrap import dedent

# Player has-a Force
class Player(object):

    def __init__(self, force):
        self.force = force
        self.weapon = ''

class Scene(object):
    def enter(self, user):
        print("This scene is incomplete")
        exit(1)

class OpeningScene(Scene):

    def enter(self, user):
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

    def enter(self, user):
        self.user = user
        print(dedent("""
        Today is the day. The day that you've been waiting for ever since you got stuck in that lousy cell.
        You don't remember who you are, and you barely remember why you're here, but here you are.
        Some might call battling for other's amusements in an audacious Utapaun Colosseum a horror, but you see it as an opportunity.
        An opportunity to leave this god-forsaken planet."""))
        input()
        print(dedent("""
        The arena warden grabs your shoulder and harshly pulls you aside to a table with various weapons strewn across it.
        These weapons are clearly not of high quality, and seem more efficient as farm tools than anything.
        Among the dust you see a rusted vibro-ax, a Tusken Raider gaffi stick, and an ancient wooden club.
        Which do you choose?"""))
        choice = input("> ")
        count_ax = choice.count("ax")
        count_stick = choice.count("stick")
        count_club = choice.count("club")
        if count_ax > 0:
            print(dedent("""
            You reach for the vibro-ax, as it seems to be the most relevant weapon available. If you want a chance, you'll need something with a sharp edge.
            The arena warden shoves you along towards the gates to the arena before the metal bars rise and amidst the headbanging noise of cheering and booing, you enter the arena."""))
            self.user.weapon = 'vibro-ax'
            return 'monster'
        elif count_stick > 0:
            print(dedent("""
            You grab the Gaderffii, as it seems to be in the best condition regardless of its interesting weapon capabilites. Better to have a functioning weapon than a failing one!
            The arena warden shoves you along towards the gates to the arena before the metal bars rise and amidst the headbanging noise of cheering and booing, you enter the arena."""))
            self.user.weapon = 'gaderffii'
            return 'monster'
        elif count_club > 0:
            print(dedent("""
            You aren't sure why, but you felt led to grab the wooden club. Something about it seems to be asking for you to choose it. Sticking with your gut feeling, you pick it up.
            The arena warden shoves you along towards the gates to the arena before the metal bars rise and amidst the headbanging noise of cheering and booing, you enter the arena."""))
            self.user.weapon = 'wooden club'
            self.user.force += 10
            return 'monster'
        else:
            print(dedent("""
            Before you are able to choose, The arena warden shoves you along towards the gates to the arena before the metal bars rise and you are thrown into the arena."""))
            return 'monster'

class Monster(Scene):

    def enter(self, user):
        self.user = user
        input()
        print(dedent(f"""
        You walk towards the center of the colosseum, ready to face whoever challenges you to a fight. little do you know, that you won't be fighting a who, but rather a what.
        Metal bars rise at the entrance across the arena and out pounces a Nexu, an agile feline with 4 red eyes and sharp quills. It spots you instantly, and rushes towards you.
        With your {self.user.weapon} in hand, you have a couple of seconds to decide what to do. The Nexu closes the gap between you and lunges at you.
        What do you do?"""))
        choice = input("> ")
        if 'attack' in choice or 'hit' in choice or 'slash' in choice or 'whack' in choice or 'stab' in choice:
            print(dedent("""
            You throw out an attack hoping to land upon the nimble beast. The Nexu halts its momentum, sidesteps your attack and then lunges in for the kill.
            You try to avoid the attack, but don't have enough energy after swinging your weapon at it, The Nexu's teeth break through your fragile skin, killing you instantly
            You are dead."""))
            exit(0)
        elif 'dodge' in choice or 'evade' in choice or 'sidestep' in choice or 'move' in choice:
            print(dedent("""
            You sidestep the Nexu's attack and are left with a slight opening to make the next move.
            What do you do?"""))
            choice = input("> ")
            if 'attack' in choice or 'hit' in choice or 'slash' in choice or 'whack' in choice or 'stab' in choice:
                print(dedent("""
                You go in for the attack, and due to the recoil of the Nexu's last lunge, you land a successful attack"""))
                if self.user.weapon == 'wooden club':
                    print(dedent("""
                    The attack does nothing but anger the Nexu, and it turns around and lunges at you once more. This time, digging its sharp claws into your skin.
                    You are dead"""))
                    exit(0)
                elif self.user.weapon == 'vibro-ax':
                    print(dedent("""
                    The attack severs through the Nexu's skin, decapitating it successfully and leaving you standing victorious"""))
                    return 'arena_master'
                elif self.user.weapon == 'gaderffii':
                    print(dedent("""
                    The spiked side of the gaffi stick pierces through the Nexu's flesh, wounding the beast.
                    Holding onto the stick, you begin to push the wound deeper. It thrashes about to try and rid itself of this stab wound,
                    and you get sent flying, landing away from your weapon.
                    The Nexu presses forward, slowly but surely, seeking to finish you off.
                    What do you do?"""))
                    choice = input("> ")
                    if 'force' in choice:
                        print(dedent("""
                        You trust in the force, and right before the Nexu lunges at you once more,
                        you pull your weapon back to you and bash the alien feline with the blunt end of the gaderffii, killing it."""))
                        self.user.force += 10
                        return 'arena_master'
                    else:
                        print(dedent("""
                        The Nexu sees through your next move and punishes accordingly with a fatal blow to the head.
                        You are dead."""))
                        exit(0)
                else:
                    print(dedent("""
                    Even though you are lacking a weapon, you try to attack the Nexu with your bare fists. This only angers it, as it flings you away and then pounces on top of you, tearing open your flesh and killing you.
                    You are dead."""))
                    exit(0)
            elif 'dodge' in choice or 'evade' in choice or 'sidestep' in choice or 'move' in choice:
                print(dedent("""
                You decide to clear even more distance between yourself and the cat, and feel safe about keeping your distance.
                The Nexu quickly catches on however, and chases you down as you try to move away. It tackles you and stabs you with its sharp quills, killing you instantly.
                You are dead."""))
                exit(0)
            elif 'force' in choice:
                print(dedent("""
                You try and use the force and are able to launch the Nexu farther away from you. You are amazed at your newly learned ability and decide to chase down the Nexu.
                You catch up to it in no time and slay the beast with a well placed attack."""))
                self.user.force += 10
                return 'arena_master'
        elif 'force' in choice:
            print(dedent("""You seek within yourself and try and use the force to push the Nexu away. You are not able to focus however, and the Nexu finishes its pounce attack, killing you instantly
            You are dead."""))
            exit(0)
        else:
            print(dedent("""
            Before you are able to react, the Nexu pounces on you, tears open your flesh and causes an uproar across the colosseum.
            You are dead."""))
            exit(0)

class ArenaMaster(Scene):

    def enter(self, user):
        self.user = user
        print(dedent("""
        After the beast falls over dead, the Arena Master takes off his cloak and jumps down from the colosseum podium, igniting a red lightsaber and revealing his identity as a sith lord.
        You panic and try and bring your thoughts together to decide what you can do to defeat him, and why he even wants you dead so badly in the first place.
        """))
        input()
        if self.user.weapon == 'wooden club':
            print(dedent(f"""You look down at your {self.user.weapon} and notice a blue glow coming from within the middle of it. You break a piece of bark off of the weapon which reveals a button.
            You press the button, and to your surprise it flashes a blue beam out the one end. Your weapon is actually a lightsaber as well! The arena master rushes towards you and engages in lightsaber combat.
            You trade blows and find the swordplay comes naturally to you, even with such a light and masterful weapon. He goes for an overhead strike, and you block it, finding yourself in a blade lock.
            He pulls out his non weapon-wielding hand, and attempts to push you back with the force. You raise your hand as well, attempting to counteract his force push with one of your own."""))
            if self.user.force >= 20:
                print(dedent("""
                You are able to withstand his force power, but it isn't easy. You both push harder until you finally send him flying backwards.
                He lands on his back without a weapon and begs for your mercy as you approach him with your lightsaber glowing in hand.
                What do you do?"""))
                choice = input("> ")
                if 'kill' in choice or 'attack' in choice or 'strike' in choice:
                    print(dedent("""
                    You have clearly beat your enemy, and decide to end it once and for all, decapitating the helpless sith lord, before escaping the arena to find what your true life before was, as a Jedi Master.
                    You Win!"""))
                    exit(0)
                else:
                    print(dedent("""
                    You realize that if you attack and kill him, then you are no better than he was. You decide to show mercy, and pick up his lightsaber before walking away.
                    To your surprise, the sith lord hops back up and launches a barrage of force lightning into your body. Your whole being quakes with electricity as he walks closer and closer.
                    The electric shock builds up until it paralyzes you and soon becomes fatal and kills you.
                    You are dead."""))
                    exit(0)
            else:
                print(dedent("""
                You aren't quite as capable as him, and you get sent flying backwards onto the ground, your weapon far from you.
                He approaches you with his red glowing lightsaber in hand, and with one fell slash, lands a fatal blow to your torso.
                You are dead."""))
                exit(0)
        else:
            print(dedent(f"""
            You look down at your {self.user.weapon} and decide to charge towards him in order to land a blow. He simply sidesteps your attack and slashes you in the back,
            leaving a gaping wound. He approaches you as you writhe on the ground in agony before impaling you with his lightsaber to finish you off.
            You are dead."""))
            exit(0)

class SceneMap(object):

    scenes = {'opening_scene': OpeningScene(),
        'weapon_room': WeaponRoom(),
        'monster': Monster(),
        'arena_master': ArenaMaster()
        }

    def __init__(self, user):
        self.user = user

    def next_scene(self, next):
        scene = SceneMap.scenes.get(next)
        next = scene.enter(self.user)
        self.next_scene(next)
