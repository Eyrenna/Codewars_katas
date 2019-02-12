def points(games):
    our_team_points = 0
    for item in games:
        if item[0] > item[2]:
            our_team_points += 3
        elif item[0] == item[2]:
            our_team_points += 1
        else:
            pass
    return our_team_points

if __name__ == "__main__":
    assert points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']) == 30
    assert points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']) == 10
    assert points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']) == 0
    assert points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']) == 15
    assert points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']) == 12