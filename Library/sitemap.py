import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from Library.models import Book


class BookSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.updated


class StaticSitemap(Sitemap):
    lastmod = None
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['about', 'contact', 'browse', ]

    def location(self, item):
        return reverse(item)


class HomepageSitemap(Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return ['home', ]

    def lastmod(self, obj):
        return datetime.date.today()

    def location(self, item):
        return reverse(item)
