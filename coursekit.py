"""Shared helper for chapter-style courses (physics, chemistry, biology, math, bangla, ict).
A subject module does:   C = Course(subject, title, tag, sub, lead);  ch = C.ch;  ch(...)×20;  COURSE, CHAPTERS = C.finish()
finish() runs the safety nets: counts per chapter, unique quiz options, and no bare "ডাক্তার" (always "হোমিওপ্যাথিক ডাক্তার")."""
import re


class Course:
    def __init__(self, subject, title, tag, sub, lead):
        self.subject = subject
        self.course = dict(slug="101", lang=subject, title=title, tag=tag, sub=sub, lead=lead)
        self.chapters = []

    def ch(self, n, title, en, intro, story, terms, concept, activity, medical, quiz):
        self.chapters.append(dict(n=n, title=title, en=en, intro=intro, story=story, terms=terms, concept=concept,
                                  activity=activity, medical=medical, quiz=quiz))

    def finish(self, count=20):
        assert len(self.chapters) == count, (self.subject, len(self.chapters))
        for i, c in enumerate(self.chapters, 1):
            assert c["n"] == i, (self.subject, "chapter order", c["n"], i)
            assert len(c["story"]) == 8, (self.subject, c["n"], "story", len(c["story"]))
            assert len(c["terms"]) == 6, (self.subject, c["n"], "terms", len(c["terms"]))
            assert len(c["quiz"]) == 6, (self.subject, c["n"], "quiz", len(c["quiz"]))
            assert len(c["medical"]) == 2, (self.subject, c["n"], "medical")
            assert len(c["concept"][1]) >= 3 and len(c["activity"][1]) >= 3, (self.subject, c["n"], "concept/activity")
            for q, opts, ans, why in c["quiz"]:
                assert 0 <= ans < len(opts) and len(set(opts)) == len(opts), (self.subject, c["n"], q)
            blob = " ".join(c["story"] + c["medical"] + [c["intro"], c["title"]] + [x for t in c["terms"] for x in t]
                            + list(c["concept"][1]) + list(c["activity"][1]) + [q for q, *_ in c["quiz"]])
            assert not re.search(r"(?<!হোমিওপ্যাথিক )ডাক্তার", blob), (self.subject, c["n"], "bare ডাক্তার")
        return self.course, self.chapters
