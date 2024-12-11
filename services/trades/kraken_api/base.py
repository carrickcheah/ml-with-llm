from abc import ABC, abstractmethod
from typing import List

from .trade import Trade

# this class willbe use in websocket.py


# TradesAPI(ABC): Think of TradesAPI as a blueprint for a special kind of LEGO robot.
# The (ABC) part means it's an Abstract Base Class,

#  The abstract class (TradesAPI) is like a rulebook for anyone building a "trading robot" (or system).
# You’re saying:
# "I don’t know exactly how this will work yet, but I want all future versions to follow these rules."


class TradesAPI(ABC):
    @abstractmethod  #
    def get_trades(self) -> List[Trade]:
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass


# @abstractmethod: These are like instructions in the blueprint that say,
# "You must add these parts, but I won’t say exactly how."
