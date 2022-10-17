import sys
sys.path.append('pgn2data')
from converter.pgn_data import PGNData
pgn_data = PGNData("pgns\\carlsen, magnus.pgn", extra_headers = ["EventType"])
result = pgn_data.export()
result.print_summary()

