"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["btry", "byrt"],
            "answer": True
        },
        {
            "input": ["boss", "boss"],
            "answer": True
        },
        {
            "input": ["solid", "disel"],
            "answer": False
        },
        {
            "input": ["false", "flaes"],
            "answer": False
        },
        {
            "input": ["true", "treu"],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input": ["race", "care"],
            "answer": True
        },
        {
            "input": ["knee", "keen"],
            "answer": True
        },
        {
            "input": ["trap", "part"],
            "answer": False
        },
        {
            "input": ["adkglaigrbosudfbklabsdlkgalkkfndah", "adkglaigrbosudfbllabsdlkgakkkfndah"],
            "answer": True
        },
        {
            "input": ["adkglaigrbosudfbklabsdlkgalkkfndah", "adkglaogrbisudlbkfabsdlkgalkkfndah"],
            "answer": False
        },
        {
            "input": ["abracadabra", "badaboom"],
            "answer": False
        },
        {
            "input": ["burx", "byrt"],
            "answer": False
        }
    ]
}
