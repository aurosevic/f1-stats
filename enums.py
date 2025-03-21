from enum import Enum


class RaceSection(Enum):
    PRACTICE_1 = 'practice/1'
    PRACTICE_2 = 'practice/2'
    PRACTICE_3 = 'practice/3'
    QUALIFYING = 'qualifying'
    STARTING_GRID = 'starting-grid'
    RACE_RESULT = 'race-result'
    SPRINT_QUALIFYING = 'sprint-qualifying'
    SPRINT_GRID = 'sprint-grid'
    SPRINT_RESULT = 'sprint-results'
    PIT_STOP_SUMMARY = 'pit-stop-summary'
    FASTEST_LAPS = 'fastest-laps'
