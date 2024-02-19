classification_prompt = """ Classify the text as labels: BOOK_ENQUIRY, ADD_TO_CART, AVAILABILITY, ADDRESS, STOP, TIMINGS, DELIVERY, OTHER
    ======================================
    LABEL_MAPPER =
        "BOOK_ENQUIRY": [Summary, Genre, Author, Science, Fiction],
        "ADD_TO_CART": ["Buy", "Add to cart"],
        "DELIVERY": ["Delivery"],
        "AVAILABILITY": ["is it available"],
        "ADDRESS": ["Address", "Location"],
        "OTHER": ["call me tomorrow", "no sounds good", "no thank you", "no", "nope", "call when you find out", "No", "call me"],
        "STOP": ["not interested", "already purchased", "already contacted", "stop", "dealing with", "salesperson is already helping", "spoke with", "sold already", "don't call"],
        ======================================
            Examples
            text: no
            labels: OTHER
            text: Summary of nemesis
            labels: BOOK_ENQUIRY
            text: Genre of nemesis
            labels: BOOK_ENQUIRY
            text: nope
            labels: OTHER
            text: Is it in the store
            labels: AVAILABILITY
            text: Can you deliver the book to my location?
            labels: DELIVERY
            text: i was wondering if the vehicle was available?
            labels: AVAILABILITY
            text: i've already received a text from the representative
            labels: STOP
            text: Already purchased
            labels: STOP
            text: I have contacted the salesperson
            labels: STOP
            text: Whats your location?
            labels: ADDRESS
            text: to see if it's available
            labels: AVAILABILITY
            text: already dealing with a salesperson
            labels: STOP
            text: please disregard this request
            labels: STOP
            text: nope thank you!
            labels: OTHER
            text: no i actually would like to purchase it as soon as possible
            labels: OTHER
            text: 4 or 5
            labels: OTHER
            text: tomorrow morning 10 am
            labels: OTHER
            text: '{text}'
            labels:
            """
generation_prompt = (
    "Provide a humane answer for the '{inquiry_message}' from a customer who is looking for a book"
    "and avoid providing a comprehensive description "
    "other than the answer to the inquiry. \n\n"
    "Use only the provided feature information: '{context}', and do not add any of your own. \n\n "
    "Do not comment that you have sold the book. \n\n"
    "Add {followup_question} at the end of the answer. \n\n"
    "Avoid repeating phrases. \n\n"
)

genre_summary_prompt = (
        """Paraphrase and break the '{inquiry_message}' from a client interested in a book if it is about the book's Genre and Summary. \n\n "
    "Remove anything else in the question not related to genre or summary"
    "Do not extend or add anything to the '{inquiry_message}' \n\n
    "If the '{inquiry_message}' is about anything else other then Genre or Summary or Recommendation of a book return FALSE \n\n "
    ======================================
    Examples
    inquiry_message: Genre of Nemesis
    answer: Genre of Nemesis
    inquiry_message: Summary of Nemesis and is the book available?
    answer: Summary of Nemesis
    inquiry_message: Genre of book and is the book available and can you deliver?
    answer: Genre of book
    inquiry_message: Author of book
    answer: False
    inquiry_message: '{inquiry_message}'
    answer:
     """
)