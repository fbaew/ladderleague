"""
Custom exceptions for the scoreboard app
"""


class NonParticipantError(Exception):
    """
    Used when an invalid player is passed to a method that expects 
    only certain players.
    """
    pass


class UndefinedOutcomeError(Exception):
    """
    Not sure that this should be called this; currently it is only used
    by Set.winner() when the Set in question was a draw.
    """
    pass
