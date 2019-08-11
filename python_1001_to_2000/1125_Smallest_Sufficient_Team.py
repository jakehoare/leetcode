_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-sufficient-team/
# In a project, you have a list of required skills req_skills, and a list of people.
# The i-th person people[i] contains a list of skills that person has.
# Consider a sufficient team: a set of people such that for every required skill in req_skills,
# there is at least one person in the team who has that skill.
# We can represent these teams by the index of each person:
# for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
# Return any sufficient team of the smallest possible size, represented by the index of each person.
# You may return the answer in any order.  It is guaranteed an answer exists.

# Represent the skills of each person as an int, with a bit set for each required skill.
# For each required skill, if we already have that skill then move to the next skill.
# Else for each person who has that skill, add their skill to the current skills and recurse for the next skill.
# When returning form recursion, reset the team and current skills.
# Time - O(m ** n) for m people and n required skills.
# Space - O(m ** n)

class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        skill_to_int = {skill: i for i, skill in enumerate(req_skills)}
        people_skills = [0] * len(people)       # skills per person represented as an int
        for i, person in enumerate(people):
            for skill in person:
                people_skills[i] |= 1 << skill_to_int[skill]

        self.has_skills = 0                     # current skills, represented as an int
        self.smallest_team = list(range(len(req_skills) + 1))
        team = []                               # current team

        def helper(next_skill):
            if len(team) >= len(self.smallest_team):    # early return is cannot improve on result
                return
            if next_skill == len(req_skills):
                self.smallest_team = team[:]
                return

            if self.has_skills & (1 << next_skill):
                helper(next_skill + 1)
            else:
                for i, person_skills in enumerate(people_skills):
                    if person_skills & (1 << next_skill):
                        copy_skills = self.has_skills   # save so can be reset after recursion
                        self.has_skills |= person_skills
                        team.append(i)
                        helper(next_skill + 1)
                        team.pop()                      # revert team and skills before next person
                        self.has_skills = copy_skills

        helper(0)
        return self.smallest_team
