import os

import numpy as np

from pongpy.interfaces.team import Team
from pongpy.models.game_info import GameInfo
from pongpy.models.state import State


PLAYER_NAME = os.environ['PLAYER_NAME']


class ChallengerTeam(Team):
    def __init__(self):
        self.direction = 1

    @property
    def name(self) -> str:
        return PLAYER_NAME

    def atk_action(self, info: GameInfo, state: State) -> int:
        '''
        前衛の青色のバーをコントロールします。
        '''
        direction = (state.ball_pos.y - state.mine_team.atk_pos.y) > 0
        return info.atk_return_limit if direction else -info.atk_return_limit

    def def_action(self, info: GameInfo, state: State) -> int:
        '''
        後衛のオレンジ色のバーをコントロールします。
        '''
        min_distance = 8
        max_distance = 16

        wall_min = 16
        wall_max = 112

        direction = (state.ball_pos.y - state.mine_team.atk_pos.y) > 0
        is_over_distance = min_distance < abs(state.mine_team.atk_pos.y - state.mine_team.def_pos.y) < max_distance

        print('is_over_distance: {}'.format(is_over_distance))
        if direction:
            if state.ball_pos.y + direction > wall_max:
                return -info.def_return_limit
            if is_over_distance:
                return info.def_return_limit
            else:
                return -info.def_return_limit
        else:
            if state.ball_pos.y + direction > wall_max:
                return info.def_return_limit
            if is_over_distance:
                return -info.def_return_limit
            else:
                return info.def_return_limit

