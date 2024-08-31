from lexical import lexical_analyzer as la
from syntax import first_follow as ff

# tokens = la.lexical_analysis("assets/test.txt")
ff.analyze_syntax("assets/test.txt")