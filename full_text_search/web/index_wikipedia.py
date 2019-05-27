import logging
import wikipedia
from .models import Page

logger = logging.getLogger('django')

def index_wikipedia(num_pages):
    for _ in range(0, num_pages):
        p = wikipedia.random()
        try:
            wiki_page = wikipedia.page(p)
            Page.objects.update_or_create(title=wiki_page.title, defaults={
                'content': wiki_page.content
            })
            logger.info('Successfully indexed %s', wiki_page)
        except Exception:
            logger.exception('Failed to index %s', p)
