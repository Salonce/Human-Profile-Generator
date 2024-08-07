from ..personality_generators import generate_subtrait, generate_trait


class Extraversion:

    def __init__(self, extraversion, friendliness, gregariousness, assertiveness, activity_level, excitement_seeking,
                 cheerfulness):
        self.extraversion = extraversion
        self.friendliness = friendliness
        self.gregariousness = gregariousness
        self.assertiveness = assertiveness
        self.activity_level = activity_level
        self.excitement_seeking = excitement_seeking
        self.cheerfulness = cheerfulness

    @classmethod
    def generate_random(cls):
        extraversion = generate_trait()
        friendliness = generate_subtrait(extraversion)
        gregariousness = generate_subtrait(extraversion)
        assertiveness = generate_subtrait(extraversion)
        activity_level = generate_subtrait(extraversion)
        excitement_seeking = generate_subtrait(extraversion)
        cheerfulness = generate_subtrait(extraversion)
        extraversion = round((friendliness + gregariousness + assertiveness + activity_level + excitement_seeking + cheerfulness) / 6)

        return cls(extraversion, friendliness, gregariousness, assertiveness, activity_level, excitement_seeking,
                   cheerfulness)

    def get_extraversion(self):
        return self.extraversion

    def get_friendliness(self):
        return self.friendliness

    def get_gregariousness(self):
        return self.gregariousness

    def get_assertiveness(self):
        return self.assertiveness

    def get_activity_level(self):
        return self.activity_level

    def get_excitement_seeking(self):
        return self.excitement_seeking

    def get_cheerfulness(self):
        return self.cheerfulness
