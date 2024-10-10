import random
from core.slot import Slot
from core.constants import PLAYER_COINS_INITIAL

# Símbolos clássicos de um caça-níqueis
slot_types = []
slot_types += [Slot(display="Cereja", value=1.1, icon="/static/images/cereja.png")] * 10
slot_types += [Slot(display="Limão", value=1.2, icon="/static/images/limao.png")] * 8
slot_types += [Slot(display="Laranja", value=1.3, icon="/static/images/laranja.png")] * 6
slot_types += [Slot(display="Melancia", value=3, icon="/static/images/melancia.png")] * 5
slot_types += [Slot(display="Sete", value=5, icon="/static/images/sete.png")] * 3
slot_types += [Slot(display="Sino", value=8, icon="/static/images/sino.png")] * 4
slot_types += [Slot(display="Bar", value=13, icon="/static/images/bar.png")] * 3
slot_types += [Slot(display="Diamante", value=17, icon="/static/images/diamante.png")] * 2
slot_types += [Slot(display="Coroa", value=30, icon="/static/images/coroa.png")]
slot_types += [Slot(display="Ferradura", value=40, icon="/static/images/ferradura.png")]
slot_types += [Slot(display="Trevo", value=63, icon="/static/images/trevo.png")]
slot_types += [Slot(display="Dólar", value=71, icon="/static/images/dolar.png")]
slot_types += [Slot(display="Estrela", value=80, icon="/static/images/estrela.png")]
slot_types += [Slot(display="Jackpot", value=100, icon="/static/images/jackpot.png")]


def random_slot():
    slot = random.choice(slot_types)
    return slot.copy(deep=True)

def reset_game(player, game):
    player.coins = PLAYER_COINS_INITIAL
