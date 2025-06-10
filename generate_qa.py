questions = [
    ("internship_what_is", ["What is an internship?", "Define internship"], "An internship is temporary work experience where students gain practical skills in their field of study."),
    ("placement_prep_tips", ["How to prepare for placements?", "Campus placement preparation guide"], "1. Master core CS concepts\n2. Practice coding\n3. Mock interviews\n4. Build projects\n5. Improve communication skills"),
    ("resume_tech_tips", ["Resume format for tech internships", "How to make a technical resume?"], "Include projects, programming languages, internships, coding profiles, and certifications."),
    # Add more (intent, [examples], answer) tuples here up to 200!
]

def generate_yamls():
    # Generate NLU
    with open("data/nlu.yml", "w", encoding="utf-8") as f:
        f.write('version: "3.1"\nnlu:\n')
        for intent, examples, _ in questions:
            f.write(f"- intent: {intent}\n  examples: |\n")
            for ex in examples:
                f.write(f"    - {ex}\n")

    # Generate Domain
    with open("domain.yml", "w", encoding="utf-8") as f:
        f.write('version: "3.1"\nintents:\n')
        for intent, _, _ in questions:
            f.write(f"  - {intent}\n")
        f.write("\nresponses:\n")
        for intent, _, answer in questions:
            f.write(f"  utter_{intent}:\n    - text: |\n        {answer}\n")
        f.write("\nactions: []\n")

    # Generate Stories
    with open("data/stories.yml", "w", encoding="utf-8") as f:
        f.write('version: "3.1"\nstories:\n')
        for intent, _, _ in questions:
            f.write(f"- story: {intent}_path\n  steps:\n  - intent: {intent}\n  - action: utter_{intent}\n")

if __name__ == "__main__":
    generate_yamls()
