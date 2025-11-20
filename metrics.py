
def cooperation_rate(player_actions):
    """Compute the cooperation rate given a list of player actions.

    Args:
        player_actions (list of str): List containing actions taken by players, 
                                      where "C" represents cooperation and "D" represents defection.

    Returns:
        float: The cooperation rate as a float between 0 and 1.
    """
    if not player_actions:
        return 0.0
    coop_count = sum(1 for action in player_actions if action == "C")
    return coop_count / len(player_actions)

def forgiveness_rate(player_actions, opponent_actions):
    """Compute the forgiveness rate given a list of player actions.

    Forgiveness is defined as the proportion of times a player cooperates
    immediately after the opponent defects.

    Args:
        player_actions (list of str): List containing actions taken by players, 
                                      where "C" represents cooperation and "D" represents defection.

    Returns:
        float: The forgiveness rate as a float between 0 and 1.
    """
    opp_defected = [i for i in range(len(opponent_actions)) if opponent_actions[i-1] == "D"]
    if opp_defected:
        forgiveness = sum(player_actions[i] == "C" for i in opp_defected) / len(opp_defected)
        return forgiveness
    return 0.0

def retaliation_rate(player_actions, opponent_actions):
    """Compute the retaliation rate given a list of player actions.

    Retaliation is defined as the proportion of times a player defects
    immediately after the opponent defects.

    Args:
        player_actions (list of str): List containing actions taken by players, 
                                      where "C" represents cooperation and "D" represents defection.

    Returns:
        float: The retaliation rate as a float between 0 and 1.
    """
    opp_defected = [i for i in range(len(opponent_actions)) if opponent_actions[i-1] == "D"]
    if opp_defected:
        retaliation = sum(player_actions[i] == "D" for i in opp_defected) / len(opp_defected)
        return retaliation
    return 0.0

def niceness(player_actions, opponent_actions):
    """Compute the niceness of a strategy given a list of player actions.

    Niceness is not defecting first. Binary variable!
    Args:
        player_actions (list of str): List containing actions taken by players, 
                                      where "C" represents cooperation and "D" represents defection.

    Returns:
        float: The niceness as a float between 0 and 1.
    """
    for t in range(len(player_actions)):
        if opponent_actions[t] == "D" and player_actions[:t].count("D") == 0:
            return 0
    return 1


def get_coop_def_rate_during_streaks(player_acts, opp_acts, min_streak = 3, coop_def = "C"):
    
    in_streak_indices = []
    curr_streak = 0
    streak_char = opp_acts[0]
    
    for i, action in enumerate(opp_acts):
        if action == streak_char:
            curr_streak += 1
        else:
            curr_streak = 1
            streak_char = action
            
        if curr_streak >= min_streak:
                in_streak_indices.extend(list(range(i - curr_streak, i)))
    
    if not in_streak_indices:
        return 0.0
    
    stats_during_streaks = sum(1 for i in in_streak_indices if player_acts[i] == coop_def)
    
    return stats_during_streaks / len(in_streak_indices)


# this requires inputting a history of actions for both players across all possible opponents
# def get_consistency()