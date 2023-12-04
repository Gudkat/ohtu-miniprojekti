"""Tarjoaa pääsyn Citation ja CitationType luokkaan"""
from citations.new_citation import Citation, CitationType
from citations.citation_strings import ARTICLE_STRINGS, INPROCEEDINGS_STRINGS, \
                                        BOOK_STRINGS


class CitationFactory():
    """Luo käyttövalmiin Citation olion kun sille antaa CitationTypen.
    Citation olio sisältää kaikki vaaditut arvot CitationAttribute listalla
    riippuen siitä mikä CitationType annettiin.
    """
    @staticmethod
    def get_new_citation(citation_type: CitationType):
        """Palauttaa uuden Citation objectin jonka attribuutit vastaavat annettua tyyppiä.
        """
        # hopefully temporary "if else hell":
        match citation_type:
            case CitationType.ARTICLE:
                return Citation(citation_type, ARTICLE_STRINGS)
            case CitationType.INPROCEEDINGS:
                return Citation(citation_type, INPROCEEDINGS_STRINGS)
            case _:
                return Citation(citation_type, BOOK_STRINGS)
