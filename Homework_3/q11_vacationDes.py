# Question 11: VacationDestinations
#
# Given an origin city, a maximum travel time k, and pairs of destinations that can be reached
# directly from each other with corresponding travel times in hours, return the number of
# destinations within k hours of the origin. Assume that having a stopover in a city adds
# an hour of travel time.
#
# Examples:
#
# Input: [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5),
#          ("Washington D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5),
#          ("Philadelphia", "Washington D.C.", 2.5)]
#
# Origin = "New York", k=5
# Output: 2 (["Boston", "Philadelphia"])
#
# Origin = "New York", k=7
# Output: 2 (["Boston", "Philadelphia", "Washington D.C.", "Newport"])
#
# Origin = "New York", k=8
# Output: 2 (["Boston", "Philadelphia", "Washington D.C.", "Newport", "Harper's Ferry", "Portland"])
