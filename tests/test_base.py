# -*- coding: utf-8 -*-
from nlplib.base import  language_langid


def test_language_langid():
    assert(language_langid(None) is None)
    assert(language_langid(u'Happy face') == 'en')
    assert (language_langid(u'Elle est contente') == 'fr')
