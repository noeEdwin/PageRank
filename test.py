def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    transition_dictionary = {}
    random_probability = (1 - damping_factor) / len(corpus)
    probability_per_page = damping_factor / len(corpus[page])

    if len(corpus[page]) == 0:
        transition_dictionary[page] = 1 / len(corpus)

    else:
        transition_dictionary[page] = random_probability
        for link in corpus[page]:
            transition_dictionary[link] = random_probability + probability_per_page

    return transition_dictionary

body = {
  "1.html": {"2.html", "3.html"},
  "2.html": {"3.html"},
  "3.html": {"2.html"}
}

print(transition_model(body, "1.html", 0.85))
