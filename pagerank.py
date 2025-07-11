import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    transition_dictionary = {}
    N = len(corpus)
    random_probability = (1 - damping_factor) / N

    if len(corpus[page]) == 0:
        for other_page in corpus:
            transition_dictionary[other_page] = 1 / N
    else:
        linked_pages = corpus[page]
        link_probability = damping_factor / len(linked_pages)
        for other_page in corpus.keys():
            transition_dictionary[other_page] = random_probability
            if other_page in linked_pages:
                transition_dictionary[other_page] += link_probability
    return transition_dictionary

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #Creating page rank dictionary
    pr_dictionary = {}
    #Picking a random page
    page = random.choice(list(corpus.keys()))
    #How many times is visited the page
    count = 0

    for page in list(corpus.keys()):
        pr_dictionary[page] = count

    for i in range(n):
        sample = transition_model(corpus, page, damping_factor)
        pr_dictionary[page] += 1
        page = random.choices(population=list(sample.keys()), weights=list(sample.values()), k=1)[0]

    for page, value in pr_dictionary.items():
        pr_dictionary[page] = value/n

    return pr_dictionary

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #giving each page the first pr
    probability_page = 1/len(corpus)
    list_pages = list(corpus.keys())
    current_prs = {}

    for page in list_pages:
        current_prs[page] = probability_page
    threshold = 0.001
    keep_iterating = True

    while keep_iterating:
        old_list = list(current_prs.values())
        new_list, dictionary = update_dictionary(damping_factor, list_pages, corpus, current_prs, {})
        # Compara valor a valor
        differences = [abs(old - new) for old, new in zip(old_list, new_list)]
        # Si alguna diferencia supera el umbral, sigue iterando
        keep_iterating = any(diff > threshold for diff in differences)

        if keep_iterating:
            current_prs = dictionary
    return current_prs

def update_dictionary(damping_factor, list_pages, corpus, current_prs, new_prs):
    for page in list_pages:
        new_pr = calculating_pr_page(damping_factor, len(corpus), corpus, page, current_prs)
        new_prs[page] = new_pr
    return list(new_prs.values()), new_prs

def calculating_pr_page(damping_factor, N, corpus, page, prs):
    list_pages = list(corpus.keys())
    new_pr = (1 - damping_factor)/N
    filter_pages = []

    for linked_page in list_pages:
        if len(corpus[linked_page]) == 0:
            new_pr += damping_factor * prs[linked_page]/N
        if page in corpus[linked_page]:
            new_pr += damping_factor * prs[linked_page]/len(corpus[linked_page])
    return new_pr

if __name__ == "__main__":
    main()
