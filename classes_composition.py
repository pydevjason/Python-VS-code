class Paper():
    def __init__(self, text, case):
        self.text = text
        self.case = case


class Briefcase():
    def __init__(self, price):
        self.price = price
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.papers]


class Attorney():
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def write_note(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_notes(self):
        print(self.briefcase.view_notes())


cheap_briefcase = Briefcase(price=19.99)
vato = Attorney(name="Vato", briefcase=cheap_briefcase)
vato.write_note("my client is innocent!", "case 23")
vato.write_note("I represent the Trump legal team!", "case 23")
vato.view_notes()
