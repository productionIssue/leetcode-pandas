import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    size_list = [0,0]
    shape = players.shape
    size_list[0] = shape[0]
    size_list[1] = shape[1]
    return size_list
